"""
database.py - Database setup and management for JEE Study Tracker
"""
import sqlite3
import json
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "jee_tracker.db")

def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_connection()
    cursor = conn.cursor()

    # Chapters table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS chapters (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        subject TEXT NOT NULL,
        name TEXT NOT NULL UNIQUE,
        class_level INTEGER NOT NULL,
        ncert_order INTEGER DEFAULT 0,
        importance TEXT NOT NULL,
        tests_given INTEGER DEFAULT 0,
        last_score_pct REAL DEFAULT 0.0,
        mastery_status TEXT DEFAULT 'Untested'
    )
    """)

    # Migration: Add ncert_order column if not present
    cursor.execute("PRAGMA table_info(chapters)")
    columns = [row[1] for row in cursor.fetchall()]
    if "ncert_order" not in columns:
        cursor.execute("ALTER TABLE chapters ADD COLUMN ncert_order INTEGER DEFAULT 0")

    # Topics table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS topics (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        chapter_id INTEGER NOT NULL,
        name TEXT NOT NULL,
        FOREIGN KEY (chapter_id) REFERENCES chapters(id),
        UNIQUE(chapter_id, name)
    )
    """)

    # Questions table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS questions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        chapter_id INTEGER NOT NULL,
        topic_name TEXT NOT NULL,
        level TEXT NOT NULL,
        type TEXT NOT NULL,
        question TEXT NOT NULL,
        options_json TEXT NOT NULL,
        correct_answer TEXT NOT NULL,
        correct_index INTEGER,
        explanation TEXT NOT NULL,
        FOREIGN KEY (chapter_id) REFERENCES chapters(id),
        UNIQUE(chapter_id, question)
    )
    """)

    # Tests taken table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS test_attempts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        chapter_id INTEGER NOT NULL,
        chapter_name TEXT NOT NULL,
        subject TEXT NOT NULL,
        exam_type TEXT NOT NULL,
        total_questions INTEGER NOT NULL,
        correct_count INTEGER NOT NULL,
        incorrect_count INTEGER NOT NULL,
        unattempted_count INTEGER NOT NULL,
        score REAL NOT NULL,
        max_score REAL NOT NULL,
        accuracy REAL NOT NULL,
        time_taken_seconds INTEGER NOT NULL,
        weak_topics_json TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (chapter_id) REFERENCES chapters(id)
    )
    """)

    # Question responses within a test
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS test_responses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        test_attempt_id INTEGER NOT NULL,
        question_id INTEGER NOT NULL,
        chapter_name TEXT NOT NULL,
        topic_name TEXT NOT NULL,
        user_answer TEXT,
        correct_answer TEXT NOT NULL,
        is_correct INTEGER NOT NULL,
        FOREIGN KEY (test_attempt_id) REFERENCES test_attempts(id)
    )
    """)

    # Aggregated topic analytics across all tests
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS topic_analytics (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        chapter_name TEXT NOT NULL,
        topic_name TEXT NOT NULL,
        subject TEXT NOT NULL,
        attempts INTEGER DEFAULT 0,
        correct INTEGER DEFAULT 0,
        accuracy REAL DEFAULT 0.0,
        status TEXT DEFAULT 'Untested',
        last_tested TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        UNIQUE(chapter_name, topic_name)
    )
    """)

    conn.commit()
    conn.close()

def seed_database(syllabus, questions):
    conn = get_connection()
    cursor = conn.cursor()

    # Populate syllabus
    for chap in syllabus:
        ncert_order = chap.get("ncert_order", 0)
        cursor.execute("""
        INSERT INTO chapters (subject, name, class_level, ncert_order, importance)
        VALUES (?, ?, ?, ?, ?)
        ON CONFLICT(name) DO UPDATE SET
            subject = excluded.subject,
            class_level = excluded.class_level,
            ncert_order = excluded.ncert_order,
            importance = excluded.importance
        """, (chap["subject"], chap["chapter"], chap["class_level"], ncert_order, chap["importance"]))

        cursor.execute("SELECT id FROM chapters WHERE name = ?", (chap["chapter"],))
        chap_row = cursor.fetchone()
        chap_id = chap_row["id"]

        for topic in chap["topics"]:
            cursor.execute("""
            INSERT OR IGNORE INTO topics (chapter_id, name)
            VALUES (?, ?)
            """, (chap_id, topic))

            # Initialize topic analytics
            cursor.execute("""
            INSERT OR IGNORE INTO topic_analytics (chapter_name, topic_name, subject, attempts, correct, accuracy, status)
            VALUES (?, ?, ?, 0, 0, 0.0, 'Untested')
            """, (chap["chapter"], topic, chap["subject"]))

    # Populate questions
    for q in questions:
        cursor.execute("SELECT id FROM chapters WHERE name = ?", (q["chapter"],))
        chap_row = cursor.fetchone()
        if not chap_row:
            continue
        chap_id = chap_row["id"]

        # Safe utf-8 sanitization for question text and explanation
        q_text = q["question"].encode("utf-8", "ignore").decode("utf-8")
        expl_text = q["explanation"].encode("utf-8", "ignore").decode("utf-8")

        cursor.execute("""
        INSERT OR IGNORE INTO questions (chapter_id, topic_name, level, type, question, options_json, correct_answer, correct_index, explanation)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            chap_id,
            q["topic"],
            q["level"],
            q["type"],
            q_text,
            json.dumps(q["options"], ensure_ascii=False),
            q["correct_answer"],
            q.get("correct_index", 0),
            expl_text
        ))

    conn.commit()
    conn.close()

if __name__ == "__main__":
    init_db()
    print("Database initialized successfully.")
