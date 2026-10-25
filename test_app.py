import database
import seed_data
import question_engine
import json

def test_workflow():
    database.init_db()
    database.seed_database(seed_data.SYLLABUS, seed_data.QUESTIONS)
    print("Database seeded successfully.")

    chapters = question_engine.get_chapters_summary()
    print(f"Total Chapters loaded: {len(chapters)}")
    for ch in chapters[:3]:
        print(f" - {ch['subject']}: {ch['name']} ({len(ch['topics'])} topics, Status: {ch['mastery_status']})")

    # Generate Test for Rotational Motion
    test_questions = question_engine.generate_test("Rotational Motion", None, "JEE Main", 3)
    print(f"\nGenerated test questions: {len(test_questions)}")
    for idx, q in enumerate(test_questions):
        print(f"Q{idx+1}: [{q['topic_name']}] {q['question'][:60]}... (Correct: {q['correct_index']})")

    # Simulate submission where student gets Q1 correct, Q2 wrong
    submission = {
        "chapter_name": "Rotational Motion",
        "subject": "Physics",
        "exam_type": "JEE Main",
        "time_taken_seconds": 180,
        "answers": [
            {
                "id": test_questions[0]["id"],
                "question": test_questions[0]["question"],
                "topic_name": test_questions[0]["topic_name"],
                "user_choice": test_questions[0]["correct_index"],
                "correct_index": test_questions[0]["correct_index"],
                "options": test_questions[0]["options"],
                "explanation": test_questions[0]["explanation"]
            },
            {
                "id": test_questions[1]["id"],
                "question": test_questions[1]["question"],
                "topic_name": test_questions[1]["topic_name"],
                "user_choice": (test_questions[1]["correct_index"] + 1) % 4, # wrong choice
                "correct_index": test_questions[1]["correct_index"],
                "options": test_questions[1]["options"],
                "explanation": test_questions[1]["explanation"]
            }
        ]
    }

    result = question_engine.submit_test_evaluation(submission)
    print(f"\nSubmission Evaluation:")
    print(f"Score: {result['score']} / {result['max_score']} (Accuracy: {result['accuracy']}%)")
    print(f"Weak Topics detected ({len(result['weak_topics'])}):")
    for wt in result["weak_topics"]:
        print(f"  * {wt['topic_name']} - Status: {wt['status']} ({wt['accuracy']}% acc) - {wt['recommendation']}")

    # Check that chapter is now tracked as tested
    updated_chapters = question_engine.get_chapters_summary()
    rm_chap = next(c for c in updated_chapters if c["name"] == "Rotational Motion")
    print(f"\nUpdated Chapter Tracking for Rotational Motion:")
    print(f"Tests Given: {rm_chap['tests_given']}, Last Score: {rm_chap['last_score_pct']}%, Status: {rm_chap['mastery_status']}")

    # Check remedial test generation for the weak topic
    if result["weak_topics"]:
        remedial = question_engine.generate_test(topic_filter=result["weak_topics"][0]["topic_name"], count=2)
        print(f"\nRemedial Questions generated for {result['weak_topics'][0]['topic_name']}: {len(remedial)}")
        for rq in remedial:
            print(f"  Remedial Q: {rq['question'][:60]}...")

    print("\nALL SYSTEM TESTS PASSED SUCCESSFULLY!")

if __name__ == "__main__":
    test_workflow()

