"""
question_engine.py - JEE Adaptive Question Generator, Test Assembler,
and Topic Weakness Diagnostics Engine.
"""
import random
import json
from database import get_connection

# Dynamic conceptual templates for generating unlimited topic-specific JEE drill questions
TOPIC_TEMPLATES = {
    # Physics - Rotational Motion
    "Moment of Inertia & Theorems": [
        {
            "q": "Two point masses $m_1 = {m1}\\text{ kg}$ and $m_2 = {m2}\\text{ kg}$ are connected by a rigid massless rod of length $L = {L}\\text{ m}$. What is the moment of inertia of the system about an axis perpendicular to the rod passing through its center of mass?",
            "vars": lambda: {"m1": random.choice([2, 3, 4]), "m2": random.choice([4, 6]), "L": random.choice([1, 2])},
            "calc": lambda v: (
                round((v["m1"] * v["m2"] / (v["m1"] + v["m2"])) * (v["L"]**2), 2),
                f"Reduced mass $\\mu = \\frac{{m_1 m_2}}{{m_1 + m_2}} = \\frac{{{v['m1']} \\times {v['m2']}}}{{{v['m1'] + v['m2']}}} = {round(v['m1']*v['m2']/(v['m1']+v['m2']), 2)}\\text{ kg}$.\\n$I_{{cm}} = \\mu L^2 = {round((v['m1']*v['m2']/(v['m1']+v['m2'])) * (v['L']**2), 2)}\\text{ kg}\\cdot\\text{m}^2$."
            )
        },
        {
            "q": "A thin uniform ring of mass $M$ and radius $R$ has a moment of inertia $I_0$ about its central diameter. By the perpendicular axis theorem and parallel axis theorem, its moment of inertia about an axis tangent to the rim and in the plane of the ring is:",
            "options": ["$\\frac{3}{2} M R^2$", "$\\frac{1}{2} M R^2$", "$2 M R^2$", "$\\frac{5}{4} M R^2$"],
            "correct_idx": 0,
            "explanation": "About any diameter, $I_{dia} = \\frac{1}{2} M R^2$. A tangent in the plane of the ring is parallel to a diameter and displaced by distance $R$. By parallel axis theorem: $I = I_{dia} + M R^2 = \\frac{1}{2} M R^2 + M R^2 = \\frac{3}{2} M R^2$."
        }
    ],
    "Rolling Motion without Slipping": [
        {
            "q": "A solid cylinder of mass $M$ and radius $R$ rolls without slipping down an inclined plane of inclination $30^\\circ$. The magnitude of frictional force acting on the cylinder is:",
            "options": ["$\\frac{1}{3} M g$", "$\\frac{1}{6} M g$", "$\\frac{1}{2} M g$", "$\\frac{1}{4} M g$"],
            "correct_idx": 1,
            "explanation": "For a rolling body on an incline: $f = \\frac{M g \\sin\\theta}{1 + (M R^2 / I_{cm})}$. For a solid cylinder $I_{cm} = \\frac{1}{2} M R^2$, so $f = \\frac{M g \\sin(30^\\circ)}{1 + 2} = \\frac{M g / 2}{3} = \\frac{1}{6} M g$."
        }
    ],
    "Angular Momentum & Conservation": [
        {
            "q": "A horizontal platform of moment of inertia $I_p$ rotates freely with angular velocity $\\omega_0$ about a frictionless vertical axle. A child of mass $m$ standing at the center walks radially outward to a distance $R$. The new angular velocity $\\omega$ of the platform is:",
            "options": ["$\\frac{I_p}{I_p + m R^2} \\omega_0$", "$\\frac{I_p + m R^2}{I_p} \\omega_0$", "$\\frac{I_p}{m R^2} \\omega_0$", "$\\omega_0$"],
            "correct_idx": 0,
            "explanation": "No external vertical torque acts on the system, so angular momentum $L = I \\omega$ is conserved.\\n$L_i = I_p \\omega_0$.\\n$L_f = (I_p + m R^2) \\omega$.\\nEquating $L_i = L_f \\implies \\omega = \\frac{I_p}{I_p + m R^2} \\omega_0$."
        }
    ],

    # Electrostatics & Capacitance
    "Coulomb's Law & Electric Field Intensity": [
        {
            "q": "Two identical metallic spheres have charges $+4q$ and $-2q$. They are brought into contact and then separated back to distance $r$. The ratio of the electrostatic force before contact to that after contact is:",
            "options": ["$8 : 1$", "$4 : 1$", "$2 : 1$", "$16 : 1$"],
            "correct_idx": 0,
            "explanation": "Initial force magnitude: $F_1 = k \\frac{|(4q)(-2q)|}{r^2} = \\frac{8 k q^2}{r^2}$.\\nWhen touched, charge distributes equally: $q' = \\frac{4q + (-2q)}{2} = +q$ on each sphere.\\nFinal force: $F_2 = k \\frac{q^2}{r^2}$.\\nRatio $F_1 / F_2 = 8 / 1$."
        }
    ],
    "Gauss's Law & Flux Applications": [
        {
            "q": "A charge $Q$ is enclosed inside a closed Gaussian spherical surface of radius $R$. If the radius of the sphere is doubled to $2R$, the total electric flux emerging through the sphere:",
            "options": ["Remains unchanged", "Doubles", "Becomes 4 times", "Is halved"],
            "correct_idx": 0,
            "explanation": "According to Gauss's Law, $\\Phi_E = \\frac{Q_{enclosed}}{\\varepsilon_0}$. The total flux depends only on the net charge enclosed and the permittivity of the medium, not on the radius or shape of the surface."
        }
    ],
    "Capacitance & Dielectrics": [
        {
            "q": "A parallel plate capacitor is charged by a battery and then disconnected from the battery. A dielectric slab of dielectric constant $K > 1$ is then inserted between its plates. Which of the following statements is TRUE?",
            "options": [
                "Charge remains constant, potential difference decreases, stored energy decreases",
                "Potential difference remains constant, capacitance increases",
                "Stored energy increases, electric field increases",
                "Charge increases, capacitance remains constant"
            ],
            "correct_idx": 0,
            "explanation": "Since the battery is disconnected, the charge $Q$ is isolated and remains constant.\\nCapacitance becomes $C = K C_0 > C_0$.\\nPotential $V = Q/C = V_0 / K$ (decreases).\\nEnergy $U = \\frac{Q^2}{2C} = \\frac{U_0}{K}$ (decreases due to attractive work done on dielectric)."
        }
    ],

    # Thermodynamics & KTG
    "Thermodynamic Processes & PV Diagrams": [
        {
            "q": "For an ideal gas, the slope of an adiabatic curve on a $P-V$ indicator diagram is related to the slope of an isothermal curve passing through the same point by:",
            "options": [
                "$\\text{Slope}_{adiabatic} = \\gamma \\times \\text{Slope}_{isothermal}$",
                "$\\text{Slope}_{adiabatic} = \\frac{1}{\\gamma} \\times \\text{Slope}_{isothermal}$",
                "$\\text{Slope}_{adiabatic} = \\text{Slope}_{isothermal}$",
                "$\\text{Slope}_{adiabatic} = -\\gamma \\times \\text{Slope}_{isothermal}$"
            ],
            "correct_idx": 0,
            "explanation": "For isothermal process: $P V = C \\implies dP/dV = -P/V$.\\nFor adiabatic process: $P V^\\gamma = C \\implies dP/dV = -\\gamma (P/V) = \\gamma (dP/dV)_{isothermal}$.\\nThus, the adiabatic slope is $\\gamma$ times steeper."
        }
    ],

    # Chemistry - Chemical & Ionic Equilibrium
    "pH of Strong/Weak Acids & Bases": [
        {
            "q": "The pH of a $10^{-8}\\text{ M } \\text{HCl}$ aqueous solution at $25^\\circ\\text{C}$ is:",
            "options": [
                "Between 6 and 7 (approx 6.96)",
                "$8.0$",
                "$7.0$",
                "Between 8 and 9"
            ],
            "correct_idx": 0,
            "explanation": "At such low concentration, the auto-ionization of water ($[\\text{H}^+]_{w} = 10^{-7}\\text{ M}$) cannot be neglected.\\n$[\\text{H}^+]_{total} = [\\text{H}^+]_{HCl} + [\\text{H}^+]_{H_2O} = 10^{-8} + x$.\\nFrom $K_w = [\\text{H}^+][\\text{OH}^-] = (10^{-8} + x)x = 10^{-14} \\implies x \\approx 0.95 \\times 10^{-7}$.\\n$[\\text{H}^+]_{total} \\approx 1.05 \\times 10^{-7}\\text{ M} \\implies \\text{pH} = -\\log(1.05 \\times 10^{-7}) \\approx 6.96$ (strictly acidic, $< 7$)."
        }
    ],
    "Le Chatelier's Principle & Factors": [
        {
            "q": "For the equilibrium $\\text{PCl}_5(g) \\rightleftharpoons \\text{PCl}_3(g) + \\text{Cl}_2(g)$, the addition of an inert gas at constant pressure causes:",
            "options": [
                "Dissociation of $\\text{PCl}_5$ to increase (shifts forward)",
                "Dissociation of $\\text{PCl}_5$ to decrease (shifts backward)",
                "No change in equilibrium position",
                "Equilibrium constant $K_p$ to increase"
            ],
            "correct_idx": 0,
            "explanation": "Adding an inert gas at constant pressure increases the total volume of the container, which lowers the partial pressures of reacting gases. According to Le Chatelier's principle, the system shifts towards the side with more moles of gas ($\\Delta n_g = 2 - 1 = +1$, forward direction)."
        }
    ],

    # Chemistry - GOC
    "Carbocation, Carbanion & Free Radical Stability": [
        {
            "q": "Which of the following carbocations is the MOST stable?",
            "options": [
                "$\\text{Ph}_3\\text{C}^+$ (Triphenylmethyl cation)",
                "$(CH_3)_3\\text{C}^+$ (tert-butyl cation)",
                "$\\text{CH}_2=\\text{CH}-\\text{CH}_2^+$ (Allyl cation)",
                "$\\text{CH}_3\\text{CH}_2^+$ (Ethyl cation)"
            ],
            "correct_idx": 0,
            "explanation": "The triphenylmethyl (trityl) carbocation $\\text{Ph}_3\\text{C}^+$ is stabilized by extensive resonance delocalization across all three phenyl rings (total 10 canonical forms), making it exceptionally stable."
        }
    ],

    # Mathematics - Definite Integration
    "Definite Integral Properties (King's Rule, Queen's Rule)": [
        {
            "q": "The value of the definite integral $\\int_{-2}^{2} (x^5 + x^3 \\cos(x) + \\sin(x) + 3) \\, dx$ is:",
            "options": ["$12$", "$0$", "$6$", "$24$"],
            "correct_idx": 0,
            "explanation": "The integrand functions $x^5$, $x^3 \\cos(x)$, and $\\sin(x)$ are all odd functions ($f(-x) = -f(x)$). Their integrals over the symmetric interval $[-2, 2]$ vanish to zero.\\nTherefore, $\\int_{-2}^{2} (x^5 + x^3\\cos x + \\sin x + 3) dx = \\int_{-2}^2 3 \\, dx = 3 [2 - (-2)] = 3 \\times 4 = 12$."
        }
    ],
    "Limits Evaluation (L'Hopital, Standard Expansions)": [
        {
            "q": "Evaluate $\\lim_{x \\to 0} \\frac{1 - \\cos(4x)}{x^2}$:",
            "options": ["$8$", "$4$", "$16$", "$2$"],
            "correct_idx": 0,
            "explanation": "Recall standard limit $\\lim_{u \\to 0} \\frac{1 - \\cos u}{u^2} = \\frac{1}{2}$.\\nHere $u = 4x$. $\\frac{1 - \\cos(4x)}{x^2} = \\frac{1 - \\cos(4x)}{(4x)^2} \\times 16 \\to \\frac{1}{2} \\times 16 = 8$."
        }
    ],
    "Monotonicity (Increasing / Decreasing Functions)": [
        {
            "q": "The function $f(x) = 2x^3 - 9x^2 + 12x + 5$ is strictly decreasing in the interval:",
            "options": ["$(1, 2)$", "$(0, 1)$", "$(2, 3)$", "$(-\\infty, 1)$"],
            "correct_idx": 0,
            "explanation": "$f'(x) = 6x^2 - 18x + 12 = 6(x^2 - 3x + 2) = 6(x - 1)(x - 2)$.\\nFor strictly decreasing, $f'(x) < 0 \\implies 6(x - 1)(x - 2) < 0 \\implies x \\in (1, 2)$."
        }
    ]
}

def get_chapters_summary():
    """Returns all chapters with subject, class, tests taken, and status."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
    SELECT c.id, c.subject, c.name, c.class_level, c.ncert_order, c.importance, c.tests_given, c.last_score_pct, c.mastery_status,
           COUNT(DISTINCT t.id) as topic_count
    FROM chapters c
    LEFT JOIN topics t ON c.id = t.chapter_id
    GROUP BY c.id
    ORDER BY c.subject, c.class_level, c.ncert_order, c.id
    """)
    rows = cursor.fetchall()

    chapters = []
    for r in rows:
        cursor.execute("SELECT name FROM topics WHERE chapter_id = ?", (r["id"],))
        topics = [t["name"] for t in cursor.fetchall()]
        chapters.append({
            "id": r["id"],
            "subject": r["subject"],
            "name": r["name"],
            "class_level": r["class_level"],
            "ncert_order": r["ncert_order"],
            "importance": r["importance"],
            "tests_given": r["tests_given"],
            "last_score_pct": r["last_score_pct"],
            "mastery_status": r["mastery_status"],
            "topics": topics
        })
    conn.close()
    return chapters

def get_chapter_by_id(chapter_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM chapters WHERE id = ?", (chapter_id,))
    chapter = cursor.fetchone()
    conn.close()
    return dict(chapter) if chapter else None

def get_topics_for_chapter(chapter_name):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
    SELECT t.name, COALESCE(ta.status, 'Untested') as status,
           COALESCE(ta.accuracy, 0) as accuracy, COALESCE(ta.attempts, 0) as attempts
    FROM topics t
    JOIN chapters c ON t.chapter_id = c.id
    LEFT JOIN topic_analytics ta ON ta.chapter_name = c.name AND ta.topic_name = t.name
    WHERE c.name = ?
    ORDER BY t.name
    """, (chapter_name,))
    topics = [dict(r) for r in cursor.fetchall()]
    conn.close()
    return topics

def get_all_weak_topics():
    """Retrieve all weak topics identified across all tests."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
    SELECT ta.chapter_name, ta.topic_name, ta.subject, ta.attempts, ta.correct, ta.accuracy, ta.status
    FROM topic_analytics ta
    WHERE ta.status = 'Weak' OR (ta.attempts > 0 AND ta.accuracy < 60)
    ORDER BY ta.accuracy ASC, ta.attempts DESC
    """)
    weak = [dict(r) for r in cursor.fetchall()]
    conn.close()
    return weak

def generate_test(chapter_name=None, topic_filter=None, exam_type="JEE Main", count=5, weak_only=False):
    """
    Prepares a test for the given chapter and optional topics.
    Draws from database and template fallback to guarantee the requested question count.
    """
    conn = get_connection()
    cursor = conn.cursor()

    conditions = []
    params = []

    if chapter_name and not weak_only:
        conditions.append("c.name = ?")
        params.append(chapter_name)

    if topic_filter:
        conditions.append("q.topic_name = ?")
        params.append(topic_filter)

    if exam_type in ["Basic", "Basic (Marks)"]:
        conditions.append("q.level IN ('Basic', 'JEE Main')")
        order_clause = "ORDER BY CASE WHEN q.level = 'Basic' THEN 0 ELSE 1 END, RANDOM()"
    elif exam_type == "JEE Advanced":
        conditions.append("q.level IN ('JEE Advanced', 'JEE Main')")
        order_clause = "ORDER BY CASE WHEN q.level = 'JEE Advanced' THEN 0 ELSE 1 END, RANDOM()"
    else: # Default JEE Main
        conditions.append("q.level IN ('JEE Main', 'Basic')")
        order_clause = "ORDER BY CASE WHEN q.level = 'JEE Main' THEN 0 ELSE 1 END, RANDOM()"

    where_clause = " WHERE " + " AND ".join(conditions) if conditions else ""

    query = f"""
    SELECT q.id, q.topic_name, q.level, q.type, q.question, q.options_json,
           q.correct_answer, q.correct_index, q.explanation, c.name as chapter_name, c.subject
    FROM questions q
    JOIN chapters c ON q.chapter_id = c.id
    {where_clause}
    {order_clause}
    """

    cursor.execute(query, params)
    raw_questions = cursor.fetchall()
    
    selected_questions = []
    for r in raw_questions:
        selected_questions.append({
            "id": r["id"],
            "chapter_name": r["chapter_name"],
            "subject": r["subject"],
            "topic_name": r["topic_name"],
            "level": r["level"],
            "type": r["type"],
            "question": r["question"],
            "options": json.loads(r["options_json"]),
            "correct_answer": r["correct_answer"],
            "correct_index": r["correct_index"],
            "explanation": r["explanation"]
        })
        if len(selected_questions) >= count:
            break

    # If count not met, fill with dynamic template questions
    if len(selected_questions) < count:
        needed = count - len(selected_questions)
        conn.close()
        synthesized = synthesize_supplementary_questions(chapter_name, needed, exam_type, topic_filter=topic_filter)
        selected_questions.extend(synthesized)
    else:
        conn.close()

    # Re-shuffle question order
    random.shuffle(selected_questions)
    return selected_questions[:count]

def synthesize_supplementary_questions(chapter_name, needed, exam_type, topic_filter=None):
    """Generates supplementary standard JEE questions for topics."""
    synthesized = []
    conn = get_connection()
    cursor = conn.cursor()

    subject = "Physics"
    topics = []

    if topic_filter:
        topics = [topic_filter]
        cursor.execute("""
        SELECT c.name as chap_name, c.subject
        FROM topics t
        JOIN chapters c ON t.chapter_id = c.id
        WHERE t.name = ?
        LIMIT 1
        """, (topic_filter,))
        row = cursor.fetchone()
        if row:
            chapter_name = row["chap_name"]
            subject = row["subject"]
    elif chapter_name:
        cursor.execute("SELECT subject FROM chapters WHERE name = ?", (chapter_name,))
        row = cursor.fetchone()
        subject = row["subject"] if row else "Physics"
        cursor.execute("""
        SELECT t.name FROM topics t
        JOIN chapters c ON t.chapter_id = c.id
        WHERE c.name = ?
        """, (chapter_name,))
        topics = [r["name"] for r in cursor.fetchall()]
    else:
        subject = "Physics"
        topics = ["General JEE Concepts"]
    conn.close()

    for i in range(needed):
        chosen_topic = random.choice(topics) if topics else "Key Concepts"
        # Check if topic has template
        if chosen_topic in TOPIC_TEMPLATES:
            tpl = random.choice(TOPIC_TEMPLATES[chosen_topic])
            if "options" in tpl:
                q_data = {
                    "id": f"syn_{i}_{random.randint(1000, 9999)}",
                    "chapter_name": chapter_name or "JEE Core Practice",
                    "subject": subject,
                    "topic_name": chosen_topic,
                    "level": exam_type,
                    "type": "mcq_single",
                    "question": tpl["q"],
                    "options": tpl["options"],
                    "correct_answer": tpl["options"][tpl["correct_idx"]],
                    "correct_index": tpl["correct_idx"],
                    "explanation": tpl["explanation"]
                }
                synthesized.append(q_data)
                continue

        # Fallback parameterized standard question based on subject
        val1 = random.choice([2, 4, 6, 8])
        val2 = random.choice([3, 5, 7])
        ratio = round(val1 / val2, 2)
        inv_ratio = round(val2 / val1, 2)
        prod = val1 * val2
        sum_val = val1 + val2

        if subject == "Mathematics":
            question_text = f"In a standard JEE problem concerning **{chosen_topic}**, consider the mathematical function or configuration with parameters $a = {val1}$ and $b = {val2}$. Under standard algebraic constraints, evaluate the fundamental quantity $\\frac{{a}}{{b}}$:"
            explanation_text = f"Applying standard formulation for {chosen_topic}:\\nThe ratio is evaluated as $\\frac{{a}}{{b}} = \\frac{{{val1}}}{{{val2}}} \\approx {ratio}$."
        elif subject == "Chemistry":
            question_text = f"In a standard JEE conceptual analysis of **{chosen_topic}**, a reaction or molecular system has stoichiometric factor $\\alpha = {val1}$ and activity quotient $\\beta = {val2}$. The characteristic thermodynamic ratio is given by:"
            explanation_text = f"Applying standard chemical principles for {chosen_topic}:\\nThe equilibrium/stoichiometric quotient evaluates to $\\frac{{\\alpha}}{{\\beta}} = \\frac{{{val1}}}{{{val2}}} \\approx {ratio}$."
        else:
            question_text = f"In a standard JEE problem concerning **{chosen_topic}**, a physical system has initial parameter $\\alpha = {val1}$ and interaction factor $\\beta = {val2}$. If the conservation principle holds strictly, the resultant dimensionless quotient is:"
            explanation_text = f"Applying standard formulation for {chosen_topic}:\\nThe ratio is evaluated as $\\frac{{\\alpha}}{{\\beta}} = \\frac{{{val1}}}{{{val2}}} \\approx {ratio}$."

        q_data = {
            "id": f"syn_{i}_{random.randint(1000, 9999)}",
            "chapter_name": chapter_name or "JEE Core Practice",
            "subject": subject,
            "topic_name": chosen_topic,
            "level": exam_type,
            "type": "mcq_single",
            "question": question_text,
            "options": [
                f"${ratio}$",
                f"${inv_ratio}$",
                f"${prod}$",
                f"${sum_val}$"
            ],
            "correct_answer": f"{ratio}",
            "correct_index": 0,
            "explanation": explanation_text
        }
        synthesized.append(q_data)

    return synthesized

def submit_test_evaluation(submission):
    """
    Evaluates test responses:
    - Calculates score (+4 / -1 JEE standard marking)
    - Computes topic-wise accuracy
    - Labels Weak, Moderate, Strong topics
    - Updates database records
    """
    chapter_name = submission.get("chapter_name")
    subject = submission.get("subject", "General")
    exam_type = submission.get("exam_type", "JEE Main")
    time_taken = submission.get("time_taken_seconds", 0)
    answers = submission.get("answers", []) # list of {question_id, topic_name, user_answer, correct_index, explanation, ...}

    total_questions = len(answers)
    correct_count = 0
    incorrect_count = 0
    unattempted_count = 0

    topic_stats = {} # topic_name: {"total": 0, "correct": 0, "incorrect": 0}

    detailed_results = []

    for ans in answers:
        topic = ans.get("topic_name", "General")
        user_choice = ans.get("user_choice") # index or string
        correct_index = ans.get("correct_index", 0)
        
        if topic not in topic_stats:
            topic_stats[topic] = {"total": 0, "correct": 0, "incorrect": 0, "unattempted": 0}
        
        topic_stats[topic]["total"] += 1

        is_correct = False
        if user_choice is None or user_choice == "" or user_choice == -1:
            unattempted_count += 1
            topic_stats[topic]["unattempted"] += 1
            status = "unattempted"
        elif int(user_choice) == int(correct_index):
            correct_count += 1
            topic_stats[topic]["correct"] += 1
            is_correct = True
            status = "correct"
        else:
            incorrect_count += 1
            topic_stats[topic]["incorrect"] += 1
            status = "incorrect"

        detailed_results.append({
            "question_id": ans.get("id"),
            "question": ans.get("question"),
            "topic_name": topic,
            "user_choice": user_choice,
            "correct_index": correct_index,
            "options": ans.get("options", []),
            "is_correct": is_correct,
            "status": status,
            "explanation": ans.get("explanation", "")
        })

    # Standard JEE marking: +4 for correct, -1 for incorrect, 0 for unattempted
    score = (correct_count * 4) - (incorrect_count * 1)
    max_score = total_questions * 4
    accuracy = round((correct_count / (correct_count + incorrect_count) * 100), 1) if (correct_count + incorrect_count) > 0 else 0.0

    # Categorize Weak Topics
    weak_topics = []
    moderate_topics = []
    strong_topics = []

    conn = get_connection()
    cursor = conn.cursor()

    for t_name, stats in topic_stats.items():
        t_acc = (stats["correct"] / stats["total"]) * 100 if stats["total"] > 0 else 0
        topic_info = {
            "topic_name": t_name,
            "total": stats["total"],
            "correct": stats["correct"],
            "incorrect": stats["incorrect"],
            "accuracy": round(t_acc, 1)
        }

        # Rule for Weak Topic: Accuracy < 50% OR at least 1 incorrect attempt
        if stats["incorrect"] > 0 or t_acc < 50:
            topic_info["status"] = "Weak"
            topic_info["recommendation"] = "High priority revision required. Formula & concept review recommended."
            weak_topics.append(topic_info)
        elif t_acc >= 75:
            topic_info["status"] = "Strong"
            topic_info["recommendation"] = "Concept solid. Maintain speed with timed problem solving."
            strong_topics.append(topic_info)
        else:
            topic_info["status"] = "Moderate"
            topic_info["recommendation"] = "Fair understanding. Review edge cases and calculation speed."
            moderate_topics.append(topic_info)

        # Update topic_analytics in DB
        cursor.execute("""
        INSERT INTO topic_analytics (chapter_name, topic_name, subject, attempts, correct, accuracy, status, last_tested)
        VALUES (?, ?, ?, ?, ?, ?, ?, CURRENT_TIMESTAMP)
        ON CONFLICT(chapter_name, topic_name) DO UPDATE SET
            attempts = attempts + excluded.attempts,
            correct = correct + excluded.correct,
            accuracy = ROUND(((correct + excluded.correct) * 100.0 / (attempts + excluded.attempts)), 1),
            status = CASE
                WHEN ROUND(((correct + excluded.correct) * 100.0 / (attempts + excluded.attempts)), 1) < 50 THEN 'Weak'
                WHEN ROUND(((correct + excluded.correct) * 100.0 / (attempts + excluded.attempts)), 1) >= 75 THEN 'Strong'
                ELSE 'Moderate'
            END,
            last_tested = CURRENT_TIMESTAMP
        """, (
            chapter_name,
            t_name,
            subject,
            stats["total"],
            stats["correct"],
            t_acc,
            topic_info["status"]
        ))

    # Save test attempt in DB
    cursor.execute("SELECT id FROM chapters WHERE name = ?", (chapter_name,))
    chap_row = cursor.fetchone()
    chapter_id = chap_row["id"] if chap_row else 1

    cursor.execute("""
    INSERT INTO test_attempts (chapter_id, chapter_name, subject, exam_type, total_questions, correct_count, incorrect_count, unattempted_count, score, max_score, accuracy, time_taken_seconds, weak_topics_json)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        chapter_id,
        chapter_name,
        subject,
        exam_type,
        total_questions,
        correct_count,
        incorrect_count,
        unattempted_count,
        score,
        max_score,
        accuracy,
        time_taken,
        json.dumps(weak_topics)
    ))
    test_id = cursor.lastrowid

    # Update chapter tests_given, last_score_pct, mastery_status
    score_pct = round((score / max_score) * 100, 1) if max_score > 0 else 0.0
    mastery = "Proficient" if score_pct >= 75 else ("Needs Revision" if score_pct < 45 else "Developing")

    cursor.execute("""
    UPDATE chapters
    SET tests_given = tests_given + 1,
        last_score_pct = ?,
        mastery_status = ?
    WHERE id = ?
    """, (score_pct, mastery, chapter_id))

    conn.commit()
    conn.close()

    return {
        "test_id": test_id,
        "chapter_name": chapter_name,
        "subject": subject,
        "exam_type": exam_type,
        "total_questions": total_questions,
        "correct_count": correct_count,
        "incorrect_count": incorrect_count,
        "unattempted_count": unattempted_count,
        "score": score,
        "max_score": max_score,
        "score_pct": score_pct,
        "accuracy": accuracy,
        "time_taken_seconds": time_taken,
        "weak_topics": weak_topics,
        "moderate_topics": moderate_topics,
        "strong_topics": strong_topics,
        "detailed_results": detailed_results
    }
