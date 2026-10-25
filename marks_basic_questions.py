"""
marks_basic_questions.py - Authentic Level 1 (Basic / Foundation) Questions
sourced and formatted according to Marks App (MathonGo) JEE Main standards.
"""

MARKS_BASIC_QUESTIONS = [
    # =========================================================================
    # PHYSICS - CLASS 11 & 12
    # =========================================================================
    {
        "chapter": "Units, Dimensions & Errors",
        "topic": "SI Units & Derived Dimensions",
        "level": "Basic",
        "type": "mcq_single",
        "question": "[Marks Basic / JEE Main] The dimensional formula for electric permittivity of free space ($\\varepsilon_0$) is:",
        "options": [
            "$\\left[\\text{M}^{-1} \\text{L}^{-3} \\text{T}^{4} \\text{A}^{2}\\right]$",
            "$\\left[\\text{M}^{1} \\text{L}^{3} \\text{T}^{-4} \\text{A}^{-2}\\right]$",
            "$\\left[\\text{M}^{-1} \\text{L}^{3} \\text{T}^{-2} \\text{A}^{1}\\right]$",
            "$\\left[\\text{M}^{1} \\text{L}^{-3} \\text{T}^{2} \\text{A}^{-1}\\right]$"
        ],
        "correct_answer": "[M^-1 L^-3 T^4 A^2]",
        "correct_index": 0,
        "explanation": "From Coulomb's Law, $F = \\frac{1}{4\\pi\\varepsilon_0} \\frac{q_1 q_2}{r^2} \\implies \\varepsilon_0 = \\frac{q^2}{4\\pi F r^2}$.\\n$[q] = [\\text{I} t] = [\\text{A T}]$, $[F] = [\\text{M L T}^{-2}]$, $[r^2] = [\\text{L}^2]$.\\nHence, $[\\varepsilon_0] = \\frac{[\\text{A}^2 \\text{T}^2]}{[\\text{M L T}^{-2}][\\text{L}^2]} = [\\text{M}^{-1} \\text{L}^{-3} \\text{T}^{4} \\text{A}^{2}]$.\\n\\n **Marks Tip**: Remember the standard relation $c = 1/\\sqrt{\\mu_0 \\varepsilon_0}$ to cross-check permittivity and permeability dimensions rapidly."
    },
    {
        "chapter": "Units, Dimensions & Errors",
        "topic": "Errors in Measurement & Combination of Errors",
        "level": "Basic",
        "type": "mcq_single",
        "question": "[Marks Basic / JEE Main] A physical quantity $P$ is related to four observables $a, b, c, d$ as $P = \\frac{a^3 b^2}{\\sqrt{c} d}$. The percentage errors of measurement in $a, b, c, d$ are $1\\%$, $2\\%$, $4\\%$, and $2\\%$ respectively. The maximum percentage error in $P$ is:",
        "options": [
            "$11\\%$",
            "$7\\%$",
            "$9\\%$",
            "$14\\%$"
        ],
        "correct_answer": "11%",
        "correct_index": 0,
        "explanation": "Using fractional error formula for powers:\\n$\\frac{\\Delta P}{P} = 3\\left(\\frac{\\Delta a}{a}\\right) + 2\\left(\\frac{\\Delta b}{b}\\right) + \\frac{1}{2}\\left(\\frac{\\Delta c}{c}\\right) + 1\\left(\\frac{\\Delta d}{d}\\right)$.\\nPercentage error = $3(1\\%) + 2(2\\%) + \\frac{1}{2}(4\\%) + 1(2\\%) = 3\\% + 4\\% + 2\\% + 2\\% = 11\\%$.\\n\\n **Marks Tip**: Errors in measurements always add up in worst-case analysis; denominator powers contribute positively with absolute exponents."
    },
    {
        "chapter": "Motion in a Straight Line",
        "topic": "Displacement, Speed & Velocity",
        "level": "Basic",
        "type": "mcq_single",
        "question": "[Marks Basic / JEE Main] The displacement $x$ of a particle moving in one dimension varies with time $t$ as $x = 2t^3 - 9t^2 + 12t + 5$ (where $x$ is in meters and $t$ is in seconds). The acceleration of the particle when its velocity becomes zero is:",
        "options": [
            "$\\pm 6\\text{ m/s}^2$",
            "$12\\text{ m/s}^2$",
            "$0\\text{ m/s}^2$",
            "$-18\\text{ m/s}^2$"
        ],
        "correct_answer": "+- 6 m/s^2",
        "correct_index": 0,
        "explanation": "Velocity $v = \\frac{dx}{dt} = 6t^2 - 18t + 12 = 6(t^2 - 3t + 2) = 6(t - 1)(t - 2)$.\\nSetting $v = 0$ gives $t = 1\\text{ s}$ and $t = 2\\text{ s}$.\\nAcceleration $a = \\frac{dv}{dt} = 12t - 18$.\\nAt $t = 1\\text{ s}$, $a = 12(1) - 18 = -6\\text{ m/s}^2$.\\nAt $t = 2\\text{ s}$, $a = 12(2) - 18 = +6\\text{ m/s}^2$.\\nThus, the acceleration is $\\pm 6\\text{ m/s}^2$.\\n\\n **Marks Tip**: Don't stop at the first root of velocity; check all physical moments where $v = 0$."
    },
    {
        "chapter": "Motion in a Plane & Projectile Motion",
        "topic": "Horizontal Projectile Motion",
        "level": "Basic",
        "type": "mcq_single",
        "question": "[Marks Basic / JEE Main] A projectile is fired from horizontal ground with speed $u$ at an angle $\\theta$ to the horizontal. If the horizontal range $R$ is equal to twice the maximum height $H$ reached ($R = 2H$), then the angle of projection $\\theta$ is:",
        "options": [
            "$\\arctan(2)$",
            "$\\arctan(1/2)$",
            "$\\arctan(4)$",
            "$45^\\circ$"
        ],
        "correct_answer": "arctan(2)",
        "correct_index": 0,
        "explanation": "We know $R = \\frac{u^2 \\sin 2\\theta}{g} = \\frac{2 u^2 \\sin\\theta \\cos\\theta}{g}$ and $H = \\frac{u^2 \\sin^2\\theta}{2g}$.\\nDividing gives the standard identity $\\frac{R}{H} = \\frac{4}{\\tan\\theta} \\implies R = 4H \\cot\\theta$.\\nGiven $R = 2H \\implies 2H = 4H \\cot\\theta \\implies \\cot\\theta = \\frac{1}{2} \\implies \\tan\\theta = 2 \\implies \\theta = \\arctan(2)$.\\n\\n **Marks Tip**: The golden projectile identity is $R \\tan\\theta = 4H$. Memorize this to solve projectile height-range comparison questions in 10 seconds."
    },
    {
        "chapter": "Laws of Motion & Friction",
        "topic": "Friction (Static, Kinetic, Two-Block Systems)",
        "level": "Basic",
        "type": "mcq_single",
        "question": "[Marks Basic / JEE Main] A block of mass $m = 2\\text{ kg}$ is pressed against a vertical rough wall by applying a horizontal force $F$. If the coefficient of static friction between block and wall is $\\mu_s = 0.4$, the minimum force $F$ required to keep the block stationary is ($g = 10\\text{ m/s}^2$):",
        "options": [
            "$50\\text{ N}$",
            "$20\\text{ N}$",
            "$8\\text{ N}$",
            "$100\\text{ N}$"
        ],
        "correct_answer": "50 N",
        "correct_index": 0,
        "explanation": "For vertical equilibrium: downward gravitational force $mg$ must be balanced by upward static friction $f_s$, so $f_s = mg = 2 \\times 10 = 20\\text{ N}$.\\nThe maximum available static friction is $f_{s,\\max} = \\mu_s N = \\mu_s F$.\\nTo prevent slipping: $f_s \\le f_{s,\\max} \\implies mg \\le \\mu_s F \\implies F \\ge \\frac{mg}{\\mu_s} = \\frac{20}{0.4} = 50\\text{ N}$.\\n\\n **Marks Tip**: Normal force here is provided by the horizontal applied push $F$, not by gravity!"
    },
    {
        "chapter": "Work, Energy & Power",
        "topic": "Work-Energy Theorem",
        "level": "Basic",
        "type": "mcq_single",
        "question": "[Marks Basic / JEE Main] A body of mass $m = 0.5\\text{ kg}$ travels in a straight line with velocity $v = k x^{3/2}$, where $k = 5\\text{ m}^{-1/2}\\text{s}^{-1}$. The work done by the net force during its displacement from $x = 0$ to $x = 2\\text{ m}$ is:",
        "options": [
            "$50\\text{ J}$",
            "$25\\text{ J}$",
            "$100\\text{ J}$",
            "$12.5\\text{ J}$"
        ],
        "correct_answer": "50 J",
        "correct_index": 0,
        "explanation": "By Work-Energy Theorem, $W_{net} = \\Delta K = \\frac{1}{2}m(v_f^2 - v_i^2)$.\\nAt $x = 0$: $v_i = 0$.\\nAt $x = 2\\text{ m}$: $v_f = 5 \\times (2)^{3/2} \\implies v_f^2 = 25 \\times 2^3 = 25 \\times 8 = 200\\text{ m}^2/\\text{s}^2$.\\n$W_{net} = \\frac{1}{2} \\times 0.5 \\times (200 - 0) = 50\\text{ J}$.\\n\\n **Marks Tip**: Always prefer the Work-Energy Theorem over $\\int F dx$ when velocity is directly given as a function of position."
    },
    {
        "chapter": "Center of Mass & Collisions",
        "topic": "Center of Mass of Discrete & Continuous Systems",
        "level": "Basic",
        "type": "mcq_single",
        "question": "[Marks Basic / JEE Main] Two particles of masses $m_1 = 1\\text{ kg}$ and $m_2 = 3\\text{ kg}$ are separated by a distance $L = 20\\text{ cm}$. The distance of the center of mass of the system from the $1\\text{ kg}$ mass is:",
        "options": [
            "$15\\text{ cm}$",
            "$5\\text{ cm}$",
            "$10\\text{ cm}$",
            "$12\\text{ cm}$"
        ],
        "correct_answer": "15 cm",
        "correct_index": 0,
        "explanation": "Taking $m_1$ as the origin ($x_1 = 0$, $x_2 = L = 20\\text{ cm}$):\\n$x_{cm} = \\frac{m_1 x_1 + m_2 x_2}{m_1 + m_2} = \\frac{0 + 3 \\times 20}{1 + 3} = \\frac{60}{4} = 15\\text{ cm}$.\\n\\n **Marks Tip**: Center of mass divides the separating distance internally in the inverse ratio of masses: $r_1 / r_2 = m_2 / m_1 = 3 / 1$."
    },
    {
        "chapter": "Rotational Motion",
        "topic": "Rolling Motion without Slipping",
        "level": "Basic",
        "type": "mcq_single",
        "question": "[Marks Basic / JEE Main] A solid uniform sphere of mass $M$ and radius $R$ rolls purely without slipping on a horizontal surface with linear speed $v$. The ratio of its rotational kinetic energy to its total kinetic energy is:",
        "options": [
            "$2 / 7$",
            "$5 / 7$",
            "$2 / 5$",
            "$1 / 2$"
        ],
        "correct_answer": "2 / 7",
        "correct_index": 0,
        "explanation": "Translational KE $K_{trans} = \\frac{1}{2} M v^2$.\\nFor a solid sphere, $I = \\frac{2}{5} M R^2$, and pure rolling gives $\\omega = v/R$.\\nRotational KE $K_{rot} = \\frac{1}{2} I \\omega^2 = \\frac{1}{2}\\left(\\frac{2}{5} M R^2\\right)\\left(\\frac{v}{R}\\right)^2 = \\frac{1}{5} M v^2$.\\nTotal KE $K_{total} = K_{trans} + K_{rot} = \\frac{1}{2} M v^2 + \\frac{1}{5} M v^2 = \\frac{7}{10} M v^2$.\\nRatio $\\frac{K_{rot}}{K_{total}} = \\frac{1/5}{7/10} = \\frac{2}{7}$.\\n\\n **Marks Tip**: For any rolling body with radius of gyration $k$: $K_{rot}/K_{total} = \\frac{k^2 / R^2}{1 + k^2 / R^2}$. For solid sphere $k^2/R^2 = 2/5 \\implies (2/5)/(1 + 2/5) = 2/7$."
    },
    {
        "chapter": "Gravitation",
        "topic": "Gravitational Field & Potential",
        "level": "Basic",
        "type": "mcq_single",
        "question": "[Marks Basic / JEE Main] The acceleration due to gravity at depth $d$ below the Earth's surface becomes one-fourth ($g/4$) of its value at the surface. If $R$ is Earth's radius, the depth $d$ is:",
        "options": [
            "$\\frac{3}{4} R$",
            "$\\frac{1}{4} R$",
            "$\\frac{1}{2} R$",
            "$\\frac{7}{8} R$"
        ],
        "correct_answer": "3/4 R",
        "correct_index": 0,
        "explanation": "Variation of $g$ with depth $d$ is given by $g_d = g\\left(1 - \\frac{d}{R}\\right)$.\\nGiven $g_d = \\frac{g}{4} \\implies \\frac{g}{4} = g\\left(1 - \\frac{d}{R}\\right) \\implies 1 - \\frac{d}{R} = \\frac{1}{4} \\implies \\frac{d}{R} = \\frac{3}{4} \\implies d = \\frac{3}{4} R$.\\n\\n **Marks Tip**: Note that with depth, $g$ decreases linearly, whereas with height above surface ($h \\ge R$), $g$ follows an inverse-square law."
    },
    {
        "chapter": "Mechanical Properties of Fluids",
        "topic": "Surface Tension & Capillarity",
        "level": "Basic",
        "type": "mcq_single",
        "question": "[Marks Basic / JEE Main] If the excess pressure inside a spherical soap bubble of radius $r_1$ is three times the excess pressure inside another soap bubble of radius $r_2$, the ratio of their surface areas ($A_1 / A_2$) is:",
        "options": [
            "$1 : 9$",
            "$9 : 1$",
            "$1 : 3$",
            "$3 : 1$"
        ],
        "correct_answer": "1 : 9",
        "correct_index": 0,
        "explanation": "Excess pressure inside a soap bubble (having 2 free surfaces) is $\\Delta P = \\frac{4T}{r}$.\\nTherefore, $\\Delta P \\propto \\frac{1}{r} \\implies \\frac{\\Delta P_1}{\\Delta P_2} = \\frac{r_2}{r_1} = 3 \\implies \\frac{r_1}{r_2} = \\frac{1}{3}$.\\nSurface area $A = 4\\pi r^2 \\propto r^2$.\\nHence, $\\frac{A_1}{A_2} = \\left(\\frac{r_1}{r_2}\\right)^2 = \\left(\\frac{1}{3}\\right)^2 = \\frac{1}{9}$.\\n\\n **Marks Tip**: Smaller bubbles have higher internal excess pressure; when two bubbles connect, air rushes from the smaller to the larger bubble."
    },
    {
        "chapter": "Thermodynamics",
        "topic": "First Law & Thermodynamic Processes",
        "level": "Basic",
        "type": "mcq_single",
        "question": "[Marks Basic / JEE Main] An ideal monoatomic gas undergoes an adiabatic expansion such that its volume doubles ($V_2 = 2V_1$). If initial temperature is $T_1 = 300\\text{ K}$, the final temperature $T_2$ is (take $\\gamma = 5/3$, $2^{2/3} \\approx 1.587$):",
        "options": [
            "$\\approx 189\\text{ K}$",
            "$150\\text{ K}$",
            "$600\\text{ K}$",
            "$240\\text{ K}$"
        ],
        "correct_answer": "189 K",
        "correct_index": 0,
        "explanation": "For an adiabatic process: $T V^{\\gamma - 1} = \\text{constant}$.\\nFor a monoatomic gas, $\\gamma = 5/3 \\implies \\gamma - 1 = 2/3$.\\n$T_2 = T_1 \\left(\\frac{V_1}{V_2}\\right)^{\\gamma - 1} = 300 \\left(\\frac{1}{2}\\right)^{2/3} = \\frac{300}{2^{2/3}} \\approx \\frac{300}{1.587} \\approx 189\\text{ K}$.\\n\\n **Marks Tip**: Gas always cools down upon adiabatic expansion because internal energy is consumed doing external work against surroundings ($W = -\\Delta U$)."
    },
    {
        "chapter": "Oscillations (Simple Harmonic Motion)",
        "topic": "Kinematics of SHM (x, v, a Relations)",
        "level": "Basic",
        "type": "mcq_single",
        "question": "[Marks Basic / JEE Main] A particle executes linear SHM with amplitude $A$. At what displacement $x$ from the mean position is its kinetic energy equal to its potential energy?",
        "options": [
            "$x = \\pm \\frac{A}{\\sqrt{2}}$",
            "$x = \\pm \\frac{A}{2}$",
            "$x = \\pm \\frac{A}{\\sqrt{3}}$",
            "$x = \\pm \\frac{\\sqrt{3}}{2} A$"
        ],
        "correct_answer": "+- A / sqrt(2)",
        "correct_index": 0,
        "explanation": "In SHM: $K = \\frac{1}{2} m \\omega^2 (A^2 - x^2)$ and $U = \\frac{1}{2} m \\omega^2 x^2$.\\nEquating $K = U \\implies \\frac{1}{2} m \\omega^2 (A^2 - x^2) = \\frac{1}{2} m \\omega^2 x^2 \\implies A^2 - x^2 = x^2 \\implies 2x^2 = A^2 \\implies x = \\pm \\frac{A}{\\sqrt{2}}$.\\n\\n **Marks Tip**: At $x = A/2$, $U = \\frac{1}{4} E_{total}$ and $K = \\frac{3}{4} E_{total}$. Remember that equality occurs at $A/\\sqrt{2} \\approx 0.707 A$."
    },
    {
        "chapter": "Electrostatics: Electric Charges & Fields",
        "topic": "Coulomb's Law & Electric Field Intensity",
        "level": "Basic",
        "type": "mcq_single",
        "question": "[Marks Basic / JEE Main] Two point charges $+9e$ and $+e$ are fixed at a distance $d = 16\\text{ cm}$ apart. A third charge $q$ is placed on the line joining them such that the entire system is in equilibrium. The distance of $q$ from the $+9e$ charge is:",
        "options": [
            "$12\\text{ cm}$",
            "$4\\text{ cm}$",
            "$8\\text{ cm}$",
            "$6\\text{ cm}$"
        ],
        "correct_answer": "12 cm",
        "correct_index": 0,
        "explanation": "Let $q$ be placed at distance $x$ from $+9e$. For net electric force on $q$ to be zero:\\n$\\frac{k (9e) q}{x^2} = \\frac{k (e) q}{(d - x)^2} \\implies \\frac{9}{x^2} = \\frac{1}{(d - x)^2}$.\\nTaking square roots: $\\frac{3}{x} = \\frac{1}{d - x} \\implies 3(d - x) = x \\implies 4x = 3d \\implies x = \\frac{3}{4} d = \\frac{3}{4}(16) = 12\\text{ cm}$.\\n\\n **Marks Tip**: For like charges $q_1$ and $q_2$, neutral point lies between them at $x = \\frac{d}{1 + \\sqrt{q_2/q_1}}$ measured from $q_1$."
    },
    {
        "chapter": "Electrostatic Potential & Capacitance",
        "topic": "Capacitance & Dielectrics",
        "level": "Basic",
        "type": "mcq_single",
        "question": "[Marks Basic / JEE Main] A parallel plate capacitor of capacitance $C_0$ is charged to a potential difference $V_0$ by a battery. The battery is now disconnected, and a dielectric slab of dielectric constant $K = 4$ is completely inserted between the plates. The new electrostatic energy $U$ stored in the capacitor in terms of initial energy $U_0$ is:",
        "options": [
            "$U_0 / 4$",
            "$4 U_0$",
            "$U_0 / 16$",
            "$U_0$"
        ],
        "correct_answer": "U_0 / 4",
        "correct_index": 0,
        "explanation": "Battery disconnected $\\implies$ charge $Q$ remains conserved ($Q = Q_0$).\\nWith dielectric inserted, capacitance increases: $C = K C_0 = 4 C_0$.\\nEnergy stored: $U = \\frac{Q^2}{2C} = \\frac{Q_0^2}{2(4 C_0)} = \\frac{1}{4}\\left(\\frac{Q_0^2}{2C_0}\\right) = \\frac{U_0}{4}$.\\n\\n **Marks Tip**: If the battery remains connected, $V = V_0 = \\text{const}$, and stored energy increases by $K$: $U = K U_0$."
    },
    {
        "chapter": "Current Electricity",
        "topic": "Ohm's Law & Drift Velocity",
        "level": "Basic",
        "type": "mcq_single",
        "question": "[Marks Basic / JEE Main] A uniform metallic wire of resistance $R = 16\\,\\Omega$ is uniformly stretched so that its length becomes twice its original length ($L' = 2L$). Assuming density remains constant, the new resistance $R'$ of the wire is:",
        "options": [
            "$64\\,\\Omega$",
            "$32\\,\\Omega$",
            "$16\\,\\Omega$",
            "$8\\,\\Omega$"
        ],
        "correct_answer": "64 Omega",
        "correct_index": 0,
        "explanation": "Volume of wire remains constant upon stretching: $V = A L = A' L' \\implies A' = A \\left(\\frac{L}{L'}\\right) = \\frac{A}{2}$.\\nResistance $R = \\rho \\frac{L}{A}$.\\nNew resistance $R' = \\rho \\frac{L'}{A'} = \\rho \\frac{2L}{A/2} = 4 \\left(\\rho \\frac{L}{A}\\right) = 4R = 4 \\times 16 = 64\\,\\Omega$.\\n\\n **Marks Tip**: When a wire is stretched $n$ times in length without adding mass: $R' = n^2 R$."
    },
    {
        "chapter": "Moving Charges & Magnetism",
        "topic": "Biot-Savart Law & Magnetic Field",
        "level": "Basic",
        "type": "mcq_single",
        "question": "[Marks Basic / JEE Main] The magnetic field at the center of a circular current-carrying loop of radius $R$ is $B_0$. The magnetic field on its axis at a distance $x = \\sqrt{3}R$ from the center is:",
        "options": [
            "$B_0 / 8$",
            "$B_0 / 4$",
            "$B_0 / 2$",
            "$B_0 / 16$"
        ],
        "correct_answer": "B_0 / 8",
        "correct_index": 0,
        "explanation": "Field on the axis: $B_{axis} = \\frac{\\mu_0 I R^2}{2(R^2 + x^2)^{3/2}}$. At center ($x = 0$): $B_0 = \\frac{\\mu_0 I}{2R}$.\\nSubstituting $x = \\sqrt{3}R$:\\n$(R^2 + x^2)^{3/2} = (R^2 + 3R^2)^{3/2} = (4R^2)^{3/2} = 8 R^3$.\\n$B_{axis} = \\frac{\\mu_0 I R^2}{2(8 R^3)} = \\frac{1}{8} \\left(\\frac{\\mu_0 I}{2R}\\right) = \\frac{B_0}{8}$.\\n\\n **Marks Tip**: Standard formula: $B_{axis} = B_0 \\cos^3\\theta$, where $\\tan\\theta = x/R$. Here $\\tan\\theta = \\sqrt{3} \\implies \\theta = 60^\\circ \\implies \\cos^3(60^\\circ) = (1/2)^3 = 1/8$."
    },
    {
        "chapter": "Electromagnetic Induction (EMI)",
        "topic": "Faraday's & Lenz's Law",
        "level": "Basic",
        "type": "mcq_single",
        "question": "[Marks Basic / JEE Main] The magnetic flux linked with a coil of resistance $10\\,\\Omega$ varies with time $t$ as $\\Phi = 6t^2 - 5t + 1$ (in Weber). The magnitude of induced current at $t = 0.5\\text{ s}$ is:",
        "options": [
            "$0.1\\text{ A}$",
            "$1.0\\text{ A}$",
            "$0.2\\text{ A}$",
            "$0.5\\text{ A}$"
        ],
        "correct_answer": "0.1 A",
        "correct_index": 0,
        "explanation": "Induced electromotive force $|e| = \\left|\\frac{d\\Phi}{dt}\\right| = |12t - 5|$.\\nAt $t = 0.5\\text{ s}$: $|e| = |12(0.5) - 5| = |6 - 5| = 1\\text{ V}$.\\nInduced current $i = \\frac{|e|}{R} = \\frac{1\\text{ V}}{10\\,\\Omega} = 0.1\\text{ A}$.\\n\\n **Marks Tip**: Always differentiate first, then substitute the numerical timestamp to find instantaneous emf."
    },
    {
        "chapter": "Dual Nature of Radiation & Matter",
        "topic": "Photoelectric Effect & Einstein's Equation",
        "level": "Basic",
        "type": "mcq_single",
        "question": "[Marks Basic / JEE Main] When light of wavelength $300\\text{ nm}$ falls on a metal surface, photoelectrons are emitted with maximum kinetic energy $1.5\\text{ eV}$. The work function of the metal is ($hc \\approx 1240\\text{ eV}\\cdot\\text{nm}$):",
        "options": [
            "$2.63\\text{ eV}$",
            "$4.13\\text{ eV}$",
            "$1.50\\text{ eV}$",
            "$3.10\\text{ eV}$"
        ],
        "correct_answer": "2.63 eV",
        "correct_index": 0,
        "explanation": "Energy of incident photon $E = \\frac{hc}{\\lambda} = \\frac{1240\\text{ eV}\\cdot\\text{nm}}{300\\text{ nm}} \\approx 4.13\\text{ eV}$.\\nBy Einstein's Photoelectric Equation: $K_{\\max} = E - \\Phi_0 \\implies \\Phi_0 = E - K_{\\max} = 4.13\\text{ eV} - 1.5\\text{ eV} = 2.63\\text{ eV}$.\\n\\n **Marks Tip**: Use $E(\\text{eV}) = \\frac{1240}{\\lambda(\\text{nm})}$ for rapid calculation in modern physics."
    },
    {
        "chapter": "Atoms",
        "topic": "Bohr's Model & Hydrogen Spectrum",
        "level": "Basic",
        "type": "mcq_single",
        "question": "[Marks Basic / JEE Main] The ratio of the radius of the 2nd Bohr orbit of $\\text{He}^+$ ion to that of the 3rd Bohr orbit of $\\text{Li}^{2+}$ ion is:",
        "options": [
            "$2 : 3$",
            "$4 : 9$",
            "$3 : 2$",
            "$8 : 27$"
        ],
        "correct_answer": "2 : 3",
        "correct_index": 0,
        "explanation": "Bohr radius formula: $r_n = 0.529 \\frac{n^2}{Z} \\propto \\frac{n^2}{Z}$.\\nFor $\\text{He}^+$: $n_1 = 2$, $Z_1 = 2 \\implies \\frac{n_1^2}{Z_1} = \\frac{2^2}{2} = 2$.\\nFor $\\text{Li}^{2+}$: $n_2 = 3$, $Z_2 = 3 \\implies \\frac{n_2^2}{Z_2} = \\frac{3^2}{3} = 3$.\\nRatio $\\frac{r_1}{r_2} = \\frac{2}{3} = 2 : 3$.\\n\\n **Marks Tip**: Don't calculate absolute radii in angstroms; always set up the proportionality ratio $r \\propto n^2 / Z$ directly."
    },
    {
        "chapter": "Semiconductor Electronics",
        "topic": "p-n Junction Diode Characteristics",
        "level": "Basic",
        "type": "mcq_single",
        "question": "[Marks Basic / JEE Main] In a forward-biased ideal silicon p-n junction diode with a knee voltage (barrier potential) of $0.7\\text{ V}$, connected in series with a resistor $R = 200\\,\\Omega$ and a $5.7\\text{ V}$ DC supply, the current flowing in the circuit is:",
        "options": [
            "$25\\text{ mA}$",
            "$28.5\\text{ mA}$",
            "$3.5\\text{ mA}$",
            "$50\\text{ mA}$"
        ],
        "correct_answer": "25 mA",
        "correct_index": 0,
        "explanation": "Under forward bias above knee voltage, the diode maintains a constant voltage drop of $V_d = 0.7\\text{ V}$.\\nVoltage drop across resistor $V_R = V_{supply} - V_d = 5.7 - 0.7 = 5.0\\text{ V}$.\\nCurrent $I = \\frac{V_R}{R} = \\frac{5.0\\text{ V}}{200\\,\\Omega} = 0.025\\text{ A} = 25\\text{ mA}$.\\n\\n **Marks Tip**: Never apply Ohm's law directly across the entire loop without subtracting the barrier drop ($V_d = 0.7\\text{V}$ for Si, $0.3\\text{V}$ for Ge)."
    },

    # =========================================================================
    # CHEMISTRY - CLASS 11 & 12
    # =========================================================================
    {
        "chapter": "Some Basic Concepts of Chemistry (Mole Concept)",
        "topic": "Mole Concept & Stoichiometry",
        "level": "Basic",
        "type": "mcq_single",
        "question": "[Marks Basic / JEE Main] The total number of electrons present in $1.6\\text{ g}$ of methane gas ($\\text{CH}_4$) is ($N_A = 6.022 \\times 10^{23}$):",
        "options": [
            "$6.022 \\times 10^{23}$",
            "$1.204 \\times 10^{24}$",
            "$6.022 \\times 10^{22}$",
            "$3.011 \\times 10^{23}$"
        ],
        "correct_answer": "6.022 x 10^23",
        "correct_index": 0,
        "explanation": "Molar mass of $\\text{CH}_4 = 12 + 4(1) = 16\\text{ g/mol}$.\\nMoles of $\\text{CH}_4 = \\frac{1.6}{16} = 0.1\\text{ mol}$.\\nOne molecule of $\\text{CH}_4$ has $6 + 4(1) = 10$ electrons.\\nTotal electrons = $0.1 \\times 10 \\times N_A = 1 \\times N_A = 6.022 \\times 10^{23}$.\\n\\n **Marks Tip**: Multiply moles by (electrons per molecule) $\\times N_A$."
    },
    {
        "chapter": "Structure of Atom",
        "topic": "Quantum Numbers & Electronic Configuration",
        "level": "Basic",
        "type": "mcq_single",
        "question": "[Marks Basic / JEE Main] Which of the following sets of quantum numbers $(n, l, m_l, m_s)$ is NOT permissible for an electron in an atom?",
        "options": [
            "$(3, 2, -3, +1/2)$",
            "$(4, 0, 0, -1/2)$",
            "$(3, 2, -1, +1/2)$",
            "$(2, 1, +1, -1/2)$"
        ],
        "correct_answer": "(3, 2, -3, +1/2)",
        "correct_index": 0,
        "explanation": "Rules for quantum numbers:\\n1. $l$ can take integer values from $0$ to $n-1$.\\n2. $m_l$ can take values from $-l$ to $+l$.\\nFor $l = 2$, allowable $m_l \\in \\{-2, -1, 0, +1, +2\\}$. A value of $m_l = -3$ is strictly forbidden because $|m_l| \\le l$.\\n\\n **Marks Tip**: Always check whether $|m_l| \\le l$ first; that is the most frequent trap in JEE quantum number questions."
    },
    {
        "chapter": "Classification of Elements & Periodicity",
        "topic": "Ionization Enthalpy & Electron Gain",
        "level": "Basic",
        "type": "mcq_single",
        "question": "[Marks Basic / JEE Main] The correct order of first ionization enthalpy ($\\Delta_i H_1$) for the elements $\\text{Be}, \\text{B}, \\text{N}, \\text{O}$ is:",
        "options": [
            "$\\text{B} < \\text{Be} < \\text{O} < \\text{N}$",
            "$\\text{Be} < \\text{B} < \\text{N} < \\text{O}$",
            "$\\text{B} < \\text{Be} < \\text{N} < \\text{O}$",
            "$\\text{Be} < \\text{B} < \\text{O} < \\text{N}$"
        ],
        "correct_answer": "B < Be < O < N",
        "correct_index": 0,
        "explanation": "General trend increases across Period 2 with two famous anomalies:\\n1. $\\text{Be} (2s^2)$ has higher $\\text{IE}_1$ than $\\text{B} (2s^2 2p^1)$ because removing an electron from completely filled $2s$ takes more energy than from $2p$.\\n2. $\\text{N} (2s^2 2p^3)$ has higher $\\text{IE}_1$ than $\\text{O} (2s^2 2p^4)$ due to extra stability of half-filled $2p^3$ subshell.\\nHence, increasing order: $\\text{B} (801) < \\text{Be} (899) < \\text{O} (1314) < \\text{N} (1402\\text{ kJ/mol})$.\\n\\n **Marks Tip**: Memorize the mnemonic: $\\text{Li} < \\text{B} < \\text{Be} < \\text{C} < \\text{O} < \\text{N} < \\text{F} < \\text{Ne}$."
    },
    {
        "chapter": "Chemical Bonding & Molecular Structure",
        "topic": "VSEPR Theory & Molecular Geometry",
        "level": "Basic",
        "type": "mcq_single",
        "question": "[Marks Basic / JEE Main] The hybridization of the central atom and the molecular geometry of $\\text{SF}_4$ are respectively:",
        "options": [
            "$sp^3d$, See-saw",
            "$sp^3$, Tetrahedral",
            "$sp^3d^2$, Square planar",
            "$sp^3d$, Trigonal bipyramidal"
        ],
        "correct_answer": "sp^3d, See-saw",
        "correct_index": 0,
        "explanation": "Steric Number for sulfur in $\\text{SF}_4$:\\nValence electrons of S = $6$. Bond pairs = $4$. Lone pairs = $\\frac{6 - 4}{2} = 1$.\\nTotal steric number = $4 + 1 = 5 \\implies sp^3d$ hybridization.\\nElectron pair geometry is trigonal bipyramidal; with 1 equatorial lone pair, molecular shape is **See-saw**.\\n\\n **Marks Tip**: Lone pair in $sp^3d$ always prefers equatorial positions to minimize $90^\\circ$ repulsions."
    },
    {
        "chapter": "Chemical Thermodynamics & Thermochemistry",
        "topic": "Gibbs Energy & Spontaneity",
        "level": "Basic",
        "type": "mcq_single",
        "question": "[Marks Basic / JEE Main] For a certain chemical reaction, $\\Delta H = +30.5\\text{ kJ/mol}$ and $\\Delta S = +61\\text{ J/mol}\\cdot\\text{K}$. The minimum temperature above which the reaction becomes spontaneous is:",
        "options": [
            "$500\\text{ K}$",
            "$250\\text{ K}$",
            "$300\\text{ K}$",
            "$1000\\text{ K}$"
        ],
        "correct_answer": "500 K",
        "correct_index": 0,
        "explanation": "Condition for spontaneity: $\\Delta G = \\Delta H - T\\Delta S < 0 \\implies T > \\frac{\\Delta H}{\\Delta S}$.\\nConvert $\\Delta H$ to Joules: $\\Delta H = 30.5 \\times 10^3\\text{ J/mol}$.\\n$T_{eq} = \\frac{30500\\text{ J/mol}}{61\\text{ J/mol}\\cdot\\text{K}} = 500\\text{ K}$.\\nFor $T > 500\\text{ K}$, $\\Delta G < 0$, so the reaction is spontaneous.\\n\\n **Marks Tip**: Beware of units! $\\Delta H$ is usually in $\\text{kJ}$ whereas $\\Delta S$ is in $\\text{J/K}$. Always convert to common units before dividing."
    },
    {
        "chapter": "Chemical Equilibrium",
        "topic": "Equilibrium Constant (Kp & Kc)",
        "level": "Basic",
        "type": "mcq_single",
        "question": "[Marks Basic / JEE Main] For the reaction $\\text{N}_2(g) + 3\\text{H}_2(g) \\rightleftharpoons 2\\text{NH}_3(g)$, the relation between equilibrium constants $K_p$ and $K_c$ is:",
        "options": [
            "$K_p = K_c (RT)^{-2}$",
            "$K_p = K_c (RT)^{2}$",
            "$K_p = K_c (RT)^{-1}$",
            "$K_p = K_c$"
        ],
        "correct_answer": "Kp = Kc (RT)^-2",
        "correct_index": 0,
        "explanation": "The general thermodynamic relation is $K_p = K_c (RT)^{\\Delta n_g}$, where $\\Delta n_g = \\sum n_{products}(g) - \\sum n_{reactants}(g)$.\\nHere $\\Delta n_g = 2 - (1 + 3) = 2 - 4 = -2$.\\nTherefore, $K_p = K_c (RT)^{-2}$.\\n\\n **Marks Tip**: Only count gaseous species when calculating $\\Delta n_g$; pure solids and liquids have activity 1."
    },
    {
        "chapter": "Solutions & Colligative Properties",
        "topic": "Depression in Freezing Point & Elevation in Boiling Point",
        "level": "Basic",
        "type": "mcq_single",
        "question": "[Marks Basic / JEE Main] Which of the following $0.1\\text{ M}$ aqueous solutions will exhibit the LOWEST freezing point?",
        "options": [
            "$\\text{Al}_2(\\text{SO}_4)_3$",
            "$\\text{BaCl}_2$",
            "$\\text{NaCl}$",
            "$\\text{Glucose}$"
        ],
        "correct_answer": "Al_2(SO_4)_3",
        "correct_index": 0,
        "explanation": "Depression in freezing point $\\Delta T_f = i \\cdot K_f \\cdot m$. Freezing point $T_f = T_f^\\circ - \\Delta T_f$.\\nHighest $\\Delta T_f$ produces the lowest freezing point.\\nAssuming complete dissociation, van't Hoff factor $i$:\\n- $\\text{Glucose}: i = 1$\\n- $\\text{NaCl}: i = 2$\\n- $\\text{BaCl}_2: i = 3$\\n- $\\text{Al}_2(\\text{SO}_4)_3: i = 2 + 3 = 5$.\\nSince $\\text{Al}_2(\\text{SO}_4)_3$ has largest $i = 5$, it has the largest $\\Delta T_f$ and thus the lowest freezing point.\\n\\n **Marks Tip**: Lowest freezing point corresponds to maximum $i \\times C$."
    },
    {
        "chapter": "Chemical Kinetics",
        "topic": "Order & Molecularity of Reaction",
        "level": "Basic",
        "type": "mcq_single",
        "question": "[Marks Basic / JEE Main] For a first-order reaction $A \\to \\text{Products}$, the half-life period is $t_{1/2} = 20\\text{ minutes}$. The time required for $75\\%$ completion of the reaction is:",
        "options": [
            "$40\\text{ minutes}$",
            "$30\\text{ minutes}$",
            "$60\\text{ minutes}$",
            "$80\\text{ minutes}$"
        ],
        "correct_answer": "40 minutes",
        "correct_index": 0,
        "explanation": "$75\\%$ completion means $25\\%$ remains unreacted: $[A] = \\frac{1}{4}[A]_0 = \\left(\\frac{1}{2}\\right)^2 [A]_0$.\\nThis corresponds to exactly two half-lives ($n = 2$).\\n$t_{75\\%} = 2 \\times t_{1/2} = 2 \\times 20\\text{ min} = 40\\text{ minutes}$.\\n\\n **Marks Tip**: Standard first-order benchmarks: $t_{75\\%} = 2 t_{1/2}$, $t_{87.5\\%} = 3 t_{1/2}$, $t_{99.9\\%} \\approx 10 t_{1/2}$."
    },
    {
        "chapter": "General Organic Chemistry (GOC)",
        "topic": "Carbocation, Carbanion & Free Radical Stability",
        "level": "Basic",
        "type": "mcq_single",
        "question": "[Marks Basic / JEE Main] The correct decreasing order of stability for the following carbocations is:\\n(I) $(CH_3)_3 C^+$, (II) $(CH_3)_2 CH^+$, (III) $CH_3 CH_2^+$, (IV) $CH_3^+$",
        "options": [
            "$\\text{I} > \\text{II} > \\text{III} > \\text{IV}$",
            "$\\text{IV} > \\text{III} > \\text{II} > \\text{I}$",
            "$\\text{I} > \\text{III} > \\text{II} > \\text{IV}$",
            "$\\text{II} > \\text{I} > \\text{III} > \\text{IV}$"
        ],
        "correct_answer": "I > II > III > IV",
        "correct_index": 0,
        "explanation": "Carbocation stability is governed by hyperconjugation (number of $\\alpha$-hydrogens) and $+I$ inductive effect of alkyl groups:\\n- $(CH_3)_3 C^+$ ($3^\\circ$): $9\\,\\alpha\\text{-H}$ hyperconjugative structures\\n- $(CH_3)_2 CH^+$ ($2^\\circ$): $6\\,\\alpha\\text{-H}$\\n- $CH_3 CH_2^+$ ($1^\\circ$): $3\\,\\alpha\\text{-H}$\\n- $CH_3^+$ (methyl): $0\\,\\alpha\\text{-H}$.\\nDecreasing order: $3^\\circ > 2^\\circ > 1^\\circ > \\text{methyl}$.\\n\\n **Marks Tip**: Stability of carbocations and free radicals follows $3^\\circ > 2^\\circ > 1^\\circ$, whereas simple carbanions follow the exact reverse: $\\text{methyl} > 1^\\circ > 2^\\circ > 3^\\circ$."
    },
    {
        "chapter": "Coordination Compounds",
        "topic": "IUPAC Nomenclature & Isomerism",
        "level": "Basic",
        "type": "mcq_single",
        "question": "[Marks Basic / JEE Main] The spin-only magnetic moment of $[\\text{Fe}(\\text{CN})_6]^{4-}$ complex ion is ($Z$ of $\\text{Fe} = 26$):",
        "options": [
            "$0\\text{ BM}$ (Diamagnetic)",
            "$4.9\\text{ BM}$",
            "$5.9\\text{ BM}$",
            "$1.73\\text{ BM}$"
        ],
        "correct_answer": "0 BM (Diamagnetic)",
        "correct_index": 0,
        "explanation": "Oxidation state of Fe in $[\\text{Fe}(\\text{CN})_6]^{4-}$ is $+2$ ($x + 6(-1) = -4 \\implies x = +2$).\\nElectronic configuration of $\\text{Fe}^{2+}$ is $[\\text{Ar}] 3d^6$.\\n$\\text{CN}^-$ is a strong field ligand (SFL) that causes pairing of electrons: $t_{2g}^6 e_g^0$.\\nNumber of unpaired electrons $n = 0$.\\nSpin-only magnetic moment $\\mu = \\sqrt{n(n+2)} = \\sqrt{0(2)} = 0\\text{ BM}$ (Diamagnetic).\\n\\n **Marks Tip**: With weak field ligand like $\\text{H}_2\\text{O}$ or $\\text{F}^-$, $[\\text{Fe}(\\text{H}_2\\text{O})_6]^{2+}$ is high-spin with $n = 4$ unpaired electrons ($\\mu = \\sqrt{24} \\approx 4.9\\text{ BM}$)."
    },

    # =========================================================================
    # MATHEMATICS - CLASS 11 & 12
    # =========================================================================
    {
        "chapter": "Quadratic Equations & Expressions",
        "topic": "Nature & Range of Roots",
        "level": "Basic",
        "type": "mcq_single",
        "question": "[Marks Basic / JEE Main] If the equation $x^2 - 2(k + 1)x + (k^2 + 2k - 3) = 0$ has real and equal roots, the value of $k$ is:",
        "options": [
            "No real value exists",
            "$k = 1$",
            "$k = -2$",
            "$k = 3$"
        ],
        "correct_answer": "No real value exists",
        "correct_index": 0,
        "explanation": "For real and equal roots, discriminant $D = 0$.\\n$D = [-2(k+1)]^2 - 4(1)(k^2 + 2k - 3) = 4(k^2 + 2k + 1) - 4(k^2 + 2k - 3)$.\\n$D = 4[k^2 + 2k + 1 - k^2 - 2k + 3] = 4(4) = 16 > 0$.\\nNotice that $D = 16$ is a positive constant strictly independent of $k$!\\nSince $D = 16 \\ne 0$ for all real $k$, the roots are always real and distinct. Thus, no value of $k$ makes the roots equal.\\n\\n **Marks Tip**: Always compute $D$ fully before assuming $k$ can be solved; when $k$ terms cancel out, $D$ is constant!"
    },
    {
        "chapter": "Complex Numbers",
        "topic": "Algebra of Complex Numbers & Modulus-Amplitude",
        "level": "Basic",
        "type": "mcq_single",
        "question": "[Marks Basic / JEE Main] If $\\omega$ is a complex cube root of unity, the value of $(1 - \\omega + \\omega^2)^5 + (1 + \\omega - \\omega^2)^5$ is:",
        "options": [
            "$32$",
            "$-32$",
            "$64$",
            "$0$"
        ],
        "correct_answer": "32",
        "correct_index": 0,
        "explanation": "Recall standard identity: $1 + \\omega + \\omega^2 = 0 \\implies 1 + \\omega^2 = -\\omega$ and $1 + \\omega = -\\omega^2$.\\nFirst term: $(1 + \\omega^2 - \\omega)^5 = (-\\omega - \\omega)^5 = (-2\\omega)^5 = -32 \\omega^5 = -32 \\omega^2$ (since $\\omega^3 = 1$).\\nSecond term: $(1 + \\omega - \\omega^2)^5 = (-\\omega^2 - \\omega^2)^5 = (-2\\omega^2)^5 = -32 \\omega^{10} = -32 \\omega$ (since $\\omega^{10} = \\omega$).\\nSum = $-32 (\\omega^2 + \\omega) = -32 (-1) = +32$.\\n\\n **Marks Tip**: Substitute $1 + \\omega = -\\omega^2$ or $1 + \\omega^2 = -\\omega$ immediately whenever you see terms of cube roots of unity."
    },
    {
        "chapter": "Sequences and Series",
        "topic": "Arithmetic Progression (AP)",
        "level": "Basic",
        "type": "mcq_single",
        "question": "[Marks Basic / JEE Main] If the sum of first $n$ terms of an AP is given by $S_n = 3n^2 + 5n$, its $m$-th term $T_m$ is equal to $164$. The value of $m$ is:",
        "options": [
            "$27$",
            "$28$",
            "$26$",
            "$25$"
        ],
        "correct_answer": "27",
        "correct_index": 0,
        "explanation": "The $n$-th term is $T_n = S_n - S_{n-1}$.\\n$T_n = (3n^2 + 5n) - [3(n-1)^2 + 5(n-1)] = 3(2n - 1) + 5 = 6n + 2$.\\nGiven $T_m = 164 \\implies 6m + 2 = 164 \\implies 6m = 162 \\implies m = 27$.\\n\\n **Marks Tip**: For $S_n = An^2 + Bn$, common difference is always $d = 2A$ and $T_n = 2An + (B - A)$. Here $d = 2(3) = 6$ and $T_n = 6n + (5 - 3) = 6n + 2$."
    },
    {
        "chapter": "Binomial Theorem",
        "topic": "General Term & Binomial Coefficients",
        "level": "Basic",
        "type": "mcq_single",
        "question": "[Marks Basic / JEE Main] The coefficient of $x^7$ in the expansion of $\\left(x^2 + \\frac{1}{x}\\right)^{11}$ is:",
        "options": [
            "$462$",
            "$330$",
            "$165$",
            "$0$"
        ],
        "correct_answer": "462",
        "correct_index": 0,
        "explanation": "General term $T_{r+1} = {}^{11}C_r (x^2)^{11-r} (x^{-1})^r = {}^{11}C_r x^{22 - 2r - r} = {}^{11}C_r x^{22 - 3r}$.\\nWe need power of $x$ to be $7$:\\n$22 - 3r = 7 \\implies 3r = 15 \\implies r = 5$.\\nCoefficient is ${}^{11}C_5 = \\frac{11 \\times 10 \\times 9 \\times 8 \\times 7}{5 \\times 4 \\times 3 \\times 2 \\times 1} = 462$.\\n\\n **Marks Tip**: Ensure $r$ is an integer in $[0, n]$; if $r$ is fractional, the coefficient is strictly $0$."
    },
    {
        "chapter": "Matrices",
        "topic": "Matrix Multiplication & Properties",
        "level": "Basic",
        "type": "mcq_single",
        "question": "[Marks Basic / JEE Main] If $A$ is a square matrix of order $3 \\times 3$ such that $\\det(A) = |A| = 4$, then the value of $|2 \\text{adj}(A)|$ is:",
        "options": [
            "$128$",
            "$64$",
            "$32$",
            "$256$"
        ],
        "correct_answer": "128",
        "correct_index": 0,
        "explanation": "For any $n \\times n$ matrix $M$ and scalar $k$: $|k M| = k^n |M|$. Here $n = 3$, so $|2 \\text{adj}(A)| = 2^3 |\\text{adj}(A)| = 8 |\\text{adj}(A)|$.\\nBy determinant property of adjoint: $|\\text{adj}(A)| = |A|^{n-1} = |A|^{3-1} = |A|^2$.\\nGiven $|A| = 4 \\implies |\\text{adj}(A)| = 4^2 = 16$.\\nTherefore, $|2 \\text{adj}(A)| = 8 \\times 16 = 128$.\\n\\n **Marks Tip**: Don't forget that the scalar factor $k$ pulls out as $k^n$, where $n$ is the dimension of the matrix."
    },
    {
        "chapter": "Limits & Derivatives (Foundations)",
        "topic": "Limits of Trigonometric & Algebraic Functions",
        "level": "Basic",
        "type": "mcq_single",
        "question": "[Marks Basic / JEE Main] The value of $\\lim_{x \\to 0} \\frac{e^{3x} - 1}{\\sin(2x)}$ is:",
        "options": [
            "$3 / 2$",
            "$2 / 3$",
            "$1$",
            "$6$"
        ],
        "correct_answer": "3 / 2",
        "correct_index": 0,
        "explanation": "Standard limits: $\\lim_{u \\to 0} \\frac{e^u - 1}{u} = 1$ and $\\lim_{v \\to 0} \\frac{\\sin v}{v} = 1$.\\nRewrite expression: $\\frac{e^{3x} - 1}{\\sin 2x} = \\frac{\\frac{e^{3x} - 1}{3x} \\times 3x}{\\frac{\\sin 2x}{2x} \\times 2x} = \\frac{1 \\times 3x}{1 \\times 2x} = \\frac{3}{2}$.\\n(Alternatively via L'Hôpital: $\\lim_{x\\to 0} \\frac{3e^{3x}}{2\\cos 2x} = \\frac{3(1)}{2(1)} = \\frac{3}{2}$).\\n\\n **Marks Tip**: Both algebraic expansion and L'Hôpital work quickly for $0/0$ indeterminate limits."
    },
    {
        "chapter": "Indefinite Integration",
        "topic": "Integration by Substitution",
        "level": "Basic",
        "type": "mcq_single",
        "question": "[Marks Basic / JEE Main] The integral $\\int \\frac{dx}{x (x^6 + 1)}$ is equal to (where $C$ is arbitrary constant):",
        "options": [
            "$\\frac{1}{6} \\ln\\left|\\frac{x^6}{x^6 + 1}\\right| + C$",
            "$\\frac{1}{6} \\ln|x^6 + 1| + C$",
            "$\\ln\\left|\\frac{x}{x^6 + 1}\\right| + C$",
            "$\\frac{1}{5} \\ln\\left|\\frac{x^5}{x^6 + 1}\\right| + C$"
        ],
        "correct_answer": "1/6 ln|x^6 / (x^6 + 1)| + C",
        "correct_index": 0,
        "explanation": "Multiply numerator and denominator by $x^5$:\\n$I = \\int \\frac{x^5 dx}{x^6 (x^6 + 1)}$.\\nLet $t = x^6 \\implies dt = 6x^5 dx \\implies x^5 dx = \\frac{dt}{6}$.\\n$I = \\frac{1}{6} \\int \\frac{dt}{t(t + 1)} = \\frac{1}{6} \\int \\left(\\frac{1}{t} - \\frac{1}{t+1}\\right) dt = \\frac{1}{6} [\\ln|t| - \\ln|t+1|] + C = \\frac{1}{6} \\ln\\left|\\frac{x^6}{x^6 + 1}\\right| + C$.\\n\\n **Marks Tip**: For $\\int \\frac{dx}{x(x^n + 1)}$, always multiply by $x^{n-1}$ to get $\\frac{1}{n} \\ln\\left|\\frac{x^n}{x^n + 1}\\right| + C$ directly."
    },
    {
        "chapter": "Definite Integration",
        "topic": "Properties of Definite Integrals (King's Rule)",
        "level": "Basic",
        "type": "mcq_single",
        "question": "[Marks Basic / JEE Main] The value of $\\int_{0}^{\\pi/2} \\frac{\\sin^4(x)}{\\sin^4(x) + \\cos^4(x)} \\, dx$ is:",
        "options": [
            "$\\pi / 4$",
            "$\\pi / 2$",
            "$\\pi$",
            "$1$"
        ],
        "correct_answer": "pi / 4",
        "correct_index": 0,
        "explanation": "Let $I = \\int_{0}^{\\pi/2} \\frac{\\sin^4 x}{\\sin^4 x + \\cos^4 x} dx$ ...(1).\\nApplying King's property $\\int_a^b f(x) dx = \\int_a^b f(a + b - x) dx$ with $a+b-x = \\pi/2 - x$:\\n$I = \\int_{0}^{\\pi/2} \\frac{\\sin^4(\\pi/2 - x)}{\\sin^4(\\pi/2 - x) + \\cos^4(\\pi/2 - x)} dx = \\int_{0}^{\\pi/2} \\frac{\\cos^4 x}{\\cos^4 x + \\sin^4 x} dx$ ...(2).\\nAdding (1) and (2):\\n$2I = \\int_{0}^{\\pi/2} \\frac{\\sin^4 x + \\cos^4 x}{\\sin^4 x + \\cos^4 x} dx = \\int_0^{\\pi/2} 1 \\, dx = \\frac{\\pi}{2} \\implies I = \\frac{\\pi}{4}$.\\n\\n **Marks Tip**: For any $\\int_a^b \\frac{f(x)}{f(x) + f(a+b-x)} dx$, the answer is unconditionally $\\frac{b - a}{2}$."
    },
    {
        "chapter": "Straight Lines & Pair of Straight Lines",
        "topic": "Distance Formulas & Parallel Lines",
        "level": "Basic",
        "type": "mcq_single",
        "question": "[Marks Basic / JEE Main] The perpendicular distance between the parallel lines $3x + 4y - 9 = 0$ and $6x + 8y + 12 = 0$ is:",
        "options": [
            "$3\\text{ units}$",
            "$2.1\\text{ units}$",
            "$1.5\\text{ units}$",
            "$4.2\\text{ units}$"
        ],
        "correct_answer": "3 units",
        "correct_index": 0,
        "explanation": "First normalize coefficients so $a$ and $b$ are identical:\\nSecond equation: divide by $2 \\implies 3x + 4y + 6 = 0$.\\nFirst equation: $3x + 4y - 9 = 0$.\\nHere $a = 3, b = 4, c_1 = -9, c_2 = +6$.\\nDistance $d = \\frac{|c_1 - c_2|}{\\sqrt{a^2 + b^2}} = \\frac{|-9 - 6|}{\\sqrt{3^2 + 4^2}} = \\frac{|-15|}{5} = 3\\text{ units}$.\\n\\n **Marks Tip**: ALWAYS equalize coefficients $(a, b)$ before applying $\\frac{|c_1 - c_2|}{\\sqrt{a^2 + b^2}}$."
    },
    {
        "chapter": "Circles",
        "topic": "Standard & General Equation of Circle",
        "level": "Basic",
        "type": "mcq_single",
        "question": "[Marks Basic / JEE Main] The radius of the circle given by the equation $2x^2 + 2y^2 - 8x + 12y - 10 = 0$ is:",
        "options": [
            "$\\sqrt{18} = 3\\sqrt{2}$",
            "$\\sqrt{26}$",
            "$5$",
            "$4$"
        ],
        "correct_answer": "3 sqrt(2)",
        "correct_index": 0,
        "explanation": "Divide by coefficient of $x^2$ ($2$) to reach standard form:\\n$x^2 + y^2 - 4x + 6y - 5 = 0$.\\nComparing with $x^2 + y^2 + 2gx + 2fy + c = 0$:\\n$2g = -4 \\implies g = -2$\\n$2f = 6 \\implies f = 3$\\n$c = -5$.\\nRadius $R = \\sqrt{g^2 + f^2 - c} = \\sqrt{(-2)^2 + (3)^2 - (-5)} = \\sqrt{4 + 9 + 5} = \\sqrt{18} = 3\\sqrt{2}$.\\n\\n **Marks Tip**: The most frequent mistake is forgetting to divide the constant term $c$ by 2."
    },
    {
        "chapter": "Vector Algebra",
        "topic": "Dot & Cross Product of Vectors",
        "level": "Basic",
        "type": "mcq_single",
        "question": "[Marks Basic / JEE Main] If vectors $\\vec{a} = 2\\hat{i} + \\lambda \\hat{j} + \\hat{k}$ and $\\vec{b} = \\hat{i} - 2\\hat{j} + 3\\hat{k}$ are perpendicular to each other, the scalar value $\\lambda$ is:",
        "options": [
            "$5 / 2$",
            "$-5 / 2$",
            "$1$",
            "$3$"
        ],
        "correct_answer": "5 / 2",
        "correct_index": 0,
        "explanation": "Two non-zero vectors are perpendicular if and only if their scalar dot product is zero: $\\vec{a} \\cdot \\vec{b} = 0$.\\n$\\vec{a} \\cdot \\vec{b} = (2)(1) + (\\lambda)(-2) + (1)(3) = 2 - 2\\lambda + 3 = 5 - 2\\lambda = 0$.\\n$2\\lambda = 5 \\implies \\lambda = \\frac{5}{2}$.\\n\\n **Marks Tip**: Perpendicular condition $\\implies \\vec{a}\\cdot\\vec{b}=0$. Parallel condition $\\implies \\vec{a}\\times\\vec{b}=\\vec{0}$ or coordinates proportional."
    },
    {
        "chapter": "Mechanical Properties of Solids",
        "topic": "Stress-Strain Relationship & Hooke's Law",
        "level": "Basic",
        "type": "mcq_single",
        "question": "[Marks Basic / JEE Main] A copper wire of length $L$ and cross-sectional area $A$ is stretched by a force $F$, producing an elongation $\\Delta L$. The elastic potential energy stored per unit volume (energy density $u$) of the wire is:",
        "options": ["$\\frac{1}{2} \\times \\text{Stress} \\times \\text{Strain}$", "$\\text{Stress} \\times \\text{Strain}$", "$\\frac{1}{2} \\frac{\\text{Stress}}{\\text{Strain}}$", "$\\frac{1}{2} Y \\times (\\text{Stress})^2$"],
        "correct_answer": "1/2 * Stress * Strain",
        "correct_index": 0,
        "explanation": "Work done in stretching a wire of initial length $L$ by $\\Delta L$ is $W = \\frac{1}{2} F \\Delta L$.\\nVolume of the wire is $V = A L$.\\nEnergy density $u = \\frac{W}{V} = \\frac{1}{2} \\left(\\frac{F}{A}\\right) \\left(\\frac{\\Delta L}{L}\\right) = \\frac{1}{2} \\times \\text{Stress} \\times \\text{Strain} = \\frac{1}{2} Y (\\text{Strain})^2 = \\frac{(\\text{Stress})^2}{2Y}$.\\n\\n**Marks Tip**: The factor of $1/2$ comes from the average restoring force $F_{avg} = (0 + F)/2$.",
    },
    {
        "chapter": "Waves & Sound",
        "topic": "Speed of Sound & Laplace Correction",
        "level": "Basic",
        "type": "mcq_single",
        "question": "[Marks Basic / JEE Main] The ratio of the speed of sound in nitrogen gas ($\\text{N}_2$) to that in helium gas ($\\text{He}$) at the same absolute temperature $T$ is:",
        "options": ["$\\frac{\\sqrt{3}}{5}$", "$\\frac{\\sqrt{5}}{3}$", "$\\frac{3}{5}$", "$\\frac{5}{3}$"],
        "correct_answer": "sqrt(3) / 5",
        "correct_index": 0,
        "explanation": "Speed of sound in an ideal gas is $v = \\sqrt{\\frac{\\gamma R T}{M}}$.\\nFor $\\text{N}_2$ (diatomic): $\\gamma_1 = 7/5$, $M_1 = 28\\text{ g/mol}$.\\nFor $\\text{He}$ (monoatomic): $\\gamma_2 = 5/3$, $M_2 = 4\\text{ g/mol}$.\\n$\\frac{v_{N_2}}{v_{He}} = \\sqrt{\\frac{\\gamma_1 / M_1}{\\gamma_2 / M_2}} = \\sqrt{\\frac{(7/5) / 28}{(5/3) / 4}} = \\sqrt{\\frac{7 / 140}{5 / 12}} = \\sqrt{\\frac{1 / 20}{5 / 12}} = \\sqrt{\\frac{12}{100}} = \\frac{\\sqrt{12}}{10} = \\frac{2\\sqrt{3}}{10} = \\frac{\\sqrt{3}}{5}$.\\n\\n**Marks Tip**: Don't forget that both $\\gamma$ and molar mass $M$ vary between monoatomic and diatomic gases.",
    },
    {
        "chapter": "Alternating Current (AC)",
        "topic": "AC Through LCR Circuit & Resonance",
        "level": "Basic",
        "type": "mcq_single",
        "question": "[Marks Basic / JEE Main] In a series $LCR$ circuit connected to an AC source of voltage $V$ and frequency $\\omega$, the inductive reactance is $X_L = 30\\,\\Omega$, capacitive reactance is $X_C = 70\\,\\Omega$, and resistance is $R = 30\\,\\Omega$. The power factor ($\\cos\\phi$) of the circuit is:",
        "options": ["$0.60$", "$0.75$", "$0.80$", "$0.50$"],
        "correct_answer": "0.60",
        "correct_index": 0,
        "explanation": "Net reactance $X = |X_L - X_C| = |30 - 70| = 40\\,\\Omega$ (capacitive).\\nImpedance $Z = \\sqrt{R^2 + X^2} = \\sqrt{30^2 + 40^2} = \\sqrt{900 + 1600} = \\sqrt{2500} = 50\\,\\Omega$.\\nPower factor $\\cos\\phi = \\frac{R}{Z} = \\frac{30}{50} = 0.60$ (leading).\\n\\n**Marks Tip**: Power factor is always a dimensionless ratio in $[0, 1]$. At resonance, $X_L = X_C \\implies Z = R \\implies \\cos\\phi = 1$.",
    },
    {
        "chapter": "Ray Optics & Optical Instruments",
        "topic": "Refraction at Spherical Surfaces & Lenses",
        "level": "Basic",
        "type": "mcq_single",
        "question": "[Marks Basic / JEE Main] A thin biconvex lens of focal length $f$ made of glass ($\\mu_g = 1.5$) is immersed in water ($\\mu_w = 4/3$). Its new focal length $f_w$ in water is:",
        "options": ["$4f$", "$2f$", "$f / 4$", "$1.5f$"],
        "correct_answer": "4f",
        "correct_index": 0,
        "explanation": "Lens maker's formula in air: $\\frac{1}{f} = (\\mu_g - 1)\\left(\\frac{1}{R_1} - \\frac{1}{R_2}\\right) = (1.5 - 1) K = 0.5 K = \\frac{1}{2} K \\implies K = \\frac{2}{f}$.\\nIn water: $\\frac{1}{f_w} = \\left(\\frac{\\mu_g}{\\mu_w} - 1\\right) K = \\left(\\frac{1.5}{4/3} - 1\\right) K = \\left(\\frac{9}{8} - 1\\right) K = \\frac{1}{8} K$.\\nSubstituting $K = \\frac{2}{f} \\implies \\frac{1}{f_w} = \\frac{1}{8} \\left(\\frac{2}{f}\\right) = \\frac{1}{4f} \\implies f_w = 4f$.\\n\\n**Marks Tip**: Immersing a glass lens ($\\mu = 1.5$) into water ($\\mu = 1.33$) multiplies its focal length by exactly $4$.",
    },
    {
        "chapter": "Wave Optics",
        "topic": "Young's Double Slit Experiment (YDSE)",
        "level": "Basic",
        "type": "mcq_single",
        "question": "[Marks Basic / JEE Main] In a Young's double-slit experiment, the slit separation is $d = 0.5\\text{ mm}$ and the screen is at distance $D = 1\\text{ m}$. If light of wavelength $\\lambda = 500\\text{ nm}$ is used, the fringe width $\\beta$ on the screen is:",
        "options": ["$1.0\\text{ mm}$", "$0.5\\text{ mm}$", "$2.0\\text{ mm}$", "$0.25\\text{ mm}$"],
        "correct_answer": "1.0 mm",
        "correct_index": 0,
        "explanation": "Fringe width formula: $\\beta = \\frac{\\lambda D}{d}$.\\nConvert everything to meters: $\\lambda = 500 \\times 10^{-9}\\text{ m}$, $D = 1\\text{ m}$, $d = 0.5 \\times 10^{-3}\\text{ m}$.\\n$\\beta = \\frac{500 \\times 10^{-9} \\times 1}{0.5 \\times 10^{-3}} = 1000 \\times 10^{-6}\\text{ m} = 10^{-3}\\text{ m} = 1.0\\text{ mm}$.\\n\\n**Marks Tip**: If the apparatus is immersed in a liquid of refractive index $\\mu$, fringe width becomes $\\beta' = \\beta / \\mu$.",
    },
    {
        "chapter": "Nuclei",
        "topic": "Radioactive Decay Law & Half Life",
        "level": "Basic",
        "type": "mcq_single",
        "question": "[Marks Basic / JEE Main] A radioactive isotope has a half-life of $T_{1/2} = 5\\text{ years}$. After a time period of $15\\text{ years}$, the percentage of original radioactive nuclei that remain undecayed is:",
        "options": ["$12.5\\%$", "$25\\%$", "$6.25\\%$", "$87.5\\%$"],
        "correct_answer": "12.5%",
        "correct_index": 0,
        "explanation": "Number of half-lives elapsed $n = \\frac{t}{T_{1/2}} = \\frac{15}{5} = 3$.\\nFraction remaining undecayed $\\frac{N}{N_0} = \\left(\\frac{1}{2}\\right)^n = \\left(\\frac{1}{2}\\right)^3 = \\frac{1}{8} = 0.125 = 12.5\\%$.\\n(Note that $87.5\\%$ has decayed).\\n\\n**Marks Tip**: Read carefully whether the question asks for 'fraction remaining' ($12.5\\%$) or 'fraction decayed' ($87.5\\%$).",
    },
    {
        "chapter": "States of Matter: Gases & Liquids",
        "topic": "Ideal Gas Equation & Gas Laws",
        "level": "Basic",
        "type": "mcq_single",
        "question": "[Marks Basic / JEE Main] Under identical conditions of temperature and pressure, the rate of diffusion of gas $X$ is four times that of sulfur dioxide gas ($\\text{SO}_2$, molar mass $64\\text{ g/mol}$). The molar mass of gas $X$ is:",
        "options": ["$4\\text{ g/mol}$", "$16\\text{ g/mol}$", "$8\\text{ g/mol}$", "$2\\text{ g/mol}$"],
        "correct_answer": "4 g/mol",
        "correct_index": 0,
        "explanation": "According to Graham's Law of Diffusion: $\\frac{r_X}{r_{SO_2}} = \\sqrt{\\frac{M_{SO_2}}{M_X}}$.\\nGiven $\\frac{r_X}{r_{SO_2}} = 4 \\implies 4 = \\sqrt{\\frac{64}{M_X}} \\implies 16 = \\frac{64}{M_X} \\implies M_X = \\frac{64}{16} = 4\\text{ g/mol}$ (Helium).\\n\\n**Marks Tip**: Rate of diffusion is inversely proportional to the square root of molar mass ($r \\propto 1/\\sqrt{M}$).",
    },
    {
        "chapter": "Ionic Equilibrium",
        "topic": "Solubility Product (Ksp) & Common Ion Effect",
        "level": "Basic",
        "type": "mcq_single",
        "question": "[Marks Basic / JEE Main] The solubility product constant ($K_{sp}$) of a sparingly soluble salt $AB_2$ at $25^\\circ\\text{C}$ is $3.2 \\times 10^{-11}$. Its molar solubility $S$ in pure water is:",
        "options": ["$2.0 \\times 10^{-4}\\text{ M}$", "$4.0 \\times 10^{-4}\\text{ M}$", "$1.0 \\times 10^{-4}\\text{ M}$", "$1.8 \\times 10^{-5}\\text{ M}$"],
        "correct_answer": "2.0 x 10^-4 M",
        "correct_index": 0,
        "explanation": "Dissociation: $AB_2(s) \\rightleftharpoons A^{2+}(aq) + 2B^-(aq)$.\\nAt equilibrium: $[A^{2+}] = S$ and $[B^-] = 2S$.\\n$K_{sp} = [A^{2+}][B^-]^2 = S(2S)^2 = 4S^3$.\\n$4S^3 = 3.2 \\times 10^{-11} \\implies S^3 = 0.8 \\times 10^{-11} = 8.0 \\times 10^{-12}$.\\n$S = \\sqrt[3]{8.0 \\times 10^{-12}} = 2.0 \\times 10^{-4}\\text{ M}$.\\n\\n**Marks Tip**: For $A_x B_y$ salt: $K_{sp} = x^x y^y S^{x+y}$. For $AB_2$: $1^1 2^2 S^{1+2} = 4S^3$.",
    },
    {
        "chapter": "Redox Reactions",
        "topic": "Balancing Redox Reactions & Equivalent Weight",
        "level": "Basic",
        "type": "mcq_single",
        "question": "[Marks Basic / JEE Main] In acidic medium, potassium permanganate ($\\text{KMnO}_4$) acts as a strong oxidizing agent and reduces to $\\text{Mn}^{2+}$. The equivalent weight of $\\text{KMnO}_4$ in acidic medium is (where $M$ is molar mass):",
        "options": ["$M / 5$", "$M / 3$", "$M / 1$", "$M / 6$"],
        "correct_answer": "M / 5",
        "correct_index": 0,
        "explanation": "In acidic medium: $\\text{MnO}_4^- + 8\\text{H}^+ + 5e^- \\to \\text{Mn}^{2+} + 4\\text{H}_2\\text{O}$.\\nChange in oxidation number of manganese: from $+7$ to $+2$, so $n\\text{-factor} = |7 - 2| = 5$.\\nEquivalent weight = $\\frac{\\text{Molar mass}}{n\\text{-factor}} = \\frac{M}{5}$.\\n\\n**Marks Tip**: Remember $n$-factor of $\\text{KMnO}_4$: 5 in acidic medium, 3 in neutral/faintly alkaline medium, 1 in strongly basic medium.",
    },
    {
        "chapter": "Hydrocarbons",
        "topic": "Alkenes: Addition Reactions (Markovnikov)",
        "level": "Basic",
        "type": "mcq_single",
        "question": "[Marks Basic / JEE Main] Addition of hydrogen bromide ($\\text{HBr}$) to propene ($\\text{CH}_3-\\text{CH}=\\text{CH}_2$) in the presence of benzoyl peroxide yields primarily:",
        "options": ["1-Bromopropane ($\\text{CH}_3\\text{CH}_2\\text{CH}_2\\text{Br}$)", "2-Bromopropane ($\\text{CH}_3\\text{CH(Br)}\\text{CH}_3$)", "1,2-Dibromopropane", "2-Bromo-2-methylpropane"],
        "correct_answer": "1-Bromopropane (CH3CH2CH2Br)",
        "correct_index": 0,
        "explanation": "In the presence of peroxide, addition of $\\text{HBr}$ to unsymmetrical alkenes follows the Kharasch effect (Anti-Markovnikov addition) via a free-radical mechanism.\\n$\\text{Br}^\\bullet$ attacks the terminal carbon to form the more stable $2^\\circ$ free radical $\\text{CH}_3-\\dot{\\text{C}}\\text{H}-\\text{CH}_2\\text{Br}$, which abstracts $\\text{H}^\\bullet$ to yield 1-bromopropane.\\n\\n**Marks Tip**: The peroxide effect operates ONLY with $\\text{HBr}$, never with $\\text{HCl}$ or $\\text{HI}$ due to endothermic elementary steps.",
    },
    {
        "chapter": "Haloalkanes and Haloarenes",
        "topic": "SN1 and SN2 Reaction Mechanisms",
        "level": "Basic",
        "type": "mcq_single",
        "question": "[Marks Basic / JEE Main] Which of the following alkyl halides undergoes nucleophilic substitution by the $S_N2$ mechanism at the FASTEST rate?",
        "options": ["$\\text{CH}_3-\\text{I}$", "$\\text{CH}_3-\\text{Cl}$", "$(\\text{CH}_3)_2\\text{CH}-\\text{I}$", "$(\\text{CH}_3)_3\\text{C}-\\text{I}$"],
        "correct_answer": "CH3-I",
        "correct_index": 0,
        "explanation": "$S_N2$ reactions proceed via a single-step backside attack: steric hindrance is the dominant factor! Reactivity order: $\\text{Methyl} > 1^\\circ > 2^\\circ \\gg 3^\\circ$.\\nAmong leaving groups: $\\text{I}^- > \\text{Br}^- > \\text{Cl}^- > \\text{F}^-$.\\nTherefore, methyl iodide ($\\text{CH}_3\\text{I}$) has both minimum steric crowding and the best leaving group ($\\text{I}^-$), reacting fastest.\\n\\n**Marks Tip**: $S_N2$ favours methyl/primary halides in polar aprotic solvents (like acetone, DMSO).",
    },
    {
        "chapter": "Alcohols, Phenols and Ethers",
        "topic": "Phenol Acidity & Electrophilic Substitution",
        "level": "Basic",
        "type": "mcq_single",
        "question": "[Marks Basic / JEE Main] The correct decreasing order of acidity for the following substituted phenols is:\\n(I) 4-Nitrophenol, (II) 4-Methylphenol, (III) Phenol, (IV) 4-Methoxyphenol",
        "options": ["$\\text{I} > \\text{III} > \\text{II} > \\text{IV}$", "$\\text{I} > \\text{II} > \\text{III} > \\text{IV}$", "$\\text{IV} > \\text{II} > \\text{III} > \\text{I}$", "$\\text{III} > \\text{I} > \\text{II} > \\text{IV}$"],
        "correct_answer": "I > III > II > IV",
        "correct_index": 0,
        "explanation": "Acidity of phenols increases with electron-withdrawing groups (EWGs) that stabilize the phenoxide anion via resonance/inductive effect, and decreases with electron-donating groups (EDGs):\\n- 4-Nitrophenol ($\\text{I}$): $-\\text{NO}_2$ has powerful $-M$ and $-I$ effects $\\implies$ most acidic ($pK_a \\approx 7.15$).\\n- Phenol ($\\text{III}$): unsubstituted benchmark ($pK_a \\approx 10.0$).\\n- 4-Methylphenol ($\\text{II}$): $-\\text{CH}_3$ has $+I$ and hyperconjugative donation $\\implies$ less acidic ($pK_a \\approx 10.26$).\\n- 4-Methoxyphenol ($\\text{IV}$): $-\\text{OCH}_3$ has strong $+M$ resonance donation $\\implies$ least acidic ($pK_a \\approx 10.20$).\\nOrder: $\\text{I} > \\text{III} > \\text{II} > \\text{IV}$.\\n\\n**Marks Tip**: $-\\text{NO}_2$ at ortho/para stabilizes phenoxide dramatically.",
    },
    {
        "chapter": "Aldehydes, Ketones and Carboxylic Acids",
        "topic": "Aldol Condensation & Cannizzaro Reaction",
        "level": "Basic",
        "type": "mcq_single",
        "question": "[Marks Basic / JEE Main] Which of the following carbonyl compounds undergoes disproportionation (Cannizzaro reaction) when heated with concentrated $50\\%$ aqueous $\\text{KOH}$?",
        "options": ["$\\text{HCHO}$ (Formaldehyde)", "$\\text{CH}_3\\text{CHO}$ (Acetaldehyde)", "$\\text{CH}_3\\text{COCH}_3$ (Acetone)", "$\\text{CH}_3\\text{CH}_2\\text{CHO}$ (Propanal)"],
        "correct_answer": "HCHO (Formaldehyde)",
        "correct_index": 0,
        "explanation": "Cannizzaro reaction is characteristic of aldehydes having NO $\\alpha$-hydrogen atoms.\\nFormaldehyde ($\\text{HCHO}$) and benzaldehyde ($\\text{PhCHO}$) lack $\\alpha$-hydrogens, so they undergo self-oxidation-reduction:\\n$2\\text{HCHO} + \\text{KOH} \\xrightarrow{\\Delta} \\text{CH}_3\\text{OH} + \\text{HCOOK}$.\\nAcetaldehyde, acetone, and propanal have enolizable $\\alpha$-hydrogens and undergo Aldol condensation instead.\\n\\n**Marks Tip**: Aldehydes with $\\alpha$-H $\\to$ Aldol; Aldehydes without $\\alpha$-H $\\to$ Cannizzaro.",
    },
    {
        "chapter": "Amines & Nitrogen Containing Compounds",
        "topic": "Basicity of Amines & Hinsberg Test",
        "level": "Basic",
        "type": "mcq_single",
        "question": "[Marks Basic / JEE Main] An organic compound $C_3H_9N$ reacts with benzenesulfonyl chloride (Hinsberg's reagent) to form a precipitate that is completely SOLUBLE in aqueous $\\text{KOH}$. The amine is:",
        "options": ["Propan-1-amine ($1^\\circ$ amine)", "$N$-Methylethanamine ($2^\\circ$ amine)", "$N,N$-Dimethylmethanamine ($3^\\circ$ amine)", "None of these"],
        "correct_answer": "Propan-1-amine (1 degree amine)",
        "correct_index": 0,
        "explanation": "In the Hinsberg test:\\n- $1^\\circ$ amine reacts with $\\text{PhSO}_2\\text{Cl}$ to form $N$-alkylbenzenesulfonamide, which has an acidic hydrogen attached to nitrogen and dissolves in $\\text{KOH}$ forming a clear salt solution.\\n- $2^\\circ$ amine forms an insoluble sulfonamide with no acidic hydrogen on nitrogen (remains insoluble in $\\text{KOH}$).\\n- $3^\\circ$ amine does not react with Hinsberg's reagent.\\nThus, the compound must be a $1^\\circ$ amine (Propan-1-amine).\\n\\n**Marks Tip**: Soluble in $\\text{KOH} \\implies 1^\\circ$ amine; Insoluble in $\\text{KOH} \\implies 2^\\circ$ amine; No reaction $\\implies 3^\\circ$ amine.",
    },
    {
        "chapter": "Permutations and Combinations",
        "topic": "Permutations & Combinations Fundamental Principles",
        "level": "Basic",
        "type": "mcq_single",
        "question": "[Marks Basic / JEE Main] The number of all possible four-digit numbers formed using the digits $1, 2, 3, 4, 5, 6$ without repetition that are divisible by $4$ is:",
        "options": ["$72$", "$96$", "$60$", "$120$"],
        "correct_answer": "72",
        "correct_index": 0,
        "explanation": "A number is divisible by $4$ if its last two digits form a number divisible by $4$.\\nAvailable digits: $\\{1, 2, 3, 4, 5, 6\\}$.\\nPossible two-digit multiples of $4$ using distinct digits from this set:\\n$12, 16, 24, 32, 36, 52, 56, 64$ (total $8$ valid pairs for the last two positions).\\nFor each pair, $2$ digits are used, leaving $4$ digits.\\nThe first two positions (thousands and hundreds) can be chosen in ${}^4P_2 = 4 \\times 3 = 12$ ways.\\nTotal numbers = $8 \\times 12 = 72$.\\n\\n**Marks Tip**: Always identify and count the valid last two digits first when dealing with divisibility by 4.",
    },
    {
        "chapter": "Conic Sections: Parabola",
        "topic": "Standard Equations & Properties of Parabola",
        "level": "Basic",
        "type": "mcq_single",
        "question": "[Marks Basic / JEE Main] The focal distance of a point $P(x_1, y_1)$ lying on the parabola $y^2 = 12x$ is $10\\text{ units}$. The $x$-coordinate ($x_1$) of point $P$ is:",
        "options": ["$7$", "$10$", "$4$", "$3$"],
        "correct_answer": "7",
        "correct_index": 0,
        "explanation": "For parabola $y^2 = 4ax$, $4a = 12 \\implies a = 3$.\\nBy definition of parabola, focal distance of any point $P(x_1, y_1)$ on $y^2 = 4ax$ is $SP = x_1 + a$.\\nGiven focal distance $= 10 \\implies x_1 + 3 = 10 \\implies x_1 = 7$.\\n\\n**Marks Tip**: Focal distance for $y^2 = 4ax$ is always simply $x_1 + a$.",
    },
    {
        "chapter": "Conic Sections: Ellipse",
        "topic": "Standard Equation & Eccentricity of Ellipse",
        "level": "Basic",
        "type": "mcq_single",
        "question": "[Marks Basic / JEE Main] The eccentricity of an ellipse whose latus rectum is equal to half of its major axis is:",
        "options": ["$1 / \\sqrt{2}$", "$1 / 2$", "$\\sqrt{3} / 2$", "$1 / 4$"],
        "correct_answer": "1 / sqrt(2)",
        "correct_index": 0,
        "explanation": "Length of latus rectum $= \\frac{2b^2}{a}$. Major axis $= 2a$.\\nGiven: $\\frac{2b^2}{a} = \\frac{1}{2}(2a) = a \\implies 2b^2 = a^2 \\implies \\frac{b^2}{a^2} = \\frac{1}{2}$.\\nEccentricity $e = \\sqrt{1 - \\frac{b^2}{a^2}} = \\sqrt{1 - \\frac{1}{2}} = \\sqrt{\\frac{1}{2}} = \\frac{1}{\\sqrt{2}}$.\\n\\n**Marks Tip**: For an ellipse, $b^2 = a^2(1 - e^2)$. Always relate latus rectum directly to $e$ via $LR = 2a(1 - e^2)$.",
    },
    {
        "chapter": "Continuity and Differentiability",
        "topic": "Differentiability & Non-Differentiable Points",
        "level": "Basic",
        "type": "mcq_single",
        "question": "[Marks Basic / JEE Main] The function $f(x) = |x - 1| + |x - 3|$ is NOT differentiable at:",
        "options": ["Exactly two points: $x = 1$ and $x = 3$", "Only one point: $x = 1$", "All real values of $x$", "Three points: $x = 1, 2, 3$"],
        "correct_answer": "Exactly two points: x = 1 and x = 3",
        "correct_index": 0,
        "explanation": "The modulus function $|u|$ is continuous everywhere but fails to be differentiable at its vertex where the inside expression becomes zero ($u = 0$), due to sharp corner (cusp).\\nHere vertices are $x = 1$ and $x = 3$.\\nCalculating left-hand and right-hand derivatives at $x = 1$:\\nFor $x < 1$: $f(x) = (1 - x) + (3 - x) = 4 - 2x \\implies f'(1^-) = -2$.\\nFor $1 < x < 3$: $f(x) = (x - 1) + (3 - x) = 2 \\implies f'(1^+) = 0$.\\nSince $LHD \\ne RHD$, non-differentiable at $x = 1$. Similarly at $x = 3$.\\n\\n**Marks Tip**: A sum of absolute linear terms $\\sum |x - a_i|$ is always continuous on $\\mathbb{R}$, but non-differentiable at each $x = a_i$.",
    },
    {
        "chapter": "Differential Equations",
        "topic": "Linear Differential Equations & Integrating Factor",
        "level": "Basic",
        "type": "mcq_single",
        "question": "[Marks Basic / JEE Main] The integrating factor (I.F.) for the linear differential equation $\\frac{dy}{dx} + \\left(\\frac{2x}{1 + x^2}\\right) y = x^2$ is:",
        "options": ["$1 + x^2$", "$\\ln(1 + x^2)$", "$\\sqrt{1 + x^2}$", "$(1 + x^2)^2$"],
        "correct_answer": "1 + x^2",
        "correct_index": 0,
        "explanation": "The differential equation is in standard first-order linear form $\\frac{dy}{dx} + P(x) y = Q(x)$, where $P(x) = \\frac{2x}{1 + x^2}$.\\nIntegrating factor $IF = e^{\\int P(x) dx}$.\\n$\\int \\frac{2x}{1 + x^2} dx = \\ln(1 + x^2)$.\\n$IF = e^{\\ln(1 + x^2)} = 1 + x^2$.\\n\\n**Marks Tip**: Standard formula simplification: $e^{\\ln(u)} = u$ and $e^{k \\ln u} = u^k$.",
    },
    {
        "chapter": "Three Dimensional Geometry (Lines & Planes)",
        "topic": "Direction Cosines & Direction Ratios",
        "level": "Basic",
        "type": "mcq_single",
        "question": "[Marks Basic / JEE Main] If a straight line makes equal angles $\\alpha$ with the positive directions of all three coordinate axes $x, y, z$, then the value of $\\cos(2\\alpha)$ is:",
        "options": ["$-1 / 3$", "$1 / 3$", "$2 / 3$", "$-2 / 3$"],
        "correct_answer": "-1 / 3",
        "correct_index": 0,
        "explanation": "Let direction cosines be $l = \\cos\\alpha, m = \\cos\\alpha, n = \\cos\\alpha$.\\nBy fundamental 3D identity: $l^2 + m^2 + n^2 = 1$.\\n$\\cos^2\\alpha + \\cos^2\\alpha + \\cos^2\\alpha = 1 \\implies 3\\cos^2\\alpha = 1 \\implies \\cos^2\\alpha = \\frac{1}{3}$.\\nUsing double-angle identity: $\\cos(2\\alpha) = 2\\cos^2\\alpha - 1 = 2\\left(\\frac{1}{3}\\right) - 1 = \\frac{2}{3} - 1 = -\\frac{1}{3}$.\\n\\n**Marks Tip**: Direction cosines always satisfy $\\cos^2\\alpha + \\cos^2\\beta + \\cos^2\\gamma = 1$, whereas direction sines satisfy $\\sin^2\\alpha + \\sin^2\\beta + \\sin^2\\gamma = 2$.",
    },
    {
        "chapter": "Probability (Foundations)",
        "topic": "Conditional Probability & Multiplication Rule",
        "level": "Basic",
        "type": "mcq_single",
        "question": "[Marks Basic / JEE Main] If two events $A$ and $B$ are such that $P(A) = 0.4$, $P(B) = 0.8$, and $P(B|A) = 0.6$, then $P(A \\cup B)$ is:",
        "options": ["$0.96$", "$0.84$", "$0.72$", "$0.90$"],
        "correct_answer": "0.96",
        "correct_index": 0,
        "explanation": "From conditional probability: $P(B|A) = \\frac{P(A \\cap B)}{P(A)} \\implies P(A \\cap B) = P(B|A) \\times P(A) = 0.6 \\times 0.4 = 0.24$.\\nBy addition theorem: $P(A \\cup B) = P(A) + P(B) - P(A \\cap B) = 0.4 + 0.8 - 0.24 = 1.20 - 0.24 = 0.96$.\\n\\n**Marks Tip**: Remember $P(A \\cap B) = P(B|A) \\cdot P(A) = P(A|B) \\cdot P(B)$.",
    },
    {
        "chapter": "Statistics",
        "topic": "Variance and Standard Deviation",
        "level": "Basic",
        "type": "mcq_single",
        "question": "[Marks Basic / JEE Main] The variance of $10$ observations is found to be $4$. If each observation is multiplied by $3$, the new variance of the resulting observations is:",
        "options": ["$36$", "$12$", "$4$", "$16$"],
        "correct_answer": "36",
        "correct_index": 0,
        "explanation": "If each observation $x_i$ is transformed by $y_i = a x_i + b$:\\n1. Adding a constant $b$ does NOT affect variance or standard deviation.\\n2. Multiplying by a constant $a$ multiplies standard deviation by $|a|$, and multiplies variance by $a^2$: $\\text{Var}(y) = a^2 \\text{Var}(x)$.\\nHere $a = 3$, so $\\text{Var}_{new} = 3^2 \\times 4 = 9 \\times 4 = 36$.\\n\\n**Marks Tip**: Standard deviation multiplies by $a$, variance multiplies by $a^2$.",
    },
]
