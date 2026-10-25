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

# =========================================================================
# ALL 6 PAGES TRANSCRIBED EXACTLY FROM USER'S IMAGES
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
    }
]

def get_quadratic_full_notes():
    """Returns the comprehensive multi-page notes for Quadratic Equations."""
    # Top level represents Sheet 1 by default, and carries the full sheets array
    main_note = dict(QUADRATIC_SHEETS[0])
    main_note["sheets"] = QUADRATIC_SHEETS
    main_note["total_pages"] = len(QUADRATIC_SHEETS)
    return main_note
