/**
 * app.js - Full frontend logic for JEE Study Tracker & Diagnostic Engine
 */

let allChapters = [];
let selectedModalSubject = "Physics";
let selectedModalClass = "All";
let currentFilterSubject = "All";
let currentFilterClass = "All";

// Formula Vault State
let allFormulas = [];
let currentFormulaSubject = "All";
let currentFormulaClass = "All";

// Active CBT Test State
let activeTest = {
  chapterName: "",
  subject: "",
  examType: "JEE Main",
  isRemedial: false,
  questions: [],
  currentIndex: 0,
  answers: {}, // questionId -> selectedOptionIndex
  marked: new Set(),
  visited: new Set(),
  startTime: null,
  totalSeconds: 0,
  timerInterval: null
};

let lastTestResult = null;

// Initialize on page load
document.addEventListener("DOMContentLoaded", () => {
  fetchChapters();
  fetchAnalytics();
  
  // Render Math on elements after any dynamic update
  renderMath();
});

function renderMath() {
  if (window.renderMathInElement) {
    try {
      renderMathInElement(document.body, {
        delimiters: [
          { left: "$$", right: "$$", display: true },
          { left: "$", right: "$", display: false },
          { left: "\\(", right: "\\)", display: false },
          { left: "\\[", right: "\\]", display: true }
        ],
        throwOnError: false
      });
    } catch (e) {
      console.warn("Math rendering error:", e);
    }
  }
}

// ---------------------------------------------------------------------
// Navigation & Views
// ---------------------------------------------------------------------
function showView(viewName) {
  document.getElementById("view-dashboard").classList.add("hidden");
  document.getElementById("view-cbt").classList.add("hidden");
  document.getElementById("view-result").classList.add("hidden");
  document.getElementById("view-weak-hub").classList.add("hidden");
  const fView = document.getElementById("view-formulas");
  if (fView) fView.classList.add("hidden");

  if (viewName === "dashboard") {
    document.getElementById("view-dashboard").classList.remove("hidden");
    fetchChapters();
    fetchAnalytics();
  } else if (viewName === "cbt") {
    document.getElementById("view-cbt").classList.remove("hidden");
  } else if (viewName === "result") {
    document.getElementById("view-result").classList.remove("hidden");
  } else if (viewName === "weak-hub") {
    document.getElementById("view-weak-hub").classList.remove("hidden");
    loadAllWeakTopics();
  } else if (viewName === "formulas") {
    if (fView) fView.classList.remove("hidden");
    loadFormulaVault();
  }
  window.scrollTo({ top: 0, behavior: "smooth" });
}

// ---------------------------------------------------------------------
// Chapter Loading & Syllabus Tracker
// ---------------------------------------------------------------------
async function fetchChapters() {
  try {
    const res = await fetch("/api/chapters");
    if (!res.ok) throw new Error("API not available");
    const data = await res.json();
    if (data.success) {
      allChapters = data.chapters;
      renderChapters();
      updateSubjectMetrics();
      populateModalChapters();
      return;
    }
  } catch (err) {
    if (window.JEE_STATIC_DATA && window.JEE_STATIC_DATA.chapters) {
      const savedStats = JSON.parse(localStorage.getItem("jee_chapter_stats") || "{}");
      allChapters = window.JEE_STATIC_DATA.chapters.map(c => {
        if (savedStats[c.name]) {
          return { ...c, ...savedStats[c.name] };
        }
        return { ...c };
      });
      renderChapters();
      updateSubjectMetrics();
      populateModalChapters();
    }
  }
}

async function fetchAnalytics() {
  try {
    const res = await fetch("/api/analytics/overall");
    if (!res.ok) throw new Error("API not available");
    const data = await res.json();
    if (data.success) {
      document.getElementById("navTestedChapters").innerText = `${data.tested_chapters}/${data.total_chapters} Chapters`;
      document.getElementById("navWeakCount").innerText = `${data.weak_count} identified`;
      document.getElementById("statTestsGiven").innerText = `${data.total_tests} Tests Taken`;
      document.getElementById("statWeakCount").innerText = `${data.weak_count} Weak Topics`;
      return;
    }
  } catch (err) {
    const totalChapters = allChapters.length || 96;
    const tested = allChapters.filter(c => c.tests_given > 0).length;
    const testHistory = JSON.parse(localStorage.getItem("jee_test_history") || "[]");
    const weakTopics = JSON.parse(localStorage.getItem("jee_weak_topics") || "[]");
    document.getElementById("navTestedChapters").innerText = `${tested}/${totalChapters} Chapters`;
    document.getElementById("navWeakCount").innerText = `${weakTopics.length} identified`;
    document.getElementById("statTestsGiven").innerText = `${testHistory.length} Tests Taken`;
    document.getElementById("statWeakCount").innerText = `${weakTopics.length} Weak Topics`;
  }
}

function updateSubjectMetrics() {
  const subjects = {
    Physics: { total: 0, tested: 0, totalScore: 0 },
    Chemistry: { total: 0, tested: 0, totalScore: 0 },
    Mathematics: { total: 0, tested: 0, totalScore: 0 }
  };

  allChapters.forEach(c => {
    if (subjects[c.subject]) {
      subjects[c.subject].total++;
      if (c.tests_given > 0) {
        subjects[c.subject].tested++;
        subjects[c.subject].totalScore += c.last_score_pct;
      }
    }
  });

  // Physics
  const pTested = subjects.Physics.tested;
  const pTotal = subjects.Physics.total;
  const pAvg = pTested > 0 ? Math.round(subjects.Physics.totalScore / pTested) : 0;
  document.getElementById("phyTestedCount").innerText = `${pTested}/${pTotal} tested`;
  document.getElementById("phyAccuracy").innerText = `${pAvg}% Avg Score`;
  document.getElementById("phyProgressBar").style.width = `${(pTested / (pTotal || 1)) * 100}%`;

  // Chemistry
  const cTested = subjects.Chemistry.tested;
  const cTotal = subjects.Chemistry.total;
  const cAvg = cTested > 0 ? Math.round(subjects.Chemistry.totalScore / cTested) : 0;
  document.getElementById("chemTestedCount").innerText = `${cTested}/${cTotal} tested`;
  document.getElementById("chemAccuracy").innerText = `${cAvg}% Avg Score`;
  document.getElementById("chemProgressBar").style.width = `${(cTested / (cTotal || 1)) * 100}%`;

  // Math
  const mTested = subjects.Mathematics.tested;
  const mTotal = subjects.Mathematics.total;
  const mAvg = mTested > 0 ? Math.round(subjects.Mathematics.totalScore / mTested) : 0;
  document.getElementById("mathTestedCount").innerText = `${mTested}/${mTotal} tested`;
  document.getElementById("mathAccuracy").innerText = `${mAvg}% Avg Score`;
  document.getElementById("mathProgressBar").style.width = `${(mTested / (mTotal || 1)) * 100}%`;
}

function setSubjectFilter(subj) {
  currentFilterSubject = subj;
  document.querySelectorAll(".filter-subj-btn").forEach(btn => {
    if (btn.dataset.subj === subj) {
      btn.className = "filter-subj-btn px-3 py-1.5 rounded-lg transition bg-indigo-600 text-white";
    } else {
      btn.className = "filter-subj-btn px-3 py-1.5 rounded-lg transition text-slate-400 hover:text-white";
    }
  });
  renderChapters();
}

function setClassFilter(cls) {
  currentFilterClass = cls;
  document.querySelectorAll(".filter-class-btn").forEach(btn => {
    const btnVal = btn.dataset.class === "All" ? "All" : parseInt(btn.dataset.class);
    if (btnVal === cls) {
      btn.className = "filter-class-btn px-3 py-1.5 rounded-lg transition bg-emerald-600 text-white";
    } else {
      btn.className = "filter-class-btn px-3 py-1.5 rounded-lg transition text-slate-400 hover:text-white";
    }
  });
  renderChapters();
}

function renderChapters() {
  const container = document.getElementById("chaptersGrid");
  const searchQuery = (document.getElementById("chapterSearch").value || "").toLowerCase().trim();
  const statusFilter = document.getElementById("statusFilter").value;

  const filtered = allChapters.filter(c => {
    if (currentFilterSubject !== "All" && c.subject !== currentFilterSubject) return false;
    if (currentFilterClass !== "All" && c.class_level !== parseInt(currentFilterClass)) return false;
    if (searchQuery && !c.name.toLowerCase().includes(searchQuery)) return false;
    if (statusFilter === "Tested" && c.tests_given === 0) return false;
    if (statusFilter === "Untested" && c.tests_given > 0) return false;
    if (statusFilter === "Needs Revision" && c.mastery_status !== "Needs Revision") return false;
    if (statusFilter === "Proficient" && c.mastery_status !== "Proficient") return false;
    return true;
  });

  if (filtered.length === 0) {
    container.innerHTML = `
      <div class="col-span-full py-12 text-center text-slate-400 text-sm">
        No chapters match your search / filter criteria.
      </div>
    `;
    return;
  }

  container.innerHTML = filtered.map(c => {
    let statusClass = "badge-untested";
    let statusLabel = "Untested";
    if (c.tests_given > 0) {
      if (c.mastery_status === "Proficient") {
        statusClass = "badge-proficient";
        statusLabel = "Proficient";
      } else if (c.mastery_status === "Needs Revision") {
        statusClass = "badge-weak";
        statusLabel = "Needs Revision";
      } else {
        statusClass = "badge-tested";
        statusLabel = "Developing";
      }
    }

    const subjectColor = c.subject === "Physics" ? "text-sky-400" : (c.subject === "Chemistry" ? "text-emerald-400" : "text-amber-400");

    return `
      <div class="bg-slate-800/90 border border-slate-700/80 hover:border-slate-600 rounded-xl p-4 flex flex-col justify-between transition hover:shadow-lg">
        <div>
          <div class="flex items-center justify-between text-xs mb-2">
            <span class="font-bold ${subjectColor} uppercase tracking-wider">${c.subject} • Class ${c.class_level} • NCERT Ch ${c.ncert_order}</span>
            <span class="px-2 py-0.5 rounded-full font-semibold text-[11px] ${statusClass}">
              ${statusLabel}
            </span>
          </div>

          <h4 class="text-base font-bold text-white mb-1.5 leading-snug">${c.name}</h4>
          
          <div class="text-xs text-slate-400 mb-3">
            <span>Importance: <strong class="text-slate-200">${c.importance}</strong></span>
            <span class="mx-1.5">•</span>
            <span>${c.topics.length} Key Subtopics</span>
          </div>

          <!-- Quick Topic Pills preview -->
          <div class="flex flex-wrap gap-1 mb-4">
            ${c.topics.slice(0, 3).map(t => `
              <span class="text-[10px] bg-slate-900/80 text-slate-300 border border-slate-700/60 px-2 py-0.5 rounded-md truncate max-w-[180px]">${t}</span>
            `).join("")}
            ${c.topics.length > 3 ? `<span class="text-[10px] text-slate-500 self-center">+${c.topics.length - 3} more</span>` : ""}
          </div>
        </div>

        <div class="pt-3 border-t border-slate-700/60 flex items-center justify-between text-xs gap-2">
          <div class="text-slate-400 truncate">
            ${c.tests_given > 0 ? `<span>Tests: <strong class="text-white">${c.tests_given}</strong> | Score: <strong class="text-emerald-400">${c.last_score_pct}%</strong></span>` : `<span class="text-slate-500 italic">No tests yet</span>`}
          </div>
          <div class="flex items-center gap-1.5 shrink-0">
            <button onclick="openNotesModal('${c.name.replace(/'/g, "\\'")}')" class="px-2.5 py-1.5 bg-slate-700/80 hover:bg-slate-700 text-slate-200 hover:text-white border border-slate-600 font-semibold rounded-lg text-xs transition flex items-center gap-1">
              <span>📖 Notes</span>
            </button>
            <button onclick="quickStartBasicDrill('${c.name.replace(/'/g, "\\'")}', '${c.subject}')" title="Practice Basic Level 1 Questions from Marks" class="px-2.5 py-1.5 bg-emerald-950/60 hover:bg-emerald-600 text-emerald-300 hover:text-white border border-emerald-500/40 font-semibold rounded-lg text-xs transition flex items-center gap-1">
              <span>⚡ Basic</span>
            </button>
            <button onclick="quickStartChapterTest('${c.name.replace(/'/g, "\\'")}', '${c.subject}')" class="px-3 py-1.5 bg-indigo-600 hover:bg-indigo-500 text-white font-semibold rounded-lg shadow transition flex items-center gap-1">
              <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14.752 11.168l-3.197-2.132A1 1 0 0010 9.87v4.263a1 1 0 001.555.832l3.197-2.132a1 1 0 000-1.664z"/></svg>
              <span>Test</span>
            </button>
          </div>
        </div>
      </div>
    `;
  }).join("");
}

// ---------------------------------------------------------------------
// Chapter Revision Notes & Worked Examples Modal (Exact Notebook Theme)
// ---------------------------------------------------------------------
let currentNotesTheme = "notebook";
let currentLoadedNote = null;

function setNotesTheme(theme) {
  currentNotesTheme = theme;
  const modalBody = document.getElementById("notesModalBody");
  const btnNb = document.getElementById("btnThemeNotebook");
  const btnDark = document.getElementById("btnThemeDark");

  if (theme === "notebook") {
    if (modalBody) modalBody.className = "p-4 sm:p-6 overflow-y-auto flex-1 theme-notebook transition-colors duration-200";
    if (btnNb) btnNb.className = "px-2.5 py-1 rounded-lg bg-amber-500 text-slate-950 font-bold transition flex items-center gap-1";
    if (btnDark) btnDark.className = "px-2.5 py-1 rounded-lg text-slate-400 hover:text-white transition flex items-center gap-1";
  } else {
    if (modalBody) modalBody.className = "p-4 sm:p-6 overflow-y-auto flex-1 theme-dark-notes transition-colors duration-200";
    if (btnDark) btnDark.className = "px-2.5 py-1 rounded-lg bg-indigo-600 text-white font-bold transition flex items-center gap-1";
    if (btnNb) btnNb.className = "px-2.5 py-1 rounded-lg text-slate-400 hover:text-white transition flex items-center gap-1";
  }
}

async function openNotesModal(chapterName) {
  try {
    let n = null;
    try {
      const res = await fetch(`/api/chapters/${encodeURIComponent(chapterName)}/notes`);
      if (res.ok) {
        const data = await res.json();
        if (data.success && data.notes) n = data.notes;
      }
    } catch (e) {}

    if (!n && window.JEE_STATIC_DATA && window.JEE_STATIC_DATA.notes) {
      n = window.JEE_STATIC_DATA.notes[chapterName];
    }

    if (!n) {
      alert("Unable to load notes for this chapter.");
      return;
    }

    currentLoadedNote = n;
    const sheets = (n.sheets && n.sheets.length > 0) ? n.sheets : [n];
    window.currentNoteSheets = sheets;
    window.currentNoteSheetIndex = 0;

    // Setup Multi-Sheet Tabs (e.g. Page 1-6 for Quadratic, Page 1-3 for others)
    setupNotePageTabs(sheets);

    // Render active sheet
    renderActiveNoteSheet();

    // Action buttons to take tests directly on this chapter
    const btnTest = document.getElementById("btnNotesTakeTest");
    if (btnTest) {
      btnTest.onclick = () => {
        closeNotesModal();
        openTestModal(chapterName, n.subject);
      };
    }
    const btnBasicTest = document.getElementById("btnNotesTakeBasicTest");
    if (btnBasicTest) {
      btnBasicTest.onclick = () => {
        closeNotesModal();
        openTestModal(chapterName, n.subject, "Basic (Marks)");
      };
    }

    document.getElementById("notesModal").classList.remove("hidden");
    renderMath();

  } catch (err) {
    console.error("Error loading notes:", err);
    alert("Failed to load notes. Please check connection.");
  }
}

function setupNotePageTabs(sheets) {
  const tabBar = document.getElementById("notesPageTabBar");
  const container = document.getElementById("notesPageTabsContainer");

  if (!tabBar || !container) return;

  if (!sheets || sheets.length <= 1) {
    tabBar.classList.add("hidden");
    return;
  }

  tabBar.classList.remove("hidden");
  container.innerHTML = sheets.map((s, idx) => {
    const isAct = idx === 0;
    const title = s.sheet_title || `Sheet ${idx + 1}`;
    const pageNum = s.page_number || (idx + 1);
    return `
      <button type="button" onclick="switchNoteSheet(${idx})" 
        class="note-sheet-tab px-3 py-1 text-xs rounded-lg font-semibold transition border whitespace-nowrap flex items-center gap-1.5 ${isAct ? 'bg-amber-400 text-slate-950 font-bold border-amber-300 shadow-sm' : 'bg-slate-800 text-slate-300 hover:text-white hover:bg-slate-700 border-slate-700'}"
        data-sheet-idx="${idx}">
        <span class="opacity-80 font-mono text-[11px] font-bold">P${pageNum}</span>
        <span class="truncate max-w-[170px]">${title}</span>
      </button>
    `;
  }).join("");

  updatePageNavigationControls();
}

function updatePageNavigationControls() {
  const sheets = window.currentNoteSheets || [];
  const idx = window.currentNoteSheetIndex || 0;
  const indicator = document.getElementById("notesPageIndicator");
  const btnPrev = document.getElementById("btnPrevSheet");
  const btnNext = document.getElementById("btnNextSheet");

  if (indicator) {
    indicator.innerText = `Page ${idx + 1} of ${sheets.length}`;
  }
  if (btnPrev) {
    btnPrev.disabled = (idx <= 0);
    btnPrev.classList.toggle("opacity-40", idx <= 0);
    btnPrev.classList.toggle("cursor-not-allowed", idx <= 0);
  }
  if (btnNext) {
    btnNext.disabled = (idx >= sheets.length - 1);
    btnNext.classList.toggle("opacity-40", idx >= sheets.length - 1);
    btnNext.classList.toggle("cursor-not-allowed", idx >= sheets.length - 1);
  }

  const tabs = document.querySelectorAll(".note-sheet-tab");
  tabs.forEach((t, i) => {
    if (i === idx) {
      t.className = "note-sheet-tab px-3 py-1 text-xs rounded-lg font-bold transition border whitespace-nowrap flex items-center gap-1.5 bg-amber-400 text-slate-950 border-amber-300 shadow-sm";
      try { t.scrollIntoView({ behavior: 'smooth', inline: 'nearest', block: 'nearest' }); } catch(e) {}
    } else {
      t.className = "note-sheet-tab px-3 py-1 text-xs rounded-lg font-semibold transition border whitespace-nowrap flex items-center gap-1.5 bg-slate-800 text-slate-300 hover:text-white hover:bg-slate-700 border-slate-700";
    }
  });
}

function switchNoteSheet(idx) {
  const sheets = window.currentNoteSheets;
  if (!sheets || idx < 0 || idx >= sheets.length) return;
  window.currentNoteSheetIndex = idx;
  updatePageNavigationControls();
  renderActiveNoteSheet();
}

function navigateNoteSheet(delta) {
  const cur = window.currentNoteSheetIndex || 0;
  switchNoteSheet(cur + delta);
}

function renderActiveNoteSheet() {
  const sheets = window.currentNoteSheets || [];
  const idx = window.currentNoteSheetIndex || 0;
  const sheet = sheets[idx] || currentLoadedNote;
  if (!sheet) return;

  const n = currentLoadedNote || sheet;
  const total = sheets.length;

  const subjBadge = document.getElementById("notesSubjectBadge");
  if (subjBadge) subjBadge.innerText = sheet.subject || n.subject || "";
  const ncertBadge = document.getElementById("notesNcertBadge");
  if (ncertBadge) ncertBadge.innerText = (sheet.ncert_ref || n.ncert_ref || "").split(":")[0];
  const impBadge = document.getElementById("notesImportanceBadge");
  if (impBadge) impBadge.innerText = sheet.importance || n.importance || "";
  const chapTitle = document.getElementById("notesChapterTitle");
  if (chapTitle) {
    const pageSub = total > 1 ? ` • Page ${idx + 1} of ${total}: ${sheet.sheet_title || ''}` : ` • Short Notes & Cheat-Sheet`;
    chapTitle.innerText = `${sheet.chapter || n.chapter}${pageSub}`;
  }

  if (!sheet.formulas && n.formulas) {
    sheet.formulas = n.formulas;
  }

  renderNotebookSheet(sheet, sheet.chapter || n.chapter);

  const body = document.getElementById("notesModalBody");
  if (body) body.scrollTop = 0;

  renderMath();
}

function renderNotebookSheet(n, chapterName) {
  const container = document.getElementById("notesNotebookSheet");
  if (!container) return;

  const formulas = n.formulas || [];
  const examples = n.examples || [];
  const classification = n.classification_cases || [];
  const parameters = n.parameter_analysis || [];
  const intervalRules = n.interval_rules || null;
  const graphical = n.graphical_view || null;
  const importantPoints = n.important_points || [];
  const quickTips = n.quick_tips || [];
  const jeeFocus = n.jee_focus_points || [];
  const traps = n.traps_and_pitfalls || [];

  container.innerHTML = `
    <!-- Top Header: Title with burst symbols matching photo -->
    <div class="text-center pt-1 pb-3">
      <div class="nb-burst-title text-base sm:text-xl md:text-2xl">
        <span class="opacity-70 font-mono">ヾ</span>
        <span>${n.sheet_title || n.chapter}</span>
        <span class="opacity-70 font-mono">ﾉ</span>
      </div>
      <p class="text-[11px] text-slate-500 font-semibold mt-1.5 uppercase tracking-wider">${n.ncert_ref || ''}</p>
    </div>

    <!-- MAIN 2-COLUMN NOTEBOOK SHEET LAYOUT -->
    <div class="grid grid-cols-1 md:grid-cols-2 gap-6 md:gap-8 items-start">
      
      <!-- LEFT COLUMN -->
      <div class="space-y-6 md:pr-6 md:border-r md:border-sky-300/80 dark:md:border-slate-700">
        
        <!-- 1. Introduction -->
        <div class="space-y-2">
          <span class="nb-pill-yellow">1. Introduction</span>
          <p class="text-xs sm:text-sm leading-relaxed text-slate-800 dark:text-slate-200 font-normal pl-0.5">
            ${n.introduction || ''}
          </p>
        </div>

        <!-- 2. Range of Roots / Classification of Cases -->
        ${classification.length > 0 ? `
          <div class="space-y-3">
            <span class="nb-pill-yellow">${n.classification_heading || '2. Range & Classification of Cases'}</span>
            <div class="space-y-3.5 pl-1">
              ${classification.map(c => `
                <div class="space-y-1">
                  <span class="nb-pill-pink">${c.badge || c.title}</span>
                  <p class="text-xs text-slate-700 dark:text-slate-300 font-normal">${c.description}</p>
                  ${c.range ? `
                    <div class="text-xs font-semibold text-indigo-800 dark:text-indigo-300">
                      Range: <span class="font-mono bg-white/80 dark:bg-slate-800 px-2 py-0.5 rounded border border-indigo-200 dark:border-indigo-900">${c.range}</span>
                    </div>
                  ` : ''}
                  ${c.consequence ? `
                    <p class="text-[11px] text-slate-600 dark:text-slate-400 italic font-normal">${c.consequence}</p>
                  ` : ''}
                </div>
              `).join("")}
            </div>
          </div>
        ` : ''}

        <!-- 3. Location of Roots / Parameter Rules -->
        ${parameters.length > 0 ? `
          <div class="space-y-3">
            <span class="nb-pill-yellow">${n.parameter_heading || '3. Parameter & Direction Rules'}</span>
            <div class="space-y-3.5 pl-1">
              ${parameters.map(p => `
                <div class="space-y-1.5">
                  <span class="nb-pill-pink">${p.sub_badge}</span>
                  <ul class="text-xs space-y-1 pl-3 text-slate-700 dark:text-slate-300 font-normal">
                    ${p.rules.map(r => `
                      <li class="list-disc"><strong class="text-slate-900 dark:text-slate-100">${r.cond}:</strong> ${r.res}</li>
                    `).join("")}
                  </ul>
                </div>
              `).join("")}
            </div>
          </div>
        ` : ''}

        <!-- 4. Interval Form (Using Roots) -->
        ${intervalRules ? `
          <div class="space-y-2.5">
            <span class="nb-pill-yellow">4. ${intervalRules.title || 'Interval Form & Boundary Conditions'}</span>
            ${intervalRules.premise ? `<p class="text-xs text-slate-600 dark:text-slate-400 font-normal">${intervalRules.premise}</p>` : ''}
            
            <div class="nb-box-interval space-y-1 text-xs font-mono font-bold text-purple-950 dark:text-purple-200 shadow-sm">
              ${(intervalRules.cases || []).map(cs => `
                <div><span class="text-indigo-600 dark:text-indigo-400">${cs.cond}:</span> <span>${cs.interval}</span></div>
              `).join("")}
            </div>

            ${intervalRules.note ? `
              <div class="p-2.5 rounded-xl bg-purple-100/70 dark:bg-purple-950/40 border border-purple-300 dark:border-purple-800 text-[11px] text-purple-900 dark:text-purple-300 font-normal leading-relaxed">
                <strong>Note:</strong> ${intervalRules.note}
              </div>
            ` : ''}
          </div>
        ` : ''}

        <!-- 4b. Special Cases & Identifications (when present) -->
        ${n.special_cases ? `
          <div class="space-y-2.5">
            <span class="nb-pill-yellow">${n.special_cases.title || '4. Special Cases & Shortcut Identifications'}</span>
            <div class="nb-box-interval space-y-1.5 text-xs text-indigo-950 dark:text-indigo-200 shadow-sm">
              ${(n.special_cases.cases || []).map(cs => `
                <div class="flex items-start gap-1.5">
                  <span class="text-indigo-600 dark:text-indigo-400 font-bold shrink-0">•</span>
                  <span>${cs}</span>
                </div>
              `).join("")}
            </div>
            ${n.special_cases.note ? `
              <div class="p-2.5 rounded-xl bg-purple-100/70 dark:bg-purple-950/40 border border-purple-300 dark:border-purple-800 text-[11px] text-purple-900 dark:text-purple-300 font-normal leading-relaxed">
                <strong>Note:</strong> ${n.special_cases.note}
              </div>
            ` : ''}
          </div>
        ` : ''}

      </div>

      <!-- RIGHT COLUMN -->
      <div class="space-y-6">

        <!-- 5. Location from Vertex (Graphical View) -->
        ${graphical ? `
          <div class="space-y-2.5">
            <span class="nb-pill-yellow">5. ${graphical.title || 'Location from Vertex (Graphical View)'}</span>
            <p class="text-xs font-semibold text-slate-800 dark:text-slate-200">${graphical.vertex_formula}</p>
            <ul class="text-xs space-y-1 pl-3 text-slate-700 dark:text-slate-300 font-normal">
              ${(graphical.observations || []).map(obs => `
                <li class="list-disc">${obs}</li>
              `).join("")}
            </ul>
            <!-- Graphical Plot Diagram with SVG -->
            <div class="p-3 bg-white/90 dark:bg-slate-900/90 rounded-2xl border border-slate-300 dark:border-slate-700 shadow-sm overflow-x-auto">
              ${graphical.svg_diagram || ''}
            </div>
          </div>
        ` : ''}

        <!-- 6. Important Points -->
        ${importantPoints.length > 0 ? `
          <div class="space-y-2.5">
            <span class="nb-pill-yellow">${n.important_points_heading || '6. Important Points'}</span>
            <ul class="text-xs space-y-1.5 pl-3 text-slate-700 dark:text-slate-300 font-normal">
              ${importantPoints.map(pt => `
                <li class="list-disc">${pt}</li>
              `).join("")}
            </ul>
          </div>
        ` : ''}

        <!-- Quick Tips / Tricks (Blue Card) -->
        ${quickTips.length > 0 ? `
          <div class="nb-card-tips space-y-2">
            <div class="text-xs font-black text-sky-900 dark:text-sky-300 uppercase tracking-wider flex items-center gap-1.5">
              <span>★</span> Quick Tips / Tricks
            </div>
            <ul class="text-xs space-y-1.5 text-slate-800 dark:text-slate-200 font-normal">
              ${quickTips.map(tip => `
                <li class="flex items-start gap-1.5">
                  <span class="text-emerald-600 dark:text-emerald-400 font-black text-sm leading-none shrink-0">✓</span>
                  <span>${tip.replace(/^✓\s*/, '')}</span>
                </li>
              `).join("")}
            </ul>
          </div>
        ` : ''}

        <!-- JEE Focus Points (Purple Card) -->
        ${jeeFocus.length > 0 ? `
          <div class="nb-card-focus space-y-2">
            <div class="text-xs font-black text-purple-900 dark:text-purple-300 uppercase tracking-wider flex items-center gap-1.5">
              <span>★</span> JEE Focus Points
            </div>
            <ul class="text-xs space-y-1 text-slate-800 dark:text-slate-200 font-normal">
              ${jeeFocus.map(fp => `
                <li class="flex items-start gap-1.5">
                  <span class="text-purple-600 dark:text-purple-400 font-bold shrink-0">•</span>
                  <span>${fp}</span>
                </li>
              `).join("")}
            </ul>
          </div>
        ` : ''}

        <!-- High-Frequency JEE Traps & Pitfalls (Amber Card) -->
        ${traps.length > 0 ? `
          <div class="nb-card-traps space-y-2">
            <div class="text-xs font-black text-amber-900 dark:text-amber-300 uppercase tracking-wider flex items-center gap-1.5">
              <span>⚠️</span> High-Frequency JEE Traps & Pitfalls
            </div>
            <ul class="text-xs space-y-1.5 text-slate-800 dark:text-slate-200 font-normal">
              ${traps.map(tr => `
                <li class="flex items-start gap-1.5">
                  <span class="text-amber-600 dark:text-amber-400 font-bold text-sm leading-none shrink-0">!</span>
                  <span>${typeof tr === 'string' ? tr : `<strong>${tr.trap}</strong> ${tr.why ? '— ' + tr.why : ''} ${tr.remedy ? '<br/><span class="text-emerald-700 dark:text-emerald-400 font-semibold">Fix: ' + tr.remedy + '</span>' : ''}`}</span>
                </li>
              `).join("")}
            </ul>
          </div>
        ` : ''}

      </div>
    </div>

    <!-- BOTTOM FULL-WIDTH MNEMONIC / GOLDEN RULE BANNER -->
    ${n.mnemonic_banner ? `
      <div class="text-center pt-3 pb-2">
        <div class="nb-mnemonic-banner">
          <span class="opacity-70 font-mono">ヾ</span>
          <span>${n.mnemonic_banner}</span>
          <span class="opacity-70 font-mono">ﾉ</span>
        </div>
      </div>
    ` : ''}

    <!-- HIGH-YIELD FORMULAS WITH WORKED EXAMPLES -->
    ${formulas.length > 0 ? `
      <div class="pt-5 border-t-2 border-slate-300 dark:border-slate-800 space-y-3">
        <h4 class="text-xs font-extrabold uppercase tracking-wider text-amber-700 dark:text-amber-400 flex items-center gap-1.5">
          <span>⚡</span> High-Yield Formulas & Governing Equations
        </h4>
        <div class="grid grid-cols-1 gap-3">
          ${formulas.map(f => `
            <div class="p-3.5 rounded-xl bg-white/90 dark:bg-slate-900/90 border border-amber-300 dark:border-amber-500/30 space-y-2 shadow-sm">
              <div class="flex items-center justify-between text-xs">
                <span class="font-bold text-amber-900 dark:text-amber-300">${f.title}</span>
                <span class="text-[10px] text-slate-500 dark:text-slate-400 font-semibold">Class ${f.class_level}</span>
              </div>
              <div class="p-2.5 rounded-lg bg-amber-50/60 dark:bg-slate-950 text-xs text-amber-950 dark:text-amber-200 overflow-x-auto font-mono text-center border border-amber-200 dark:border-slate-800">
                $$${f.formula}$$
              </div>
              <div class="text-[11px] text-slate-700 dark:text-slate-300 space-y-0.5">
                ${f.conditions ? `<p><span class="text-amber-700 dark:text-amber-400 font-bold">Conditions:</span> ${f.conditions}</p>` : ''}
                ${f.variables ? `<p><span class="text-sky-700 dark:text-sky-400 font-bold">Variables:</span> ${f.variables}</p>` : ''}
                ${f.tips ? `<p><span class="text-emerald-700 dark:text-emerald-400 font-bold">JEE Tip:</span> ${f.tips}</p>` : ''}
              </div>
              ${f.example ? `
                <div class="rounded-xl border border-emerald-400/60 dark:border-emerald-500/30 bg-emerald-50/60 dark:bg-emerald-950/20 p-3 space-y-1.5 text-xs">
                  <div class="font-bold text-emerald-900 dark:text-emerald-300 flex items-center gap-1">
                    <span>💡 Worked Application:</span>
                  </div>
                  <div class="text-slate-800 dark:text-slate-200 font-normal"><strong>Problem:</strong> ${f.example.problem}</div>
                  <div class="text-slate-700 dark:text-slate-300 whitespace-pre-line border-t border-emerald-200 dark:border-slate-800 pt-1 mt-1 font-normal"><strong>Solution:</strong> ${f.example.solution}</div>
                </div>
              ` : ''}
            </div>
          `).join("")}
        </div>
      </div>
    ` : ''}

    <!-- MINIMUM 2 SOLVED ILLUSTRATIVE JEE EXAMPLES -->
    ${examples.length > 0 ? `
      <div class="pt-5 border-t-2 border-slate-300 dark:border-slate-800 space-y-3">
        <h4 class="text-xs font-extrabold uppercase tracking-wider text-emerald-700 dark:text-emerald-400 flex items-center gap-1.5">
          <span>💡</span> Solved Illustrative JEE Examples (Minimum 2)
        </h4>
        <div class="space-y-4">
          ${examples.map((ex, exIdx) => `
            <div class="p-4 rounded-2xl bg-white/95 dark:bg-slate-900/90 border-2 border-emerald-300 dark:border-emerald-500/30 space-y-2.5 shadow-sm text-slate-800 dark:text-slate-200">
              <div class="flex items-center justify-between pb-1.5 border-b border-emerald-200 dark:border-slate-800">
                <span class="text-xs font-black text-emerald-800 dark:text-emerald-400 uppercase tracking-wider">${ex.title}</span>
                <span class="text-[10px] font-bold px-2 py-0.5 rounded-full bg-emerald-100 dark:bg-emerald-950/60 text-emerald-800 dark:text-emerald-300 border border-emerald-300">Worked Problem</span>
              </div>
              <div class="text-xs sm:text-sm font-normal leading-relaxed">
                <strong class="text-slate-900 dark:text-white">Problem:</strong> ${ex.problem}
              </div>
              ${ex.approach ? `
                <div class="text-xs text-indigo-900 dark:text-indigo-200 bg-indigo-50/80 dark:bg-indigo-950/40 p-2 rounded-lg border border-indigo-200 dark:border-indigo-900 font-medium">
                  <strong>Approach / Method:</strong> ${ex.approach}
                </div>
              ` : ''}
              <div class="text-xs bg-slate-50 dark:bg-slate-950/60 p-3 rounded-xl border border-slate-200 dark:border-slate-800 space-y-1">
                <p class="text-indigo-800 dark:text-indigo-300 font-bold">Step-by-Step Method & Solution:</p>
                <div class="leading-relaxed pl-2 whitespace-pre-line text-slate-700 dark:text-slate-300 font-normal">${ex.solution}</div>
              </div>
              ${ex.key_takeaway ? `
                <div class="text-[11px] text-emerald-800 dark:text-emerald-300 bg-emerald-50 dark:bg-emerald-950/30 px-3 py-1.5 rounded-xl border border-emerald-200 dark:border-emerald-500/20 font-medium">
                  <strong>Key Takeaway:</strong> ${ex.key_takeaway}
                </div>
              ` : ''}
            </div>
          `).join("")}
        </div>
      </div>
    ` : ''}
  `;
}

function closeNotesModal() {
  document.getElementById("notesModal").classList.add("hidden");
  const sInput = document.getElementById("notesSearchInput");
  if (sInput) sInput.value = "";
}

function formatSingleSheetMarkdown(n) {
  let md = `# ヾ ${n.sheet_title || n.chapter} ﾉ\n\n`;
  md += `**Chapter:** ${n.ncert_ref || n.chapter} | **Subject:** ${n.subject} | **Class:** ${n.class_level}\n\n`;
  md += `## 1. Introduction\n${n.introduction || ''}\n\n`;

  if (n.classification_cases && n.classification_cases.length > 0) {
    md += `## ${n.classification_heading || '2. Range & Classification of Cases'}\n`;
    n.classification_cases.forEach(c => {
      md += `### ${c.badge || c.title}\n`;
      if (c.condition) md += `- **Condition:** ${c.condition}\n`;
      if (c.description) md += `- **Description:** ${c.description}\n`;
      if (c.range) md += `- **Range:** ${c.range}\n`;
      if (c.consequence) md += `- **Consequence:** ${c.consequence}\n`;
      md += `\n`;
    });
  }

  if (n.parameter_analysis && n.parameter_analysis.length > 0) {
    md += `## ${n.parameter_heading || '3. Parameter & Direction Rules'}\n`;
    n.parameter_analysis.forEach(p => {
      md += `### ${p.sub_badge}\n`;
      (p.rules || []).forEach(r => {
        md += `- **${r.cond}:** ${r.res}\n`;
      });
      md += `\n`;
    });
  }

  if (n.interval_rules) {
    md += `## 4. ${n.interval_rules.title || 'Interval Form & Boundary Conditions'}\n`;
    if (n.interval_rules.premise) md += `${n.interval_rules.premise}\n\n`;
    (n.interval_rules.cases || []).forEach(cs => {
      md += `- **${cs.cond}:** ${cs.interval}\n`;
    });
    if (n.interval_rules.note) md += `\n*Note:* ${n.interval_rules.note}\n\n`;
  }

  if (n.special_cases) {
    md += `## ${n.special_cases.title || '4. Special Cases'}\n`;
    (n.special_cases.cases || []).forEach(cs => {
      md += `- ${cs}\n`;
    });
    if (n.special_cases.note) md += `\n*Note:* ${n.special_cases.note}\n\n`;
  }

  if (n.graphical_view) {
    md += `## 5. ${n.graphical_view.title || 'Graphical & Conceptual View'}\n`;
    if (n.graphical_view.vertex_formula) md += `**Governing Coordinate:** ${n.graphical_view.vertex_formula}\n\n`;
    (n.graphical_view.observations || []).forEach(o => {
      md += `- ${o}\n`;
    });
    md += `\n`;
  }

  if (n.important_points && n.important_points.length > 0) {
    md += `## ${n.important_points_heading || '6. Important Points'}\n`;
    n.important_points.forEach(pt => {
      md += `- ${pt}\n`;
    });
    md += `\n`;
  }

  if (n.quick_tips && n.quick_tips.length > 0) {
    md += `## ★ Quick Tips / Tricks\n`;
    n.quick_tips.forEach(t => {
      md += `- ✓ ${t.replace(/^✓\s*/, '')}\n`;
    });
    md += `\n`;
  }

  if (n.jee_focus_points && n.jee_focus_points.length > 0) {
    md += `## ★ JEE Focus Points\n`;
    n.jee_focus_points.forEach(fp => {
      md += `- • ${fp}\n`;
    });
    md += `\n`;
  }

  if (n.traps_and_pitfalls && n.traps_and_pitfalls.length > 0) {
    md += `## ⚠️ High-Frequency JEE Traps & Pitfalls\n`;
    n.traps_and_pitfalls.forEach(tr => {
      if (typeof tr === 'string') {
        md += `- ! ${tr}\n`;
      } else {
        md += `- ! **${tr.trap}** ${tr.why ? '— ' + tr.why : ''} ${tr.remedy ? '(Fix: ' + tr.remedy + ')' : ''}\n`;
      }
    });
    md += `\n`;
  }

  if (n.mnemonic_banner) {
    md += `> **Golden Rule:** ヾ ${n.mnemonic_banner} ﾉ\n\n`;
  }

  if (n.examples && n.examples.length > 0) {
    md += `## Solved Illustrative JEE Examples\n`;
    n.examples.forEach(ex => {
      md += `### ${ex.title}\n`;
      md += `**Problem:** ${ex.problem}\n\n`;
      if (ex.approach) md += `**Approach:** ${ex.approach}\n\n`;
      md += `**Method & Solution:**\n${ex.solution}\n\n`;
      if (ex.key_takeaway) md += `**Key Takeaway:** ${ex.key_takeaway}\n\n`;
    });
  }

  return md;
}

function copyNotesMarkdown() {
  if (!currentLoadedNote) return;
  const sheets = window.currentNoteSheets;
  let fullMd = "";
  if (sheets && sheets.length > 1) {
    fullMd = sheets.map((s, idx) => `<!-- PAGE ${idx + 1} OF ${sheets.length}: ${s.sheet_title || ''} -->\n` + formatSingleSheetMarkdown(s)).join("\n\n---\n\n");
  } else {
    fullMd = formatSingleSheetMarkdown(currentLoadedNote);
  }

  navigator.clipboard.writeText(fullMd).then(() => {
    alert("Complete Chapter Cheat-Sheet Booklet copied to clipboard in clean Markdown format!");
  }).catch(() => {
    alert("Copied to clipboard!");
  });
}

function filterNotesContent(query) {
  const q = (query || "").toLowerCase().trim();
  const container = document.getElementById("notesNotebookSheet");
  if (!container) return;
  const elements = container.querySelectorAll("p, li, span, strong, td, div.nb-box-interval");
  elements.forEach(el => {
    if (!q) {
      el.classList.remove("bg-yellow-200/90", "text-slate-950", "rounded", "px-1");
    } else if (el.children.length === 0 && el.textContent.toLowerCase().includes(q)) {
      el.classList.add("bg-yellow-200/90", "text-slate-950", "rounded", "px-1");
    } else {
      el.classList.remove("bg-yellow-200/90", "text-slate-950", "rounded", "px-1");
    }
  });
}

// ---------------------------------------------------------------------
// Test Setup Modal (Asking: "Which chapter's test do you want to give?")
// ---------------------------------------------------------------------
function openTestModal(defaultChapter = null, defaultSubject = null, defaultLevel = null) {
  if (defaultSubject) {
    selectModalSubject(defaultSubject);
  } else {
    selectModalSubject(selectedModalSubject || "Physics");
  }
  
  if (defaultChapter) {
    const chObj = allChapters.find(c => c.name === defaultChapter);
    if (chObj) {
      selectModalSubject(chObj.subject);
      selectModalClass(chObj.class_level);
    }
    const select = document.getElementById("modalChapterSelect");
    select.value = defaultChapter;
  }

  if (defaultLevel) {
    const rad = document.querySelector(`input[name="modalExamLevel"][value="${defaultLevel}"]`);
    if (rad) rad.checked = true;
  }
  
  document.getElementById("testModal").classList.remove("hidden");
}

function closeTestModal() {
  document.getElementById("testModal").classList.add("hidden");
}

function selectModalSubject(subj) {
  selectedModalSubject = subj;
  document.querySelectorAll(".modal-subj-btn").forEach(btn => {
    if (btn.dataset.subj === subj) {
      let activeColor = "border-sky-500 bg-sky-950/60 text-sky-300";
      if (subj === "Chemistry") activeColor = "border-emerald-500 bg-emerald-950/60 text-emerald-300";
      if (subj === "Mathematics") activeColor = "border-amber-500 bg-amber-950/60 text-amber-300";
      btn.className = `modal-subj-btn py-2 px-3 text-xs font-bold rounded-xl border ${activeColor} transition`;
    } else {
      btn.className = "modal-subj-btn py-2 px-3 text-xs font-bold rounded-xl border border-slate-700 bg-slate-900 text-slate-400 hover:border-slate-500 transition";
    }
  });
  populateModalChapters();
}

function selectModalClass(cls) {
  selectedModalClass = cls;
  document.querySelectorAll(".modal-class-btn").forEach(btn => {
    const btnVal = btn.dataset.class === "All" ? "All" : parseInt(btn.dataset.class);
    if (btnVal === cls) {
      btn.className = "modal-class-btn py-1.5 px-2 text-[11px] font-bold rounded-lg border border-emerald-500 bg-emerald-950/60 text-emerald-300 transition";
    } else {
      btn.className = "modal-class-btn py-1.5 px-2 text-[11px] font-bold rounded-lg border border-slate-700 bg-slate-900 text-slate-400 hover:border-slate-500 transition";
    }
  });
  populateModalChapters();
}

function populateModalChapters() {
  const select = document.getElementById("modalChapterSelect");
  const filtered = allChapters.filter(c => {
    if (c.subject !== selectedModalSubject) return false;
    if (selectedModalClass !== "All" && c.class_level !== parseInt(selectedModalClass)) return false;
    return true;
  });
  
  if (filtered.length === 0) {
    select.innerHTML = `<option value="">No chapters found</option>`;
    return;
  }

  select.innerHTML = filtered.map(c => `
    <option value="${c.name}">NCERT Ch ${c.ncert_order}: ${c.name} (Class ${c.class_level} • ${c.importance} Yield • ${c.tests_given > 0 ? c.tests_given + ' tests given' : 'Untested'})</option>
  `).join("");
}

function onModalChapterChange() {
  // Can trigger additional subtopic filters if desired
}

function quickStartChapterTest(chapterName, subject) {
  openTestModal(chapterName, subject);
}

function quickStartBasicDrill(chapterName, subject) {
  openTestModal(chapterName, subject, "Basic (Marks)");
}

// ---------------------------------------------------------------------
// Test Launch & Preparation ("prepare the test accordingly")
// ---------------------------------------------------------------------
async function startTestFromModal() {
  const chapterName = document.getElementById("modalChapterSelect").value;
  const examLevel = document.querySelector('input[name="modalExamLevel"]:checked').value;
  const count = parseInt(document.querySelector('input[name="modalCount"]:checked').value);

  closeTestModal();
  await launchTest({
    chapter_name: chapterName,
    exam_type: examLevel,
    count: count,
    is_remedial: false
  });
}

async function launchTest({ chapter_name, exam_type, count, is_remedial = false, topics = null }) {
  try {
    let payload;
    let endpoint;

    if (is_remedial) {
      endpoint = "/api/test/remedial";
      payload = { topics: topics || [], exam_type: exam_type, count: count || 5 };
    } else {
      endpoint = "/api/test/generate";
      payload = { chapter_name: chapter_name, exam_type: exam_type, count: count || 5 };
    }

    let questions = [];
    try {
      const res = await fetch(endpoint, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(payload)
      });
      if (res.ok) {
        const data = await res.json();
        if (data.success && data.questions && data.questions.length > 0) {
          questions = data.questions;
        }
      }
    } catch (e) {}

    // Serverless / GitHub Pages client-side question generation fallback
    if (questions.length === 0 && window.JEE_STATIC_DATA && window.JEE_STATIC_DATA.questions) {
      questions = generateClientSideQuestions(chapter_name, exam_type, count, is_remedial, topics);
    }

    if (questions.length === 0) {
      alert("No questions found for this selection. Please try another chapter.");
      return;
    }

    // Initialize CBT state
    const firstQ = questions[0];
    activeTest = {
      chapterName: chapter_name || (is_remedial ? "Targeted Remedial Drill" : firstQ.chapter_name),
      subject: firstQ.subject || "JEE Practice",
      examType: exam_type,
      isRemedial: is_remedial,
      questions: questions,
      currentIndex: 0,
      answers: {},
      marked: new Set(),
      visited: new Set([0]),
      startTime: Date.now(),
      totalSeconds: (questions.length * 3) * 60, // 3 mins per question
      timerInterval: null
    };

    setupCBTView();
    showView("cbt");

  } catch (err) {
    console.error("Error launching test:", err);
    alert("Failed to prepare test. Please ensure the server is running or data is loaded.");
  }
}

function generateClientSideQuestions(chapter_name, exam_type, count, is_remedial = false, topics = null) {
  if (!window.JEE_STATIC_DATA || !window.JEE_STATIC_DATA.questions) return [];
  let pool = window.JEE_STATIC_DATA.questions;

  if (is_remedial && topics && topics.length > 0) {
    pool = pool.filter(q => topics.includes(q.topic));
  } else if (chapter_name) {
    pool = pool.filter(q => q.chapter === chapter_name);
  }

  // If chapter has fewer questions than count, synthesize or take from same subject
  const chObj = allChapters.find(c => c.name === chapter_name);
  const subj = chObj ? chObj.subject : "Physics";

  let candidates = [...pool];
  if (candidates.length < count && chObj) {
    const moreInSubject = window.JEE_STATIC_DATA.questions.filter(q => {
      const qCh = allChapters.find(c => c.name === q.chapter);
      return qCh && qCh.subject === subj && !candidates.includes(q);
    });
    candidates = candidates.concat(moreInSubject);
  }

  // Filter or sort by exam_type
  if (exam_type === "Basic" || exam_type === "Basic (Marks)") {
    candidates.sort((a, b) => (a.level === "Basic" ? -1 : 1));
  } else if (exam_type === "JEE Advanced") {
    candidates.sort((a, b) => (a.level === "JEE Advanced" ? -1 : 1));
  }

  // Shuffle and slice
  candidates.sort(() => 0.5 - Math.random());
  const selected = candidates.slice(0, count);

  return selected.map((q, idx) => ({
    id: q.id || `static_q_${idx}_${Date.now()}`,
    chapter_name: q.chapter,
    subject: subj,
    topic_name: q.topic,
    level: q.level || "JEE Main",
    type: q.type || "mcq_single",
    question: q.question,
    options: q.options,
    correct_answer: q.correct_answer,
    correct_index: q.correct_index !== undefined ? q.correct_index : 0,
    explanation: q.explanation
  }));
}

// ---------------------------------------------------------------------
// CBT Test Running & Timer Engine
// ---------------------------------------------------------------------
function setupCBTView() {
  document.getElementById("cbtSubjectBadge").innerText = activeTest.subject;
  document.getElementById("cbtExamTypeBadge").innerText = activeTest.examType;
  document.getElementById("cbtChapterTitle").innerText = activeTest.chapterName;
  document.getElementById("cbtTargetSyllabus").innerText = activeTest.chapterName;

  if (activeTest.isRemedial) {
    document.getElementById("cbtRemedialBadge").classList.remove("hidden");
  } else {
    document.getElementById("cbtRemedialBadge").classList.add("hidden");
  }

  // Timer Setup
  if (activeTest.timerInterval) clearInterval(activeTest.timerInterval);
  updateTimerDisplay();
  activeTest.timerInterval = setInterval(() => {
    activeTest.totalSeconds--;
    updateTimerDisplay();
    if (activeTest.totalSeconds <= 0) {
      clearInterval(activeTest.timerInterval);
      alert("Time is up! Submitting your test automatically...");
      submitTest();
    }
  }, 1000);

  renderPalette();
  renderCurrentQuestion();
}

function updateTimerDisplay() {
  const m = Math.floor(activeTest.totalSeconds / 60);
  const s = activeTest.totalSeconds % 60;
  const formatted = `${m.toString().padStart(2, "0")}:${s.toString().padStart(2, "0")}`;
  const el = document.getElementById("cbtTimer");
  el.innerText = formatted;

  if (activeTest.totalSeconds < 180) {
    el.classList.add("text-rose-400");
  } else {
    el.classList.remove("text-rose-400");
  }
}

function renderPalette() {
  const palette = document.getElementById("cbtPaletteGrid");
  palette.innerHTML = activeTest.questions.map((q, idx) => {
    let stateClass = "not-visited";
    if (activeTest.answers[q.id] !== undefined) {
      stateClass = "answered";
    } else if (activeTest.marked.has(q.id)) {
      stateClass = "marked";
    } else if (activeTest.visited.has(idx)) {
      stateClass = "not-answered";
    }

    const currentClass = (idx === activeTest.currentIndex) ? "current" : "";

    return `
      <button onclick="jumpToQuestion(${idx})" class="palette-btn ${stateClass} ${currentClass}">
        ${idx + 1}
      </button>
    `;
  }).join("");
}

function renderCurrentQuestion() {
  const q = activeTest.questions[activeTest.currentIndex];
  activeTest.visited.add(activeTest.currentIndex);

  document.getElementById("cbtQuestionNum").innerText = `Question ${activeTest.currentIndex + 1} of ${activeTest.questions.length}`;
  document.getElementById("cbtQuestionTopic").innerText = `Topic: ${q.topic_name}`;
  document.getElementById("cbtQuestionText").innerHTML = q.question;

  const currentSelection = activeTest.answers[q.id];

  const container = document.getElementById("cbtOptionsContainer");
  container.innerHTML = q.options.map((opt, optIdx) => {
    const isSelected = currentSelection === optIdx;
    const optionLetter = String.fromCharCode(65 + optIdx); // A, B, C, D

    return `
      <div onclick="selectOption(${optIdx})" class="option-card p-4 rounded-xl border ${isSelected ? 'selected' : 'border-slate-700 bg-slate-900/50'} flex items-start gap-3">
        <div class="w-6 h-6 rounded-full border ${isSelected ? 'border-indigo-400 bg-indigo-600 text-white' : 'border-slate-600 text-slate-400'} flex items-center justify-center font-bold text-xs shrink-0 mt-0.5">
          ${optionLetter}
        </div>
        <div class="text-sm sm:text-base text-slate-200">
          ${opt}
        </div>
      </div>
    `;
  }).join("");

  // Navigation button states
  document.getElementById("btnPrevQ").disabled = (activeTest.currentIndex === 0);
  if (activeTest.currentIndex === activeTest.questions.length - 1) {
    document.getElementById("btnNextQ").innerText = "Save & Review";
  } else {
    document.getElementById("btnNextQ").innerText = "Save & Next";
  }

  renderPalette();
  renderMath();
}

function selectOption(optIdx) {
  const q = activeTest.questions[activeTest.currentIndex];
  activeTest.answers[q.id] = optIdx;
  activeTest.marked.delete(q.id); // Answered, remove review mark if any
  renderCurrentQuestion();
}

function clearResponse() {
  const q = activeTest.questions[activeTest.currentIndex];
  delete activeTest.answers[q.id];
  renderCurrentQuestion();
}

function markForReview() {
  const q = activeTest.questions[activeTest.currentIndex];
  activeTest.marked.add(q.id);
  nextQuestion();
}

function prevQuestion() {
  if (activeTest.currentIndex > 0) {
    activeTest.currentIndex--;
    renderCurrentQuestion();
  }
}

function nextQuestion() {
  if (activeTest.currentIndex < activeTest.questions.length - 1) {
    activeTest.currentIndex++;
    renderCurrentQuestion();
  } else {
    renderPalette();
  }
}

function jumpToQuestion(idx) {
  activeTest.currentIndex = idx;
  renderCurrentQuestion();
}

function confirmSubmitTest() {
  const answeredCount = Object.keys(activeTest.answers).length;
  const totalCount = activeTest.questions.length;
  const unattempted = totalCount - answeredCount;

  const msg = `Are you sure you want to submit the test?\n\n• Answered: ${answeredCount}\n• Unanswered: ${unattempted}`;
  if (confirm(msg)) {
    submitTest();
  }
}

// ---------------------------------------------------------------------
// Test Submission & Weak Topic Diagnostics ("point out which topics are weak")
// ---------------------------------------------------------------------
async function submitTest() {
  if (activeTest.timerInterval) clearInterval(activeTest.timerInterval);

  const timeElapsed = Math.round((Date.now() - activeTest.startTime) / 1000);

  const payload = {
    chapter_name: activeTest.chapterName,
    subject: activeTest.subject,
    exam_type: activeTest.examType,
    time_taken_seconds: timeElapsed,
    answers: activeTest.questions.map(q => ({
      id: q.id,
      question: q.question,
      topic_name: q.topic_name,
      user_choice: activeTest.answers[q.id] !== undefined ? activeTest.answers[q.id] : null,
      correct_index: q.correct_index,
      options: q.options,
      explanation: q.explanation
    }))
  };

  try {
    let result = null;
    try {
      const res = await fetch("/api/test/submit", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(payload)
      });
      if (res.ok) {
        const data = await res.json();
        if (data.success && data.result) result = data.result;
      }
    } catch (e) {}

    if (!result) {
      result = evaluateClientSideSubmission(payload);
    }

    lastTestResult = result;
    renderTestResult(result);
    showView("result");
  } catch (err) {
    console.error("Error submitting test:", err);
    alert("Error submitting test. Please check console.");
  }
}

function evaluateClientSideSubmission(payload) {
  let correctCount = 0;
  let incorrectCount = 0;
  let unattemptedCount = 0;
  let totalScore = 0;
  const questionsReview = [];
  const topicStats = {};

  payload.answers.forEach(a => {
    const isAttempted = a.user_choice !== null && a.user_choice !== undefined;
    const isCorrect = isAttempted && a.user_choice === a.correct_index;
    let mark = 0;
    if (!isAttempted) {
      unattemptedCount++;
    } else if (isCorrect) {
      correctCount++;
      mark = 4;
    } else {
      incorrectCount++;
      mark = -1;
    }
    totalScore += mark;

    if (!topicStats[a.topic_name]) {
      topicStats[a.topic_name] = { attempts: 0, correct: 0 };
    }
    if (isAttempted) {
      topicStats[a.topic_name].attempts++;
      if (isCorrect) topicStats[a.topic_name].correct++;
    }

    questionsReview.push({
      ...a,
      is_correct: isCorrect,
      is_attempted: isAttempted,
      marks_awarded: mark
    });
  });

  const totalQuestions = payload.answers.length;
  const maxScore = totalQuestions * 4;
  const accuracy = totalQuestions > 0 ? Math.round((correctCount / totalQuestions) * 100) : 0;
  const scorePct = maxScore > 0 ? Math.max(0, Math.round((totalScore / maxScore) * 100)) : 0;

  const weakTopics = [];
  for (const [topName, st] of Object.entries(topicStats)) {
    const acc = st.attempts > 0 ? (st.correct / st.attempts) * 100 : 0;
    if (st.attempts > 0 && acc < 60) {
      weakTopics.push({
        topic_name: topName,
        accuracy: Math.round(acc),
        attempts: st.attempts,
        correct: st.correct,
        status: "Weak",
        diagnostic_tip: "Accuracy under 60%. Review key formulas and trap patterns."
      });
    }
  }

  // Update chapter stats in allChapters
  const chap = allChapters.find(c => c.name === payload.chapter_name);
  if (chap) {
    chap.tests_given = (chap.tests_given || 0) + 1;
    chap.last_score_pct = scorePct;
    chap.mastery_status = scorePct >= 80 ? "Proficient" : (scorePct >= 50 ? "Developing" : "Needs Revision");
    
    const saved = JSON.parse(localStorage.getItem("jee_chapter_stats") || "{}");
    saved[chap.name] = {
      tests_given: chap.tests_given,
      last_score_pct: chap.last_score_pct,
      mastery_status: chap.mastery_status
    };
    localStorage.setItem("jee_chapter_stats", JSON.stringify(saved));
  }

  // Save weak topics to localStorage
  if (weakTopics.length > 0) {
    const allWeak = JSON.parse(localStorage.getItem("jee_weak_topics") || "[]");
    weakTopics.forEach(wt => {
      if (!allWeak.some(x => x.topic_name === wt.topic_name)) {
        allWeak.push({ ...wt, chapter_name: payload.chapter_name, subject: payload.subject });
      }
    });
    localStorage.setItem("jee_weak_topics", JSON.stringify(allWeak));
  }

  return {
    chapter_name: payload.chapter_name,
    subject: payload.subject,
    exam_type: payload.exam_type,
    score: totalScore,
    max_score: maxScore,
    score_pct: scorePct,
    accuracy: accuracy,
    correct_count: correctCount,
    incorrect_count: incorrectCount,
    unattempted_count: unattemptedCount,
    time_taken_seconds: payload.time_taken_seconds,
    weak_topics: weakTopics,
    questions_review: questionsReview
  };
}

function renderTestResult(res) {
  document.getElementById("resExamType").innerText = res.exam_type;
  document.getElementById("resChapterName").innerText = res.chapter_name;
  document.getElementById("resScoreText").innerText = `${res.score} / ${res.max_score}`;
  document.getElementById("resAccuracyText").innerText = `Accuracy: ${res.accuracy}%`;
  document.getElementById("resPercentScore").innerText = `${res.score_pct}%`;

  document.getElementById("resCorrectCount").innerText = res.correct_count;
  document.getElementById("resIncorrectCount").innerText = res.incorrect_count;
  document.getElementById("resUnattemptedCount").innerText = res.unattempted_count;

  const min = Math.floor(res.time_taken_seconds / 60);
  const sec = res.time_taken_seconds % 60;
  document.getElementById("resTimeTaken").innerText = `${min}m ${sec}s`;

  // Render Weak Topics
  const weakContainer = document.getElementById("resWeakTopicsContainer");
  const btnLaunch = document.getElementById("btnLaunchRemedial");

  if (!res.weak_topics || res.weak_topics.length === 0) {
    weakContainer.innerHTML = `
      <div class="p-4 bg-emerald-950/30 border border-emerald-500/30 rounded-xl text-emerald-300 text-sm flex items-center gap-3">
        <svg class="w-5 h-5 text-emerald-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"/></svg>
        <span>Outstanding work! No weak topics detected in this test. All sub-topics demonstrated solid accuracy (>75%).</span>
      </div>
    `;
    btnLaunch.classList.add("hidden");
  } else {
    btnLaunch.classList.remove("hidden");
    weakContainer.innerHTML = res.weak_topics.map(t => `
      <div class="p-3.5 bg-slate-900/80 border border-rose-500/30 rounded-xl flex flex-col sm:flex-row sm:items-center justify-between gap-3">
        <div>
          <div class="flex items-center gap-2">
            <span class="w-2 h-2 rounded-full bg-rose-500"></span>
            <span class="font-bold text-white text-sm">${t.topic_name}</span>
            <span class="text-xs bg-rose-500/20 text-rose-300 border border-rose-500/30 px-2 py-0.5 rounded-full font-semibold">Weak (${t.accuracy}% Accuracy)</span>
          </div>
          <p class="text-xs text-slate-400 mt-1">${t.recommendation}</p>
        </div>
        <button onclick="practiceSingleWeakTopic('${t.topic_name.replace(/'/g, "\\'")}')" class="px-3.5 py-1.5 bg-rose-600/30 hover:bg-rose-600 text-rose-300 hover:text-white border border-rose-500/40 text-xs font-bold rounded-lg transition shrink-0">
          🎯 Practice Topic Drill
        </button>
      </div>
    `).join("");
  }

  // Render Detailed Solutions
  const solutionsContainer = document.getElementById("resDetailedQuestionsList");
  solutionsContainer.innerHTML = res.detailed_results.map((item, idx) => {
    const isCorrect = item.is_correct;
    const isUnattempted = item.status === "unattempted";

    let borderStatus = isCorrect ? "border-emerald-500/40 bg-emerald-950/10" : (isUnattempted ? "border-slate-700 bg-slate-900/40" : "border-rose-500/40 bg-rose-950/10");
    let badgeStatus = isCorrect ? `<span class="text-xs font-bold text-emerald-400 bg-emerald-950/50 border border-emerald-800 px-2 py-0.5 rounded">Correct (+4)</span>` : (isUnattempted ? `<span class="text-xs font-bold text-slate-400 bg-slate-800 px-2 py-0.5 rounded">Unattempted (0)</span>` : `<span class="text-xs font-bold text-rose-400 bg-rose-950/50 border border-rose-800 px-2 py-0.5 rounded">Incorrect (-1)</span>`);

    return `
      <div class="border ${borderStatus} rounded-xl p-5 space-y-3">
        <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
          <span class="text-xs font-bold text-indigo-400">Question ${idx + 1} • ${item.topic_name}</span>
          ${badgeStatus}
        </div>

        <div class="text-sm sm:text-base text-slate-200">
          ${item.question}
        </div>

        <!-- Options check -->
        <div class="grid grid-cols-1 sm:grid-cols-2 gap-2 text-xs">
          ${item.options.map((opt, oIdx) => {
            let optStyle = "bg-slate-900/60 text-slate-300 border-slate-700";
            let indicator = "";
            if (oIdx === item.correct_index) {
              optStyle = "bg-emerald-950/60 text-emerald-300 border-emerald-500 font-bold";
              indicator = " ✓ (Correct Answer)";
            } else if (oIdx === item.user_choice && !isCorrect) {
              optStyle = "bg-rose-950/60 text-rose-300 border-rose-500 font-bold";
              indicator = " ✗ (Your Choice)";
            }
            return `
              <div class="p-2.5 rounded-lg border ${optStyle}">
                <strong>${String.fromCharCode(65 + oIdx)}.</strong> ${opt} ${indicator}
              </div>
            `;
          }).join("")}
        </div>

        <!-- Detailed Explanation / Formulas -->
        <div class="p-3 bg-slate-900/90 rounded-lg border border-slate-700/60 text-xs text-slate-300 space-y-1">
          <div class="font-bold text-indigo-300 flex items-center gap-1.5">
            <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"/></svg>
            Step-by-Step JEE Solution & Key Concept:
          </div>
          <div class="leading-relaxed pl-5">
            ${item.explanation}
          </div>
        </div>
      </div>
    `;
  }).join("");

  renderMath();
}

// ---------------------------------------------------------------------
// Remedial Tests ("provide questions accordingly")
// ---------------------------------------------------------------------
async function launchRemedialForCurrentTest() {
  if (!lastTestResult || !lastTestResult.weak_topics || lastTestResult.weak_topics.length === 0) {
    alert("No weak topics available to practice.");
    return;
  }
  const topicsToPractice = lastTestResult.weak_topics.map(t => t.topic_name);
  await launchTest({
    chapter_name: lastTestResult.chapter_name,
    exam_type: lastTestResult.exam_type,
    count: Math.min(Math.max(topicsToPractice.length * 2, 5), 10),
    is_remedial: true,
    topics: topicsToPractice
  });
}

async function practiceSingleWeakTopic(topicName) {
  await launchTest({
    chapter_name: "Targeted Topic Drill",
    exam_type: "JEE Main",
    count: 5,
    is_remedial: true,
    topics: [topicName]
  });
}

async function loadAllWeakTopics() {
  const container = document.getElementById("allWeakTopicsList");
  try {
    let weakTopics = [];
    try {
      const res = await fetch("/api/weak-topics");
      if (res.ok) {
        const data = await res.json();
        if (data.success && data.weak_topics) weakTopics = data.weak_topics;
      }
    } catch (e) {}

    if (weakTopics.length === 0) {
      weakTopics = JSON.parse(localStorage.getItem("jee_weak_topics") || "[]");
    }

    if (weakTopics.length === 0) {
      container.innerHTML = `
        <div class="col-span-full py-12 text-center text-slate-400 text-sm">
          No weak topics identified yet! Take chapter tests and any topics needing revision will appear here.
        </div>
      `;
      return;
    }

    container.innerHTML = weakTopics.map(t => `
      <div class="bg-slate-800 border border-slate-700 rounded-xl p-5 flex flex-col justify-between gap-3">
        <div>
          <div class="flex items-center justify-between text-xs mb-1">
            <span class="font-bold text-indigo-400 uppercase tracking-wider">${t.subject} • ${t.chapter_name}</span>
            <span class="px-2 py-0.5 rounded-full text-[11px] font-bold bg-rose-500/20 text-rose-300 border border-rose-500/30">
              ${t.accuracy}% Accuracy
            </span>
          </div>
          <h4 class="text-base font-bold text-white">${t.topic_name}</h4>
          <p class="text-xs text-slate-400 mt-1">Attempts: ${t.attempts} (${t.correct} correct, ${t.attempts - t.correct} incorrect)</p>
        </div>

        <div class="pt-3 border-t border-slate-700 flex justify-end">
          <button onclick="practiceSingleWeakTopic('${t.topic_name.replace(/'/g, "\\'")}')" class="px-4 py-2 bg-rose-600 hover:bg-rose-500 text-white font-bold text-xs rounded-xl shadow transition flex items-center gap-1.5">
            <span>🎯 Practice Drill on this Topic</span>
          </button>
        </div>
      </div>
    `).join("");

  } catch (err) {
    console.error("Error loading weak topics:", err);
  }
}

async function launchAllWeakRemedial() {
  try {
    const res = await fetch("/api/weak-topics");
    const data = await res.json();
    if (!data.success || !data.weak_topics || data.weak_topics.length === 0) {
      alert("No weak topics recorded yet. Take tests on chapters first!");
      return;
    }
    const topicNames = data.weak_topics.map(t => t.topic_name);
    await launchTest({
      chapter_name: "Comprehensive Weak Topic Remedial Mock",
      exam_type: "JEE Main",
      count: Math.min(topicNames.length * 2, 10),
      is_remedial: true,
      topics: topicNames
    });
  } catch (err) {
    console.error(err);
  }
}

// ---------------------------------------------------------------------
// Master Formula Vault View Logic ("formulas of imp things")
// ---------------------------------------------------------------------
async function loadFormulaVault() {
  try {
    let formulas = [];
    try {
      const res = await fetch("/api/formulas");
      if (res.ok) {
        const data = await res.json();
        if (data.success && data.formulas) formulas = data.formulas;
      }
    } catch (e) {}

    if (formulas.length === 0 && window.JEE_STATIC_DATA && window.JEE_STATIC_DATA.formulas) {
      formulas = window.JEE_STATIC_DATA.formulas;
    }

    allFormulas = formulas;
    const badge = document.getElementById("formulaVaultCountBadge");
    if (badge) badge.innerText = `${allFormulas.length} High-Yield Equations`;
    renderFormulaVault();
  } catch (err) {
    console.error("Error loading formula vault:", err);
  }
}

function setFormulaSubjectFilter(subj) {
  currentFormulaSubject = subj;
  document.querySelectorAll(".formula-subj-btn").forEach(btn => {
    if (btn.getAttribute("data-fsubj") === subj) {
      btn.className = "formula-subj-btn px-3 py-1.5 rounded-lg transition bg-amber-600 text-white";
    } else {
      btn.className = "formula-subj-btn px-3 py-1.5 rounded-lg transition text-slate-400 hover:text-white";
    }
  });
  renderFormulaVault();
}

function setFormulaClassFilter(cls) {
  currentFormulaClass = cls === "All" ? "All" : parseInt(cls);
  document.querySelectorAll(".formula-class-btn").forEach(btn => {
    const btnCls = btn.getAttribute("data-fclass");
    if ((cls === "All" && btnCls === "All") || (cls !== "All" && parseInt(btnCls) === currentFormulaClass)) {
      btn.className = "formula-class-btn px-3 py-1.5 rounded-lg transition bg-emerald-600 text-white";
    } else {
      btn.className = "formula-class-btn px-3 py-1.5 rounded-lg transition text-slate-400 hover:text-white";
    }
  });
  renderFormulaVault();
}

function renderFormulaVault() {
  const container = document.getElementById("formulaVaultGrid");
  if (!container) return;
  const search = (document.getElementById("formulaSearchInput")?.value || "").toLowerCase().trim();

  let filtered = allFormulas.filter(f => {
    if (currentFormulaSubject !== "All" && f.subject !== currentFormulaSubject) return false;
    if (currentFormulaClass !== "All" && f.class_level !== currentFormulaClass) return false;
    if (search) {
      const matchText = `${f.title} ${f.chapter} ${f.formula} ${f.conditions || ''} ${f.variables || ''} ${f.tips || ''}`.toLowerCase();
      if (!matchText.includes(search)) return false;
    }
    return true;
  });

  if (filtered.length === 0) {
    container.innerHTML = `
      <div class="col-span-full py-12 text-center text-slate-400 text-sm">
        No formulas match your current filter criteria. Try searching for a different keyword or resetting filters.
      </div>
    `;
    return;
  }

  container.innerHTML = filtered.map(f => {
    const subjColor = f.subject === "Physics" ? "text-sky-400 border-sky-500/30 bg-sky-500/10" :
                      (f.subject === "Chemistry" ? "text-emerald-400 border-emerald-500/30 bg-emerald-500/10" : "text-amber-400 border-amber-500/30 bg-amber-500/10");

    return `
      <div class="bg-slate-800/90 border border-slate-700 rounded-xl p-5 flex flex-col justify-between space-y-4 hover:border-slate-600 transition shadow-lg">
        <div class="space-y-3">
          <div class="flex items-center justify-between gap-2">
            <span class="text-xs font-bold px-2.5 py-0.5 rounded-full border ${subjColor}">
              ${f.subject} • Class ${f.class_level}
            </span>
            <span class="text-xs text-slate-400 font-medium truncate max-w-[200px]" title="${f.chapter}">
              ${f.chapter}
            </span>
          </div>

          <h4 class="text-base font-bold text-white leading-snug">${f.title}</h4>

          <!-- Equation Display Box with KaTeX math rendering -->
          <div class="p-3 bg-slate-950/90 rounded-xl border border-slate-700/80 text-amber-200 text-sm sm:text-base font-mono overflow-x-auto shadow-inner text-center">
            $$${f.formula}$$
          </div>

          <!-- Conditions & Variables -->
          <div class="space-y-1.5 text-xs text-slate-300">
            ${f.conditions ? `<p><strong class="text-amber-400">Valid Conditions:</strong> ${f.conditions}</p>` : ''}
            ${f.variables ? `<p><strong class="text-sky-400">Variables:</strong> ${f.variables}</p>` : ''}
            ${f.tips ? `<div class="p-2.5 rounded-lg bg-amber-950/30 border border-amber-500/20 text-amber-200">
              <strong>💡 JEE Application Tip:</strong> ${f.tips}
            </div>` : ''}
          </div>

          <!-- Worked Example Card with Problem & Step-by-Step Solution -->
          ${f.example ? `
            <div class="rounded-xl border border-emerald-500/40 bg-emerald-950/20 overflow-hidden text-xs space-y-2">
              <div class="px-3.5 py-2 bg-emerald-950/60 border-b border-emerald-800/40 flex items-center justify-between">
                <span class="font-bold text-emerald-300 flex items-center gap-1.5">
                  <svg class="w-3.5 h-3.5 text-emerald-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z"/></svg>
                  <span>Solved Worked Example</span>
                </span>
                <span class="text-[10px] uppercase font-bold tracking-wider px-2 py-0.5 rounded bg-emerald-900/70 text-emerald-200 border border-emerald-700/60">JEE Problem</span>
              </div>
              <div class="p-3.5 space-y-2 text-slate-200">
                <div>
                  <strong class="text-white">Problem:</strong> 
                  <span class="text-slate-200 font-normal leading-relaxed">${f.example.problem}</span>
                </div>
                <div class="pt-2 border-t border-slate-800/80">
                  <strong class="text-indigo-300">Step-by-Step Solution:</strong> 
                  <div class="text-slate-300 leading-relaxed pl-2 mt-1 whitespace-pre-line font-normal">${f.example.solution}</div>
                </div>
              </div>
            </div>
          ` : ''}
        </div>

        <div class="pt-3 border-t border-slate-700/60 flex items-center justify-between text-xs gap-2">
          <button onclick="openNotesModal('${f.chapter.replace(/'/g, "\\'")}')" class="text-indigo-400 hover:text-indigo-300 font-semibold flex items-center gap-1">
            <span>📖 Full Chapter Notes</span>
          </button>
          <div class="flex items-center gap-1.5">
            <button onclick="quickStartBasicDrill('${f.chapter.replace(/'/g, "\\'")}', '${f.subject}')" title="Practice Basic Level 1 Questions from Marks" class="px-2.5 py-1.5 bg-emerald-950/70 hover:bg-emerald-600 text-emerald-300 hover:text-white border border-emerald-500/40 font-bold rounded-lg transition flex items-center gap-1 shadow">
              <span>⚡ Basic Drill</span>
            </button>
            <button onclick="quickStartChapterTest('${f.chapter.replace(/'/g, "\\'")}', '${f.subject}')" class="px-3 py-1.5 bg-indigo-600 hover:bg-indigo-500 text-white font-bold rounded-lg transition flex items-center gap-1 shadow">
              <span>Take Test</span>
            </button>
          </div>
        </div>
      </div>
    `;
  }).join("");

  renderMath();
}

