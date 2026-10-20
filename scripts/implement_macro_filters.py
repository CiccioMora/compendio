# -*- coding: utf-8 -*-
"""
implement_macro_filters.py
Aggiunge i macro filtri "Incantesimi" e "Rune" all'interfaccia:
- Switch macro in evidenza sopra i filtri
- Quando "Incantesimi" è attivo: si visualizzano i sotto-filtri (Anni, Duello, Tipologia, Valenze)
- Quando "Rune" è attivo: i sotto-filtri specifici degli incantesimi vengono nascosti per massima pulizia
- La searchbar rimane attiva e prominente per tutte le sezioni
- Conteggio dinamico sincronizzato
"""

import re

BASE_DIR = '/Users/andreamorachioli/.gemini/antigravity/scratch/portale-incantesimi'

# 1. Modifica index.html
with open(f'{BASE_DIR}/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

macro_html = """      <!-- TOP: PROMINENT SEARCH BAR (NOME, FORMULA, DESCRIZIONE, RUNE) -->
      <div>
        <div class="flex items-center justify-between mb-1.5">
          <label for="searchInput" class="text-xs font-bold uppercase tracking-wider text-amber-400 flex items-center gap-1.5">
            <span>🔍</span> Ricerca Globale (Incantesimi & Rune)
          </label>
          <span class="text-[11px] text-slate-400 hidden sm:inline">
            Ricerca attiva simultanea su: <strong>Nome</strong>, <strong>Formula</strong>, <strong>Descrizione</strong>, <strong>Movimento</strong> e <strong>Rune</strong>
          </span>
        </div>
        <div class="relative">
          <span class="absolute inset-y-0 left-0 pl-3.5 flex items-center pointer-events-none text-slate-400 text-lg">
            ⚡
          </span>
          <input 
            type="text" 
            id="searchInput" 
            placeholder="Cerca per nome, formula, significato runico, valenza o parola chiave..." 
            class="w-full pl-11 pr-10 py-3 rounded-xl bg-slate-950/90 border border-slate-700/90 text-sm text-slate-100 placeholder-slate-500 focus:outline-none focus:border-amber-500 focus:ring-2 focus:ring-amber-500/20 transition shadow-inner"
          >
          <button id="clearSearchBtn" title="Cancella ricerca" class="absolute inset-y-0 right-0 pr-3.5 flex items-center text-slate-500 hover:text-amber-300 transition hidden text-base font-bold">
            ✕
          </button>
        </div>
      </div>

      <!-- MACRO FILTERS SWITCHER (INCANTESIMI / RUNE) -->
      <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-3 pt-1 border-b border-slate-800/80 pb-3">
        <div class="flex items-center gap-2.5 flex-wrap">
          <span class="text-xs font-bold uppercase tracking-wider text-slate-400">Archivio:</span>
          <div class="inline-flex rounded-xl bg-slate-950 p-1 border border-slate-800 shadow-inner" id="macroFilterGroup">
            <button type="button" data-macro="spells" id="macroSpellsBtn" class="macro-btn px-4 py-2 rounded-lg text-xs font-bold transition flex items-center gap-2 bg-amber-500 text-slate-950 shadow-md">
              <span>🪄</span>
              <span id="macroSpellsText">Incantesimi (177)</span>
            </button>
            <button type="button" data-macro="runes" id="macroRunesBtn" class="macro-btn px-4 py-2 rounded-lg text-xs font-bold transition flex items-center gap-2 text-slate-400 hover:text-indigo-300 hover:bg-slate-900">
              <span>ᛟ</span>
              <span id="macroRunesText">Rune (25)</span>
            </button>
          </div>
        </div>

        <!-- Macro Context Hint -->
        <div class="text-xs text-slate-400 flex items-center gap-2">
          <span id="activeMacroHint" class="text-slate-400 text-[11px]">Visualizzazione: <strong class="text-amber-300">177 Incantesimi Didattici</strong></span>
        </div>
      </div>

      <!-- SPELL SUB-FILTERS CONTAINER (VISIBILE SOLO IN SEZIONE INCANTESIMI) -->
      <div id="spellSubFilters" class="space-y-4">
        <!-- FILTER CONTROLS GRID (ANNO, DUELLO, TIPOLOGIA, RESET) -->
        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-3 pt-1">
          
          <!-- Filter 1: Anno di Studio -->
          <div>
            <label for="yearSelect" class="block text-xs font-semibold text-slate-300 mb-1 flex items-center gap-1">
              <span>📅</span> Filtro Anno di Corso:
            </label>
            <select id="yearSelect" class="w-full px-3 py-2.5 rounded-xl bg-slate-950/90 border border-slate-700 text-xs text-slate-200 focus:outline-none focus:border-amber-500 transition">
              <option value="ALL">Tutti gli Incantesimi (177)</option>
              <option value="1">I Anno (24)</option>
              <option value="2">II Anno (15)</option>
              <option value="3">III Anno (18)</option>
              <option value="4">IV Anno (16)</option>
              <option value="5">V Anno (13)</option>
              <option value="6">VI Anno (43)</option>
              <option value="7">VII Anno (31)</option>
              <option value="0">Altri (17)</option>
            </select>
          </div>

          <!-- Filter 2: Utilizzo in Duello -->
          <div>
            <label for="duelFilter" class="block text-xs font-semibold text-slate-300 mb-1 flex items-center gap-1">
              <span>⚔️</span> Utilizzo in Duello:
            </label>
            <select id="duelFilter" class="w-full px-3 py-2.5 rounded-xl bg-slate-950/90 border border-slate-700 text-xs text-slate-200 focus:outline-none focus:border-amber-500 transition">
              <option value="ALL">Duello: Qualsiasi (177)</option>
              <option value="YES">⚔️ Utilizzabile in Duello: SÌ (100)</option>
              <option value="NO">⛔ Non da Duello / Rituale: NO (77)</option>
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
              <span id="resultsCountBadge" class="text-amber-400 font-code font-semibold">177 incantesimi trovati</span>
            </div>
            <div class="flex items-center gap-1.5 overflow-x-auto pb-1.5 scrollbar-none" id="yearTabsContainer">
              <button data-year="ALL" class="year-tab px-3 py-1.5 rounded-lg text-xs font-semibold transition whitespace-nowrap bg-amber-500 text-slate-950 shadow-md">
                Tutti (177)
              </button>
              <button data-year="1" class="year-tab px-3 py-1.5 rounded-lg text-xs font-semibold transition whitespace-nowrap bg-slate-800 text-slate-300 hover:bg-slate-700">
                I Anno (24)
              </button>
              <button data-year="2" class="year-tab px-3 py-1.5 rounded-lg text-xs font-semibold transition whitespace-nowrap bg-slate-800 text-slate-300 hover:bg-slate-700">
                II Anno (15)
              </button>
              <button data-year="3" class="year-tab px-3 py-1.5 rounded-lg text-xs font-semibold transition whitespace-nowrap bg-slate-800 text-slate-300 hover:bg-slate-700">
                III Anno (18)
              </button>
              <button data-year="4" class="year-tab px-3 py-1.5 rounded-lg text-xs font-semibold transition whitespace-nowrap bg-slate-800 text-slate-300 hover:bg-slate-700">
                IV Anno (16)
              </button>
              <button data-year="5" class="year-tab px-3 py-1.5 rounded-lg text-xs font-semibold transition whitespace-nowrap bg-slate-800 text-slate-300 hover:bg-slate-700">
                V Anno (13)
              </button>
              <button data-year="6" class="year-tab px-3 py-1.5 rounded-lg text-xs font-semibold transition whitespace-nowrap bg-slate-800 text-slate-300 hover:bg-slate-700">
                VI Anno (43)
              </button>
              <button data-year="7" class="year-tab px-3 py-1.5 rounded-lg text-xs font-semibold transition whitespace-nowrap bg-slate-800 text-slate-300 hover:bg-slate-700">
                VII Anno (31)
              </button>
              <button data-year="0" class="year-tab px-3 py-1.5 rounded-lg text-xs font-semibold transition whitespace-nowrap bg-slate-800 text-slate-300 hover:bg-slate-700">
                Altri (17)
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
                  Tutti (177)
                </button>
                <button data-duel="YES" class="duel-seg-btn px-3 py-1.5 rounded-lg text-xs font-semibold text-slate-400 hover:text-emerald-300 hover:bg-slate-800/80 transition">
                  ⚔️ Da Duello: SÌ (100)
                </button>
                <button data-duel="NO" class="duel-seg-btn px-3 py-1.5 rounded-lg text-xs font-semibold text-slate-400 hover:text-rose-300 hover:bg-slate-800/80 transition">
                  ⛔ Non da Duello: NO (77)
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
      </div>"""

# Sostituisci il blocco filtri dentro <div class="glass-panel p-5 sm:p-6 rounded-2xl border border-amber-500/25 shadow-2xl space-y-4">
search_start = html.find('<!-- TOP: PROMINENT SEARCH BAR (NOME, FORMULA, DESCRIZIONE) -->')
search_end = html.find('<!-- MAIN CARDS GRID CONTAINER -->')

if search_start != -1 and search_end != -1:
    # Trova la chiusura della glass-panel
    div_end = html.rfind('</div>\n  </section>', search_start, search_end)
    old_section = html[search_start:div_end]
    html = html[:search_start] + macro_html + "\n    " + html[div_end:]
    print("Blocco filtri in index.html sostituito con successo.")
else:
    print("ERRORE: Marcatori non trovati in index.html")

with open(f'{BASE_DIR}/index.html', 'w', encoding='utf-8') as f:
    f.write(html)


# 2. Modifica app.js
with open(f'{BASE_DIR}/app.js', 'r', encoding='utf-8') as f:
    app_js = f.read()

# Aggiorna Application State
app_js = re.sub(
    r'// --- Application State ---\s+let activeYear = "ALL";',
    '// --- Application State ---\n    let activeMacro = "spells"; // "spells" | "runes"\n    let activeYear = "ALL";',
    app_js
)

# Aggiungi elementi DOM per Macro Filtri se non presenti
if "const macroSpellsBtn" not in app_js:
    dom_injection = """    // Macro Filter Elements
    const macroSpellsBtn = document.getElementById("macroSpellsBtn");
    const macroRunesBtn = document.getElementById("macroRunesBtn");
    const spellSubFilters = document.getElementById("spellSubFilters");
    const activeMacroHint = document.getElementById("activeMacroHint");
    const macroSpellsText = document.getElementById("macroSpellsText");
    const macroRunesText = document.getElementById("macroRunesText");
"""
    app_js = app_js.replace(
        '    // DOM Elements\n    const spellsGrid',
        dom_injection + '\n    // DOM Elements\n    const spellsGrid'
    )

# Aggiorna matchesSearch helper
matches_helper = """    // Helper per ricerca universale su ogni scheda (incantesimo o runa)
    function matchesQuery(item, query) {
      if (!query || query.trim() === "") return true;
      const q = query.trim().toLowerCase();
      const matchName = (item.nome || "").toLowerCase().includes(q);
      const matchFormula = (item.formula || "").toLowerCase().includes(q);
      const matchDesc = (item.descrizione || "").toLowerCase().includes(q);
      const matchMov = (item.movimento || "").toLowerCase().includes(q);
      const matchTipo = (item.tipologia || "").toLowerCase().includes(q);
      const matchRune = (item.runeAssociate || "").toLowerCase().includes(q);
      const matchAett = (item.aett || "").toLowerCase().includes(q);
      const matchSimbolo = (item.simbolo || "").toLowerCase().includes(q);
      const matchLettera = (item.lettera || "").toLowerCase().includes(q);
      const matchPos = item.posizioneAlfabeto ? `pos. ${item.posizioneAlfabeto}`.toLowerCase().includes(q) : false;
      const matchVal = `v${item.valenza}`.toLowerCase().includes(q) || `valenza ${item.valenza}`.toLowerCase().includes(q);

      return matchName || matchFormula || matchDesc || matchMov || matchTipo || matchRune || matchAett || matchSimbolo || matchLettera || matchPos || matchVal;
    }

    // Aggiornamento badge live sui macro bottoni durante la ricerca
    function updateMacroButtonBadges() {
      const q = searchQuery.trim().toLowerCase();
      let spellsCount = 0;
      let runesCount = 0;

      if (q === "") {
        spellsCount = SPELLS_DATA.filter(s => !s.isRune).length;
        runesCount = SPELLS_DATA.filter(s => s.isRune).length;
      } else {
        spellsCount = SPELLS_DATA.filter(s => !s.isRune && matchesQuery(s, q)).length;
        runesCount = SPELLS_DATA.filter(s => s.isRune && matchesQuery(s, q)).length;
      }

      if (macroSpellsText) macroSpellsText.textContent = `Incantesimi (${spellsCount})`;
      if (macroRunesText) macroRunesText.textContent = `Rune (${runesCount})`;
    }

    // Gestore del cambio Macro Filtro
    function setMacroFilter(macro) {
      activeMacro = macro;

      if (macro === "spells") {
        macroSpellsBtn?.classList.remove("text-slate-400", "hover:text-amber-300", "hover:bg-slate-900");
        macroSpellsBtn?.classList.add("bg-amber-500", "text-slate-950", "shadow-md");

        macroRunesBtn?.classList.remove("bg-indigo-600", "text-white", "shadow-md");
        macroRunesBtn?.classList.add("text-slate-400", "hover:text-indigo-300", "hover:bg-slate-900");

        if (spellSubFilters) spellSubFilters.classList.remove("hidden");
        if (activeMacroHint) {
          activeMacroHint.innerHTML = `Visualizzazione: <strong class="text-amber-300">${SPELLS_DATA.filter(s => !s.isRune).length} Incantesimi Didattici</strong>`;
        }
      } else {
        macroRunesBtn?.classList.remove("text-slate-400", "hover:text-indigo-300", "hover:bg-slate-900");
        macroRunesBtn?.classList.add("bg-indigo-600", "text-white", "shadow-md");

        macroSpellsBtn?.classList.remove("bg-amber-500", "text-slate-950", "shadow-md");
        macroSpellsBtn?.classList.add("text-slate-400", "hover:text-amber-300", "hover:bg-slate-900");

        if (spellSubFilters) spellSubFilters.classList.add("hidden");
        if (activeMacroHint) {
          activeMacroHint.innerHTML = `Visualizzazione: <strong class="text-indigo-300">${SPELLS_DATA.filter(s => s.isRune).length} Antiche Rune Futhark</strong>`;
        }
      }

      renderSpells();
    }
"""

if "function setMacroFilter" not in app_js:
    app_js = app_js.replace(
        "    // Highlighting helper",
        matches_helper + "\n    // Highlighting helper"
    )

# Aggiorna getFilteredSpells per supportare activeMacro e matchesQuery
get_filtered_spells_code = """    // Filter Logic
    function getFilteredSpells() {
      return SPELLS_DATA.filter(spell => {
        // 0. Macro Filter (Incantesimi vs Rune)
        if (activeMacro === "spells" && spell.isRune) return false;
        if (activeMacro === "runes" && !spell.isRune) return false;

        // I filtri specifici si applicano solo nella sezione Incantesimi
        if (activeMacro === "spells") {
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
        }

        // 5. Search Query (universale per tutte le sezioni!)
        if (!matchesQuery(spell, searchQuery)) return false;

        return true;
      });
    }"""

app_js = re.sub(
    r'    // Filter Logic\s+function getFilteredSpells\(\) \{[\s\S]*?return true;\s+\}\);\s+\}',
    get_filtered_spells_code,
    app_js
)

# Aggiorna renderSpells per risultati testuali corretti
app_js = re.sub(
    r'resultsCountBadge\.textContent = `\$\{filtered\.length\} incantesimi trovati`;',
    'resultsCountBadge.textContent = activeMacro === "spells" ? `${filtered.length} incantesimi trovati` : `${filtered.length} rune trovate`;',
    app_js
)

# Aggiungi listener dei bottoni macro e chiamata a updateMacroButtonBadges
if "macroSpellsBtn?.addEventListener" not in app_js:
    listeners_code = """    // Macro Filter Listeners
    macroSpellsBtn?.addEventListener("click", () => setMacroFilter("spells"));
    macroRunesBtn?.addEventListener("click", () => setMacroFilter("runes"));
"""
    app_js = app_js.replace(
        '    // Reset filters handler',
        listeners_code + '\n    // Reset filters handler'
    )

# Aggiorna searchInput per chiamare updateMacroButtonBadges
app_js = re.sub(
    r'clearSearchBtn\.classList\.add\("hidden"\);\s+\}\s+renderSpells\(\);',
    'clearSearchBtn.classList.add("hidden");\n      }\n      updateMacroButtonBadges();\n      renderSpells();',
    app_js
)

app_js = re.sub(
    r'clearSearchBtn\.addEventListener\("click", \(\) => \{\s+searchInput\.value = "";\s+searchQuery = "";\s+clearSearchBtn\.classList\.add\("hidden"\);\s+renderSpells\(\);',
    'clearSearchBtn.addEventListener("click", () => {\n      searchInput.value = "";\n      searchQuery = "";\n      clearSearchBtn.classList.add("hidden");\n      updateMacroButtonBadges();\n      renderSpells();',
    app_js
)

with open(f'{BASE_DIR}/app.js', 'w', encoding='utf-8') as f:
    f.write(app_js)

print("app.js aggiornato con la logica dei Macro Filtri.")
