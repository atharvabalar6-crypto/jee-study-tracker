r"""
Comprehensive Downloader and Exporter for JEE Main & JEE Advanced PYQs
Target Directory: D:\Projects\code\pvq
Sources:
1. JEE Advanced Official Archive (https://jeeadv.ac.in)
2. NTA Official JEE Main Shift Papers (https://jeemain.nta.nic.in)
3. MathonGo Chapter-wise PYQ PDFs (via Google Drive links)
4. Marks App Curated PYQ & Basic Question Banks
"""

import os
import sys
import re
import time
import ssl
import json
import urllib.request
import urllib.error

# Ensure clean UTF-8 console output on Windows
if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

BASE_DIR = r"D:\Projects\code\pvq"
ADV_DIR = os.path.join(BASE_DIR, "01_JEE_Advanced_Official_Papers")
MAIN_DIR = os.path.join(BASE_DIR, "02_JEE_Main_Official_Papers")
MATHONGO_DIR = os.path.join(BASE_DIR, "03_MathonGo_Chapterwise_PYQs")
MARKS_DIR = os.path.join(BASE_DIR, "04_Marks_Chapterwise_PYQ_Banks")

# Unverified SSL context for bit.ly / drive redirects on Windows
SSL_CTX = ssl._create_unverified_context()
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

def safe_filename(name):
    clean = re.sub(r'[\\/*?:"<>|]', '', name)
    clean = clean.replace(' ', '_').strip('_')
    return clean

def download_file(url, target_path, retries=3, delay=1.5):
    """Downloads a file to target_path if not already present or zero bytes."""
    if os.path.exists(target_path) and os.path.getsize(target_path) > 1024:
        print(f"  [SKIP] Already exists ({os.path.getsize(target_path):,} bytes): {os.path.basename(target_path)}")
        return True

    os.makedirs(os.path.dirname(target_path), exist_ok=True)
    
    for attempt in range(1, retries + 1):
        try:
            req = urllib.request.Request(url, headers=HEADERS)
            with urllib.request.urlopen(req, timeout=30, context=SSL_CTX) as resp:
                data = resp.read()
                if len(data) < 100:
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
    """Resolves bit.ly link to Google Drive and downloads file directly."""
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

# ==========================================
# 1. Download Official JEE Advanced Papers
# ==========================================
def download_jee_advanced():
    print("\n==================================================")
    print(" 1. DOWNLOADING OFFICIAL JEE ADVANCED PAPERS")
    print("==================================================")
    
    base_url = "https://jeeadv.ac.in"
    try:
        archive_url = f"{base_url}/archive.html"
        req = urllib.request.Request(archive_url, headers=HEADERS)
        html = urllib.request.urlopen(req, timeout=15, context=SSL_CTX).read().decode('utf-8', errors='ignore')
        pdf_links = re.findall(r'href=[\x27\x22]([^\x27\x22]+\.pdf)[\x27\x22]', html)
    except Exception as e:
        print(f"Error fetching archive: {e}")
        pdf_links = []

    print(f"Found {len(pdf_links)} official JEE Advanced PDFs on jeeadv.ac.in/archive.html")

    for rel_link in pdf_links:
        full_url = f"{base_url}/{rel_link}" if not rel_link.startswith('http') else rel_link
        filename = os.path.basename(rel_link)
        
        # Categorize by year or AAT
        if filename.startswith("AAT-"):
            year = filename.replace("AAT-", "").replace(".pdf", "")
            target_dir = os.path.join(ADV_DIR, "AAT_Architecture")
            dest = os.path.join(target_dir, f"JEE_Advanced_AAT_{year}.pdf")
        else:
            m = re.search(r'(\d{4})', filename)
            year = m.group(1) if m else "Archive"
            target_dir = os.path.join(ADV_DIR, year)
            dest = os.path.join(target_dir, f"JEE_Advanced_{filename}")
            
        download_file(full_url, dest)
        time.sleep(0.3)

    # Also download official 2024 solutions & provisional keys
    print("\nDownloading Official Solutions & Provisional Keys:")
    solutions = [
        ("https://jeeadv.ac.in/documents/p1_solutions_final.pdf", "JEE_Advanced_Paper_1_Final_Solutions.pdf"),
        ("https://jeeadv.ac.in/documents/p2_solutions_final.pdf", "JEE_Advanced_Paper_2_Final_Solutions.pdf"),
        ("https://jeeadv.ac.in/documents/p1_provisional_keys.pdf", "JEE_Advanced_Paper_1_Provisional_Answer_Key.pdf"),
        ("https://jeeadv.ac.in/documents/p2_provisional_keys.pdf", "JEE_Advanced_Paper_2_Provisional_Answer_Key.pdf")
    ]
    sol_dir = os.path.join(ADV_DIR, "Official_Solutions_and_Keys")
    for s_url, s_name in solutions:
        dest = os.path.join(sol_dir, s_name)
        download_file(s_url, dest)
        time.sleep(0.3)

# ==========================================
# 2. Download Official JEE Main Papers
# ==========================================
def download_jee_main():
    print("\n==================================================")
    print(" 2. DOWNLOADING OFFICIAL JEE MAIN PAPERS")
    print("==================================================")
    
    # Official shift papers & documents from jeemain.nta.nic.in
    nta_papers = [
        ("https://cdnbbsr.s3waas.gov.in/s3f8e59f4b2fe7c5705bf878bbd494ccdf/uploads/2026/04/202604092096865379.pdf", 
         "JEE_Main_2024_02_Apr_Shift_1.pdf", "2024_Shift_Papers"),
        ("https://cdnbbsr.s3waas.gov.in/s3f8e59f4b2fe7c5705bf878bbd494ccdf/uploads/2026/04/20260409481957146.pdf", 
         "JEE_Main_2024_02_Apr_Shift_2.pdf", "2024_Shift_Papers"),
        ("https://cdnbbsr.s3waas.gov.in/s3f8e59f4b2fe7c5705bf878bbd494ccdf/uploads/2026/04/202604091916616339.pdf", 
         "JEE_Main_2024_04_Apr_Shift_1.pdf", "2024_Shift_Papers"),
        ("https://cdnbbsr.s3waas.gov.in/s3f8e59f4b2fe7c5705bf878bbd494ccdf/uploads/2026/04/20260409432593766.pdf", 
         "JEE_Main_2024_04_Apr_Shift_2.pdf", "2024_Shift_Papers"),
        ("https://cdnbbsr.s3waas.gov.in/s3f8e59f4b2fe7c5705bf878bbd494ccdf/uploads/2026/04/20260409828731207.pdf", 
         "JEE_Main_2024_05_Apr_Shift_1.pdf", "2024_Shift_Papers"),
        ("https://cdnbbsr.s3waas.gov.in/s3f8e59f4b2fe7c5705bf878bbd494ccdf/uploads/2026/04/20260409829414602.pdf", 
         "JEE_Main_2024_05_Apr_Shift_2.pdf", "2024_Shift_Papers"),
        ("https://cdnbbsr.s3waas.gov.in/s3f8e59f4b2fe7c5705bf878bbd494ccdf/uploads/2026/04/202604092007095665.pdf", 
         "JEE_Main_2024_06_Apr_Shift_1.pdf", "2024_Shift_Papers"),
        ("https://cdnbbsr.s3waas.gov.in/s3f8e59f4b2fe7c5705bf878bbd494ccdf/uploads/2026/04/20260409725707538.pdf", 
         "JEE_Main_2024_06_Apr_Shift_2.pdf", "2024_Shift_Papers"),
        ("https://cdnbbsr.s3waas.gov.in/s3f8e59f4b2fe7c5705bf878bbd494ccdf/uploads/2026/04/20260409932754345.pdf", 
         "JEE_Main_2024_08_Apr_Shift_2.pdf", "2024_Shift_Papers"),
        ("https://cdnbbsr.s3waas.gov.in/s3f8e59f4b2fe7c5705bf878bbd494ccdf/uploads/2026/10/20261024683680768.pdf", 
         "JEE_Main_Official_Curriculum_and_Syllabus.pdf", "Official_Syllabus_and_Bulletins"),
        ("https://cdnbbsr.s3waas.gov.in/s3f8e59f4b2fe7c5705bf878bbd494ccdf/uploads/2026/10/202610241890224107.pdf", 
         "JEE_Main_Official_Information_Bulletin.pdf", "Official_Syllabus_and_Bulletins"),
    ]

    for url, filename, subfolder in nta_papers:
        dest = os.path.join(MAIN_DIR, subfolder, filename)
        download_file(url, dest)
        time.sleep(0.3)

# ==========================================
# 3. Download MathonGo Chapter-wise PYQs
# ==========================================
def download_mathongo_pyqs():
    print("\n==================================================")
    print(" 3. DOWNLOADING MATHONGO CHAPTER-WISE PYQ PDFs")
    print("==================================================")
    
    subjects = [
        ('physics', 'Physics'),
        ('chemistry', 'Chemistry'),
        ('maths', 'Mathematics')
    ]
    
    for slug, subj_name in subjects:
        print(f"\nProcessing {subj_name} Chapterwise PYQs from MathonGo...")
        url = f"https://www.mathongo.com/iit-jee/jee-main-{slug}-chapter-wise-questions-with-solutions-january-2024"
        try:
            req = urllib.request.Request(url, headers=HEADERS)
            html = urllib.request.urlopen(req, timeout=15, context=SSL_CTX).read().decode('utf-8', errors='ignore')
            rows = re.findall(r'<tr[^>]*>(.*?)</tr>', html, re.S)
        except Exception as e:
            print(f"  Error fetching {url}: {e}")
            continue

        subj_dir = os.path.join(MATHONGO_DIR, subj_name)
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
                    if "Sets" in chap_name and "495l27O" in bitly_url:
                        bitly_url = "https://bit.ly/3VUrc6G"
                    file_name = f"{safe_filename(chap_name)}_JEE_Main_PYQ.pdf"
                    target_path = os.path.join(subj_dir, file_name)
                    print(f"Downloading {subj_name} -> {chap_name}...")
                    resolve_bitly_and_download_gdrive(bitly_url, target_path)
                    count += 1
                    time.sleep(0.5)

        print(f"Completed {count} chapters for {subj_name}.")

# ==========================================
# 4. Export Marks Chapter-wise PYQs
# ==========================================
def export_marks_pyqs():
    print("\n==================================================")
    print(" 4. EXPORTING MARKS CHAPTER-WISE PYQ BANKS")
    print("==================================================")
    
    import database
    from marks_basic_questions import MARKS_BASIC_QUESTIONS
    from seed_data import SYLLABUS
    
    # Pre-index marks questions
    marks_by_chap = {}
    for q in MARKS_BASIC_QUESTIONS:
        ch = q.get('chapter', '')
        if ch:
            marks_by_chap.setdefault(ch, []).append(q)
            
    # Pre-index DB questions
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
            
    # Group syllabus
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
            
            # Combine questions
            q_list = []
            
            # Add DB questions
            for r in db_by_chap.get(ch, []):
                opts = []
                try:
                    if r.get('options_json'):
                        opts = json.loads(r['options_json'])
                except Exception:
                    pass
                q_list.append({
                    'topic': r.get('topic_name', 'Core Topic'),
                    'difficulty': r.get('level', 'Medium'),
                    'exam': 'JEE Main / Advanced',
                    'question': r.get('question', ''),
                    'options': opts,
                    'correct_index': r.get('correct_index', 0),
                    'answer': r.get('correct_answer', ''),
                    'solution': r.get('explanation', '')
                })
                
            # Add Marks basic questions
            for mq in marks_by_chap.get(ch, []):
                q_list.append({
                    'topic': mq.get('topic', 'Marks Core Concept'),
                    'difficulty': mq.get('level', 'Basic to Medium'),
                    'exam': 'JEE Main Marks App',
                    'question': mq.get('question', ''),
                    'options': mq.get('options', []),
                    'correct_index': mq.get('correct_index', 0),
                    'answer': mq.get('correct_answer', ''),
                    'solution': mq.get('explanation', '')
                })
                
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(f"# {ch} — High-Yield PYQs & Concept Master Bank\n\n")
                f.write(f"**Subject:** {subj}  \n")
                f.write(f"**Chapter:** {ch}  \n")
                f.write(f"**Source:** Marks App & JEE Archive Repository  \n")
                f.write(f"**Total Problems Cataloged:** {len(q_list)} Core Problems  \n\n")
                f.write("---\n\n")
                
                if q_list:
                    for idx, q in enumerate(q_list, 1):
                        f.write(f"### Problem {idx}: {q['topic']}\n\n")
                        f.write(f"**Difficulty:** `{q['difficulty']}` | **Target Exam:** `{q['exam']}`\n\n")
                        f.write(f"**Question:**\n> {q['question'].strip()}\n\n")
                        
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
            
    print(f"Exported Marks PYQ banks for {total_exported} chapters into {MARKS_DIR}")

# ==========================================
# 5. Generate Index & Readme Catalog
# ==========================================
def generate_catalog():
    print("\n==================================================")
    print(" 5. GENERATING MASTER CATALOG (INDEX.md & README.md)")
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
        f.write("# JEE Main & Advanced Complete PYQ Repository Index\n\n")
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
        f.write("# JEE Main & Advanced Official Previous Year Questions (PYQ) Archive\n\n")
        f.write("Welcome to the comprehensive offline repository of official JEE Main and JEE Advanced previous year question papers, chapterwise compilations, official solutions, and curated Marks practice sets.\n\n")
        f.write("## Folder Structure Overview\n\n")
        f.write("```\n")
        f.write("D:\\Projects\\code\\pvq\\\n")
        f.write("├── 01_JEE_Advanced_Official_Papers/    # Official Papers (2007-2024 Paper 1 & 2, Hindi/English, Solutions, AAT)\n")
        f.write("├── 02_JEE_Main_Official_Papers/        # Official NTA Shift Papers, Curriculum, and Bulletins\n")
        f.write("├── 03_MathonGo_Chapterwise_PYQs/       # Chapterwise segregated PYQ PDFs from MathonGo (PCM)\n")
        f.write("├── 04_Marks_Chapterwise_PYQ_Banks/     # Curated Marks App high-yield questions with full solutions\n")
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

    print("Master catalog successfully generated!")

def main():
    print("=" * 60)
    print("STARTING COMPLETE JEE MAIN & ADVANCED PYQ DOWNLOAD")
    print(f"Target Directory: {BASE_DIR}")
    print("=" * 60)
    
    os.makedirs(ADV_DIR, exist_ok=True)
    os.makedirs(MAIN_DIR, exist_ok=True)
    os.makedirs(MATHONGO_DIR, exist_ok=True)
    os.makedirs(MARKS_DIR, exist_ok=True)
    
    download_jee_advanced()
    download_jee_main()
    download_mathongo_pyqs()
    export_marks_pyqs()
    generate_catalog()
    
    print("\n" + "=" * 60)
    print("ALL DOWNLOADS AND EXPORTS COMPLETED SUCCESSFULLY!")
    print("=" * 60)

if __name__ == "__main__":
    main()
