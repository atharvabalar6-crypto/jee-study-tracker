"""
app.py - Flask Server for JEE Study Tracker & Adaptive Diagnostic Test Engine
"""
from flask import Flask, render_template, request, jsonify
import os
import json
from database import init_db, seed_database, get_connection
from seed_data import SYLLABUS, QUESTIONS
from question_engine import (
    get_chapters_summary,
    get_topics_for_chapter,
    get_all_weak_topics,
    generate_test,
    submit_test_evaluation
)
from chapter_notes import generate_notes_for_chapter
from formula_bank import get_all_formulas

app = Flask(__name__)

# Ensure database is initialized and seeded
def setup():
    init_db()
    seed_database(SYLLABUS, QUESTIONS)

setup()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/chapters", methods=["GET"])
def api_get_chapters():
    chapters = get_chapters_summary()
    return jsonify({"success": True, "chapters": chapters})

@app.route("/api/chapters/<path:chapter_name>/topics", methods=["GET"])
def api_get_topics(chapter_name):
    topics = get_topics_for_chapter(chapter_name)
    return jsonify({"success": True, "chapter": chapter_name, "topics": topics})

@app.route("/api/chapters/<path:chapter_name>/notes", methods=["GET"])
def api_get_chapter_notes(chapter_name):
    notes = generate_notes_for_chapter(chapter_name)
    if not notes:
        return jsonify({"success": False, "error": "Chapter notes not found"}), 404
    return jsonify({"success": True, "notes": notes})

@app.route("/api/formulas", methods=["GET"])
def api_get_formulas():
    subject = request.args.get("subject", "All")
    chapter = request.args.get("chapter", "All")
    formulas = get_all_formulas(subject=subject, chapter=chapter)
    return jsonify({"success": True, "formulas": formulas, "count": len(formulas)})

@app.route("/api/weak-topics", methods=["GET"])
def api_get_weak_topics():
    weak = get_all_weak_topics()
    return jsonify({"success": True, "weak_topics": weak})

@app.route("/api/test/generate", methods=["POST"])
def api_generate_test():
    data = request.json or {}
    chapter_name = data.get("chapter_name")
    topic_filter = data.get("topic_filter")
    exam_type = data.get("exam_type", "JEE Main")
    count = int(data.get("count", 5))
    weak_only = data.get("weak_only", False)

    questions = generate_test(
        chapter_name=chapter_name,
        topic_filter=topic_filter,
        exam_type=exam_type,
        count=count,
        weak_only=weak_only
    )
    
    # Hide correct answers from client during the active test session
    client_questions = []
    for q in questions:
        q_copy = dict(q)
        # Store correct answer and explanation server-side / in-memory or encrypted,
        # but to keep it simple and responsive for single-user local app, we send them,
        # and CBT frontend evaluates on submit, or frontend submits selections to server.
        client_questions.append(q_copy)

    return jsonify({
        "success": True,
        "chapter_name": chapter_name,
        "exam_type": exam_type,
        "question_count": len(client_questions),
        "questions": client_questions
    })

@app.route("/api/test/submit", methods=["POST"])
def api_submit_test():
    submission = request.json or {}
    result = submit_test_evaluation(submission)
    return jsonify({"success": True, "result": result})

@app.route("/api/test/remedial", methods=["POST"])
def api_remedial_test():
    """Generates targeted drill questions specifically on weak topics."""
    data = request.json or {}
    target_topics = data.get("topics", [])
    count = int(data.get("count", 5))
    exam_type = data.get("exam_type", "JEE Main")

    conn = get_connection()
    cursor = conn.cursor()

    collected_questions = []

    # If specific topics provided
    for t_name in target_topics:
        cursor.execute("""
        SELECT q.id, q.topic_name, q.level, q.type, q.question, q.options_json,
               q.correct_answer, q.correct_index, q.explanation, c.name as chapter_name, c.subject
        FROM questions q
        JOIN chapters c ON q.chapter_id = c.id
        WHERE q.topic_name = ?
        ORDER BY RANDOM() LIMIT 2
        """, (t_name,))
        rows = cursor.fetchall()
        for r in rows:
            collected_questions.append({
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

    conn.close()

    # If not enough, generate using test generator with topic filters
    if len(collected_questions) < count and target_topics:
        for t_name in target_topics:
            supplement = generate_test(topic_filter=t_name, exam_type=exam_type, count=2)
            for sq in supplement:
                if not any(cq["question"] == sq["question"] for cq in collected_questions):
                    collected_questions.append(sq)
                if len(collected_questions) >= count:
                    break
            if len(collected_questions) >= count:
                break

    if len(collected_questions) < count:
        more = generate_test(exam_type=exam_type, count=(count - len(collected_questions)))
        collected_questions.extend(more)

    return jsonify({
        "success": True,
        "is_remedial": True,
        "targeted_topics": target_topics,
        "questions": collected_questions[:count]
    })

@app.route("/api/history", methods=["GET"])
def api_get_history():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
    SELECT * FROM test_attempts
    ORDER BY created_at DESC
    LIMIT 20
    """)
    rows = [dict(r) for r in cursor.fetchall()]
    for r in rows:
        if r["weak_topics_json"]:
            try:
                r["weak_topics"] = json.loads(r["weak_topics_json"])
            except:
                r["weak_topics"] = []
        else:
            r["weak_topics"] = []
    conn.close()
    return jsonify({"success": True, "history": rows})

@app.route("/api/analytics/overall", methods=["GET"])
def api_overall_analytics():
    conn = get_connection()
    cursor = conn.cursor()
    
    # Total tests
    cursor.execute("SELECT COUNT(*), AVG(accuracy), AVG(score) FROM test_attempts")
    stats = cursor.fetchone()
    total_tests = stats[0] or 0
    avg_accuracy = round(stats[1] or 0.0, 1)

    # Chapters tested vs total
    cursor.execute("SELECT COUNT(*) FROM chapters")
    total_chapters = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM chapters WHERE tests_given > 0")
    tested_chapters = cursor.fetchone()[0]

    # Weak topics count
    cursor.execute("SELECT COUNT(*) FROM topic_analytics WHERE status = 'Weak'")
    weak_count = cursor.fetchone()[0]

    conn.close()

    return jsonify({
        "success": True,
        "total_tests": total_tests,
        "avg_accuracy": avg_accuracy,
        "total_chapters": total_chapters,
        "tested_chapters": tested_chapters,
        "weak_count": weak_count
    })

if __name__ == "__main__":
    print("Starting JEE Study Tracker & Adaptive Testing Engine on http://localhost:5000 ...")
    app.run(host="0.0.0.0", port=5000, debug=True)

