"""
add_all_marks_questions.py - Generates comprehensive Marks Basic / Foundation Questions
for all 34 missing chapters and second questions for high-yield chapters.
Appends them to marks_basic_questions.py and updates the SQLite database.
"""

import os
import sys
import json
import sqlite3

# Ensure UTF-8 console output
if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

NEW_MARKS_QUESTIONS = [
    # =========================================================================
    # PHYSICS (5 MISSING CHAPTERS + EXTRA HIGH YIELD)
    # =========================================================================
    {
        "chapter": "Thermal Properties of Matter & Calorimetry",
        "topic": "Thermal Expansion & Calorimetry Principle",
        "level": "Basic",
        "type": "mcq_single",
        "question": "[Marks Basic / JEE Main] A copper rod of length $L_0 = 1.0\\text{ m}$ is heated from $20^\\circ\\text{C}$ to $120^\\circ\\text{C}$. If the coefficient of linear expansion of copper is $\\alpha = 1.7 \\times 10^{-5}\\text{ K}^{-1}$, the fractional increase in the length ($\\Delta L / L_0$) of the rod is:",
        "options": [
            "$1.7 \\times 10^{-3}$",
            "$3.4 \\times 10^{-3}$",
            "$1.7 \\times 10^{-4}$",
            "$5.1 \\times 10^{-3}$"
        ],
        "correct_answer": "1.7 * 10^-3",
        "correct_index": 0,
        "explanation": "Linear thermal expansion is given by $\\Delta L = L_0 \\alpha \\Delta T$.\\nHere, $\\Delta T = 120 - 20 = 100^\\circ\\text{C} = 100\\text{ K}$.\\nFractional change $\\frac{\\Delta L}{L_0} = \\alpha \\Delta T = (1.7 \\times 10^{-5}\\text{ K}^{-1})(100\\text{ K}) = 1.7 \\times 10^{-3}$.\\n\\n **Marks Tip**: Remember volumetric coefficient $\\gamma = 3\\alpha$ and superficial coefficient $\\beta = 2\\alpha$ for isotropic solids."
    },
    {
        "chapter": "Thermal Properties of Matter & Calorimetry",
        "topic": "Stefan-Boltzmann Law & Newton's Law of Cooling",
        "level": "Basic",
        "type": "mcq_single",
        "question": "[Marks Basic / JEE Main] A spherical black body of radius $R_1 = 12\\text{ cm}$ radiates $450\\text{ W}$ of power at temperature $500\\text{ K}$. If the radius were halved and the absolute temperature doubled, the radiated power would become:",
        "options": [
            "$1800\\text{ W}$",
            "$900\\text{ W}$",
            "$3600\\text{ W}$",
            "$450\\text{ W}$"
        ],
        "correct_answer": "1800 W",
        "correct_index": 0,
        "explanation": "By Stefan-Boltzmann law, radiant power $P = e \\sigma A T^4 = e \\sigma (4\\pi R^2) T^4 \\implies P \\propto R^2 T^4$.\\nNew power $P' = P \\cdot \\left(\\frac{R'}{R}\\right)^2 \\cdot \\left(\\frac{T'}{T}\\right)^4 = 450 \\cdot \\left(\\frac{1}{2}\\right)^2 \\cdot (2)^4 = 450 \\cdot \\frac{1}{4} \\cdot 16 = 450 \\times 4 = 1800\\text{ W}$.\\n\\n **Marks Tip**: Radiative power scales as fourth power of absolute temperature ($T^4$ in Kelvin), but only as square of linear dimensions ($R^2$)."
    },
    {
        "chapter": "Kinetic Theory of Gases (KTG)",
        "topic": "RMS Speed, Mean Free Path & Degrees of Freedom",
        "level": "Basic",
        "type": "mcq_single",
        "question": "[Marks Basic / JEE Main] The temperature at which the root mean square (rms) speed of nitrogen gas ($\\text{N}_2$) molecules equals the rms speed of oxygen ($\\text{O}_2$) molecules at $320\\text{ K}$ is (Molar masses: $M_{\\text{N}_2} = 28\\text{ g/mol}$, $M_{\\text{O}_2} = 32\\text{ g/mol}$):",
        "options": [
            "$280\\text{ K}$",
            "$300\\text{ K}$",
            "$260\\text{ K}$",
            "$365\\text{ K}$"
        ],
        "correct_answer": "280 K",
        "correct_index": 0,
        "explanation": "RMS velocity $v_{\\text{rms}} = \\sqrt{\\frac{3RT}{M}}$.\\nEquating $v_{\\text{rms}}(\\text{N}_2) = v_{\\text{rms}}(\\text{O}_2) \\implies \\frac{T_{\\text{N}_2}}{M_{\\text{N}_2}} = \\frac{T_{\\text{O}_2}}{M_{\\text{O}_2}}$.\\n$T_{\\text{N}_2} = T_{\\text{O}_2} \\cdot \\frac{M_{\\text{N}_2}}{M_{\\text{O}_2}} = 320 \\times \\frac{28}{32} = 10 \\times 28 = 280\\text{ K}$.\\n\\n **Marks Tip**: RMS speed is directly proportional to $\\sqrt{T/M}$. Always verify units of molar mass cancel out."
    },
    {
        "chapter": "Kinetic Theory of Gases (KTG)",
        "topic": "Equipartition of Energy & Specific Heats of Gases",
        "level": "Basic",
        "type": "mcq_single",
        "question": "[Marks Basic / JEE Main] For an ideal rigid diatomic gas, the molar heat capacity at constant volume $C_v$ and the adiabatic index $\\gamma = C_p / C_v$ are respectively:",
        "options": [
            "$C_v = \\frac{5}{2}R,\\; \\gamma = \\frac{7}{5}$",
            "$C_v = \\frac{3}{2}R,\\; \\gamma = \\frac{5}{3}$",
            "$C_v = 3R,\\; \\gamma = \\frac{4}{3}$",
            "$C_v = \\frac{7}{2}R,\\; \\gamma = \\frac{9}{7}$"
        ],
        "correct_answer": "Cv = 5/2 R, gamma = 7/5",
        "correct_index": 0,
        "explanation": "A rigid diatomic molecule (e.g., $\\text{O}_2, \\text{N}_2$) has 3 translational + 2 rotational = 5 degrees of freedom ($f = 5$).\\nInternal energy per mole $U = \\frac{f}{2}RT = \\frac{5}{2}RT$.\\n$C_v = \\frac{dU}{dT} = \\frac{5}{2}R$.\\nBy Mayer's relation, $C_p = C_v + R = \\frac{7}{2}R$.\\nHence, $\\gamma = \\frac{C_p}{C_v} = \\frac{7/2}{5/2} = \\frac{7}{5} = 1.40$.\\n\\n **Marks Tip**: If vibrational modes are active (at high temperature), add 2 vibrational degrees of freedom ($f = 7$)."
    },
    {
        "chapter": "Magnetism & Matter",
        "topic": "Magnetic Dipole Moment & Earth's Magnetism",
        "level": "Basic",
        "type": "mcq_single",
        "question": "[Marks Basic / JEE Main] A magnetic needle of magnetic dipole moment $M = 0.5\\text{ A}\\cdot\\text{m}^2$ is placed in a uniform magnetic field $B = 0.4\\text{ T}$. The work done in rotating the needle from its stable equilibrium position ($\\theta = 0^\\circ$) through $180^\\circ$ is:",
        "options": [
            "$0.4\\text{ J}$",
            "$0.2\\text{ J}$",
            "$0.8\\text{ J}$",
            "$0\\text{ J}$"
        ],
        "correct_answer": "0.4 J",
        "correct_index": 0,
        "explanation": "Potential energy of a magnetic dipole is $U(\\theta) = -M B \\cos\\theta$.\\nAt initial stable position: $U_i = -MB \\cos 0^\\circ = -MB$.\\nAt final inverted position: $U_f = -MB \\cos 180^\\circ = +MB$.\\nWork done $W = \\Delta U = U_f - U_i = MB - (-MB) = 2MB$.\\n$W = 2 \\times 0.5 \\times 0.4 = 0.4\\text{ J}$.\\n\\n **Marks Tip**: Rotating a dipole by $180^\\circ$ from parallel to anti-parallel always requires exactly $2MB$ of external work."
    },
    {
        "chapter": "Electromagnetic Waves",
        "topic": "EM Wave Characteristics & Poynting Vector",
        "level": "Basic",
        "type": "mcq_single",
        "question": "[Marks Basic / JEE Main] In a plane electromagnetic wave propagating in free space, the peak value of electric field is $E_0 = 600\\text{ V/m}$. The peak value of the associated magnetic field $B_0$ is ($c = 3 \\times 10^8\\text{ m/s}$):",
        "options": [
            "$2 \\times 10^{-6}\\text{ T}$",
            "$1.8 \\times 10^{11}\\text{ T}$",
            "$5 \\times 10^{-7}\\text{ T}$",
            "$2 \\times 10^{-5}\\text{ T}$"
        ],
        "correct_answer": "2 * 10^-6 T",
        "correct_index": 0,
        "explanation": "In an electromagnetic wave in vacuum, electric and magnetic field amplitudes are related by $c = \\frac{E_0}{B_0}$.\\n$B_0 = \\frac{E_0}{c} = \\frac{600}{3 \\times 10^8} = 2 \\times 10^{-6}\\text{ T} = 2\\;\\mu\\text{T}$.\\n\\n **Marks Tip**: Electric field and magnetic field oscillate strictly in phase and perpendicular to each other and the wave vector $\\vec{k} \\parallel \\vec{E} \\times \\vec{B}$."
    },
    {
        "chapter": "Experimental Skills & Error Analysis",
        "topic": "Vernier Callipers & Screw Gauge Least Count",
        "level": "Basic",
        "type": "mcq_single",
        "question": "[Marks Basic / JEE Main] A vernier calliper has $1\\text{ mm}$ main scale divisions (MSD). 20 vernier scale divisions (VSD) coincide with 19 main scale divisions. The least count (LC) of the instrument is:",
        "options": [
            "$0.05\\text{ mm}$",
            "$0.01\\text{ mm}$",
            "$0.1\\text{ mm}$",
            "$0.02\\text{ mm}$"
        ],
        "correct_answer": "0.05 mm",
        "correct_index": 0,
        "explanation": "Given $20\\text{ VSD} = 19\\text{ MSD} \\implies 1\\text{ VSD} = \\frac{19}{20}\\text{ MSD}$.\\nLeast Count $\\text{LC} = 1\\text{ MSD} - 1\\text{ VSD} = 1\\text{ MSD} - \\frac{19}{20}\\text{ MSD} = \\frac{1}{20}\\text{ MSD}$.\\nSince $1\\text{ MSD} = 1\\text{ mm}$, $\\text{LC} = \\frac{1}{20}\\text{ mm} = 0.05\\text{ mm}$.\\n\\n **Marks Tip**: Least count is always $1\\text{ MSD} \\times \\left(1 - \\frac{m}{n}\\right)$ where $n\\text{ VSD} = m\\text{ MSD}$."
    },

    # =========================================================================
    # CHEMISTRY (14 MISSING CHAPTERS + EXTRA HIGH YIELD)
    # =========================================================================
    {
        "chapter": "Hydrogen & its Compounds",
        "topic": "Hydrides, Heavy Water & Hydrogen Peroxide",
        "level": "Basic",
        "type": "mcq_single",
        "question": "[Marks Basic / JEE Main] The volume strength of a $1.5\\text{ M}$ solution of hydrogen peroxide ($\\text{H}_2\\text{O}_2$) is (Molar volume of gas at STP = $22.4\\text{ L}$):",
        "options": [
            "$16.8\\text{ volume}$",
            "$11.2\\text{ volume}$",
            "$5.6\\text{ volume}$",
            "$22.4\\text{ volume}$"
        ],
        "correct_answer": "16.8 volume",
        "correct_index": 0,
        "explanation": "Decomposition: $2\\text{H}_2\\text{O}_2 \\to 2\\text{H}_2\\text{O} + \\text{O}_2(\\text{g})$.\\n2 moles of $\\text{H}_2\\text{O}_2$ give $1\\text{ mole} = 22.4\\text{ L}$ of $\\text{O}_2$ at STP.\\nHence, $1\\text{ mole} = 1\\text{ M}$ solution gives $11.2\\text{ L}$ of $\\text{O}_2$.\\nVolume strength $= 11.2 \\times \\text{Molarity} = 11.2 \\times 1.5 = 16.8\\text{ volume}$.\\n\\n **Marks Tip**: Formula shortcuts: $\\text{Volume Strength} = 11.2 \\times M = 5.6 \\times N$."
    },
    {
        "chapter": "s-Block Elements (Alkali & Alkaline Earth Metals)",
        "topic": "Chemical Trends, Hydration Enthalpy & Anomalous Properties",
        "level": "Basic",
        "type": "mcq_single",
        "question": "[Marks Basic / JEE Main] Among the alkali metal ions, the highest ionic mobility in aqueous solution is exhibited by:",
        "options": [
            "$\\text{Cs}^+$",
            "$\\text{Li}^+$",
            "$\\text{Na}^+$",
            "$\\text{K}^+$"
        ],
        "correct_answer": "Cs^+",
        "correct_index": 0,
        "explanation": "Hydration enthalpy depends inversely on ionic size (charge density): $\\text{Li}^+ > \\text{Na}^+ > \\text{K}^+ > \\text{Rb}^+ > \\text{Cs}^+$.\\nBecause $\\text{Li}^+$ has the highest charge density, it has the thickest hydration shell, making its effective hydrated ionic radius the largest.\\nConsequently, $\\text{Li}^+(\\text{aq})$ moves slowest, while $\\text{Cs}^+(\\text{aq})$ has the smallest hydrated radius and highest aqueous ionic mobility.\\n\\n **Marks Tip**: Ionic radius: $\\text{Li}^+ < \\text{Cs}^+$, but Hydrated radius: $\\text{Li}^+(\\text{aq}) > \\text{Cs}^+(\\text{aq})$."
    },
    {
        "chapter": "p-Block Elements (Group 13 & 14)",
        "topic": "Inert Pair Effect & Group 13/14 Chemistry",
        "level": "Basic",
        "type": "mcq_single",
        "question": "[Marks Basic / JEE Main] In Group 13, the relative stability of $+1$ oxidation state compared to $+3$ oxidation state follows the order:",
        "options": [
            "$\\text{Tl}^+ > \\text{In}^+ > \\text{Ga}^+ > \\text{Al}^+$",
            "$\\text{Al}^+ > \\text{Ga}^+ > \\text{In}^+ > \\text{Tl}^+$",
            "$\\text{Ga}^+ > \\text{In}^+ > \\text{Tl}^+ > \\text{Al}^+$",
            "$\\text{In}^+ > \\text{Tl}^+ > \\text{Ga}^+ > \\text{Al}^+$"
        ],
        "correct_answer": "Tl^+ > In^+ > Ga^+ > Al^+",
        "correct_index": 0,
        "explanation": "Due to the inert pair effect—the reluctance of outer $ns^2$ electrons to participate in bonding due to poor shielding by inner $d$ and $f$ electrons—the stability of the lower oxidation state ($+1$) increases down the group.\\nThus, $\\text{Tl}^+$ is the most stable $+1$ species, while $\\text{Tl}^{3+}$ acts as a strong oxidizing agent.\\n\\n **Marks Tip**: Inert pair effect stabilizes oxidation state $(G - 2)$ down p-block groups: $\\text{Tl}(+1)$, $\\text{Pb}(+2)$, $\\text{Bi}(+3)$."
    },
    {
        "chapter": "Isomerism in Organic Compounds",
        "topic": "Geometrical, Optical & Tautomeric Isomerism",
        "level": "Basic",
        "type": "mcq_single",
        "question": "[Marks Basic / JEE Main] The total number of stereoisomers possible for tartaric acid ($\\text{HOOC}-\\text{CH(OH)}-\\text{CH(OH)}-\\text{COOH}$) is:",
        "options": [
            "$3$",
            "$4$",
            "$2$",
            "$5$"
        ],
        "correct_answer": "3",
        "correct_index": 0,
        "explanation": "Tartaric acid has $n = 2$ symmetric chiral carbons.\\nFor molecules with an even number of identical chiral centers:\\nTotal stereoisomers $= 2^{n-1} + 2^{(n/2)-1} = 2^1 + 2^0 = 2 + 1 = 3$.\\nThese consist of 1 pair of enantiomers ($d$- and $l$-tartaric acid) and 1 optically inactive meso compound.\\n\\n **Marks Tip**: Symmetrical chiral compounds always have fewer stereoisomers than $2^n$ due to internal planes of symmetry generating meso forms."
    },
    {
        "chapter": "Environmental Chemistry",
        "topic": "Atmospheric Pollution & Photochemical Smog",
        "level": "Basic",
        "type": "mcq_single",
        "question": "[Marks Basic / JEE Main] Photochemical smog is characterized as an oxidizing smog. Its primary oxidizing constituents are:",
        "options": [
            "$\\text{O}_3$, $\\text{PAN}$ and $\\text{NO}_2$",
            "$\\text{SO}_2$, smoke and particulate carbon",
            "$\\text{CO}$, $\\text{CO}_2$ and $\\text{CH}_4$",
            "$\\text{H}_2\\text{S}$, $\\text{NH}_3$ and $\\text{NO}$"
        ],
        "correct_answer": "O3, PAN and NO2",
        "correct_index": 0,
        "explanation": "Photochemical smog occurs in warm, sunny dry climates. Nitrogen oxides ($\\text{NO}_x$) and unburnt hydrocarbons undergo photochemical reactions to produce ozone ($\\text{O}_3$), peroxyacetyl nitrate ($\\text{PAN}$), and acrolein.\\nBecause it is rich in oxidants, it is classified as oxidizing smog.\\nIn contrast, classical London smog contains $\\text{SO}_2$ and is reducing in nature.\\n\\n **Marks Tip**: Photochemical smog = Oxidizing (Ozone + PAN + NO2). Classical smog = Reducing (SO2 + smoke)."
    },
    {
        "chapter": "Electrochemistry",
        "topic": "Standard Electrode Potentials & Nernst Equation",
        "level": "Basic",
        "type": "mcq_single",
        "question": "[Marks Basic / JEE Main] For the Daniell cell $\\text{Zn}(s)|\\text{Zn}^{2+}(aq)\\|\\text{Cu}^{2+}(aq)|\\text{Cu}(s)$ with $E^\\circ_{\\text{cell}} = 1.10\\text{ V}$, the equilibrium constant $K_c$ at $298\\text{ K}$ is given by (take $\\frac{2.303 RT}{F} = 0.059\\text{ V}$):",
        "options": [
            "$10^{37.3}$",
            "$10^{18.6}$",
            "$10^{-37.3}$",
            "$10^{1.10}$"
        ],
        "correct_answer": "10^37.3",
        "correct_index": 0,
        "explanation": "At equilibrium, $E_{\\text{cell}} = 0$, so $E^\\circ_{\\text{cell}} = \\frac{0.059}{n} \\log_{10} K_c$.\\nHere $n = 2$ electrons transferred.\\n$1.10 = \\frac{0.059}{2} \\log_{10} K_c \\implies \\log_{10} K_c = \\frac{2.20}{0.059} \\approx 37.288 \\implies K_c \\approx 10^{37.3}$.\\n\\n **Marks Tip**: $E^\\circ_{\\text{cell}} > 0$ implies huge $K_c \\gg 1$, showing Daniell cell reaction proceeds essentially to 100% completion."
    },
    {
        "chapter": "Surface Chemistry",
        "topic": "Adsorption Isotherms & Colloids Coagulation",
        "level": "Basic",
        "type": "mcq_single",
        "question": "[Marks Basic / JEE Main] According to Hardy-Schulze rule, the coagulating power of an electrolyte for a negatively charged sol (such as $\\text{As}_2\\text{S}_3$ sol) increases in the order:",
        "options": [
            "$\\text{Na}^+ < \\text{Ba}^{2+} < \\text{Al}^{3+}$",
            "$\\text{Al}^{3+} < \\text{Ba}^{2+} < \\text{Na}^+$",
            "$\\text{Cl}^- < \\text{SO}_4^{2-} < \\text{PO}_4^{3-}$",
            "$\\text{Ba}^{2+} < \\text{Na}^+ < \\text{Al}^{3+}$"
        ],
        "correct_answer": "Na^+ < Ba^2+ < Al^3+",
        "correct_index": 0,
        "explanation": "Hardy-Schulze Rule states:\\n1. The effective ion causing coagulation carries charge opposite to the sol particle (positively charged cations for negative $\\text{As}_2\\text{S}_3$ sol).\\n2. Coagulating power increases rapidly with the valency of the flocculating ion (proportional to $z^6$).\\nHence: $\\text{Al}^{3+} (+3) > \\text{Ba}^{2+} (+2) > \\text{Na}^+ (+1)$.\\n\\n **Marks Tip**: Coagulating power is inversely proportional to Coagulation / Flocculation value!"
    },
    {
        "chapter": "Principles of Metallurgy",
        "topic": "Ellingham Diagram, Froth Flotation & Refining",
        "level": "Basic",
        "type": "mcq_single",
        "question": "[Marks Basic / JEE Main] In the froth flotation process for the concentration of sulfide ores, pine oil and sodium ethyl xanthate act respectively as:",
        "options": [
            "Frother and Collector",
            "Collector and Frother",
            "Depressant and Flux",
            "Slag former and Collector"
        ],
        "correct_answer": "Frother and Collector",
        "correct_index": 0,
        "explanation": "In froth flotation:\\n- Pine oil / eucalyptus oil acts as a **Frother** to produce stable foam.\\n- Potassium/Sodium xanthates act as **Collectors**, attaching non-polar hydrophobic chains to sulfide ore particles to make them water-repellent.\\n- $\\text{NaCN}$ acts as a **Depressant** (e.g., selectively floats $\\text{PbS}$ by depressing $\\text{ZnS}$ via complex $[\\text{Zn}(\\text{CN})_4]^{2-}$).\\n\\n **Marks Tip**: Collectors enhance non-wettability of mineral particles with water."
    },
    {
        "chapter": "p-Block Elements (Group 15, 16, 17, 18)",
        "topic": "Oxoacids & Interhalogen Geometry",
        "level": "Basic",
        "type": "mcq_single",
        "question": "[Marks Basic / JEE Main] The geometry and hybridization of the central xenon atom in xenon tetrafluoride ($\\text{XeF}_4$) are respectively:",
        "options": [
            "Square planar, $sp^3d^2$",
            "Tetrahedral, $sp^3$",
            "See-saw, $sp^3d$",
            "Square pyramidal, $sp^3d^2$"
        ],
        "correct_answer": "Square planar, sp^3d^2",
        "correct_index": 0,
        "explanation": "Valence electrons on $\\text{Xe} = 8$.\\nForming 4 single bonds with fluorine leaves 4 non-bonding electrons = 2 lone pairs.\\nSteric number $= 4\\text{ (bond pairs)} + 2\\text{ (lone pairs)} = 6 \\implies sp^3d^2$ hybridization.\\nElectron pair geometry is octahedral; with 2 axial lone pairs trans to each other, molecular shape is **square planar**.\\n\\n **Marks Tip**: Axial lone pairs minimize lone pair-bonding pair repulsions at $90^\\circ$."
    },
    {
        "chapter": "d and f Block Elements",
        "topic": "Electronic Configuration & Magnetic Moment",
        "level": "Basic",
        "type": "mcq_single",
        "question": "[Marks Basic / JEE Main] The spin-only magnetic moment of $\\text{Fe}^{2+}$ ion ($Z = 26$) is:",
        "options": [
            "$4.90\\text{ BM}$",
            "$5.92\\text{ BM}$",
            "$3.87\\text{ BM}$",
            "$2.83\\text{ BM}$"
        ],
        "correct_answer": "4.90 BM",
        "correct_index": 0,
        "explanation": "Neutral $\\text{Fe}$ is $[\\text{Ar}] 3d^6 4s^2$.\\nLoss of two $4s$ electrons gives $\\text{Fe}^{2+}: [\\text{Ar}] 3d^6 4s^0$.\\nIn $3d^6$, there is 1 paired orbital and 4 unpaired electrons ($n = 4$).\\nSpin-only magnetic moment $\\mu = \\sqrt{n(n + 2)} = \\sqrt{4(6)} = \\sqrt{24} \\approx 4.899 \\approx 4.90\\text{ BM}$.\\n\\n **Marks Tip**: Quick shortcut: magnetic moment is always 'n point something' where $n$ is number of unpaired electrons! $\\sqrt{24} = 4.9\\text{ BM}$."
    },
    {
        "chapter": "Qualitative Inorganic Analysis (Salt Analysis)",
        "topic": "Group Analysis & Wet Tests for Cations/Anions",
        "level": "Basic",
        "type": "mcq_single",
        "question": "[Marks Basic / JEE Main] In the brown ring test for nitrate ion ($\\text{NO}_3^-$), the brown ring formed at the junction of two layers is due to the coordination complex:",
        "options": [
            "$[\\text{Fe}(\\text{H}_2\\text{O})_5(\\text{NO})]^{2+}$",
            "$[\\text{Fe}(\\text{H}_2\\text{O})_6]^{3+}$",
            "$[\\text{Fe}(\\text{NO})_4]^{2+}$",
            "$[\\text{Fe}(\\text{SO}_4)_2(\\text{NO})]^-$"
        ],
        "correct_answer": "[Fe(H2O)5(NO)]2+",
        "correct_index": 0,
        "explanation": "Reaction: $\\text{NO}_3^- + 3\\text{Fe}^{2+} + 4\\text{H}^+ \\to \\text{NO} + 3\\text{Fe}^{3+} + 2\\text{H}_2\\text{O}$.\\nThe generated nitric oxide combines with unreacted ferrous sulfate solution:\\n$[\\text{Fe}(\\text{H}_2\\text{O})_6]^{2+} + \\text{NO} \\to [\\text{Fe}(\\text{H}_2\\text{O})_5(\\text{NO})]^{2+} + \\text{H}_2\\text{O}$.\\nHere iron has an unusual $+1$ formal oxidation state, and $\\text{NO}$ is present as nitrosonium ion $\\text{NO}^+$.\\n\\n **Marks Tip**: Oxidation state of Fe in the brown ring complex is $+1$ with 3 unpaired electrons (magnetic moment $\\mu = 3.87\\text{ BM}$)."
    },
    {
        "chapter": "Biomolecules",
        "topic": "Carbohydrates, Amino Acids & Peptide Bond",
        "level": "Basic",
        "type": "mcq_single",
        "question": "[Marks Basic / JEE Main] Which of the following standard $\\alpha$-amino acids is optically inactive?",
        "options": [
            "Glycine",
            "Alanine",
            "Valine",
            "Leucine"
        ],
        "correct_answer": "Glycine",
        "correct_index": 0,
        "explanation": "Glycine has the formula $\\text{H}_2\\text{N}-\\text{CH}_2-\\text{COOH}$.\\nThe $\\alpha$-carbon is attached to two hydrogen atoms ($\\text{H}$ and $\\text{H}$), an amino group ($-\\text{NH}_2$), and a carboxyl group ($-\\text{COOH}$).\\nBecause it lacks four different substituents, the $\\alpha$-carbon is achiral. All other 19 proteinogenic amino acids are chiral and optically active.\\n\\n **Marks Tip**: Glycine is the simplest and ONLY achiral naturally occurring standard amino acid."
    },
    {
        "chapter": "Polymers",
        "topic": "Classification & Condensation Polymers",
        "level": "Basic",
        "type": "mcq_single",
        "question": "[Marks Basic / JEE Main] Nylon-6,6 is a condensation polyamide synthesized by the polycondensation of:",
        "options": [
            "Hexamethylenediamine and Adipic acid",
            "Caprolactam",
            "Terephthalic acid and Ethylene glycol",
            "Phenol and Formaldehyde"
        ],
        "correct_answer": "Hexamethylenediamine and Adipic acid",
        "correct_index": 0,
        "explanation": "Nylon-6,6 is made from two 6-carbon monomers:\\n1. Hexamethylenediamine ($\\text{H}_2\\text{N}-(\\text{CH}_2)_6-\\text{NH}_2$)\\n2. Adipic acid ($\\text{HOOC}-(\\text{CH}_2)_4-\\text{COOH}$)\\nCondensation releases water molecules and forms repeating amide linkages ($-\\text{CO}-\\text{NH}-$).\\n\\n **Marks Tip**: The numbers '6,6' denote the number of carbons in the diamine and dibasic acid respectively."
    },
    {
        "chapter": "Chemistry in Everyday Life & Practical Organic",
        "topic": "Medicinal Chemistry & Soaps/Detergents",
        "level": "Basic",
        "type": "mcq_single",
        "question": "[Marks Basic / JEE Main] The antiseptic property of Dettol is primarily attributed to a mixture of:",
        "options": [
            "Chloroxylenol and $\\alpha$-Terpineol",
            "Bithionol and Phenol",
            "Iodoform and Boric acid",
            "Aspirin and Paracetamol"
        ],
        "correct_answer": "Chloroxylenol and alpha-Terpineol",
        "correct_index": 0,
        "explanation": "Dettol is a popular antiseptic consisting of chloroxylenol (4-chloro-3,5-dimethylphenol) and $\\alpha$-terpineol dissolved in suitable solvent.\\nAntiseptics are antimicrobial substances applied to living tissues without causing damage.\\n\\n **Marks Tip**: Bithionol is added to soaps to impart antiseptic properties and reduce body odor."
    },

    # =========================================================================
    # MATHEMATICS (15 MISSING CHAPTERS + EXTRA HIGH YIELD)
    # =========================================================================
    {
        "chapter": "Sets, Relations and Functions",
        "topic": "Types of Relations & Equivalence Relations",
        "level": "Basic",
        "type": "mcq_single",
        "question": "[Marks Basic / JEE Main] Let set $A = \\{1, 2, 3\\}$. A relation $R$ on $A$ is defined as $R = \\{(1, 1), (2, 2), (3, 3), (1, 2), (2, 1), (2, 3)\\}$. To make $R$ an equivalence relation, the minimum additional ordered pairs that must be added are:",
        "options": [
            "$\\{(3, 2), (1, 3), (3, 1)\\}$",
            "$\\{(3, 2)\\}$ only",
            "$\\{(1, 3), (3, 1)\\}$ only",
            "$\\{(3, 2), (2, 2)\\}$"
        ],
        "correct_answer": "{(3, 2), (1, 3), (3, 1)}",
        "correct_index": 0,
        "explanation": "1. Reflexive: $(1, 1), (2, 2), (3, 3) \\in R$ (satisfied).\\n2. Symmetric: $(2, 3) \\in R \\implies$ must add $(3, 2)$.\\n3. Transitive: $(1, 2) \\in R$ and $(2, 3) \\in R \\implies$ must add $(1, 3)$.\\nBy symmetry of $(1, 3)$, we must also add $(3, 1)$.\\nCheck transitive with all added: fully closed equivalence relation.\\nHence, minimum added pairs are $(3, 2), (1, 3), (3, 1)$.\\n\\n **Marks Tip**: An equivalence relation on a 3-element set where all elements are connected must contain all $3^2 = 9$ pairs."
    },
    {
        "chapter": "Trigonometric Functions & Identities",
        "topic": "Compound Angles & Maximum/Minimum Values",
        "level": "Basic",
        "type": "mcq_single",
        "question": "[Marks Basic / JEE Main] The maximum and minimum values of the expression $f(x) = 5 \\cos x + 12 \\sin x + 7$ are respectively:",
        "options": [
            "$20$ and $-6$",
            "$19$ and $-5$",
            "$24$ and $0$",
            "$12$ and $-12$"
        ],
        "correct_answer": "20 and -6",
        "correct_index": 0,
        "explanation": "For any expression of form $a \\cos x + b \\sin x$, its range is $[-\\sqrt{a^2 + b^2}, +\\sqrt{a^2 + b^2}]$.\\nHere $a = 5, b = 12 \\implies \\sqrt{5^2 + 12^2} = \\sqrt{25 + 144} = \\sqrt{169} = 13$.\\nSo $-13 \\le 5 \\cos x + 12 \\sin x \\le 13$.\\nAdding 7 across the inequality:\\n$-13 + 7 \\le f(x) \\le 13 + 7 \\implies -6 \\le f(x) \\le 20$.\\n\\n **Marks Tip**: Remember Pythagorean triplets $(3,4,5)$, $(5,12,13)$, $(7,24,25)$, $(8,15,17)$ to compute $\\sqrt{a^2 + b^2}$ in your head."
    },
    {
        "chapter": "Trigonometric Equations",
        "topic": "General Solutions of Trigonometric Equations",
        "level": "Basic",
        "type": "mcq_single",
        "question": "[Marks Basic / JEE Main] The number of distinct solutions of the equation $2 \\sin^2 x - 3 \\sin x + 1 = 0$ in the interval $[0, 2\\pi]$ is:",
        "options": [
            "$3$",
            "$2$",
            "$4$",
            "$1$"
        ],
        "correct_answer": "3",
        "correct_index": 0,
        "explanation": "Factor the quadratic in $\\sin x$:\\n$2\\sin^2 x - 2\\sin x - \\sin x + 1 = 0 \\implies (2\\sin x - 1)(\\sin x - 1) = 0$.\\nCase 1: $\\sin x = 1 \\implies x = \\frac{\\pi}{2}$ (1 solution in $[0, 2\\pi]$).\\nCase 2: $\\sin x = \\frac{1}{2} \\implies x = \\frac{\\pi}{6}$ and $x = \\pi - \\frac{\\pi}{6} = \\frac{5\\pi}{6}$ (2 solutions in $[0, 2\\pi]$).\\nTotal distinct solutions $= 1 + 2 = 3$ solutions.\\n\\n **Marks Tip**: Always check boundary values at endpoints $0$ and $2\\pi$ to ensure no roots are double counted or omitted."
    },
    {
        "chapter": "Linear Inequalities",
        "topic": "Modulus Inequalities & Wavy Curve Method",
        "level": "Basic",
        "type": "mcq_single",
        "question": "[Marks Basic / JEE Main] The solution set of the inequality $|2x - 5| \\le 7$ is:",
        "options": [
            "$[-1, 6]$",
            "$(-1, 6)$",
            "$[-6, 1]$",
            "$(-\\infty, -1] \\cup [6, \\infty)$"
        ],
        "correct_answer": "[-1, 6]",
        "correct_index": 0,
        "explanation": "By definition, $|u| \\le a \\iff -a \\le u \\le a$ (for $a > 0$).\\nHere $-7 \\le 2x - 5 \\le 7$.\\nAdd 5 to all parts: $-2 \\le 2x \\le 12$.\\nDivide by 2: $-1 \\le x \\le 6 \\implies x \\in [-1, 6]$.\\n\\n **Marks Tip**: Non-strict inequalities ($\\le, \\ge$) preserve closed interval brackets $[\\dots]$."
    },
    {
        "chapter": "Conic Sections: Hyperbola",
        "topic": "Standard Hyperbola & Eccentricity",
        "level": "Basic",
        "type": "mcq_single",
        "question": "[Marks Basic / JEE Main] If the eccentricity of a hyperbola $\\frac{x^2}{a^2} - \\frac{y^2}{b^2} = 1$ is $e = \\frac{\\sqrt{5}}{2}$, then the length of its latus rectum is ($2a = 4$):",
        "options": [
            "$1$",
            "$2$",
            "$4$",
            "$\\sqrt{5}$"
        ],
        "correct_answer": "1",
        "correct_index": 0,
        "explanation": "Given $2a = 4 \\implies a = 2$.\\nEccentricity relation: $b^2 = a^2 (e^2 - 1)$.\\n$b^2 = 2^2 \\left(\\left(\\frac{\\sqrt{5}}{2}\\right)^2 - 1\\right) = 4 \\left(\\frac{5}{4} - 1\\right) = 4 \\times \\frac{1}{4} = 1$.\\nLength of latus rectum $= \\frac{2b^2}{a} = \\frac{2(1)}{2} = 1$.\\n\\n **Marks Tip**: For ellipse $b^2 = a^2(1 - e^2)$ with $e < 1$; for hyperbola $b^2 = a^2(e^2 - 1)$ with $e > 1$."
    },
    {
        "chapter": "Introduction to 3D Geometry (Class 11)",
        "topic": "Section Formula & Distance Between 3D Points",
        "level": "Basic",
        "type": "mcq_single",
        "question": "[Marks Basic / JEE Main] The ratio in which the $xy$-plane divides the line segment joining the points $A(-2, 4, 7)$ and $B(3, -5, 8)$ is:",
        "options": [
            "$-7 : 8$ (externally)",
            "$7 : 8$ (internally)",
            "$4 : 5$ (internally)",
            "$2 : 3$ (externally)"
        ],
        "correct_answer": "-7 : 8 (externally)",
        "correct_index": 0,
        "explanation": "Any point on the $xy$-plane has $z = 0$.\\nLet the ratio be $k : 1$.\\nUsing section formula for $z$-coordinate: $z = \\frac{k z_2 + z_1}{k + 1} = \\frac{8k + 7}{k + 1} = 0 \\implies 8k + 7 = 0 \\implies k = -\\frac{7}{8}$.\\nThe negative sign confirms the division is external in the ratio $7 : 8$.\\n\\n **Marks Tip**: Shortcut: The plane divides the line in ratio $-z_1 / z_2$ for $xy$-plane, $-y_1 / y_2$ for $xz$-plane, and $-x_1 / x_2$ for $yz$-plane."
    },
    {
        "chapter": "Mathematical Reasoning & Induction",
        "topic": "Tautology, Contradiction & Contrapositive",
        "level": "Basic",
        "type": "mcq_single",
        "question": "[Marks Basic / JEE Main] The contrapositive of the conditional statement: 'If a natural number $n$ is divisible by 6, then it is divisible by 2' is:",
        "options": [
            "If $n$ is not divisible by 2, then $n$ is not divisible by 6",
            "If $n$ is divisible by 2, then $n$ is divisible by 6",
            "If $n$ is not divisible by 6, then $n$ is not divisible by 2",
            "If $n$ is divisible by 6, then $n$ is not divisible by 2"
        ],
        "correct_answer": "If n is not divisible by 2, then n is not divisible by 6",
        "correct_index": 0,
        "explanation": "For an implication $p \\to q$:\\n- Converse is $q \\to p$\\n- Inverse is $\\sim p \\to \\sim q$\\n- Contrapositive is $\\sim q \\to \\sim p$\\nHere $p$: '$n$ is divisible by 6' and $q$: '$n$ is divisible by 2'.\\nContrapositive: 'If $n$ is not divisible by 2, then $n$ is not divisible by 6'.\\nAn implication is always logically equivalent to its contrapositive ($p \\to q \\equiv \\sim q \\to \\sim p$).\\n\\n **Marks Tip**: Truth table never changes when switching a statement with its contrapositive."
    },
    {
        "chapter": "Relations and Functions (Advanced)",
        "topic": "Invertible Functions & Bijective Mapping",
        "level": "Basic",
        "type": "mcq_single",
        "question": "[Marks Basic / JEE Main] If $f: \\mathbb{R} \\to \\mathbb{R}$ is defined by $f(x) = 3x - 5$, then the inverse function $f^{-1}(x)$ is:",
        "options": [
            "$\\frac{x + 5}{3}$",
            "$\\frac{x - 5}{3}$",
            "$3x + 5$",
            "$\\frac{1}{3x - 5}$"
        ],
        "correct_answer": "(x + 5)/3",
        "correct_index": 0,
        "explanation": "Let $y = f(x) = 3x - 5$.\\nSolve for $x$ in terms of $y$:\\n$y + 5 = 3x \\implies x = \\frac{y + 5}{3}$.\\nInterchanging variables gives $f^{-1}(x) = \\frac{x + 5}{3}$.\\n\\n **Marks Tip**: Graph of $f^{-1}(x)$ is the exact reflection of $f(x)$ across the mirror line $y = x$."
    },
    {
        "chapter": "Inverse Trigonometric Functions (ITF)",
        "topic": "Principal Value Branch & Sum Identities",
        "level": "Basic",
        "type": "mcq_single",
        "question": "[Marks Basic / JEE Main] The value of $\\sin^{-1}\\left(\\sin\\frac{5\\pi}{6}\\right) + \\cos^{-1}\\left(\\cos\\frac{7\\pi}{6}\\right)$ is:",
        "options": [
            "$\\pi$",
            "$\\frac{2\\pi}{3}$",
            "$\\frac{5\\pi}{6}$",
            "$2\\pi$"
        ],
        "correct_answer": "pi",
        "correct_index": 0,
        "explanation": "1. For $\\sin^{-1}(\\sin\\theta)$, principal range is $[-\\frac{\\pi}{2}, \\frac{\\pi}{2}]$.\\n$\\frac{5\\pi}{6} = \\pi - \\frac{\\pi}{6} \\implies \\sin\\frac{5\\pi}{6} = \\sin\\frac{\\pi}{6} \\implies \\sin^{-1}\\left(\\sin\\frac{5\\pi}{6}\\right) = \\frac{\\pi}{6}$.\\n2. For $\\cos^{-1}(\\cos\\phi)$, principal range is $[0, \\pi]$.\\n$\\frac{7\\pi}{6} = 2\\pi - \\frac{5\\pi}{6} \\implies \\cos\\frac{7\\pi}{6} = \\cos\\frac{5\\pi}{6} \\implies \\cos^{-1}\\left(\\cos\\frac{7\\pi}{6}\\right) = \\frac{5\\pi}{6}$.\\nSum $= \\frac{\\pi}{6} + \\frac{5\\pi}{6} = \\frac{6\\pi}{6} = \\pi$.\\n\\n **Marks Tip**: Always bring the angle inside the principal branch before evaluating inverse trigonometric expressions."
    },
    {
        "chapter": "Determinants",
        "topic": "Properties of Determinants & Cramer's Rule",
        "level": "Basic",
        "type": "mcq_single",
        "question": "[Marks Basic / JEE Main] If $A$ is a square matrix of order $3 \\times 3$ with $\\det(A) = 4$, then $\\det(2A)$ and $\\det(\\text{adj}(A))$ are respectively:",
        "options": [
            "$32$ and $16$",
            "$8$ and $16$",
            "$32$ and $64$",
            "$24$ and $12$"
        ],
        "correct_answer": "32 and 16",
        "correct_index": 0,
        "explanation": "For a square matrix $A$ of order $n$:\\n1. $\\det(k A) = k^n \\det(A)$. For $n = 3$, $\\det(2A) = 2^3 \\det(A) = 8 \\times 4 = 32$.\\n2. $\\det(\\text{adj}(A)) = [\\det(A)]^{n - 1}$. For $n = 3$, $\\det(\\text{adj}(A)) = [\\det(A)]^2 = 4^2 = 16$.\\n\\n **Marks Tip**: Scaling a matrix by scalar $k$ multiplies every row by $k$, pulling out $k^n$."
    },
    {
        "chapter": "Applications of Derivatives: Tangents & Normals",
        "topic": "Slope of Tangent & Orthogonality",
        "level": "Basic",
        "type": "mcq_single",
        "question": "[Marks Basic / JEE Main] The slope of the normal to the parabola $y^2 = 4x$ at the point $(1, 2)$ is:",
        "options": [
            "$-1$",
            "$1$",
            "$-2$",
            "$\\frac{1}{2}$"
        ],
        "correct_answer": "-1",
        "correct_index": 0,
        "explanation": "Differentiating $y^2 = 4x$ with respect to $x$:\\n$2y \\frac{dy}{dx} = 4 \\implies \\frac{dy}{dx} = \\frac{2}{y}$.\\nAt $(1, 2)$, slope of tangent $m_{\\text{tangent}} = \\frac{2}{2} = 1$.\\nSlope of normal $m_{\\text{normal}} = -\\frac{1}{m_{\\text{tangent}}} = -\\frac{1}{1} = -1$.\\n\\n **Marks Tip**: For parametric parabola $(at^2, 2at)$, slope of tangent is $1/t$ and slope of normal is $-t$."
    },
    {
        "chapter": "Applications of Derivatives: Monotonicity & Extrema",
        "topic": "Critical Points & Strictly Increasing Functions",
        "level": "Basic",
        "type": "mcq_single",
        "question": "[Marks Basic / JEE Main] The function $f(x) = 2x^3 - 9x^2 + 12x + 1$ is strictly increasing in the interval:",
        "options": [
            "$(-\\infty, 1) \\cup (2, \\infty)$",
            "$(1, 2)$",
            "$[1, 2]$",
            "$(-\\infty, \\infty)$"
        ],
        "correct_answer": "(-inf, 1) U (2, inf)",
        "correct_index": 0,
        "explanation": "Find $f'(x)$:\\n$f'(x) = 6x^2 - 18x + 12 = 6(x^2 - 3x + 2) = 6(x - 1)(x - 2)$.\\nFor strictly increasing: $f'(x) > 0 \\implies (x - 1)(x - 2) > 0$.\\nBy wavy curve sign scheme: positive when $x < 1$ or $x > 2$.\\nHence, $f(x)$ is strictly increasing on $(-\\infty, 1) \\cup (2, \\infty)$.\\n\\n **Marks Tip**: Roots of $f'(x) = 0$ partition the real line into alternating increasing/decreasing sub-intervals."
    },
    {
        "chapter": "Area Under Curves (Application of Integrals)",
        "topic": "Area Enclosed Between Standard Parabola and Line",
        "level": "Basic",
        "type": "mcq_single",
        "question": "[Marks Basic / JEE Main] The area bounded by the parabola $y^2 = 4x$ and the line $y = 2x$ is:",
        "options": [
            "$\\frac{1}{3}$",
            "$\\frac{2}{3}$",
            "$\\frac{4}{3}$",
            "$\\frac{1}{6}$"
        ],
        "correct_answer": "1/3",
        "correct_index": 0,
        "explanation": "Points of intersection: $(2x)^2 = 4x \\implies 4x^2 - 4x = 0 \\implies 4x(x - 1) = 0 \\implies x = 0, x = 1$.\\nFor $x \\in [0, 1]$, the curve $y = 2\\sqrt{x}$ lies above $y = 2x$.\\n$\\text{Area} = \\int_0^1 (2\\sqrt{x} - 2x) dx = \\left[ 2 \\cdot \\frac{2}{3} x^{3/2} - x^2 \\right]_0^1 = \\frac{4}{3} - 1 = \\frac{1}{3}$.\\n\\n **Marks Tip**: Standard formula for area between $y^2 = 4ax$ and $y = mx$ is $\\text{Area} = \\frac{8a^2}{3m^3}$. Here $a = 1, m = 2 \\implies \\frac{8(1)}{3(8)} = \\frac{1}{3}$."
    },
    {
        "chapter": "Probability (Advanced: Bayes & Distributions)",
        "topic": "Bayes' Theorem & Total Probability",
        "level": "Basic",
        "type": "mcq_single",
        "question": "[Marks Basic / JEE Main] Box I contains 2 gold and 3 silver coins. Box II contains 3 gold and 3 silver coins. A box is chosen at random and a coin is drawn. If the drawn coin is gold, the probability that it was drawn from Box I is:",
        "options": [
            "$\\frac{4}{9}$",
            "$\\frac{5}{9}$",
            "$\\frac{1}{2}$",
            "$\\frac{2}{5}$"
        ],
        "correct_answer": "4/9",
        "correct_index": 0,
        "explanation": "$P(B_1) = P(B_2) = \\frac{1}{2}$.\\n$P(G|B_1) = \\frac{2}{5}$, $P(G|B_2) = \\frac{3}{6} = \\frac{1}{2}$.\\nTotal probability $P(G) = P(B_1)P(G|B_1) + P(B_2)P(G|B_2) = \\frac{1}{2}\\left(\\frac{2}{5}\\right) + \\frac{1}{2}\\left(\\frac{1}{2}\\right) = \\frac{1}{5} + \\frac{1}{4} = \\frac{9}{20}$.\\nBy Bayes' Theorem:\\n$P(B_1|G) = \\frac{P(B_1)P(G|B_1)}{P(G)} = \\frac{1/5}{9/20} = \\frac{4}{9}$.\\n\\n **Marks Tip**: Always write out the prior probabilities first; Bayes' formula is simply $\\frac{\\text{favorable path}}{\\text{sum of all paths}}$."
    },
    {
        "chapter": "Linear Programming",
        "topic": "Feasible Region & Corner Point Optimization",
        "level": "Basic",
        "type": "mcq_single",
        "question": "[Marks Basic / JEE Main] The maximum value of $Z = 3x + 4y$ subject to constraints $x + y \\le 4$, $x \\ge 0$, $y \\ge 0$ is:",
        "options": [
            "$16$",
            "$12$",
            "$14$",
            "$20$"
        ],
        "correct_answer": "16",
        "correct_index": 0,
        "explanation": "The feasible region is the triangular region with corner points:\\n- $(0, 0) \\implies Z = 0$\\n- $(4, 0) \\implies Z = 3(4) + 4(0) = 12$\\n- $(0, 4) \\implies Z = 3(0) + 4(4) = 16$\\nComparing values, maximum value is $16$ achieved at vertex $(0, 4)$.\\n\\n **Marks Tip**: Fundamental Theorem of LPP guarantees that the optimal value of an objective function always occurs at one of the corner vertices of the bounded feasible region."
    }
]

def update_marks_file():
    from marks_basic_questions import MARKS_BASIC_QUESTIONS
    existing_q_texts = set(q['question'] for q in MARKS_BASIC_QUESTIONS)
    
    added_count = 0
    for nq in NEW_MARKS_QUESTIONS:
        if nq['question'] not in existing_q_texts:
            MARKS_BASIC_QUESTIONS.append(nq)
            existing_q_texts.add(nq['question'])
            added_count += 1
            
    print(f"Added {added_count} new Marks Basic questions into memory.")
    print(f"Total Marks Basic questions now: {len(MARKS_BASIC_QUESTIONS)}")

    # Write back to marks_basic_questions.py
    with open("marks_basic_questions.py", "w", encoding="utf-8") as f:
        f.write('"""\nmarks_basic_questions.py - Authentic Level 1 (Basic / Foundation) Questions\nsourced and formatted according to Marks App (MathonGo) JEE Main standards.\n"""\n\n')
        f.write('MARKS_BASIC_QUESTIONS = [\n')
        for q in MARKS_BASIC_QUESTIONS:
            dumped = json.dumps(q, ensure_ascii=False, indent=4)
            indented = "\n".join("    " + line for line in dumped.splitlines())
            f.write(indented + ",\n")
        f.write("]\n")
    print("Successfully updated marks_basic_questions.py on disk!")

def seed_to_database():
    import database
    from marks_basic_questions import MARKS_BASIC_QUESTIONS
    from seed_data import SYLLABUS
    
    conn = database.get_connection()
    cursor = conn.cursor()
    
    inserted = 0
    for q in MARKS_BASIC_QUESTIONS:
        cursor.execute("SELECT id FROM chapters WHERE name = ?", (q["chapter"],))
        chap_row = cursor.fetchone()
        if not chap_row:
            print(f"  Warning: Chapter not found in DB: {q['chapter']}")
            continue
        chap_id = chap_row["id"]
        
        cursor.execute("""
        INSERT OR IGNORE INTO questions (chapter_id, topic_name, level, type, question, options_json, correct_answer, correct_index, explanation)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            chap_id,
            q["topic"],
            q["level"],
            q["type"],
            q["question"],
            json.dumps(q["options"], ensure_ascii=False),
            q["correct_answer"],
            q.get("correct_index", 0),
            q["explanation"]
        ))
        if cursor.rowcount > 0:
            inserted += 1
            
    conn.commit()
    conn.close()
    print(f"Seeded {inserted} questions into SQLite database.")

def main():
    print("=" * 60)
    print("EXPANDING MARKS APP BASIC QUESTIONS FOR ALL 96 CHAPTERS")
    print("=" * 60)
    update_marks_file()
    seed_to_database()

if __name__ == "__main__":
    main()
