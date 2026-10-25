"""
quadratic_notes_full.py - Complete 6-Page Notebook Cheat-Sheet Collection for
'Quadratic Equations & Expressions', transcribed with exact fidelity from the user's
uploaded handwritten ruled notebook notes.
"""

def generate_quadratic_svg_page1():
    """Page 1 graphical view: 3 parabolas for D > 0, D = 0, D < 0."""
    return """
    <svg viewBox="0 0 460 160" class="w-full h-auto max-w-[450px] mx-auto select-none" xmlns="http://www.w3.org/2000/svg">
      <!-- D > 0 -->
      <g transform="translate(10, 5)">
        <line x1="5" y1="85" x2="135" y2="85" stroke="#475569" stroke-width="1.5"/>
        <line x1="70" y1="130" x2="70" y2="10" stroke="#475569" stroke-width="1.5"/>
        <text x="138" y="89" font-size="10" font-weight="bold" fill="#334155">x</text>
        <text x="67" y="9" font-size="10" font-weight="bold" fill="#334155">y</text>
        <path d="M 20 20 Q 70 135 120 20" fill="none" stroke="#2563eb" stroke-width="2.5"/>
        <text x="36" y="100" font-size="11" font-weight="bold" fill="#1e40af">α</text>
        <text x="96" y="100" font-size="11" font-weight="bold" fill="#1e40af">β</text>
        <text x="70" y="142" font-size="11" font-weight="bold" text-anchor="middle" fill="#0f172a">D > 0</text>
        <text x="70" y="154" font-size="9" text-anchor="middle" fill="#475569">(two real roots)</text>
      </g>
      <!-- D = 0 -->
      <g transform="translate(160, 5)">
        <line x1="5" y1="85" x2="135" y2="85" stroke="#475569" stroke-width="1.5"/>
        <line x1="70" y1="130" x2="70" y2="10" stroke="#475569" stroke-width="1.5"/>
        <text x="138" y="89" font-size="10" font-weight="bold" fill="#334155">x</text>
        <text x="67" y="9" font-size="10" font-weight="bold" fill="#334155">y</text>
        <path d="M 20 20 Q 70 85 120 20" fill="none" stroke="#2563eb" stroke-width="2.5"/>
        <circle cx="70" cy="85" r="3.5" fill="#2563eb"/>
        <text x="70" y="100" font-size="9" font-weight="bold" text-anchor="middle" fill="#1e40af">-b/(2a)</text>
        <text x="70" y="142" font-size="11" font-weight="bold" text-anchor="middle" fill="#0f172a">D = 0</text>
        <text x="70" y="154" font-size="9" text-anchor="middle" fill="#475569">(equal roots)</text>
      </g>
      <!-- D < 0 -->
      <g transform="translate(310, 5)">
        <line x1="5" y1="85" x2="135" y2="85" stroke="#475569" stroke-width="1.5"/>
        <line x1="70" y1="130" x2="70" y2="10" stroke="#475569" stroke-width="1.5"/>
        <text x="138" y="89" font-size="10" font-weight="bold" fill="#334155">x</text>
        <text x="67" y="9" font-size="10" font-weight="bold" fill="#334155">y</text>
        <path d="M 20 20 Q 70 50 120 20" fill="none" stroke="#2563eb" stroke-width="2.5"/>
        <text x="70" y="142" font-size="11" font-weight="bold" text-anchor="middle" fill="#0f172a">D < 0</text>
        <text x="70" y="154" font-size="9" text-anchor="middle" fill="#475569">(no real roots)</text>
      </g>
    </svg>
    """

def generate_quadratic_svg_page5():
    """Page 5 graphical view: 6 parabolas (a > 0 row and a < 0 row)."""
    return """
    <svg viewBox="0 0 460 210" class="w-full h-auto max-w-[450px] mx-auto select-none" xmlns="http://www.w3.org/2000/svg">
      <!-- Row 1: a > 0 -->
      <g transform="translate(10, 5)">
        <line x1="5" y1="55" x2="135" y2="55" stroke="#64748b" stroke-width="1.5"/>
        <line x1="70" y1="85" x2="70" y2="5" stroke="#64748b" stroke-width="1.5"/>
        <path d="M 20 15 Q 70 85 120 15" fill="none" stroke="#2563eb" stroke-width="2"/>
        <text x="36" y="66" font-size="9" font-weight="bold" fill="#1e40af">α</text>
        <text x="96" y="66" font-size="9" font-weight="bold" fill="#1e40af">β</text>
        <text x="70" y="96" font-size="9" font-weight="bold" text-anchor="middle" fill="#0f172a">a > 0, D > 0</text>
        <text x="70" y="106" font-size="8" text-anchor="middle" fill="#2563eb">(+, -, +)</text>
      </g>
      <g transform="translate(160, 5)">
        <line x1="5" y1="55" x2="135" y2="55" stroke="#64748b" stroke-width="1.5"/>
        <line x1="70" y1="85" x2="70" y2="5" stroke="#64748b" stroke-width="1.5"/>
        <path d="M 20 15 Q 70 55 120 15" fill="none" stroke="#2563eb" stroke-width="2"/>
        <circle cx="70" cy="55" r="2.5" fill="#2563eb"/>
        <text x="70" y="96" font-size="9" font-weight="bold" text-anchor="middle" fill="#0f172a">a > 0, D = 0</text>
        <text x="70" y="106" font-size="8" text-anchor="middle" fill="#2563eb">(+, 0, +)</text>
      </g>
      <g transform="translate(310, 5)">
        <line x1="5" y1="55" x2="135" y2="55" stroke="#64748b" stroke-width="1.5"/>
        <line x1="70" y1="85" x2="70" y2="5" stroke="#64748b" stroke-width="1.5"/>
        <path d="M 20 15 Q 70 35 120 15" fill="none" stroke="#2563eb" stroke-width="2"/>
        <text x="70" y="96" font-size="9" font-weight="bold" text-anchor="middle" fill="#0f172a">a > 0, D < 0</text>
        <text x="70" y="106" font-size="8" text-anchor="middle" fill="#2563eb">(+, +)</text>
      </g>
      <!-- Row 2: a < 0 -->
      <g transform="translate(10, 110)">
        <line x1="5" y1="40" x2="135" y2="40" stroke="#64748b" stroke-width="1.5"/>
        <line x1="70" y1="85" x2="70" y2="5" stroke="#64748b" stroke-width="1.5"/>
        <path d="M 20 75 Q 70 5 120 75" fill="none" stroke="#dc2626" stroke-width="2"/>
        <text x="36" y="36" font-size="9" font-weight="bold" fill="#b91c1c">α</text>
        <text x="96" y="36" font-size="9" font-weight="bold" fill="#b91c1c">β</text>
        <text x="70" y="96" font-size="9" font-weight="bold" text-anchor="middle" fill="#0f172a">a < 0, D > 0</text>
        <text x="70" y="106" font-size="8" text-anchor="middle" fill="#dc2626">(-, +, -)</text>
      </g>
      <g transform="translate(160, 110)">
        <line x1="5" y1="40" x2="135" y2="40" stroke="#64748b" stroke-width="1.5"/>
        <line x1="70" y1="85" x2="70" y2="5" stroke="#64748b" stroke-width="1.5"/>
        <path d="M 20 75 Q 70 40 120 75" fill="none" stroke="#dc2626" stroke-width="2"/>
        <circle cx="70" cy="40" r="2.5" fill="#dc2626"/>
        <text x="70" y="96" font-size="9" font-weight="bold" text-anchor="middle" fill="#0f172a">a < 0, D = 0</text>
        <text x="70" y="106" font-size="8" text-anchor="middle" fill="#dc2626">(-, 0, -)</text>
      </g>
      <g transform="translate(310, 110)">
        <line x1="5" y1="40" x2="135" y2="40" stroke="#64748b" stroke-width="1.5"/>
        <line x1="70" y1="85" x2="70" y2="5" stroke="#64748b" stroke-width="1.5"/>
        <path d="M 20 75 Q 70 60 120 75" fill="none" stroke="#dc2626" stroke-width="2"/>
        <text x="70" y="96" font-size="9" font-weight="bold" text-anchor="middle" fill="#0f172a">a < 0, D < 0</text>
        <text x="70" y="106" font-size="8" text-anchor="middle" fill="#dc2626">(-, -)</text>
      </g>
    </svg>
    """

def generate_quadratic_svg_page7():
    """Page 7 graphical view: Modulus parabola y = |f(x)| folded over x-axis with line y = k cutting at 4 roots."""
    return """
    <svg viewBox="0 0 460 160" class="w-full h-auto max-w-[450px] mx-auto select-none" xmlns="http://www.w3.org/2000/svg">
      <line x1="20" y1="120" x2="440" y2="120" stroke="#475569" stroke-width="1.8"/>
      <line x1="230" y1="150" x2="230" y2="10" stroke="#475569" stroke-width="1.5"/>
      <text x="442" y="124" font-size="10" font-weight="bold" fill="#334155">x</text>
      <text x="225" y="10" font-size="10" font-weight="bold" fill="#334155">y</text>
      
      <!-- Folded parabola y = |ax^2 + bx + c| -->
      <path d="M 60 20 Q 110 120 145 120 Q 230 40 315 120 Q 350 120 400 20" fill="none" stroke="#2563eb" stroke-width="2.8"/>
      
      <!-- Ghost original below axis -->
      <path d="M 145 120 Q 230 200 315 120" fill="none" stroke="#94a3b8" stroke-width="1.5" stroke-dasharray="3,3"/>
      
      <!-- Line y = k -->
      <line x1="30" y1="75" x2="430" y2="75" stroke="#dc2626" stroke-width="1.8" stroke-dasharray="4,2"/>
      <text x="432" y="72" font-size="10" font-weight="bold" fill="#dc2626">y = k</text>
      
      <!-- 4 intersection dots -->
      <circle cx="85" cy="75" r="3.5" fill="#dc2626"/>
      <circle cx="178" cy="75" r="3.5" fill="#dc2626"/>
      <circle cx="282" cy="75" r="3.5" fill="#dc2626"/>
      <circle cx="375" cy="75" r="3.5" fill="#dc2626"/>
      <text x="85" y="65" font-size="9" font-weight="bold" text-anchor="middle" fill="#991b1b">x₁</text>
      <text x="178" y="65" font-size="9" font-weight="bold" text-anchor="middle" fill="#991b1b">x₂</text>
      <text x="282" y="65" font-size="9" font-weight="bold" text-anchor="middle" fill="#991b1b">x₃</text>
      <text x="375" y="65" font-size="9" font-weight="bold" text-anchor="middle" fill="#991b1b">x₄</text>
      
      <!-- Apex of fold -->
      <circle cx="230" cy="55" r="3" fill="#059669"/>
      <text x="230" y="42" font-size="9" font-weight="bold" text-anchor="middle" fill="#047857">Peak = |D|/(4a)</text>
      
      <!-- Roots alpha, beta -->
      <circle cx="145" cy="120" r="3" fill="#1e40af"/>
      <text x="145" y="135" font-size="10" font-weight="bold" text-anchor="middle" fill="#1e40af">α</text>
      <circle cx="315" cy="120" r="3" fill="#1e40af"/>
      <text x="315" y="135" font-size="10" font-weight="bold" text-anchor="middle" fill="#1e40af">β</text>
      
      <text x="230" y="152" font-size="9" font-weight="bold" text-anchor="middle" fill="#1e293b">4 distinct roots when 0 &lt; k &lt; |D|/(4a)</text>
    </svg>
    """

def generate_quadratic_svg_page8():
    """Page 8 graphical view: Rational quadratic y = (x^2-x+1)/(x^2+x+1) bounded between y_min and y_max with asymptote."""
    return """
    <svg viewBox="0 0 460 160" class="w-full h-auto max-w-[450px] mx-auto select-none" xmlns="http://www.w3.org/2000/svg">
      <line x1="20" y1="90" x2="440" y2="90" stroke="#475569" stroke-width="1.8"/>
      <line x1="230" y1="150" x2="230" y2="10" stroke="#475569" stroke-width="1.5"/>
      <text x="442" y="94" font-size="10" font-weight="bold" fill="#334155">x</text>
      <text x="225" y="10" font-size="10" font-weight="bold" fill="#334155">y</text>
      
      <!-- Horizontal Asymptote y = 1 -->
      <line x1="20" y1="80" x2="440" y2="80" stroke="#64748b" stroke-width="1.2" stroke-dasharray="4,3"/>
      <text x="35" y="75" font-size="9" font-weight="bold" fill="#475569">Asymptote y = 1 (a₁/a₂)</text>
      
      <!-- Max bound y = 3 -->
      <line x1="80" y1="30" x2="380" y2="30" stroke="#059669" stroke-width="1.2" stroke-dasharray="2,2"/>
      <circle cx="160" cy="30" r="3.5" fill="#059669"/>
      <text x="160" y="22" font-size="9" font-weight="bold" text-anchor="middle" fill="#047857">Max y = 3 (at x = -1)</text>
      
      <!-- Min bound y = 1/3 -->
      <line x1="80" y1="125" x2="380" y2="125" stroke="#dc2626" stroke-width="1.2" stroke-dasharray="2,2"/>
      <circle cx="300" cy="125" r="3.5" fill="#dc2626"/>
      <text x="300" y="142" font-size="9" font-weight="bold" text-anchor="middle" fill="#b91c1c">Min y = 1/3 (at x = 1)</text>
      
      <!-- Smooth rational curve -->
      <path d="M 40 82 C 100 80, 130 30, 160 30 C 200 30, 250 125, 300 125 C 340 125, 380 80, 430 80" 
            fill="none" stroke="#7c3aed" stroke-width="2.8"/>
            
      <text x="230" y="155" font-size="9" font-weight="bold" text-anchor="middle" fill="#1e3a8a">Real x ⟹ Discriminant D_x ≥ 0 ⟹ y ∈ [1/3, 3]</text>
    </svg>
    """

# =========================================================================
# ALL 8 PAGES TRANSCRIBED EXACTLY FROM USER'S IMAGES & HIGH-YIELD JEE CURRICULUM
# =========================================================================

QUADRATIC_SHEETS = [
    # ---------------------------------------------------------------------
    # PAGE 1: Nature of Roots & Discriminant
    # ---------------------------------------------------------------------
    {
        "page_number": 1,
        "sheet_title": "Nature of Roots & Discriminant",
        "chapter": "Quadratic Equations & Expressions",
        "subject": "Mathematics",
        "class_level": 11,
        "ncert_ref": "Class 11, Chapter 5 • Sheet 1 of 6",
        "importance": "Very High",
        "mnemonic_banner": "Discriminant tells the nature... Coefficients tell the location...",
        "classification_heading": "2. Nature of Roots",
        "parameter_heading": "3. Roots in Terms of Discriminant",
        "important_points_heading": "4. Properties & Important Points",
        "introduction": "For a quadratic equation $ax^2 + bx + c = 0$ ($a \\ne 0$), the nature of roots depends on the discriminant $D = b^2 - 4ac$.",
        "classification_cases": [
            {
                "badge": "1) If D > 0",
                "title": "Two Distinct Real Roots",
                "condition": "D > 0",
                "description": "Two distinct real roots (unequal & real).",
                "range": "\\alpha, \\beta = \\frac{-b \\pm \\sqrt{D}}{2a}",
                "consequence": "Parabola intersects the x-axis at two distinct real points $\\alpha$ and $\\beta$."
            },
            {
                "badge": "2) If D = 0",
                "title": "Two Equal Real Roots",
                "condition": "D = 0",
                "description": "Two equal real roots (repeated roots).",
                "range": "\\alpha = \\beta = -\\frac{b}{2a}",
                "consequence": "Parabola touches the x-axis at its vertex $\\left(-\\frac{b}{2a}, 0\\right)$."
            },
            {
                "badge": "3) If D < 0",
                "title": "No Real Roots (Complex Conjugates)",
                "condition": "D < 0",
                "description": "No real roots (complex conjugate roots).",
                "range": "\\alpha, \\beta = -\\frac{b}{2a} \\pm i\\frac{\\sqrt{-D}}{2a}",
                "consequence": "Parabola does not intersect the x-axis (lies entirely above or entirely below)."
            }
        ],
        "parameter_analysis": [
            {
                "parameter": "If D > 0",
                "sub_cases": [
                    {"cond": "\\alpha, \\beta = \\frac{-b \\pm \\sqrt{D}}{2a}", "res": "Real & distinct roots."}
                ]
            },
            {
                "parameter": "If D = 0",
                "sub_cases": [
                    {"cond": "\\alpha = \\beta = -\\frac{b}{2a}", "res": "Real & equal (repeated) roots."}
                ]
            },
            {
                "parameter": "If D < 0",
                "sub_cases": [
                    {"cond": "\\alpha, \\beta = -\\frac{b}{2a} \\pm i\\frac{\\sqrt{-D}}{2a}", "res": "Complex conjugate pair ($i = \\sqrt{-1}$)."}
                ]
            }
        ],
        "graphical_view": {
            "title": "5. Graphical View: Consider y = ax^2 + bx + c (a ≠ 0)",
            "vertex_formula": "Vertex is located at $\\left(-\\frac{b}{2a}, -\\frac{D}{4a}\\right)$.",
            "observations": [
                "If $D > 0$: Parabola cuts x-axis at two points (two real roots).",
                "If $D = 0$: Parabola touches x-axis (vertex on x-axis, equal roots).",
                "If $D < 0$: Parabola does not intersect x-axis (no real roots)."
            ],
            "svg_diagram": generate_quadratic_svg_page1()
        },
        "special_cases": [
            "1) If $a + b + c = 0 \\implies x = 1$ is a root (since $1 + b + c = 0$).",
            "2) If $a - b + c = 0 \\implies x = -1$ is a root (since $1 - b + c = 0$).",
            "3) If $c = 0 \\implies$ roots are $x = 0$ and $x = -b/a$.",
            "4) If $a + c = b \\implies$ one root is $x = -1$ (since $a - b + c = 0$)."
        ],
        "important_points": [
            "For real roots, $D \\ge 0 \\iff (b^2 - 4ac) \\ge 0$.",
            "For real and distinct roots, $D > 0$.",
            "For equal roots, $D = 0 \\implies$ parabola touches x-axis (vertex on x-axis).",
            "For no real roots, $D < 0 \\implies$ parabola does not intersect x-axis.",
            "If $D \\ge 0$, sum of roots $= -b/a$, product of roots $= c/a$.",
            "If $D < 0$, roots are complex conjugates and $\\alpha + \\beta = -b/a, \\alpha\\beta = c/a$ still holds.",
            "★ Remember: Discriminant tells the number and nature of real roots without actually solving the quadratic equation."
        ],
        "quick_tips": [
            "Use $D = b^2 - 4ac$ directly — no need to find roots first.",
            "For equations with parameters, set $D > 0, D = 0$ or $D < 0$ as per question.",
            "If sum and product of roots are given, use $\\alpha + \\beta = -b/a$ and $\\alpha\\beta = c/a$.",
            "For quadratic in $x$, check if $x = 1$ or $x = -1$ is a root using $a+b+c$ or $a-b+c$.",
            "Graphical interpretation helps in quick conceptual understanding."
        ],
        "jee_focus_points": [
            "Concept + Graphs (very important)",
            "Cases with parameters ($k, m,$ etc.)",
            "Roots given conditions (sum, product, relation)",
            "Quick value checking ($x = 1, -1, 0$)",
            "Complex roots and their properties"
        ],
        "traps_and_pitfalls": [
            {
                "trap": "Assuming 'real roots' means D > 0.",
                "why": "Real roots means D ≥ 0, which includes the repeated roots case D = 0.",
                "remedy": "Always set D ≥ 0 for 'real roots' unless the question explicitly specifies 'distinct'."
            }
        ],
        "examples": [
            {
                "title": "(i) Nature of Roots of 2x^2 - 4x + 3 = 0",
                "problem": "Find the nature of roots of $2x^2 - 4x + 3 = 0$.",
                "approach": "Calculate discriminant $D = b^2 - 4ac$.",
                "solution": "$D = b^2 - 4ac = (-4)^2 - 4(2)(3) = 16 - 24 = -8 < 0$.\\n$\\implies$ No real roots (complex conjugate roots).",
                "key_takeaway": "Since $D < 0$, roots are imaginary and form a complex conjugate pair."
            },
            {
                "title": "(ii) Parameter Evaluation for Equal Roots",
                "problem": "Find the values of $k$ for which the equation $kx^2 - 4x + 4 = 0$ has real and equal roots.",
                "approach": "Set discriminant $D = 0$ and check $a \\ne 0$.",
                "solution": "$D = (-4)^2 - 4(k)(4) = 16 - 16k$.\\nFor equal roots, $D = 0 \\implies 16 - 16k = 0 \\implies k = 1$.\\nCheck: for $k = 1$, coefficient $a = 1 \\ne 0$ (valid quadratic).",
                "key_takeaway": "Always verify that the solved parameter does not make the leading coefficient $a$ zero."
            },
            {
                "title": "(iii) Sum and Product Verification for x^2 - 6x + 9 = 0",
                "problem": "If $\\alpha, \\beta$ are roots of $x^2 - 6x + 9 = 0$, find $\\alpha + \\beta$ and $\\alpha\\beta$.",
                "approach": "Calculate $D$ and apply Vieta's formulas.",
                "solution": "$D = (-6)^2 - 4(1)(9) = 36 - 36 = 0 \\implies$ equal roots.\\n$\\alpha + \\beta = -\\frac{b}{a} = -\\frac{-6}{1} = 6, \\quad \\alpha\\beta = \\frac{c}{a} = \\frac{9}{1} = 9$.\\nRoots are $\\alpha = \\beta = 3$.",
                "key_takeaway": "Vieta's relations hold unconditionally whether roots are distinct, equal, or complex."
            }
        ]
    },

    # ---------------------------------------------------------------------
    # PAGE 2: Relations Between Roots & Coefficients
    # ---------------------------------------------------------------------
    {
        "page_number": 2,
        "sheet_title": "Relations Between Roots & Coefficients",
        "chapter": "Quadratic Equations & Expressions",
        "subject": "Mathematics",
        "class_level": 11,
        "ncert_ref": "Class 11, Chapter 5 • Sheet 2 of 6",
        "importance": "Very High",
        "mnemonic_banner": "Practice + Concept = JEE Success",
        "classification_heading": "2. General Form (Quadratic)",
        "parameter_heading": "5. Using Power Sums (Newton's Identities)",
        "important_points_heading": "8. Important Identities",
        "introduction": "For a polynomial equation $ax^2 + bx + c = 0$ with roots $\\alpha$ and $\\beta$, the relations between roots and coefficients are given by $\\alpha + \\beta = -\\frac{b}{a}, \\alpha\\beta = \\frac{c}{a}$. These relations help in finding roots, forming equations, and solving JEE type problems quickly.",
        "classification_cases": [
            {
                "badge": "Quadratic (Degree 2)",
                "title": "ax^2 + bx + c = 0 (a ≠ 0)",
                "condition": "Roots \\alpha, \\beta",
                "description": "Sum of roots $= -\\frac{\\text{coefficient of } x}{\\text{coefficient of } x^2}$, Product $= \\frac{\\text{constant term}}{\\text{coefficient of } x^2}$.",
                "range": "\\alpha + \\beta = -\\frac{b}{a}, \\quad \\alpha\\beta = \\frac{c}{a}",
                "consequence": "Equation can be factored as $a(x - \\alpha)(x - \\beta) = 0$."
            },
            {
                "badge": "Cubic (Degree 3)",
                "title": "ax^3 + bx^2 + cx + d = 0 (a ≠ 0)",
                "condition": "Roots \\alpha, \\beta, \\gamma",
                "description": "Alternating signs for elementary symmetric polynomials.",
                "range": "\\sum \\alpha = -\\frac{b}{a}, \\quad \\sum \\alpha\\beta = \\frac{c}{a}, \\quad \\alpha\\beta\\gamma = -\\frac{d}{a}",
                "consequence": "Forms $x^3 - S_1 x^2 + S_2 x - S_3 = 0$."
            },
            {
                "badge": "Quartic (Degree 4)",
                "title": "ax^4 + bx^3 + cx^2 + dx + e = 0 (a ≠ 0)",
                "condition": "Roots \\alpha, \\beta, \\gamma, \\delta",
                "description": "Four symmetric sums with pattern $(-, +, -, +)$.",
                "range": "\\sum \\alpha = -\\frac{b}{a}, \\; \\sum \\alpha\\beta = \\frac{c}{a}, \\; \\sum \\alpha\\beta\\gamma = -\\frac{d}{a}, \\; \\prod \\alpha = \\frac{e}{a}",
                "consequence": "Forms $x^4 - S_1 x^3 + S_2 x^2 - S_3 x + S_4 = 0$."
            }
        ],
        "parameter_analysis": [
            {
                "parameter": "Power Sums: S_n = α^n + β^n",
                "sub_cases": [
                    {"cond": "\\alpha^2 + \\beta^2", "res": "$(\\alpha + \\beta)^2 - 2\\alpha\\beta = \\frac{b^2 - 2ac}{a^2}$"},
                    {"cond": "\\alpha^3 + \\beta^3", "res": "$(\\alpha + \\beta)^3 - 3\\alpha\\beta(\\alpha + \\beta) = \\frac{-b^3 + 3abc}{a^3}$"},
                    {"cond": "\\alpha^4 + \\beta^4", "res": "$(\\alpha^2 + \\beta^2)^2 - 2(\\alpha\\beta)^2 = \\left(\\frac{b^2 - 2ac}{a^2}\\right)^2 - 2\\left(\\frac{c}{a}\\right)^2$"},
                    {"cond": "Newton's Theorem", "res": "$a S_n + b S_{n-1} + c S_{n-2} = 0$ for any integer $n$."}
                ]
            }
        ],
        "special_cases": [
            "(i) If one root is 1, then $a + b + c = 0$ (for $ax^2 + bx + c = 0$).",
            "(ii) If one root is -1, then $a - b + c = 0$.",
            "(iii) If roots are reciprocal ($\\alpha, \\beta, \\frac{1}{\\alpha}, \\frac{1}{\\beta}$), then $a = c$ (for $ax^4 + bx^3 + cx^2 + bx + a = 0$).",
            "(iv) If roots are in AP ($a-d, a, a+d$), then $b^2 = 4ac$ condition links with common difference."
        ],
        "important_points": [
            "$\\alpha + \\frac{1}{\\alpha} = \\frac{S+2}{\\alpha}, \\alpha\\beta = 1$ (for $x^2 - Sx + 1 = 0$).",
            "If $\\alpha, \\beta$ are roots, then $(x - \\alpha)(x - \\beta) = x^2 - (\\alpha + \\beta)x + \\alpha\\beta$.",
            "If $\\alpha, \\beta, \\gamma$ are roots, then $(x - \\alpha)(x - \\beta)(x - \\gamma) = x^3 - (\\alpha+\\beta+\\gamma)x^2 + (\\alpha\\beta+\\beta\\gamma+\\gamma\\alpha)x - \\alpha\\beta\\gamma$.",
            "Useful for: finding higher powers, solving equations in terms of roots, JEE numerical & conceptual questions."
        ],
        "quick_tips": [
            "If $1$ is a root $\\implies a + b + c = 0$.",
            "If $-1$ is a root $\\implies a - b + c = 0$.",
            "For reciprocal roots $\\implies$ constant term $= a$ ($c = a$).",
            "For roots in GP ($\\alpha, \\alpha r, \\alpha r^2$) $\\implies \\alpha\\beta + \\beta\\gamma + \\gamma\\alpha = 3\\alpha^2 r^2$.",
            "If roots are $\\alpha, \\beta$ and $\\alpha + \\beta = k \\implies \\alpha, \\beta$ are roots of $x^2 - kx + \\alpha\\beta = 0$.",
            "Always write the equation in standard form before applying formulas."
        ],
        "jee_focus_points": [
            "Use Vieta's formulas (sum & product of roots).",
            "In quadratic, always relate with $D = b^2 - 4ac$.",
            "For cubic/quartic, remember the sign pattern ($-, +, -, +$).",
            "In questions, check special roots ($1, -1, 0,$ reciprocal, AP, GP, etc.).",
            "Use identities to avoid lengthy calculations."
        ],
        "traps_and_pitfalls": [
            {
                "trap": "Sign confusion in Vieta's cubic / quartic relations.",
                "why": "Signs strictly alternate: $\\sum \\alpha = -b/a$, $\\sum \\alpha\\beta = +c/a$, $\\sum \\alpha\\beta\\gamma = -d/a$, $\\alpha\\beta\\gamma\\delta = +e/a$.",
                "remedy": "Associate odd number of roots in product with negative sign, even with positive sign."
            }
        ],
        "examples": [
            {
                "title": "Newton's Identity Application",
                "problem": "If $\\alpha, \\beta$ are roots of $x^2 - 6x - 2 = 0$ and $a_n = \\alpha^n - \\beta^n$, find the value of $\\frac{a_{10} - 2a_8}{2a_9}$.",
                "approach": "Use Newton's recursive identity: $a_{n} - 6a_{n-1} - 2a_{n-2} = 0$.",
                "solution": "From $x^2 - 6x - 2 = 0$, for $n = 10$:\\n$a_{10} - 6a_9 - 2a_8 = 0 \\implies a_{10} - 2a_8 = 6a_9$.\\nDividing by $2a_9$:\\n$\\frac{a_{10} - 2a_8}{2a_9} = \\frac{6a_9}{2a_9} = 3$.",
                "key_takeaway": "Newton's identity bypasses solving for roots completely and solves high-power JEE questions in 30 seconds."
            },
            {
                "title": "Reciprocal Roots Condition",
                "problem": "For what condition on coefficients do the roots of $ax^2 + bx + c = 0$ become reciprocals of each other?",
                "approach": "Let roots be $\\alpha$ and $1/\\alpha$. Product of roots $\\alpha \\cdot (1/\\alpha) = 1$.",
                "solution": "Product of roots $\\alpha\\beta = \\frac{c}{a} = 1 \\implies c = a$.\\nCheck: $a \\ne 0$ and $D = b^2 - 4a^2 \\ge 0$ for real roots.",
                "key_takeaway": "Whenever roots are reciprocals of each other, the coefficient of $x^2$ equals the constant term ($a = c$)."
            }
        ]
    },

    # ---------------------------------------------------------------------
    # PAGE 3: Formation of Quadratic Equation
    # ---------------------------------------------------------------------
    {
        "page_number": 3,
        "sheet_title": "Formation of Quadratic Equation",
        "chapter": "Quadratic Equations & Expressions",
        "subject": "Mathematics",
        "class_level": 11,
        "ncert_ref": "Class 11, Chapter 5 • Sheet 3 of 6",
        "importance": "High",
        "mnemonic_banner": "Practice Formulas + Apply Conditions = JEE Success",
        "classification_heading": "3. Formation from Given Roots & Conditions",
        "parameter_heading": "6. Formation Using Specific Constraints",
        "important_points_heading": "7. Formation by Substitution",
        "introduction": "A quadratic equation is of the form $ax^2 + bx + c = 0$ ($a \\ne 0$). Many problems in JEE can be reduced to a quadratic equation by suitable substitution, manipulation or using given conditions. In this topic, we learn different ways to form a quadratic equation from given information.",
        "classification_cases": [
            {
                "badge": "(i) Roots Given (α, β)",
                "title": "From Individual Roots",
                "condition": "Roots \\alpha, \\beta known",
                "description": "Expand $(x - \\alpha)(x - \\beta) = 0$.",
                "range": "x^2 - (\\alpha + \\beta)x + \\alpha\\beta = 0",
                "consequence": "Example: If roots are $2$ and $3$, equation is $x^2 - (2+3)x + (2)(3) = x^2 - 5x + 6 = 0$."
            },
            {
                "badge": "(ii) Sum & Product (S, P)",
                "title": "From Sum S and Product P",
                "condition": "\\alpha + \\beta = S, \\alpha\\beta = P",
                "description": "Direct substitution into standard monic form.",
                "range": "x^2 - Sx + P = 0",
                "consequence": "Example: If $\\alpha + \\beta = 7, \\alpha\\beta = 10$, equation is $x^2 - 7x + 10 = 0$."
            },
            {
                "badge": "(iii) One Root Known",
                "title": "When One Root is Known",
                "condition": "\\alpha known, \\beta = c/(a\\alpha)",
                "description": "The second root is $\\beta = \\frac{c}{a\\alpha}$ (for $\\alpha \\ne 0$).",
                "range": "x^2 - \\left(\\alpha + \\frac{c}{a\\alpha}\\right)x + \\frac{c}{a} = 0",
                "consequence": "Equation is fully determined once $a, c,$ and $\\alpha$ are fixed."
            }
        ],
        "parameter_analysis": [
            {
                "parameter": "Constraint Formulations",
                "sub_cases": [
                    {"cond": "Known Difference: |\\alpha - \\beta| = d", "res": "Since $d^2 = S^2 - 4P \\implies P = \\frac{S^2 - d^2}{4}$. Equation: $x^2 - Sx + \\frac{S^2 - d^2}{4} = 0$, or $4x^2 - 4Sx + (S^2 - d^2) = 0$."},
                    {"cond": "Reciprocal Roots: \\alpha\\beta = 1", "res": "If $\\alpha\\beta = 1$ and $\\alpha + \\beta = S$, then equation is $x^2 - Sx + 1 = 0$."},
                    {"cond": "Roots Differ by Unity: d = 1", "res": "$b^2 - 4ac = a^2 \\implies D = a^2$."}
                ]
            }
        ],
        "special_cases": [
            "If $x + \\frac{1}{x} = k$, then $x^2 + \\frac{1}{x^2} = k^2 - 2$.",
            "If $x - \\frac{1}{x} = k$, then $x^2 + \\frac{1}{x^2} = k^2 + 2$.",
            "These substitution forms are exceptionally useful in symmetric equations of the form $ax^4 + bx^3 + cx^2 + bx + a = 0$."
        ],
        "important_points": [
            "Coefficients of $x^2, x$ and constant term can be formed using given conditions on roots.",
            "Quadratic equation is unique up to a non-zero scaling factor for given roots.",
            "Always check the value of discriminant $D = b^2 - 4ac$ to verify that the formed equation produces real roots when required."
        ],
        "quick_tips": [
            "Always use Vieta's formulas when roots/sum/product are given.",
            "If one root is given, use $\\beta = \\frac{c}{a\\alpha}$.",
            "For reciprocal roots, use $\\alpha\\beta = 1$ and $\\alpha + \\beta = S$.",
            "To form quadratic with known difference of roots, use $d^2 = S^2 - 4P$.",
            "In symmetric expressions $(x + 1/x, x - 1/x)$, try substitution $t = x + 1/x$ or $t = x - 1/x$."
        ],
        "jee_focus_points": [
            "Forming new equations whose roots are functions of original roots (e.g. $\\alpha^2, \\beta^2$ or $\\frac{\\alpha}{\\beta}, \\frac{\\beta}{\\alpha}$).",
            "Transformation of equations: replace $x$ by $f^{-1}(y)$.",
            "Symmetric substitution techniques."
        ],
        "traps_and_pitfalls": [
            {
                "trap": "Writing $x^2 + Sx + P = 0$ instead of $x^2 - Sx + P = 0$.",
                "why": "Sum of roots $\\alpha + \\beta = -b/a$, so the linear coefficient is $-(\\alpha + \\beta) = -S$.",
                "remedy": "Always double check the negative sign before $S$: $x^2 - Sx + P = 0$."
            }
        ],
        "examples": [
            {
                "title": "Equation with Roots as Powers (α^2, β^2)",
                "problem": "If $\\alpha, \\beta$ are roots of $x^2 - 4x + 1 = 0$, form the quadratic equation whose roots are $\\alpha^2$ and $\\beta^2$.",
                "approach": "Find $S' = \\alpha^2 + \\beta^2$ and $P' = (\\alpha\\beta)^2$.",
                "solution": "Here $\\alpha + \\beta = 4$ and $\\alpha\\beta = 1$.\\n$S' = \\alpha^2 + \\beta^2 = (\\alpha + \\beta)^2 - 2\\alpha\\beta = 4^2 - 2(1) = 14$.\\n$P' = (\\alpha\\beta)^2 = 1^2 = 1$.\\nNew equation: $x^2 - S'x + P' = 0 \\implies x^2 - 14x + 1 = 0$.",
                "key_takeaway": "Alternatively, substitute $y = x^2 \\implies x = \\sqrt{y}$: $(\\sqrt{y})^2 + 1 = 4\\sqrt{y} \\implies y + 1 = 4\\sqrt{y} \\implies (y+1)^2 = 16y \\implies y^2 - 14y + 1 = 0$."
            }
        ]
    },

    # ---------------------------------------------------------------------
    # PAGE 4: Common Roots of Two Quadratic Equations
    # ---------------------------------------------------------------------
    {
        "page_number": 4,
        "sheet_title": "Common Roots of Two Quadratic Equations",
        "chapter": "Quadratic Equations & Expressions",
        "subject": "Mathematics",
        "class_level": 11,
        "ncert_ref": "Class 11, Chapter 5 • Sheet 4 of 6",
        "importance": "Very High",
        "mnemonic_banner": "Common roots ⟹ Compare ratios ⟹ Apply case ⟹ Get the result",
        "classification_heading": "3. Methods & Classification of Cases",
        "parameter_heading": "4. Another Useful Form (Determinant Method)",
        "important_points_heading": "6. Special Cases & Analytical Rules",
        "introduction": "Two quadratic equations are said to have common roots, if they have at least one root in common. In other words, the equations are satisfied by the same value(s) of $x$.\\nLet $a_1 x^2 + b_1 x + c_1 = 0$ and $a_2 x^2 + b_2 x + c_2 = 0$ with $(a_i, b_i, c_i) \\ne (0,0,0)$.",
        "classification_cases": [
            {
                "badge": "Case 1: Both Roots Common",
                "title": "Both Roots are Identical",
                "condition": "\\frac{a_1}{a_2} = \\frac{b_1}{b_2} = \\frac{c_1}{c_2}",
                "description": "The two quadratic equations are completely proportional and have the exact same two roots.",
                "range": "\\frac{a_1}{a_2} = \\frac{b_1}{b_2} = \\frac{c_1}{c_2} (\\ne 0)",
                "consequence": "One equation is simply a non-zero scalar multiple of the other."
            },
            {
                "badge": "Case 2: Exactly One Common Root",
                "title": "One Root in Common",
                "condition": "(c_1 a_2 - c_2 a_1)^2 = (a_1 b_2 - a_2 b_1)(b_1 c_2 - b_2 c_1)",
                "description": "Obtained by cross-multiplication method: $\\frac{\\alpha^2}{b_1 c_2 - b_2 c_1} = \\frac{-\\alpha}{a_1 c_2 - a_2 c_1} = \\frac{1}{a_1 b_2 - a_2 b_1}$.",
                "range": "\\alpha = \\frac{c_1 a_2 - c_2 a_1}{a_1 b_2 - a_2 b_1} = \\frac{b_1 c_2 - b_2 c_1}{c_1 a_2 - c_2 a_1}",
                "consequence": "Equating the two expressions for the common root $\\alpha$ gives the condition."
            },
            {
                "badge": "Case 3: No Common Root",
                "title": "Distinct Disjoint Roots",
                "condition": "\\frac{a_1}{a_2} \\ne \\frac{b_1}{b_2} \\text{ and condition not satisfied}",
                "description": "Neither root of equation 1 satisfies equation 2.",
                "range": "(c_1 a_2 - c_2 a_1)^2 \\ne (a_1 b_2 - a_2 b_1)(b_1 c_2 - b_2 c_1)",
                "consequence": "The solution sets of both equations are disjoint."
            }
        ],
        "parameter_analysis": [
            {
                "parameter": "Determinant Eliminant Form",
                "sub_cases": [
                    {"cond": "Linear Dependence", "res": "Condition can be expressed via determinant eliminant: $\\begin{vmatrix} a_1 & b_1 & c_1 \\\\ a_2 & b_2 & c_2 \\\\ 1 & 1 & 0 \\end{vmatrix} = 0$."},
                    {"cond": "Subtracting Equations", "res": "Subtract $(a_1 - a_2)x^2 + (b_1 - b_2)x + (c_1 - c_2) = 0$. If $a_1 = a_2$, linear equation immediately yields common root $x = -\\frac{c_1 - c_2}{b_1 - b_2}$."}
                ]
            }
        ],
        "special_cases": [
            "If $\\frac{c_1}{a_1} = \\frac{c_2}{a_2}$ and $b_1 = b_2 = 0$, then $x = 0$ is a common root.",
            "If $a_1 = a_2$ and $b_1 = b_2$, then the equations differ only in constant term (no common root unless $c_1 = c_2$).",
            "If one equation has imaginary roots (with real coefficients) and shares a root with another real-coefficient equation, then BOTH roots must be common!"
        ],
        "important_points": [
            "If $a_1 x^2 + b_1 x + c_1 = 0$ has $D_1 < 0$ (imaginary roots), and shares a root with $a_2 x^2 + b_2 x + c_2 = 0$ with real coefficients, then both roots MUST be common because imaginary roots occur in conjugate pairs!",
            "This implies $\\frac{a_1}{a_2} = \\frac{b_1}{b_2} = \\frac{c_1}{c_2}$ directly without testing one common root."
        ],
        "quick_tips": [
            "Always compare $\\frac{a_1}{a_2}, \\frac{b_1}{b_2}, \\frac{c_1}{c_2}$ first.",
            "If ratios are equal $\\implies$ same roots.",
            "If one equation has known imaginary roots, both roots must be common.",
            "Determinant method is very useful in MCQs and parameter elimination questions."
        ],
        "jee_focus_points": [
            "Questions where one equation has integer roots that can be found by inspection, then substituted into the second equation.",
            "Questions with imaginary roots forcing both roots to be common.",
            "Parameters ($k, p, q$) such that exactly one root is shared."
        ],
        "traps_and_pitfalls": [
            {
                "trap": "Applying single common root condition when one equation has D < 0.",
                "why": "Imaginary roots must come in conjugate pairs for real polynomials; you cannot share just one!",
                "remedy": "Check $D$ of both equations first. If $D < 0$, apply $\\frac{a_1}{a_2} = \\frac{b_1}{b_2} = \\frac{c_1}{c_2}$ immediately."
            }
        ],
        "examples": [
            {
                "title": "(1) Both Roots Common: x^2 - 3x + 2 = 0 and 2x^2 - 6x + 4 = 0",
                "problem": "Find the common roots of $x^2 - 3x + 2 = 0$ and $2x^2 - 6x + 4 = 0$.",
                "approach": "Compare coefficient ratios.",
                "solution": "$a_1 = 1, b_1 = -3, c_1 = 2; \\quad a_2 = 2, b_2 = -6, c_2 = 4$.\\n$\\frac{a_1}{a_2} = \\frac{1}{2}, \\quad \\frac{b_1}{b_2} = \\frac{-3}{-6} = \\frac{1}{2}, \\quad \\frac{c_1}{c_2} = \\frac{2}{4} = \\frac{1}{2}$.\\nSince all ratios are equal, the equations have the exact same roots: $x = 1, 2$.",
                "key_takeaway": "Proportional coefficients guarantee both roots are identical."
            },
            {
                "title": "(2) Both Roots Common: x^2 + 5x + 6 = 0 and 2x^2 + 10x + 12 = 0",
                "problem": "Find the common roots of $x^2 + 5x + 6 = 0$ and $2x^2 + 10x + 12 = 0$.",
                "approach": "Compare coefficient ratios.",
                "solution": "$\\frac{a_1}{a_2} = \\frac{1}{2}, \\quad \\frac{b_1}{b_2} = \\frac{5}{10} = \\frac{1}{2}, \\quad \\frac{c_1}{c_2} = \\frac{6}{12} = \\frac{1}{2}$.\\nSame roots: $x = -2, -3$.",
                "key_takeaway": "Linear dependence across all 3 coefficients implies identical solution sets."
            },
            {
                "title": "(3) No Common Root: x^2 - 4x + 3 = 0 and x^2 + x - 6 = 0",
                "problem": "Find the common roots of $x^2 - 4x + 3 = 0$ and $x^2 + x - 6 = 0$.",
                "approach": "Solve roots of each and check intersection.",
                "solution": "First equation: $(x - 1)(x - 3) = 0 \\implies x = 1, 3$.\\nSecond equation: $(x + 3)(x - 2) = 0 \\implies x = 2, -3$.\\nIntersection: $\\{1, 3\\} \\cap \\{2, -3\\} = \\emptyset \\implies$ No common root.",
                "key_takeaway": "Always factor directly if equations have simple integer coefficients."
            }
        ]
    },

    # ---------------------------------------------------------------------
    # PAGE 5: Quadratic Inequalities & Sign of Quadratic Expression
    # ---------------------------------------------------------------------
    {
        "page_number": 5,
        "sheet_title": "Quadratic Inequalities & Sign of Quadratic Expression",
        "chapter": "Quadratic Equations & Expressions",
        "subject": "Mathematics",
        "class_level": 11,
        "ncert_ref": "Class 11, Chapter 5 • Sheet 5 of 6",
        "importance": "Very High",
        "mnemonic_banner": "Practice + Concept = JEE Success",
        "classification_heading": "2. Solving ax^2 + bx + c > 0 / < 0 (a ≠ 0)",
        "parameter_heading": "3. Sign Chart Method",
        "important_points_heading": "6. Important Points & Sign Criteria",
        "introduction": "A quadratic inequality is an inequality of the form $ax^2 + bx + c > 0, ax^2 + bx + c < 0, \\ge 0$ or $\\le 0$ ($a \\ne 0$). The solution set is found using the roots of the corresponding quadratic equation and the sign of the parabola.\\nKey Points: Factorise the quadratic expression (if possible), find roots using discriminant or formula, and use sign chart / number line to get the solution.",
        "classification_cases": [
            {
                "badge": "(i) D > 0 (Two Real & Distinct Roots)",
                "title": "Roots α < β",
                "condition": "D > 0",
                "description": "Parabola crosses x-axis at two points.",
                "range": "For a > 0: f(x) > 0 \\implies x \\in (-\\infty, \\alpha) \\cup (\\beta, \\infty); \\quad f(x) < 0 \\implies x \\in (\\alpha, \\beta)",
                "consequence": "Expression is negative between the roots, positive outside."
            },
            {
                "badge": "(ii) D = 0 (Equal Roots α)",
                "title": "Parabola Touches Axis",
                "condition": "D = 0",
                "description": "Repeated root $\\alpha = -b/(2a)$.",
                "range": "For a > 0: f(x) > 0 \\implies x \\in (-\\infty, \\alpha) \\cup (\\alpha, \\infty); \\quad f(x) < 0 \\implies \\emptyset",
                "consequence": "Expression is strictly positive everywhere except at $x = \\alpha$ where it is $0$."
            },
            {
                "badge": "(iii) D < 0 (No Real Roots)",
                "title": "Definite Sign (Never Crosses Axis)",
                "condition": "D < 0",
                "description": "Expression preserves the sign of leading coefficient $a$ for all $x \\in \\mathbb{R}$.",
                "range": "If a > 0: f(x) > 0 for all x \\in \\mathbb{R}. If a < 0: f(x) < 0 for all x \\in \\mathbb{R}.",
                "consequence": "Golden theorem: $ax^2 + bx + c > 0 \\; \\forall x \\in \\mathbb{R} \\iff a > 0$ and $D < 0$."
            }
        ],
        "parameter_analysis": [
            {
                "parameter": "Sign Chart for a > 0 (Opens Upwards)",
                "sub_cases": [
                    {"cond": "Interval $(-\\infty, \\alpha)$", "res": "Sign of $f(x)$ is **$+$** (positive)"},
                    {"cond": "Interval $(\\alpha, \\beta)$", "res": "Sign of $f(x)$ is **$-$** (negative)"},
                    {"cond": "Interval $(\\beta, \\infty)$", "res": "Sign of $f(x)$ is **$+$** (positive)"}
                ]
            },
            {
                "parameter": "Sign Chart for a < 0 (Opens Downwards)",
                "sub_cases": [
                    {"cond": "Interval $(-\\infty, \\alpha)$", "res": "Sign of $f(x)$ is **$-$** (negative)"},
                    {"cond": "Interval $(\\alpha, \\beta)$", "res": "Sign of $f(x)$ is **$+$** (positive)"},
                    {"cond": "Interval $(\\beta, \\infty)$", "res": "Sign of $f(x)$ is **$-$** (negative)"}
                ]
            }
        ],
        "graphical_view": {
            "title": "4. Graphical View: The 6 Parabola Orientations",
            "vertex_formula": "Vertex is $\\left(-\\frac{b}{2a}, -\\frac{D}{4a}\\right)$. Minimum if $a>0$, Maximum if $a<0$.",
            "observations": [
                "Top Row (a > 0): D > 0 cuts twice (+, -, +); D = 0 touches at vertex (+, 0, +); D < 0 floats entirely above (+, +).",
                "Bottom Row (a < 0): D > 0 cuts twice (-, +, -); D = 0 touches at vertex (-, 0, -); D < 0 hangs entirely below (-, -)."
            ],
            "svg_diagram": generate_quadratic_svg_page5()
        },
        "special_cases": [
            "(i) $ax^2 + bx + c \\ge 0$ (or $\\le 0$): Include the endpoints $(\\alpha, \\beta)$ in the solution set.",
            "(ii) If one root is $0$: $c = 0 \\implies ax^2 + bx = 0 \\implies x(ax + b) = 0 \\implies x = 0$ or $x = -b/a$.",
            "(iii) If roots are unequal and of opposite signs: product of roots $< 0 \\implies c/a < 0$. Expression has opposite signs on either side of roots.",
            "(iv) If $\\alpha, \\beta$ are real and of same sign: $c/a > 0$ and $\\alpha\\beta > 0$."
        ],
        "important_points": [
            "$D = b^2 - 4ac$ determines the nature of roots.",
            "The sign of $ax^2 + bx + c$ is decided by $a, \\alpha, \\beta$.",
            "For inequalities, include/exclude endpoints based on $>, <, \\ge, \\le$.",
            "For $D < 0$, the expression keeps the same sign throughout $\\mathbb{R}$ (positive if $a > 0$, negative if $a < 0$)."
        ],
        "quick_tips": [
            "Use discriminant to find intervals of positivity/negativity.",
            "In inequality problems, factorise if possible.",
            "Remember: Product of roots $= c/a$, Sum of roots $= -b/a$.",
            "If $c/a < 0 \\implies$ roots are of opposite signs.",
            "Draw a rough graph to check the sign pattern immediately."
        ],
        "jee_focus_points": [
            "Quadratic inequalities in single variable.",
            "Sign of quadratic expression.",
            "Use of discriminant in inequalities.",
            "Mixed problems (with linear factors / parameters).",
            "Conceptual questions based on parabola and sign chart."
        ],
        "traps_and_pitfalls": [
            {
                "trap": "Forgetting to flip the inequality sign when dividing by negative coefficient a.",
                "why": "Dividing by $a < 0$ reverses the inequality direction ($> \\to <$).",
                "remedy": "Make $a > 0$ before factorizing by multiplying through by $-1$ and reversing the inequality."
            }
        ],
        "examples": [
            {
                "title": "Always Positive Condition on Quadratic",
                "problem": "Find all values of $m$ for which $(m - 2)x^2 + 8x + (m + 4) > 0$ holds for all real $x$.",
                "approach": "Apply $a > 0$ and $D < 0$.",
                "solution": "Condition 1 ($a > 0$): $m - 2 > 0 \\implies m > 2$.\\nCondition 2 ($D < 0$): $8^2 - 4(m - 2)(m + 4) < 0$\\n$64 - 4(m^2 + 2m - 8) < 0 \\implies 16 - (m^2 + 2m - 8) < 0$\\n$m^2 + 2m - 24 > 0 \\implies (m + 6)(m - 4) > 0$\\n$\\implies m < -6$ or $m > 4$.\\nTaking intersection with $m > 2$:\\n$m \\in (4, \\infty)$.",
                "key_takeaway": "Both conditions $a > 0$ and $D < 0$ MUST hold simultaneously. Take their strict set intersection."
            }
        ]
    },

    # ---------------------------------------------------------------------
    # PAGE 6: Range & Location of Roots
    # ---------------------------------------------------------------------
    {
        "page_number": 6,
        "sheet_title": "Range & Location of Roots",
        "chapter": "Quadratic Equations & Expressions",
        "subject": "Mathematics",
        "class_level": 11,
        "ncert_ref": "Class 11, Chapter 5 • Sheet 6 of 6",
        "importance": "Very High",
        "mnemonic_banner": "Discriminant tells the nature... Coefficients tell the location...",
        "classification_heading": "2. Range of Roots (Using Discriminant)",
        "parameter_heading": "3. Location of Roots (With Respect to Origin)",
        "important_points_heading": "6. Important Points",
        "introduction": "For a quadratic equation $ax^2 + bx + c = 0$, the range and location of roots depend on the discriminant $D = b^2 - 4ac$ and the coefficients of the equation. The roots can be real, equal or non-real (complex), and they may lie in different intervals on the number line.",
        "classification_cases": [
            {
                "badge": "(i) Real and Distinct Roots (D > 0)",
                "title": "Real and Distinct Roots",
                "condition": "D > 0",
                "description": "Two distinct real roots, $x_1, x_2 \\in \\mathbb{R}$.",
                "range": "x \\in (-\\infty, \\infty)",
                "consequence": "Parabola cuts x-axis at two distinct points."
            },
            {
                "badge": "(ii) Real and Equal Roots (D = 0)",
                "title": "Real and Equal Roots",
                "condition": "D = 0",
                "description": "Two equal real roots, $x_1 = x_2 = -\\frac{b}{2a}$.",
                "range": "x \\in \\mathbb{R} \\text{ (a single point)}",
                "consequence": "Parabola touches x-axis at vertex."
            },
            {
                "badge": "(iii) Non-real (Complex) Roots (D < 0)",
                "title": "Non-real (Complex) Roots",
                "condition": "D < 0",
                "description": "No real roots.",
                "range": "x \\notin \\mathbb{R} \\text{ (complex conjugate pair)}",
                "consequence": "Parabola does not cut x-axis."
            }
        ],
        "parameter_analysis": [
            {
                "parameter": "(i) Product of Roots: αβ = c / a",
                "sub_cases": [
                    {"cond": "If c / a > 0", "res": "Roots have the **SAME sign** (both positive or both negative)."},
                    {"cond": "If c / a < 0", "res": "Roots have **OPPOSITE signs** (one positive, one negative)."},
                    {"cond": "If c = 0", "res": "One root is strictly **0**."}
                ]
            },
            {
                "parameter": "(ii) Sum of Roots: α + β = -b / a",
                "sub_cases": [
                    {"cond": "If -b / a > 0 (with c/a > 0)", "res": "Both roots are strictly **POSITIVE**."},
                    {"cond": "If -b / a < 0 (with c/a > 0)", "res": "Both roots are strictly **NEGATIVE**."},
                    {"cond": "If -b / a = 0 (with c/a < 0)", "res": "Roots are equal in magnitude, opposite in sign ($\alpha = -\\beta$)."}
                ]
            }
        ],
        "interval_rules": {
            "title": "4. Interval Form (Using Roots)",
            "subtitle": "If α and β are the roots (α < β), then:",
            "rules": [
                {"cond": "For D > 0", "interval": "x \\in (-\\infty, \\alpha] \\cup [\\beta, \\infty)"},
                {"cond": "For D = 0", "interval": "x \\in (-\\infty, \\alpha] \\cup [\\alpha, \\infty) = \\mathbb{R}"},
                {"cond": "For D < 0", "interval": "x \\notin \\mathbb{R} \\text{ (no real interval)}"}
            ],
            "note": "This gives the set of real values of x for which the quadratic expression is defined (or non-negative, depending on the question)."
        },
        "graphical_view": {
            "title": "5. Location from Vertex (Graphical View)",
            "vertex_formula": "For y = ax^2 + bx + c, vertex is $\\left(-\\frac{b}{2a}, -\\frac{D}{4a}\\right)$.",
            "observations": [
                "If D > 0 ⟹ parabola cuts x-axis at two points (roots real and distinct).",
                "If D = 0 ⟹ parabola touches x-axis at vertex (equal roots).",
                "If D < 0 ⟹ parabola does not cut x-axis (no real roots)."
            ],
            "svg_diagram": generate_quadratic_svg_page1()
        },
        "important_points": [
            "If $\\alpha$ and $\\beta$ are roots, then $\\alpha + \\beta = -b/a$ and $\\alpha\\beta = c/a$.",
            "The roots are real $\\iff D \\ge 0$.",
            "The roots are equal $\\iff D = 0$.",
            "The roots are non-real (complex) $\\iff D < 0$.",
            "The roots are in AP $\\iff 2\\alpha + 2\\beta = -b/a \\implies \\alpha + \\beta = -b/(2a)$.",
            "The roots are in GP $\\iff \\alpha\\beta = \\frac{(\\alpha+\\beta)^2}{4} \\implies \\frac{c}{a} = \\left(-\\frac{b}{2a}\\right)^2$.",
            "For a quadratic inequality, boundary points are the roots of the corresponding equation."
        ],
        "quick_tips": [
            "Use $D = b^2 - 4ac$ to find nature and range of roots.",
            "Use $\\alpha + \\beta = -b/a, \\alpha\\beta = c/a$ for sign and location.",
            "Use vertex $(-b/(2a), -D/(4a))$ for graphical view.",
            "If $c = 0$, one root is $0$ (and the other is $-b/a$).",
            "If product $> 0 \\implies$ same sign, if $< 0 \\implies$ opposite.",
            "Use the interval form to find the set of $x$ values."
        ],
        "jee_focus_points": [
            "Range of roots (using D).",
            "Location of roots with respect to origin.",
            "Use of $\\alpha + \\beta, \\alpha\\beta$ for sign and intervals.",
            "Vertex form and its significance.",
            "Application in quadratic inequalities.",
            "Quick decision using $D, b, c$."
        ],
        "traps_and_pitfalls": [
            {
                "trap": "Assuming both roots lie in $(k_1, k_2)$ by only checking $f(k_1) > 0$ and $f(k_2) > 0$.",
                "why": "The parabola could lie entirely above the interval without cutting the axis, or the vertex could lie outside.",
                "remedy": "Must verify ALL 3 conditions: (1) $D \\ge 0$, (2) $a f(k_1) > 0$ and $a f(k_2) > 0$, (3) $k_1 < -b/(2a) < k_2$."
            }
        ],
        "examples": [
            {
                "title": "Roots Greater than a Real Number k",
                "problem": "Find the values of $a$ for which both roots of $x^2 - 6ax + 2 - 2a + 9a^2 = 0$ are greater than $3$.",
                "approach": "Apply Location of Roots Condition: (1) $D \\ge 0$, (2) $f(3) > 0$, (3) $-b/(2a) > 3$.",
                "solution": "1. $D/4 = (3a)^2 - (2 - 2a + 9a^2) = 2a - 2 \\ge 0 \\implies a \\ge 1$.\\n2. $f(3) = 9 - 18a + 2 - 2a + 9a^2 = 9a^2 - 20a + 11 > 0$\\n$(9a - 11)(a - 1) > 0 \\implies a < 1$ or $a > 11/9$.\\n3. Vertex abscissa: $-\\frac{-6a}{2} = 3a > 3 \\implies a > 1$.\\nIntersection of $a \\ge 1$, $(a < 1 \\text{ or } a > 11/9)$, and $a > 1$:\\n$a \\in (11/9, \\infty)$.",
                "key_takeaway": "Strict adherence to the 3-part location of roots system avoids false parameter solutions."
            }
        ]
    },

    # ---------------------------------------------------------------------
    # PAGE 7: Location of Roots (Advanced JEE Cases) & Modulus Quadratics
    # ---------------------------------------------------------------------
    {
        "page_number": 7,
        "sheet_title": "Location of Roots (Advanced) & Modulus Quadratics",
        "chapter": "Quadratic Equations & Expressions",
        "subject": "Mathematics",
        "class_level": 11,
        "ncert_ref": "Class 11, Chapter 5 • Sheet 7 of 8",
        "importance": "Very High (JEE Advanced Core)",
        "mnemonic_banner": "Roots separated by k ⟹ a·f(k) < 0 ... Discriminant check is redundant!",
        "classification_heading": "2. Advanced Interval Bounding Conditions (for a > 0)",
        "parameter_heading": "3. Modulus & Nested Quadratic Equations",
        "important_points_heading": "6. Important Points & Theorems",
        "introduction": "For JEE Advanced, location of roots extends to bounding roots strictly inside an open interval $(k_1, k_2)$, alternating root conditions across multiple intervals, and solving modulus quadratics $|ax^2 + bx + c| = k$ and $a x^2 + b|x| + c = 0$.",
        "classification_cases": [
            {
                "badge": "(i) Both Roots Lie in (k₁, k₂)",
                "title": "Both Roots Trapped in (k₁, k₂)",
                "condition": "k₁ < α ≤ β < k₂",
                "description": "Both roots are strictly between real constants $k_1$ and $k_2$.",
                "range": "x \\in (k_1, k_2)",
                "consequence": "Must satisfy ALL 4 conditions: (1) $D \\ge 0$, (2) $a f(k_1) > 0$, (3) $a f(k_2) > 0$, (4) $k_1 < -b/(2a) < k_2$."
            },
            {
                "badge": "(ii) Exactly One Root in (k₁, k₂)",
                "title": "Single Root in Interval",
                "condition": "f(k₁) · f(k₂) < 0",
                "description": "One root lies strictly inside $(k_1, k_2)$ while the other lies outside.",
                "range": "\\alpha \\in (k_1, k_2) \\text{ or } \\beta \\in (k_1, k_2)",
                "consequence": "Opposite signs of function values guarantee the graph cuts x-axis between $k_1$ and $k_2$. If $f(k_1) f(k_2) = 0$, test endpoints directly."
            },
            {
                "badge": "(iii) Roots Separated by k₁ and k₂",
                "title": "Both Constants Lie Between Roots",
                "condition": "α < k₁ < k₂ < β",
                "description": "Both real constants lie strictly between the two distinct real roots.",
                "range": "k_1, k_2 \\in (\\alpha, \\beta)",
                "consequence": "$a f(k_1) < 0$ and $a f(k_2) < 0$. (Notice: $D > 0$ is AUTOMATICALLY guaranteed; no need to check $D$!)."
            }
        ],
        "parameter_analysis": [
            {
                "sub_badge": "(i) Equations of Form |ax² + bx + c| = k",
                "rules": [
                    {"cond": "If k < 0", "res": "No real solutions (modulus is always non-negative)."},
                    {"cond": "If k = 0", "res": "At most 2 roots (roots of $ax^2 + bx + c = 0$)."},
                    {"cond": "If 0 < k < |D|/(4a)", "res": "Exactly 4 distinct real roots (line cuts folded parabola 4 times)."},
                    {"cond": "If k = |D|/(4a)", "res": "Exactly 3 distinct real roots (line is tangent to the inverted vertex)."},
                    {"cond": "If k > |D|/(4a)", "res": "Exactly 2 distinct real roots."}
                ]
            },
            {
                "sub_badge": "(ii) Equations of Form a x² + b|x| + c = 0",
                "rules": [
                    {"cond": "Substitution", "res": "Let $t = |x| \\ge 0 \\implies a t^2 + b t + c = 0$."},
                    {"cond": "Each t > 0", "res": "Yields TWO real solutions: $x = \\pm t$."},
                    {"cond": "Root t = 0", "res": "Yields ONE real solution: $x = 0$."},
                    {"cond": "Root t < 0", "res": "Yields ZERO real solutions (discard extraneous negative roots)."}
                ]
            }
        ],
        "graphical_view": {
            "title": "Location & Modulus Parabola Fold (Graphical View)",
            "vertex_formula": "Peak of inverted vertex: $\\left(-\\frac{b}{2a}, \\frac{|D|}{4a}\\right)$ | $y = |ax^2+bx+c|$",
            "observations": [
                "The portion of the parabola below the x-axis ($D > 0$) is reflected upward across the x-axis.",
                "Horizontal line $y = k$ cuts the folded curve in 0, 2, 3, or 4 points depending on $k$ relative to $|D|/(4a)$.",
                "For $a f(k) < 0$, the parabola's vertex is guaranteed to be below the x-axis, making $D > 0$ unconditional."
            ],
            "svg_diagram": generate_quadratic_svg_page7()
        },
        "special_cases": {
            "title": "4. Rapid Root Existence & Sign Theorems",
            "cases": [
                "If $a f(k) < 0$ for ANY real $k$, then $D = b^2 - 4ac > 0$ strictly (Roots are real and distinct without calculating $D$).",
                "If $a$ and $c$ have opposite signs ($ac < 0$), then roots are ALWAYS real and distinct with opposite signs.",
                "Descartes' Rule of Signs: Number of positive roots $\\le$ sign variations in $P(x)$; number of negative roots $\\le$ sign variations in $P(-x)$.",
                "For $|x - \\alpha| + |x - \\beta| = k$: Minimum value of LHS is $|\\alpha - \\beta|$. If $k < |\\alpha - \\beta|$, no solution; if $k = |\\alpha - \\beta|$, infinite solutions in $[\\alpha, \\beta]$."
            ],
            "note": "Always check whether endpoint equality is permitted in intervals before closing brackets."
        },
        "important_points": [
            "To prove roots are real, showing $f(k_1) f(k_2) < 0$ is often faster than computing $D = b^2 - 4ac$.",
            "When roots are separated by $k$, $a f(k) < 0$ automatically ensures $D > 0$.",
            "For $t = |x|$, never forget to restrict $t \\ge 0$; negative roots of the quadratic in $t$ are discarded.",
            "In interval trapping ($k_1 < \\alpha \\le \\beta < k_2$), forgetting the vertex condition $-b/(2a) \\in (k_1, k_2)$ is the most common error.",
            "If $f(x) = 0$ has roots $\\alpha, \\beta$, then $f(|x|) = 0$ has $2 \\times$ (number of positive roots) solutions if $0$ is not a root."
        ],
        "quick_tips": [
            "✓ If $a f(k) < 0$, skip $D$ computation — $D > 0$ is guaranteed!",
            "✓ For $|x|^2 - 5|x| + 6 = 0 \\implies t = 2, 3 \\implies x = \\pm 2, \\pm 3$ (4 real roots).",
            "✓ Line $y = k$ gives exactly 3 roots for $|ax^2+bx+c|=k$ when $k = |D|/(4a)$.",
            "✓ If $f(k_1) f(k_2) < 0$, exactly an odd number of roots (at least one) lie in $(k_1, k_2)$.",
            "✓ Always test endpoints if intervals are closed $[k_1, k_2]$."
        ],
        "jee_focus_points": [
            "Both roots strictly inside $(k_1, k_2)$.",
            "Separation of roots by specified real numbers.",
            "Number of solutions of $|f(x)| = k$ and $f(|x|) = k$.",
            "Parameter value for exactly 3 distinct real roots.",
            "Descartes' Rule of signs for polynomial roots."
        ],
        "traps_and_pitfalls": [
            {
                "trap": "Omitting the vertex condition $k_1 < -b/(2a) < k_2$ when trapping both roots.",
                "why": "Conditions $D \\ge 0, a f(k_1) > 0, a f(k_2) > 0$ are satisfied even when BOTH roots lie outside the interval on the same side!",
                "remedy": "Always enforce $k_1 < -b/(2a) < k_2$ alongside $a f(k_1) > 0, a f(k_2) > 0$, and $D \\ge 0$."
            },
            {
                "trap": "Treating $t = |x|$ as unrestricted and claiming 4 roots when one $t < 0$.",
                "why": "$|x| = t$ has real solutions if and only if $t \\ge 0$.",
                "remedy": "Check the sign of each root $t$; only positive roots produce $x = \\pm t$."
            }
        ],
        "examples": [
            {
                "title": "Roots Separated by Specified Numbers",
                "problem": "Find all values of $a$ for which one root of the equation $(a - 5)x^2 - 2ax + a - 4 = 0$ is smaller than $1$ and the other root is greater than $2$.",
                "approach": "Let $f(x) = (a - 5)x^2 - 2ax + a - 4$. Since $1$ and $2$ lie between the roots $\\alpha < 1 < 2 < \\beta$, we require $(a - 5) f(1) < 0$ and $(a - 5) f(2) < 0$.",
                "solution": "1. Evaluate $f(1)$:\\n$f(1) = (a - 5)(1)^2 - 2a(1) + a - 4 = a - 5 - 2a + a - 4 = -9$.\\nCondition 1: $(a - 5) f(1) < 0 \\implies (a - 5)(-9) < 0 \\implies a - 5 > 0 \\implies a > 5$.\\n2. Evaluate $f(2)$:\\n$f(2) = (a - 5)(4) - 2a(2) + a - 4 = 4a - 20 - 4a + a - 4 = a - 24$.\\nCondition 2: $(a - 5) f(2) < 0 \\implies (a - 5)(a - 24) < 0 \\implies a \\in (5, 24)$.\\n3. Take intersection of $a > 5$ and $a \\in (5, 24)$:\\n$a \\in (5, 24)$.",
                "key_takeaway": "When numbers lie between the roots, $(a - 5) f(k) < 0$ guarantees $D > 0$ unconditionally without extra discriminant calculations."
            }
        ]
    },

    # ---------------------------------------------------------------------
    # PAGE 8: Range of Rational Quadratic Functions & Algebraic Optimization
    # ---------------------------------------------------------------------
    {
        "page_number": 8,
        "sheet_title": "Range of Rational Expressions & Advanced Transformations",
        "chapter": "Quadratic Equations & Expressions",
        "subject": "Mathematics",
        "class_level": 11,
        "ncert_ref": "Class 11, Chapter 5 • Sheet 8 of 8",
        "importance": "Very High (JEE Advanced Core)",
        "mnemonic_banner": "Cross-multiply... Set D_x ≥ 0 ... Check leading coefficient for asymptotes!",
        "classification_heading": "2. Types of Rational Expressions & Range Determination",
        "parameter_heading": "3. Advanced Root Transformations & Symmetries",
        "important_points_heading": "6. Important Points & Theorems",
        "introduction": "Determining the range of rational quadratic expressions $y = \\frac{a_1 x^2 + b_1 x + c_1}{a_2 x^2 + b_2 x + c_2}$ for real $x \\in \\mathbb{R}$ is among the most frequent JEE Advanced algebra topics. Cross-multiplying to form a quadratic in $x$ and enforcing $D_x \\ge 0$ yields the allowable values of $y$.",
        "classification_cases": [
            {
                "badge": "(i) Linear / Quadratic (y = L(x) / Q(x))",
                "title": "Linear over Quadratic",
                "condition": "y (a₂ x² + b₂ x + c₂) - (a₁ x + b₁) = 0",
                "description": "Cross-multiply to form $a_2 y x^2 + (b_2 y - a_1)x + (c_2 y - b_1) = 0$.",
                "range": "D_x \\ge 0 \\implies y \\in [y_{min}, y_{max}]",
                "consequence": "Always test $y = 0$ separately (horizontal asymptote as $x \\to \\pm \\infty$)."
            },
            {
                "badge": "(ii) Quadratic / Quadratic (No Common Factor)",
                "title": "Quadratic over Quadratic",
                "condition": "(a₂ y - a₁)x² + (b₂ y - b₁)x + (c₂ y - c₁) = 0",
                "description": "For $x \\in \\mathbb{R}$, discriminant $D_x = (b_2 y - b_1)^2 - 4(a_2 y - a_1)(c_2 y - c_1) \\ge 0$.",
                "range": "y \\in [y_1, y_2] \\text{ or } y \\in (-\\infty, y_1] \\cup [y_2, \\infty)",
                "consequence": "Examine $y = a_1/a_2$ (when coefficient of $x^2$ vanishes) to see if it corresponds to a real $x$."
            },
            {
                "badge": "(iii) Rational Expression with Common Factor",
                "title": "Punctured Rational Curve",
                "condition": "Common factor (x - α) cancels",
                "description": "If numerator and denominator share factor $(x - \\alpha)$, simplify to linear fractional.",
                "range": "y \\in \\mathbb{R} \\setminus \\{y_0\\}",
                "consequence": "The cancelled point $x = \\alpha$ produces a hole (puncture). The value $y_0 = f(\\alpha)$ must be excluded from the range."
            }
        ],
        "parameter_analysis": [
            {
                "sub_badge": "(i) Transformation of Roots (New Equation Formation)",
                "rules": [
                    {"cond": "Roots α + k, β + k", "res": "Replace $x$ with $x - k$ in $ax^2 + bx + c = 0$."},
                    {"cond": "Roots kα, kβ", "res": "Replace $x$ with $x/k$ in $ax^2 + bx + c = 0$."},
                    {"cond": "Roots 1/α, 1/β", "res": "Replace $x$ with $1/x \\implies c x^2 + b x + a = 0$."},
                    {"cond": "Roots α², β²", "res": "Write $a x^2 + c = -b x$, square both sides: $(a x^2 + c)^2 = b^2 x^2$, then substitute $y = x^2$."},
                    {"cond": "Roots -α, -β", "res": "Replace $x$ with $-x \\implies a x^2 - b x + c = 0$."}
                ]
            },
            {
                "sub_badge": "(ii) Quadratic Optimization on a Closed Interval [p, q]",
                "rules": [
                    {"cond": "If Vertex -b/(2a) ∈ [p, q]", "res": "Evaluate $f(p), f(q),$ and $f(-b/(2a))$. Maximum is the greatest, minimum is the least."},
                    {"cond": "If Vertex -b/(2a) ∉ [p, q]", "res": "Function is strictly monotonic on $[p, q]$. Extrema occur ONLY at the endpoints $f(p)$ and $f(q)$."}
                ]
            }
        ],
        "graphical_view": {
            "title": "Rational Quadratic Function & Asymptotes (Graphical View)",
            "vertex_formula": "y = (x² - x + 1)/(x² + x + 1) | Range: [1/3, 3] | Asymptote: y = 1",
            "observations": [
                "Denominator $x^2 + x + 1 > 0$ for all real $x$ ($D < 0$), so curve is continuous everywhere without vertical asymptotes.",
                "Horizontal asymptote $y = a_1/a_2 = 1$ is approached as $x \\to \\pm \\infty$ and crossed at $x = 0$.",
                "Global minimum $y = 1/3$ occurs at $x = 1$; global maximum $y = 3$ occurs at $x = -1$."
            ],
            "svg_diagram": generate_quadratic_svg_page8()
        },
        "special_cases": {
            "title": "4. Special Range Theorems & Hole Removals",
            "cases": [
                "Leading Coefficient Check: When setting $D_x \\ge 0$, always check if the leading coefficient $(a_2 y - a_1) = 0$. If $y = a_1/a_2$, the equation becomes linear and may yield a real $x$.",
                "If denominator $Q_2(x) > 0$ for all real $x$ ($a_2 > 0, D_2 < 0$), the function has NO vertical asymptotes and is continuous everywhere on $\\mathbb{R}$.",
                "If the quadratic expression is a perfect square, the range is $[0, \\infty)$ or $(-\\infty, 0]$.",
                "For $x > 0$, $x + 1/x \\ge 2$ (equality at $x = 1$); for $x < 0$, $x + 1/x \\le -2$ (equality at $x = -1$)."
            ],
            "note": "Always verify whether the horizontal asymptote value $y = a_1/a_2$ is attained for a finite real $x$!"
        },
        "important_points": [
            "Discriminant method for range applies ONLY when $x$ can take all real values in the domain.",
            "Always test $y = a_1/a_2$ separately when the coefficient of $x^2$ vanishes.",
            "Punctured points (holes) caused by cancelled common factors must be removed from the range.",
            "For restricted intervals $[p, q]$, always compare $f(p), f(q)$ and $f(-b/2a)$ (if in interval).",
            "If numerator and denominator share a root, the degree drops and range excludes the value at the hole."
        ],
        "quick_tips": [
            "✓ For $y = \\frac{x^2 - x + 1}{x^2 + x + 1}$, cross-multiply, set $D_x \\ge 0 \\implies y \\in [1/3, 3]$.",
            "✓ If $x$ is real, $D_x \\ge 0$ is the master key for quadratic rational ranges.",
            "✓ If roots are squared (\\alpha^2, \\beta^2), write $a x^2 + c = -b x \\implies (a x^2 + c)^2 = b^2 x^2$.",
            "✓ To find $\\alpha^4 + \\beta^4$, use Newton sums $S_4 = -b/a S_3 - c/a S_2$."
        ],
        "jee_focus_points": [
            "Range of $y = \\frac{a_1 x^2 + b_1 x + c_1}{a_2 x^2 + b_2 x + c_2}$ for $x \\in \\mathbb{R}$.",
            "Finding range when numerator and denominator have a common factor.",
            "Restricted domain extrema $[p, q]$.",
            "Transformation of equations to find symmetric polynomials."
        ],
        "traps_and_pitfalls": [
            {
                "trap": "Assuming $y = a_1/a_2$ cannot be in the range.",
                "why": "When $y = a_1/a_2$, the $x^2$ term vanishes and leaves a linear equation in $x$. If that linear equation has a real solution, $a_1/a_2$ IS in the range!",
                "remedy": "Explicitly substitute $y = a_1/a_2$ into the cross-multiplied equation and check if a real $x$ exists."
            },
            {
                "trap": "Forgetting to exclude $y$-values corresponding to cancelled holes $(x - \\alpha) = 0$.",
                "why": "The original function is undefined at $x = \\alpha$.",
                "remedy": "Calculate $y_0 = \\text{lim}_{x \\to \\alpha} f(x)$ and remove $y_0$ from the final range."
            }
        ],
        "examples": [
            {
                "title": "Complete Range of Rational Quadratic Expression",
                "problem": "Find the complete range of the rational expression $y = \\frac{x^2 - 3x + 4}{x^2 + 3x + 4}$ for all real $x \\in \\mathbb{R}$.",
                "approach": "Cross-multiply to formulate a quadratic in $x$: $(y - 1)x^2 + 3(y + 1)x + 4(y - 1) = 0$. Enforce real $x \\implies D_x \\ge 0$, and test $y = 1$ separately.",
                "solution": "1. If $y = 1$:\\n$0 \\cdot x^2 + 3(2)x + 0 = 0 \\implies 6x = 0 \\implies x = 0 \\in \\mathbb{R}$. Thus $y = 1$ is in the range.\\n2. If $y \\ne 1$, quadratic in $x$ must have real roots ($D_x \\ge 0$):\\n$D_x = [3(y + 1)]^2 - 4(y - 1)[4(y - 1)] \\ge 0$\\n$9(y^2 + 2y + 1) - 16(y^2 - 2y + 1) \\ge 0$\\n$9y^2 + 18y + 9 - 16y^2 + 32y - 16 \\ge 0$\\n$-7y^2 + 50y - 7 \\ge 0 \\implies 7y^2 - 50y + 7 \\le 0$\\n$(7y - 1)(y - 7) \\le 0 \\implies y \\in [1/7, 7]$.\\n3. Since $y = 1 \\in [1/7, 7]$, the complete range is $y \\in [1/7, 7]$.",
                "key_takeaway": "Always verify the coefficient of $x^2$ ($y = 1$); here $x = 0$ confirms $y = 1$ is attainable."
            }
        ]
    }
]

def get_quadratic_full_notes():
    """Returns the comprehensive multi-page notes for Quadratic Equations."""
    # Top level represents Sheet 1 by default, and carries the full sheets array
    main_note = dict(QUADRATIC_SHEETS[0])
    main_note["sheets"] = QUADRATIC_SHEETS
    main_note["total_pages"] = len(QUADRATIC_SHEETS)
    return main_note

