# JEE Mains & Advanced Study Tracker & Adaptive Diagnostic Test Engine

> 🌐 **Live Web Application (Hosted on GitHub Pages):**  
> **[https://atharvabalar6-crypto.github.io/jee-study-tracker/](https://atharvabalar6-crypto.github.io/jee-study-tracker/)**

A web-based study tracker and adaptive testing engine tailored specifically for **JEE Mains & Advanced** aspirants.

---

## 🌟 Key Features

1. **First-Step Interactive Chapter Selector ("Which Chapter's Test Do You Want to Take?")**:
   - Asks the student which chapter they want to test before anything else.
   - Lets students filter by Subject (**Physics**, **Chemistry**, **Mathematics**), choose their target exam level (**JEE Main** vs **JEE Advanced**), and configure question volume (5, 10, or 15 questions).

2. **Full JEE Syllabus Chapter & Mastery Tracker**:
   - Covers all **96 chapters** across Class 11 & Class 12 (Physics: 30, Chemistry: 32, Mathematics: 34).
   - Dedicated **Class 11 / Class 12 filter** to study and test by school grade.
   - Real-time tracking of:
     - **Tests Given** per chapter
     - **Last Score %** & Average Accuracy
     - **Mastery Status**: `Untested`, `Developing`, `Proficient`, or `Needs Revision`
     - Dynamic progress bars for Physics, Chemistry, and Mathematics

3. **Authentic Computer Based Test (CBT) Interface**:
   - Real JEE exam atmosphere with countdown timer.
   - Interactive **Question Palette** showing live states (*Answered*, *Not Answered*, *Marked for Review*, *Not Visited*).
   - Real LaTeX math rendering with KaTeX for scientific formulas, equations, and diagrams.
   - Authentic JEE marking scheme (+4 for correct, -1 for incorrect).

4. **Deep Sub-Topic Weakness Diagnostics ("Point Out Which Topics Are Weak")**:
   - Analyzes accuracy and mistake frequency at the granular sub-topic level (e.g., in *Rotational Motion*: "Moment of Inertia", "Rolling Motion without Slipping", "Toppling & Work-Energy", "Torque & Equilibrium").
   - Automatically classifies topics into 🔴 **Weak Topics**, 🟡 **Moderate**, and 🟢 **Strong**.
   - Provides targeted diagnostic tips explaining why marks were lost.

5. **Instant Remedial Drill Generator ("Provide Questions Accordingly")**:
   - Features a one-click **"Practice Identified Weak Topics Now"** button right after test evaluation.
   - Automatically creates custom drill tests focused exclusively on the student's identified weak sub-topics to solidify understanding.
   - Dedicated **"Weak Topics Hub"** aggregating all historical weak areas across the syllabus for cumulative revision.

6. **Full Question-by-Question Review with Step-by-Step Solutions**:
   - Comprehensive derivations, formula cheat sheets, and conceptual takeaways for every question.

7. **Marks App Basic Question Bank & Drill Integration**:
   - Integrated authentic Level 1 / Basic questions from **Marks App (by MathonGo)**.
   - Tests core conceptual definitions, fundamental formula substitutions, and standard JEE Main PYQ models.
   - Dedicated difficulty levels in Test Setup:
     - **⚡ Basic (Marks)**: Foundation & single-formula drills (+4/-1) with pro-tips
     - **🎯 JEE Main**: Standard multi-step speed drills (+4/-1)
     - **🔥 JEE Advanced**: Multi-concept deep analytical problems (+4/-1)
   - One-click **⚡ Basic** buttons directly on every Chapter Card, Formula Card, and Notes Modal.

---

## 🚀 Quick Start

### 1. Requirements
- Python 3.10+
- Flask (`py -m pip install flask`)

### 2. Run the Application
Open your terminal in this directory and run:
```bash
py app.py
```

### 3. Open in Browser
Navigate to:
```
http://localhost:5000
```

---

## 📂 Project Architecture

```
study tracker/
├── app.py                 # Flask server with REST APIs & view handlers
├── database.py            # SQLite schema (chapters, topics, questions, attempts, analytics)
├── seed_data.py           # Comprehensive JEE syllabus chapters, topics & question bank
├── question_engine.py     # Adaptive test assembler, scoring engine & weakness classifier
├── templates/
│   └── index.html         # Modern SPA dashboard, CBT exam interface & analytics
├── static/
│   ├── css/
│   │   └── style.css      # Dark-mode styling, question palette, option cards
│   └── js/
│       └── app.js         # State management, CBT timer, test submission & remedial drills
└── test_app.py            # Automated test suite
```

---

## 🏆 Scoring Scheme
- **Correct Answer**: `+4` marks
- **Incorrect Answer**: `-1` mark
- **Unattempted**: `0` marks

