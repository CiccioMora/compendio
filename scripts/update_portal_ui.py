import re

with open('/Users/andreamorachioli/.gemini/antigravity/scratch/portale-incantesimi/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update the CONTROLS HTML section
old_controls_pattern = re.compile(r'<!-- CONTROLS: SEARCH & FILTERS -->[\s\S]*?<!-- MAIN CARDS GRID CONTAINER -->')

new_controls_html = '''<!-- CONTROLS: SEARCH & FILTERS -->
  <section class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 mb-6">
    <div class="glass-panel p-5 sm:p-6 rounded-2xl border border-amber-500/25 shadow-2xl space-y-4">
      
      <!-- TOP: PROMINENT SEARCH BAR (NOME, FORMULA, DESCRIZIONE) -->
      <div>
        <div class="flex items-center justify-between mb-1.5">
          <label for="searchInput" class="text-xs font-bold uppercase tracking-wider text-amber-400 flex items-center gap-1.5">
            <span>🔍</span> Ricerca Incantesimo o Testo nella Descrizione
          </label>
          <span class="text-[11px] text-slate-400 hidden sm:inline">
            Ricerca attiva simultanea su: <strong>Nome</strong>, <strong>Formula</strong>, <strong>Descrizione</strong> e <strong>Movimento</strong>
          </span>
        </div>
        <div class="relative">
          <span class="absolute inset-y-0 left-0 pl-3.5 flex items-center pointer-events-none text-slate-400 text-lg">
            ⚡
          </span>
          <input 
            type="text" 
            id="searchInput" 
            placeholder="Cerca per nome (es. Flipendo), formula (es. Stupeficium), o parole chiave nella descrizione (es. 'fumo', 'duello', 'pietra', 'ossa', 'ferite')..." 
            class="w-full pl-11 pr-10 py-3 rounded-xl bg-slate-950/90 border border-slate-700/90 text-sm text-slate-100 placeholder-slate-500 focus:outline-none focus:border-amber-500 focus:ring-2 focus:ring-amber-500/20 transition shadow-inner"
          >
          <button id="clearSearchBtn" title="Cancella ricerca" class="absolute inset-y-0 right-0 pr-3.5 flex items-center text-slate-500 hover:text-amber-300 transition hidden text-base font-bold">
            ✕
          </button>
        </div>
      </div>

      <!-- FILTER CONTROLS GRID (ANNO, DUELLO, TIPOLOGIA, RESET) -->
      <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-3 pt-1">
        
        <!-- Filter 1: Anno di Studio -->
        <div>
          <label for="yearSelect" class="block text-xs font-semibold text-slate-300 mb-1 flex items-center gap-1">
            <span>📅</span> Filtro Anno di Corso:
          </label>
          <select id="yearSelect" class="w-full px-3 py-2.5 rounded-xl bg-slate-950/90 border border-slate-700 text-xs text-slate-200 focus:outline-none focus:border-amber-500 transition">
            <option value="ALL">Tutti gli Anni (129)</option>
            <option value="1">I Anno — Fondamenti & Cinetica (16)</option>
            <option value="2">II Anno — Fatture & Inanimati (14)</option>
            <option value="3">III Anno — Gelo, Impatto & Locomozione (16)</option>
            <option value="4">IV Anno — Tattiche & Medimagia (20)</option>
            <option value="5">V Anno — Umana, Esplosivi & Maledizioni (24)</option>
            <option value="6,7">M.A.G.O. & Arti Oscure (16)</option>
            <option value="0">Grimorio Aritmantico (Hawstein) (23)</option>
          </select>
        </div>

        <!-- Filter 2: Utilizzo in Duello -->
        <div>
          <label for="duelFilter" class="block text-xs font-semibold text-slate-300 mb-1 flex items-center gap-1">
            <span>⚔️</span> Utilizzo in Duello:
          </label>
          <select id="duelFilter" class="w-full px-3 py-2.5 rounded-xl bg-slate-950/90 border border-slate-700 text-xs text-slate-200 focus:outline-none focus:border-amber-500 transition">
            <option value="ALL">Duello: Qualsiasi (129)</option>
            <option value="YES">⚔️ Utilizzabile in Duello: SÌ (86)</option>
            <option value="NO">⛔ Non da Duello / Rituale: NO (43)</option>
          </select>
        </div>

        <!-- Filter 3: Tipologia -->
        <div>
          <label for="typeFilter" class="block text-xs font-semibold text-slate-300 mb-1 flex items-center gap-1">
            <span>🏷️</span> Tipologia Magica:
          </label>
          <select id="typeFilter" class="w-full px-3 py-2.5 rounded-xl bg-slate-950/90 border border-slate-700 text-xs text-slate-200 focus:outline-none focus:border-amber-500 transition">
            <option value="ALL">Tutte le Tipologie</option>
            <option value="Offensivo">⚔️ Offensivo / Attacco</option>
            <option value="Difensivo">🛡️ Difensivo / Scudo</option>
            <option value="Schiantesimo">⚡ Schiantesimo</option>
            <option value="Fattura">⚠️ Fattura</option>
            <option value="Maledizione">☠️ Maledizione / M. Oscura</option>
            <option value="Curativo">🌿 Curativo / Medimagia</option>
            <option value="Trasfigurazione">🪄 Trasfigurazione</option>
            <option value="Elementale">🔥 Elementale (4 Elementi)</option>
            <option value="Aritmantico">📐 Aritmantico / Tracciatura</option>
            <option value="Utilità">✨ Utilità & Cinetica</option>
          </select>
        </div>

        <!-- Filter 4: Reset Button -->
        <div class="flex items-end">
          <button id="resetAllFiltersBtn" class="w-full py-2.5 px-3 rounded-xl bg-slate-800/90 hover:bg-slate-700 text-xs font-semibold text-amber-300 border border-amber-500/30 hover:border-amber-400 transition flex items-center justify-center gap-1.5 shadow-sm">
            <span>🔄</span> Ripristina Tutti i Filtri
          </button>
        </div>

      </div>

      <!-- ROW 3: QUICK VISUAL TABS & SEGMENTED CONTROLS -->
      <div class="border-t border-slate-800/80 pt-3 space-y-3">
        
        <!-- Year Quick Tabs -->
        <div>
          <div class="text-[11px] font-semibold uppercase tracking-wider text-slate-400 mb-1.5 flex items-center justify-between">
            <span>Filtro Rapido per Anno di Corso:</span>
            <span id="resultsCountBadge" class="text-amber-400 font-code font-semibold">129 incantesimi trovati</span>
          </div>
          <div class="flex items-center gap-1.5 overflow-x-auto pb-1.5 scrollbar-none" id="yearTabsContainer">
            <button data-year="ALL" class="year-tab px-3 py-1.5 rounded-lg text-xs font-semibold transition whitespace-nowrap bg-amber-500 text-slate-950 shadow-md">
              Tutti (129)
            </button>
            <button data-year="1" class="year-tab px-3 py-1.5 rounded-lg text-xs font-semibold transition whitespace-nowrap bg-slate-800 text-slate-300 hover:bg-slate-700">
              I Anno (16)
            </button>
            <button data-year="2" class="year-tab px-3 py-1.5 rounded-lg text-xs font-semibold transition whitespace-nowrap bg-slate-800 text-slate-300 hover:bg-slate-700">
              II Anno (14)
            </button>
            <button data-year="3" class="year-tab px-3 py-1.5 rounded-lg text-xs font-semibold transition whitespace-nowrap bg-slate-800 text-slate-300 hover:bg-slate-700">
              III Anno (16)
            </button>
            <button data-year="4" class="year-tab px-3 py-1.5 rounded-lg text-xs font-semibold transition whitespace-nowrap bg-slate-800 text-slate-300 hover:bg-slate-700">
              IV Anno (20)
            </button>
            <button data-year="5" class="year-tab px-3 py-1.5 rounded-lg text-xs font-semibold transition whitespace-nowrap bg-slate-800 text-slate-300 hover:bg-slate-700">
              V Anno (24)
            </button>
            <button data-year="6,7" class="year-tab px-3 py-1.5 rounded-lg text-xs font-semibold transition whitespace-nowrap bg-slate-800 text-slate-300 hover:bg-slate-700">
              M.A.G.O. (16)
            </button>
            <button data-year="0" class="year-tab px-3 py-1.5 rounded-lg text-xs font-semibold transition whitespace-nowrap bg-slate-800 text-slate-300 hover:bg-slate-700">
              Aritmanzia & Trattati (23)
            </button>
          </div>
        </div>

        <!-- Duel Segmented Buttons & Valence Pills -->
        <div class="flex flex-wrap items-center justify-between gap-3 pt-1 text-xs">
          <!-- Segmented Duel Controls -->
          <div class="flex items-center gap-2">
            <span class="text-slate-400 font-medium">Duello:</span>
            <div class="inline-flex rounded-xl bg-slate-950 p-1 border border-slate-800 shadow-inner" id="duelSegmentedGroup">
              <button data-duel="ALL" class="duel-seg-btn px-3 py-1.5 rounded-lg text-xs font-semibold bg-amber-500/20 text-amber-300 border border-amber-500/40 transition">
                Tutti (129)
              </button>
              <button data-duel="YES" class="duel-seg-btn px-3 py-1.5 rounded-lg text-xs font-semibold text-slate-400 hover:text-emerald-300 hover:bg-slate-800/80 transition">
                ⚔️ Da Duello: SÌ (86)
              </button>
              <button data-duel="NO" class="duel-seg-btn px-3 py-1.5 rounded-lg text-xs font-semibold text-slate-400 hover:text-rose-300 hover:bg-slate-800/80 transition">
                ⛔ Non in Duello: NO (43)
              </button>
            </div>
          </div>

          <!-- Quick Valence Filter Pills -->
          <div class="flex items-center gap-1 flex-wrap">
            <span class="text-slate-400 font-medium mr-1">Valenza:</span>
            <button data-val="ALL" class="val-pill px-2.5 py-1 rounded bg-amber-500/20 text-amber-300 border border-amber-500/30 font-code font-semibold text-[11px]">Tutte</button>
            <button data-val="1" class="val-pill px-2 py-1 rounded bg-slate-800/80 text-slate-300 hover:bg-slate-700 font-code text-[11px]">V1</button>
            <button data-val="2" class="val-pill px-2 py-1 rounded bg-slate-800/80 text-slate-300 hover:bg-slate-700 font-code text-[11px]">V2</button>
            <button data-val="3" class="val-pill px-2 py-1 rounded bg-slate-800/80 text-slate-300 hover:bg-slate-700 font-code text-[11px]">V3</button>
            <button data-val="4" class="val-pill px-2 py-1 rounded bg-slate-800/80 text-slate-300 hover:bg-slate-700 font-code text-[11px]">V4</button>
            <button data-val="5" class="val-pill px-2 py-1 rounded bg-slate-800/80 text-slate-300 hover:bg-slate-700 font-code text-[11px]">V5</button>
            <button data-val="6" class="val-pill px-2 py-1 rounded bg-slate-800/80 text-slate-300 hover:bg-slate-700 font-code text-[11px]">V6</button>
            <button data-val="7" class="val-pill px-2 py-1 rounded bg-slate-800/80 text-slate-300 hover:bg-slate-700 font-code text-[11px]">V7</button>
            <button data-val="8" class="val-pill px-2 py-1 rounded bg-slate-800/80 text-slate-300 hover:bg-slate-700 font-code text-[11px]">V8</button>
            <button data-val="9" class="val-pill px-2 py-1 rounded bg-slate-800/80 text-slate-300 hover:bg-slate-700 font-code text-[11px]">V9</button>
          </div>
        </div>

      </div>

    </div>
  </section>

  <!-- MAIN CARDS GRID CONTAINER -->'''

html = old_controls_pattern.sub(new_controls_html, html)

# 2. Update JavaScript logic for synchronized filtering and highlight
old_js_start = html.find('// --- Application State ---')
new_js = '''// --- Application State ---
    let activeYear = "ALL";
    let activeType = "ALL";
    let activeDuel = "ALL";
    let activeValence = "ALL";
    let searchQuery = "";

    // Pythagorean table reference
    const PYTHAGOREAN = {
      'A':1, 'B':2, 'C':3, 'D':4, 'E':5, 'F':6, 'G':7, 'H':8, 'I':9,
      'J':1, 'K':2, 'L':3, 'M':4, 'N':5, 'O':6, 'P':7, 'Q':8, 'R':9,
      'S':1, 'T':2, 'U':3, 'V':4, 'W':5, 'X':6, 'Y':7, 'Z':8
    };

    const GEOMETRY_MAP = {
      1: "Circonferenza (Acqua)",
      2: "Angolo / Linea",
      3: "Triangolo equilatero",
      4: "Quadrato",
      5: "Pentagono regolare (Aria)",
      6: "Esagono regolare (Terra)",
      7: "Ettagono regolare (Opposizione)",
      8: "Ottagono regolare (Fuoco)",
      9: "Ellisse (Reincarnazione)"
    };

    const ELEMENT_MAP = {
      1: "Acqua (Formula Coerceo)",
      5: "Aria (Formula Finge)",
      6: "Terra (Formula Adultero)",
      8: "Fuoco (Formula Plasma)"
    };

    // DOM Elements
    const spellsGrid = document.getElementById("spellsGrid");
    const noResultsState = document.getElementById("noResultsState");
    const searchInput = document.getElementById("searchInput");
    const clearSearchBtn = document.getElementById("clearSearchBtn");
    const yearSelect = document.getElementById("yearSelect");
    const typeFilter = document.getElementById("typeFilter");
    const duelFilter = document.getElementById("duelFilter");
    const yearTabs = document.querySelectorAll(".year-tab");
    const duelSegBtns = document.querySelectorAll(".duel-seg-btn");
    const valPills = document.querySelectorAll(".val-pill");
    const resultsCountBadge = document.getElementById("resultsCountBadge");
    const resetAllFiltersBtn = document.getElementById("resetAllFiltersBtn");

    // Stats Elements
    const statTotal = document.getElementById("statTotal");
    const statDuel = document.getElementById("statDuel");
    const statDark = document.getElementById("statDark");
    const statArith = document.getElementById("statArith");

    // Modal Elements
    const spellModal = document.getElementById("spellModal");
    const modalCard = document.getElementById("modalCard");
    const closeModalBtn = document.getElementById("closeModalBtn");
    const modalBadges = document.getElementById("modalBadges");
    const modalTitle = document.getElementById("modalTitle");
    const modalFormula = document.getElementById("modalFormula");
    const modalEtymology = document.getElementById("modalEtymology");
    const modalDesc = document.getElementById("modalDesc");
    const modalMovement = document.getElementById("modalMovement");
    const modalDuelTactics = document.getElementById("modalDuelTactics");
    const wandPathElement = document.getElementById("wandPathElement");
    const replayWandAnimBtn = document.getElementById("replayWandAnimBtn");
    const modalValenceNum = document.getElementById("modalValenceNum");
    const modalValenceSum = document.getElementById("modalValenceSum");
    const modalOppositeNum = document.getElementById("modalOppositeNum");
    const modalRepeatMax = document.getElementById("modalRepeatMax");
    const modalRepeatStatus = document.getElementById("modalRepeatStatus");
    const modalGeometry = document.getElementById("modalGeometry");
    const modalLetterBreakdown = document.getElementById("modalLetterBreakdown");
    const modalArithNotes = document.getElementById("modalArithNotes");

    // Calculator Elements
    const calculatorModal = document.getElementById("calculatorModal");
    const calcCard = document.getElementById("calcCard");
    const openCalculatorBtn = document.getElementById("openCalculatorBtn");
    const closeCalcBtn = document.getElementById("closeCalcBtn");
    const calcInput = document.getElementById("calcInput");
    const calcNorm = document.getElementById("calcNorm");
    const calcLetters = document.getElementById("calcLetters");
    const calcSum = document.getElementById("calcSum");
    const calcValence = document.getElementById("calcValence");
    const calcOpposite = document.getElementById("calcOpposite");
    const calcFigure = document.getElementById("calcFigure");
    const calcElement = document.getElementById("calcElement");

    // Quick Duel Button
    const quickDuelToggle = document.getElementById("quickDuelToggle");
    const quickDuelText = document.getElementById("quickDuelText");

    // Update Global Statistics
    function updateStats() {
      statTotal.textContent = SPELLS_DATA.length;
      statDuel.textContent = SPELLS_DATA.filter(s => s.inDuello).length;
      statDark.textContent = SPELLS_DATA.filter(s => s.tipologia.includes("Maledizione") || s.tipologia.includes("Fattura")).length;
      statArith.textContent = SPELLS_DATA.filter(s => s.anno === 0 || s.tipologia.includes("Aritmantico") || s.tipologia.includes("Elementale") || s.tipologia.includes("Trasfigurazione")).length;
    }

    // Highlighting helper
    function highlightText(text, query) {
      if (!query || query.trim().length === 0) return text;
      const clean = query.trim().replace(/[.*+?^${}()|[\\]\\\\]/g, '\\\\$&');
      const regex = new RegExp(`(${clean})`, 'gi');
      return text.replace(regex, '<mark class="bg-amber-400/40 text-amber-200 px-0.5 rounded font-semibold">$1</mark>');
    }

    // Filter Logic
    function getFilteredSpells() {
      return SPELLS_DATA.filter(spell => {
        // 1. Year filter
        if (activeYear !== "ALL") {
          const allowedYears = activeYear.split(",").map(Number);
          if (!allowedYears.includes(spell.anno)) return false;
        }

        // 2. Type filter
        if (activeType !== "ALL") {
          if (!spell.tipologia.toLowerCase().includes(activeType.toLowerCase())) return false;
        }

        // 3. Duel filter
        if (activeDuel === "YES" && !spell.inDuello) return false;
        if (activeDuel === "NO" && spell.inDuello) return false;

        // 4. Valence filter
        if (activeValence !== "ALL" && spell.valenza !== Number(activeValence)) return false;

        // 5. Search Query (searches in: name, formula, description, movement, type)
        if (searchQuery.trim() !== "") {
          const q = searchQuery.toLowerCase();
          const matchName = spell.nome.toLowerCase().includes(q);
          const matchFormula = spell.formula.toLowerCase().includes(q);
          const matchDesc = spell.descrizione.toLowerCase().includes(q);
          const matchMov = spell.movimento.toLowerCase().includes(q);
          const matchTipo = spell.tipologia.toLowerCase().includes(q);
          if (!matchName && !matchFormula && !matchDesc && !matchMov && !matchTipo) return false;
        }

        return true;
      });
    }

    // Render Cards
    function renderSpells() {
      const filtered = getFilteredSpells();
      resultsCountBadge.textContent = `${filtered.length} incantesimi trovati`;

      if (filtered.length === 0) {
        spellsGrid.innerHTML = "";
        noResultsState.classList.remove("hidden");
        return;
      }

      noResultsState.classList.add("hidden");

      spellsGrid.innerHTML = filtered.map(spell => {
        // Type color badge
        let typeBadgeClass = "bg-amber-500/10 text-amber-300 border-amber-500/30";
        if (spell.tipologia.includes("Offensivo") || spell.tipologia.includes("Schiantesimo")) {
          typeBadgeClass = "bg-rose-500/10 text-rose-300 border-rose-500/30";
        } else if (spell.tipologia.includes("Difensivo")) {
          typeBadgeClass = "bg-sky-500/10 text-sky-300 border-sky-500/30";
        } else if (spell.tipologia.includes("Maledizione")) {
          typeBadgeClass = "bg-purple-500/15 text-purple-300 border-purple-500/30";
        } else if (spell.tipologia.includes("Curativo")) {
          typeBadgeClass = "bg-emerald-500/10 text-emerald-300 border-emerald-500/30";
        } else if (spell.tipologia.includes("Elementale")) {
          typeBadgeClass = "bg-orange-500/10 text-orange-300 border-orange-500/30";
        } else if (spell.tipologia.includes("Trasfigurazione")) {
          typeBadgeClass = "bg-teal-500/10 text-teal-300 border-teal-500/30";
        }

        // Duel badge
        const duelBadge = spell.inDuello
          ? `<span class="inline-flex items-center gap-1 px-2.5 py-0.5 rounded-full text-[11px] font-bold bg-emerald-500/15 text-emerald-300 border border-emerald-500/30 shadow-sm">
               <span>⚔️</span> Duello: SÌ
             </span>`
          : `<span class="inline-flex items-center gap-1 px-2.5 py-0.5 rounded-full text-[11px] font-bold bg-slate-800 text-slate-400 border border-slate-700">
               <span>⛔</span> Duello: NO
             </span>`;

        return `
          <div class="glass-card rounded-2xl p-5 flex flex-col justify-between cursor-pointer group" onclick="openSpellDetails('${spell.id}')">
            <div>
              <!-- Header info: Year & Duel -->
              <div class="flex items-center justify-between gap-2 mb-3">
                <span class="px-2.5 py-0.5 rounded-md text-xs font-semibold bg-slate-800/90 text-amber-300 border border-slate-700">
                  ${spell.annoLabel}
                </span>
                ${duelBadge}
              </div>

              <!-- Spell Name with Highlight -->
              <h3 class="text-lg font-bold font-magic text-slate-100 group-hover:text-amber-300 transition-colors line-clamp-1 mb-1">
                ${highlightText(spell.nome, searchQuery)}
              </h3>

              <!-- Formula Box with Highlight -->
              <div class="flex items-center gap-2 mb-3">
                <span class="font-code text-xs px-2.5 py-1 rounded-lg bg-amber-500/10 border border-amber-500/25 text-amber-200 font-bold tracking-wide">
                  ⚡ ${highlightText(spell.formula, searchQuery)}
                </span>
                <span class="text-xs px-2 py-0.5 rounded border ${typeBadgeClass} truncate max-w-[150px]">
                  ${spell.tipologia.split('/')[0].trim()}
                </span>
              </div>

              <!-- Description with Highlight on matched search query -->
              <p class="text-xs text-slate-300 line-clamp-3 leading-relaxed mb-4">
                ${highlightText(spell.descrizione, searchQuery)}
              </p>
            </div>

            <!-- Footer Arithmantic Summary -->
            <div class="border-t border-slate-800/80 pt-3 space-y-2">
              <div class="flex items-center justify-between text-xs">
                <div class="flex items-center gap-1.5">
                  <span class="text-slate-400">Valenza:</span>
                  <span class="font-code font-bold text-amber-400 bg-amber-950/60 px-1.5 py-0.5 rounded border border-amber-700/40">
                    V${spell.valenza}
                  </span>
                  <span class="text-[11px] text-slate-400" title="Valenza opposta di simmetria">
                    (Opp. ${spell.valenzaOpposta})
                  </span>
                </div>
                <div class="text-[11px] text-sky-400 font-medium truncate max-w-[120px]" title="${spell.figuraGeometrica}">
                  ${spell.figuraGeometrica.split('(')[0].trim()}
                </div>
              </div>

              <!-- Wand Movement snippet -->
              <div class="text-[11px] text-slate-400 line-clamp-1 italic bg-slate-950/40 px-2 py-1 rounded">
                🪄 ${highlightText(spell.movimento, searchQuery)}
              </div>

              <div class="pt-1 flex items-center justify-end text-xs text-amber-400 font-semibold group-hover:translate-x-1 transition-transform">
                <span>Consulta Scheda & Gesto →</span>
              </div>
            </div>
          </div>
        `;
      }).join("");
    }

    // Modal Details Opener
    window.openSpellDetails = function(spellId) {
      const spell = SPELLS_DATA.find(s => s.id === spellId);
      if (!spell) return;

      modalTitle.textContent = spell.nome;
      modalFormula.textContent = spell.formula;
      modalEtymology.textContent = spell.etimologia || "";
      modalDesc.textContent = spell.descrizione;
      modalMovement.textContent = spell.movimento;

      // Badges
      let badgesHtml = `
        <span class="px-3 py-1 rounded-full text-xs font-bold bg-amber-500/20 text-amber-300 border border-amber-500/40">
          ${spell.annoLabel}
        </span>
        <span class="px-3 py-1 rounded-full text-xs font-bold bg-slate-800 text-slate-200 border border-slate-700">
          ${spell.tipologia}
        </span>
      `;
      if (spell.inDuello) {
        badgesHtml += `
          <span class="px-3 py-1 rounded-full text-xs font-bold bg-emerald-500/20 text-emerald-300 border border-emerald-500/40">
            ⚔️ Abilitato in Duello
          </span>
        `;
      } else {
        badgesHtml += `
          <span class="px-3 py-1 rounded-full text-xs font-bold bg-rose-500/20 text-rose-300 border border-rose-500/40">
            ⛔ Non Utilizzabile in Duello
          </span>
        `;
      }
      modalBadges.innerHTML = badgesHtml;

      // Tactical Duello Notes
      modalDuelTactics.innerHTML = `<strong>Tattica di Duello:</strong> ${spell.duelloNote}`;

      // Arithmancy breakdown
      modalValenceNum.textContent = spell.valenza;
      modalValenceSum.textContent = `Somma: ${spell.sommaLettere}`;
      modalOppositeNum.textContent = spell.valenzaOpposta;
      modalRepeatMax.textContent = spell.ripetibile ? `${spell.maxRipetizioni} volte` : "1 volta";
      modalRepeatStatus.textContent = spell.ripetibile ? "Incanto Ripetibile" : "Irripetibile";
      modalGeometry.textContent = spell.figuraGeometrica;

      // Letter breakdown computation for modal
      const letters = spell.formula.toUpperCase().split("").filter(c => PYTHAGOREAN[c]);
      const breakdown = letters.map(c => `${c}=${PYTHAGOREAN[c]}`).join(" + ");
      modalLetterBreakdown.textContent = `${breakdown} = ${spell.sommaLettere} ➔ Riduzione: Valenza ${spell.valenza}`;
      modalArithNotes.textContent = spell.noteAritmantiche || "";

      // Set Wand SVG Path & trigger animation
      wandPathElement.setAttribute("d", spell.movimentoSvg || "M 30,75 L 120,75");
      animateWandPath();

      // Show modal
      spellModal.classList.remove("hidden");
      setTimeout(() => {
        spellModal.classList.remove("opacity-0");
        modalCard.classList.remove("scale-95");
      }, 10);
    };

    function animateWandPath() {
      wandPathElement.classList.remove("wand-path-anim");
      void wandPathElement.offsetWidth; // trigger reflow
      wandPathElement.classList.add("wand-path-anim");
    }

    replayWandAnimBtn.addEventListener("click", animateWandPath);

    function closeModal() {
      spellModal.classList.add("opacity-0");
      modalCard.classList.add("scale-95");
      setTimeout(() => {
        spellModal.classList.add("hidden");
      }, 250);
    }
    closeModalBtn.addEventListener("click", closeModal);
    spellModal.addEventListener("click", (e) => {
      if (e.target === spellModal) closeModal();
    });

    // Calculator Tool Logic
    function calculateWordArithmancy(word) {
      if (!word) {
        calcNorm.textContent = "-";
        calcLetters.textContent = "-";
        calcSum.textContent = "0";
        calcValence.textContent = "-";
        calcOpposite.textContent = "-";
        calcFigure.textContent = "-";
        calcElement.textContent = "-";
        return;
      }

      const clean = word.toUpperCase().split("").filter(c => PYTHAGOREAN[c]);
      if (clean.length === 0) return;

      const sum = clean.reduce((acc, c) => acc + PYTHAGOREAN[c], 0);
      let reduced = sum;
      while (reduced > 9) {
        reduced = String(reduced).split("").reduce((acc, d) => acc + Number(d), 0);
      }
      const opposite = 5 - reduced + 5;

      calcNorm.textContent = clean.join("");
      calcLetters.textContent = clean.map(c => `${c}(${PYTHAGOREAN[c]})`).join(" + ");
      calcSum.textContent = sum;
      calcValence.textContent = reduced;
      calcOpposite.textContent = opposite;
      calcFigure.textContent = GEOMETRY_MAP[reduced] || "-";
      calcElement.textContent = ELEMENT_MAP[reduced] || `Simmetria speculare: ${opposite}`;
    }

    calcInput.addEventListener("input", (e) => {
      calculateWordArithmancy(e.target.value);
    });

    document.querySelectorAll(".calc-sample").forEach(btn => {
      btn.addEventListener("click", () => {
        calcInput.value = btn.dataset.word;
        calculateWordArithmancy(btn.dataset.word);
      });
    });

    openCalculatorBtn.addEventListener("click", () => {
      calculatorModal.classList.remove("hidden");
      setTimeout(() => {
        calculatorModal.classList.remove("opacity-0");
        calcCard.classList.remove("scale-95");
      }, 10);
      calcInput.focus();
    });

    function closeCalculator() {
      calculatorModal.classList.add("opacity-0");
      calcCard.classList.add("scale-95");
      setTimeout(() => {
        calculatorModal.classList.add("hidden");
      }, 250);
    }
    closeCalcBtn.addEventListener("click", closeCalculator);
    calculatorModal.addEventListener("click", (e) => {
      if (e.target === calculatorModal) closeCalculator();
    });

    // --- SYNCHRONIZED YEAR FILTERING ---
    function setYearFilter(yearValue) {
      activeYear = yearValue;
      if (yearSelect) yearSelect.value = yearValue;

      yearTabs.forEach(t => {
        if (t.dataset.year === yearValue) {
          t.classList.remove("bg-slate-800", "text-slate-300");
          t.classList.add("bg-amber-500", "text-slate-950", "shadow-md");
        } else {
          t.classList.remove("bg-amber-500", "text-slate-950", "shadow-md");
          t.classList.add("bg-slate-800", "text-slate-300");
        }
      });
      renderSpells();
    }

    yearSelect.addEventListener("change", (e) => {
      setYearFilter(e.target.value);
    });

    yearTabs.forEach(tab => {
      tab.addEventListener("click", () => {
        setYearFilter(tab.dataset.year);
      });
    });

    // --- SYNCHRONIZED DUELLO FILTERING ---
    function setDuelFilter(duelValue) {
      activeDuel = duelValue;
      if (duelFilter) duelFilter.value = duelValue;

      duelSegBtns.forEach(btn => {
        if (btn.dataset.duel === duelValue) {
          btn.classList.remove("text-slate-400", "border-transparent");
          btn.classList.add("bg-amber-500/20", "text-amber-300", "border", "border-amber-500/40");
        } else {
          btn.classList.remove("bg-amber-500/20", "text-amber-300", "border", "border-amber-500/40");
          btn.classList.add("text-slate-400");
        }
      });

      updateQuickDuelButton();
      renderSpells();
    }

    duelFilter.addEventListener("change", (e) => {
      setDuelFilter(e.target.value);
    });

    duelSegBtns.forEach(btn => {
      btn.addEventListener("click", () => {
        setDuelFilter(btn.dataset.duel);
      });
    });

    // Quick duel button toggle in top header
    quickDuelToggle.addEventListener("click", () => {
      if (activeDuel === "YES") {
        setDuelFilter("ALL");
      } else {
        setDuelFilter("YES");
      }
    });

    function updateQuickDuelButton() {
      if (activeDuel === "YES") {
        quickDuelToggle.classList.remove("bg-indigo-500/15", "text-indigo-300", "border-indigo-500/30");
        quickDuelToggle.classList.add("bg-emerald-500", "text-slate-950", "border-emerald-400", "font-bold");
        quickDuelText.textContent = "Duello: ATTIVO (Filtro)";
      } else {
        quickDuelToggle.classList.add("bg-indigo-500/15", "text-indigo-300", "border-indigo-500/30");
        quickDuelToggle.classList.remove("bg-emerald-500", "text-slate-950", "border-emerald-400", "font-bold");
        quickDuelText.textContent = "Solo Duello";
      }
    }

    // Valence pills event listeners
    valPills.forEach(pill => {
      pill.addEventListener("click", () => {
        valPills.forEach(p => {
          p.classList.remove("bg-amber-500/20", "text-amber-300", "border-amber-500/30", "border");
          p.classList.add("bg-slate-800/80", "text-slate-300");
        });
        pill.classList.remove("bg-slate-800/80", "text-slate-300");
        pill.classList.add("bg-amber-500/20", "text-amber-300", "border-amber-500/30", "border");

        activeValence = pill.dataset.val;
        renderSpells();
      });
    });

    // Dropdown type filter
    typeFilter.addEventListener("change", (e) => {
      activeType = e.target.value;
      renderSpells();
    });

    // Search bar event (instant search with character matching)
    searchInput.addEventListener("input", (e) => {
      searchQuery = e.target.value;
      if (searchQuery.trim() !== "") {
        clearSearchBtn.classList.remove("hidden");
      } else {
        clearSearchBtn.classList.add("hidden");
      }
      renderSpells();
    });

    clearSearchBtn.addEventListener("click", () => {
      searchInput.value = "";
      searchQuery = "";
      clearSearchBtn.classList.add("hidden");
      renderSpells();
    });

    // Reset filters handler
    function resetAllFilters() {
      activeYear = "ALL";
      activeType = "ALL";
      activeDuel = "ALL";
      activeValence = "ALL";
      searchQuery = "";
      searchInput.value = "";
      clearSearchBtn.classList.add("hidden");
      typeFilter.value = "ALL";
      
      setYearFilter("ALL");
      setDuelFilter("ALL");

      valPills.forEach(p => {
        p.classList.remove("bg-amber-500/20", "text-amber-300", "border-amber-500/30", "border");
        p.classList.add("bg-slate-800/80", "text-slate-300");
      });
      document.querySelector('.val-pill[data-val="ALL"]').classList.add("bg-amber-500/20", "text-amber-300", "border-amber-500/30", "border");

      renderSpells();
    }

    resetAllFiltersBtn?.addEventListener("click", resetAllFilters);
    document.getElementById("resetFiltersBtn")?.addEventListener("click", resetAllFilters);

    // Keyboard ESC listener
    window.addEventListener("keydown", (e) => {
      if (e.key === "Escape") {
        closeModal();
        closeCalculator();
      }
    });

    // Initial boot
    updateStats();
    renderSpells();
  </script>
</body>
</html>
'''

html = html[:old_js_start] + new_js

with open('/Users/andreamorachioli/.gemini/antigravity/scratch/portale-incantesimi/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

with open('/Users/andreamorachioli/.gemini/antigravity/brain/3a4f7fa7-8206-4f51-b303-aa9b9d9eaf5c/portale_incantesimi.html', 'w', encoding='utf-8') as f:
    f.write(html)

print('Portal UI successfully updated in both index.html and portale_incantesimi.html!')
