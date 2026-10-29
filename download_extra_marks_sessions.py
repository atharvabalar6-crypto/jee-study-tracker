r"""
download_extra_marks_sessions.py - Downloads additional chapterwise PYQs and basic questions
from MathonGo / Marks for April 2024 and January 2023 sessions into D:\Projects\code\pvq.
Re-exports the updated 96 Marks Chapterwise Markdown Banks with all basic questions.
"""

import os
import sys
import re
import time
import ssl
import json
import urllib.request
import urllib.error

if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

BASE_DIR = r"D:\Projects\code\pvq"
MATHONGO_DIR = os.path.join(BASE_DIR, "03_MathonGo_Chapterwise_PYQs")
MARKS_DIR = os.path.join(BASE_DIR, "04_Marks_Chapterwise_PYQ_Banks")

SSL_CTX = ssl._create_unverified_context()
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

def safe_filename(name):
    clean = re.sub(r'[\\/*?:"<>|]', '', name)
    clean = clean.replace('&amp;', 'and').replace('&', 'and')
    clean = clean.replace(' ', '_').strip('_')
    return clean

def download_file(url, target_path, retries=3, delay=1.0):
    if os.path.exists(target_path) and os.path.getsize(target_path) > 1024:
        print(f"  [SKIP] Already exists ({os.path.getsize(target_path):,} bytes): {os.path.basename(target_path)}")
        return True

    os.makedirs(os.path.dirname(target_path), exist_ok=True)
    
    for attempt in range(1, retries + 1):
        try:
            req = urllib.request.Request(url, headers=HEADERS)
            with urllib.request.urlopen(req, timeout=30, context=SSL_CTX) as resp:
                data = resp.read()
                if len(data) < 500:
                    print(f"  [WARN] Tiny response ({len(data)} bytes) for {url}")
                    return False
                with open(target_path, 'wb') as f:
                    f.write(data)
                print(f"  [OK] Downloaded ({len(data):,} bytes): {os.path.basename(target_path)}")
                return True
        except Exception as e:
            print(f"  [RETRY {attempt}/{retries}] Error downloading {url}: {e}")
            time.sleep(delay * attempt)
            
    print(f"  [FAIL] Could not download {url}")
    return False

def resolve_bitly_and_download_gdrive(bitly_url, target_path):
    if os.path.exists(target_path) and os.path.getsize(target_path) > 1024:
        print(f"  [SKIP] Already exists ({os.path.getsize(target_path):,} bytes): {os.path.basename(target_path)}")
        return True

    try:
        req = urllib.request.Request(bitly_url, headers=HEADERS)
        with urllib.request.urlopen(req, timeout=15, context=SSL_CTX) as resp:
            final_url = resp.url
            
        m = re.search(r'/d/([a-zA-Z0-9_-]+)', final_url)
        if not m:
            print(f"  [WARN] Could not extract Google Drive file ID from {final_url}")
            return False
            
        file_id = m.group(1)
        direct_url = f"https://drive.usercontent.google.com/download?id={file_id}&export=download&authuser=0"
        return download_file(direct_url, target_path)
    except Exception as e:
        print(f"  [FAIL] Bitly resolution error for {bitly_url}: {e}")
        return False

def download_session(session_slug, folder_label):
    print(f"\n==================================================")
    print(f" DOWNLOADING {folder_label.upper()} CHAPTERWISE PYQs")
    print(f"==================================================")
    
    subjects = [
        ('physics', 'Physics'),
        ('chemistry', 'Chemistry'),
        ('maths', 'Mathematics')
    ]
    
    session_dir = os.path.join(MATHONGO_DIR, folder_label)
    
    total_downloaded = 0
    for subj_slug, subj_name in subjects:
        url = f"https://www.mathongo.com/iit-jee/jee-main-{subj_slug}-chapter-wise-questions-with-solutions-{session_slug}"
        print(f"\nFetching {subj_name} for {folder_label} from {url}...")
        try:
            req = urllib.request.Request(url, headers=HEADERS)
            html = urllib.request.urlopen(req, timeout=15, context=SSL_CTX).read().decode('utf-8', errors='ignore')
            rows = re.findall(r'<tr[^>]*>(.*?)</tr>', html, re.S)
        except Exception as e:
            print(f"  Error fetching {url}: {e}")
            continue

        subj_dir = os.path.join(session_dir, subj_name)
        os.makedirs(subj_dir, exist_ok=True)
        
        count = 0
        for r in rows:
            cells = re.findall(r'<td[^>]*>(.*?)</td>', r, re.S)
            if len(cells) >= 2:
                chap_name = re.sub(r'<[^>]+>', '', cells[0]).strip()
                if not chap_name or chap_name.lower() in ('chapter', 'download'):
                    continue
                link_m = re.search(r'href=[\x27\x22]([^\x27\x22]+)[\x27\x22]', cells[1])
                if link_m:
                    bitly_url = link_m.group(1).strip()
                    file_name = f"{safe_filename(chap_name)}_{folder_label}_PYQ.pdf"
                    target_path = os.path.join(subj_dir, file_name)
                    print(f"Downloading {subj_name} -> {chap_name}...")
                    if resolve_bitly_and_download_gdrive(bitly_url, target_path):
                        count += 1
                    time.sleep(0.4)

        print(f"Finished {count} chapters for {subj_name} ({folder_label}).")
        total_downloaded += count

    print(f"Total downloaded for {folder_label}: {total_downloaded}")

def export_all_96_marks_banks():
    print("\n==================================================")
    print(" RE-EXPORTING ALL 96 MARKS CHAPTERWISE PYQ BANKS")
    print("==================================================")
    
    import database
    from marks_basic_questions import MARKS_BASIC_QUESTIONS
    from seed_data import SYLLABUS

    marks_by_chap = {}
    for q in MARKS_BASIC_QUESTIONS:
        ch = q.get('chapter', '')
        if ch:
            marks_by_chap.setdefault(ch, []).append(q)

    conn = database.get_connection()
    db_rows = conn.execute('''
        SELECT c.subject, c.name as chapter_name, q.*
        FROM questions q
        JOIN chapters c ON q.chapter_id = c.id
    ''').fetchall()
    
    db_by_chap = {}
    for row in db_rows:
        r = dict(row)
        ch = r.get('chapter_name', '')
        if ch:
            db_by_chap.setdefault(ch, []).append(r)

    grouped = {}
    for item in SYLLABUS:
        s = item.get('subject', 'General')
        ch = item.get('chapter', '')
        if ch:
            grouped.setdefault(s, []).append((ch, item.get('topics', [])))

    total_exported = 0
    for subj, chapters in grouped.items():
        subj_dir = os.path.join(MARKS_DIR, subj)
        os.makedirs(subj_dir, exist_ok=True)
        print(f"\nExporting {subj} PYQ Banks ({len(chapters)} chapters)...")
        
        for ch, topics in chapters:
            filename = f"{safe_filename(ch)}_Marks_PYQ_Bank.md"
            filepath = os.path.join(subj_dir, filename)
            
            seen_questions = set()
            q_list = []
            
            # Add Marks basic questions first
            for mq in marks_by_chap.get(ch, []):
                q_text = mq.get('question', '').strip()
                if q_text and q_text not in seen_questions:
                    seen_questions.add(q_text)
                    q_list.append({
                        'topic': mq.get('topic', 'Marks Core Concept'),
                        'difficulty': mq.get('level', 'Basic to Foundation'),
                        'exam': 'JEE Main Marks App (Level 1)',
                        'question': q_text,
                        'options': mq.get('options', []),
                        'correct_index': mq.get('correct_index', 0),
                        'answer': mq.get('correct_answer', ''),
                        'solution': mq.get('explanation', '')
                    })

            # Add DB questions
            for r in db_by_chap.get(ch, []):
                q_text = r.get('question', '').strip()
                if q_text and q_text not in seen_questions:
                    seen_questions.add(q_text)
                    opts = []
                    try:
                        if r.get('options_json'):
                            opts = json.loads(r['options_json'])
                    except Exception:
                        pass
                    q_list.append({
                        'topic': r.get('topic_name', 'Core Topic'),
                        'difficulty': r.get('level', 'Basic to Medium'),
                        'exam': 'JEE Main / Advanced',
                        'question': q_text,
                        'options': opts,
                        'correct_index': r.get('correct_index', 0),
                        'answer': r.get('correct_answer', ''),
                        'solution': r.get('explanation', '')
                    })
                
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(f"# {ch} — High-Yield PYQs & Concept Master Bank\n\n")
                f.write(f"**Subject:** {subj}  \n")
                f.write(f"**Chapter:** {ch}  \n")
                f.write(f"**Source:** Marks App (MathonGo) & JEE Archive Repository  \n")
                f.write(f"**Total Problems Cataloged:** {len(q_list)} Core Problems with Full Solutions  \n\n")
                f.write("---\n\n")
                
                if q_list:
                    for idx, q in enumerate(q_list, 1):
                        f.write(f"### Problem {idx}: {q['topic']}\n\n")
                        f.write(f"**Difficulty:** `{q['difficulty']}` | **Target Exam:** `{q['exam']}`\n\n")
                        f.write(f"**Question:**\n> {q['question']}\n\n")
                        
                        opts = q.get('options', [])
                        if opts:
                            f.write("**Options:**\n")
                            for oi, opt in enumerate(opts):
                                f.write(f"- **({chr(65+oi)})** {opt}\n")
                            f.write("\n")
                            
                        c_idx = q.get('correct_index', 0)
                        c_letter = chr(65 + c_idx) if 0 <= c_idx < 26 else 'A'
                        f.write(f"**Correct Answer:** `({c_letter}) {q.get('answer', '')}`\n\n")
                        f.write("**Detailed Step-by-Step Solution & High-Yield Analysis:**\n")
                        f.write(f"{q.get('solution', 'Standard method applies. Verify dimensional consistency and limits.')}\n\n")
                        f.write("---\n\n")
                else:
                    f.write("### Essential Syllabus Subtopics & Core Focus Areas\n\n")
                    for top in topics:
                        f.write(f"- **{top}**: High-yield problem templates and recurring PYQ archetypes.\n")
                    f.write("\n")
                    f.write("*Note: Refer to the live web tracker at `https://atharvabalar6-crypto.github.io/jee-study-tracker/` for complete interactive sheets, dynamic practice tests, and full solutions.*\n")
            
            total_exported += 1
            
    print(f"Successfully exported {total_exported} chapter banks into {MARKS_DIR}")

def generate_catalog():
    print("\n==================================================")
    print(" GENERATING MASTER CATALOG (INDEX.md & README.md)")
    print("==================================================")
    
    all_files = []
    total_bytes = 0
    
    for root, dirs, files in os.walk(BASE_DIR):
        for file in files:
            if file in ("INDEX.md", "README.md"):
                continue
            fp = os.path.join(root, file)
            size = os.path.getsize(fp)
            rel = os.path.relpath(fp, BASE_DIR)
            all_files.append((rel, size))
            total_bytes += size

    all_files.sort(key=lambda x: x[0])
    total_mb = total_bytes / (1024 * 1024)
    print(f"Total files cataloged: {len(all_files)} ({total_mb:.2f} MB)")

    # Write INDEX.md
    index_path = os.path.join(BASE_DIR, "INDEX.md")
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write("# JEE Main & Advanced Complete PYQ & Marks Archive Index\n\n")
        f.write(f"- **Total Stored Files:** {len(all_files)}\n")
        f.write(f"- **Total Storage Size:** {total_mb:.2f} MB\n")
        f.write(f"- **Primary Directory:** `D:\\Projects\\code\\pvq`\n")
        f.write("- **Generated Date:** 2026\n\n")
        f.write("---\n\n")
        f.write("## File Catalog\n\n")
        f.write("| File Name / Relative Path | Size (KB) |\n")
        f.write("| :--- | :--- |\n")
        for rel, size in all_files:
            f.write(f"| `{rel}` | {size / 1024:.1f} KB |\n")

    # Write README.md
    readme_path = os.path.join(BASE_DIR, "README.md")
    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write("# JEE Main & Advanced Official Previous Year Questions (PYQ) & Marks Archive\n\n")
        f.write("Welcome to the comprehensive offline repository of official JEE Main and JEE Advanced previous year question papers, chapterwise compilations, official solutions, and curated Marks practice sets.\n\n")
        f.write("## Folder Structure Overview\n\n")
        f.write("```\n")
        f.write("D:\\Projects\\code\\pvq\\\n")
        f.write("├── 01_JEE_Advanced_Official_Papers/    # Official Papers (2007-2024 Paper 1 & 2, Hindi/English, Solutions, AAT)\n")
        f.write("├── 02_JEE_Main_Official_Papers/        # Official NTA Shift Papers, Curriculum, and Bulletins\n")
        f.write("├── 03_MathonGo_Chapterwise_PYQs/       # Chapterwise segregated PYQ PDFs from MathonGo (Jan 2024, Apr 2024, Jan 2023)\n")
        f.write("├── 04_Marks_Chapterwise_PYQ_Banks/     # Curated Marks App high-yield questions with full solutions for all 96 chapters\n")
        f.write("├── INDEX.md                            # Detailed file-by-file table of contents\n")
        f.write("└── README.md                           # Repository documentation\n")
        f.write("```\n\n")
        f.write("## Official Sources\n")
        f.write("- **JEE Advanced:** Official Joint Entrance Examination (Advanced) Board [`jeeadv.ac.in`](https://jeeadv.ac.in)\n")
        f.write("- **JEE Main:** National Testing Agency [`jeemain.nta.nic.in`](https://jeemain.nta.nic.in)\n")
        f.write("- **MathonGo:** Chapterwise segregation [`mathongo.com`](https://www.mathongo.com)\n")
        f.write("- **Marks App:** Question banks & solution metrics [`web.getmarks.app`](https://web.getmarks.app/)\n\n")
        f.write("## Live Web Revision Platform\n")
        f.write("Use alongside the interactive cheat-sheet revision platform with 8-page ruled notes for all 96 chapters:\n")
        f.write("- Live GitHub Pages: [https://atharvabalar6-crypto.github.io/jee-study-tracker/](https://atharvabalar6-crypto.github.io/jee-study-tracker/)\n")
        f.write("- Local Server: `http://localhost:5000`\n")

    print("Master catalog successfully updated!")

def main():
    print("=" * 60)
    print("DOWNLOADING ADDITIONAL MARKS / MATHONGO CHAPTERWISE PYQ SESSIONS")
    print(f"Target Directory: {BASE_DIR}")
    print("=" * 60)
    
    download_session("april-2024", "April_2024")
    download_session("january-2023", "January_2023")
    export_all_96_marks_banks()
    generate_catalog()
    
    print("\n" + "=" * 60)
    print("ALL EXTRA SESSIONS AND MARKS BANKS COMPLETED!")
    print("=" * 60)

if __name__ == "__main__":
    main()
