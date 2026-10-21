// app.js - Logica Applicativa e Interattività del Portale degli Incantesimi

// --- Application State ---
    let activeMacro = "spells"; // "spells" | "runes"
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

    // Macro Filter Elements
    const macroSpellsBtn = document.getElementById("macroSpellsBtn");
    const macroRunesBtn = document.getElementById("macroRunesBtn");
    const spellSubFilters = document.getElementById("spellSubFilters");
    const activeMacroHint = document.getElementById("activeMacroHint");
    const macroSpellsText = document.getElementById("macroSpellsText");
    const macroRunesText = document.getElementById("macroRunesText");

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
    const wandCanvasBox = document.getElementById("wandCanvasBox");
    const wandTrackLabel = document.getElementById("wandTrackLabel");
    let isCompassActive = false;
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

    function updateFilterCounts() {
      const yearCounts = {};
      const spellItems = SPELLS_DATA.filter(s => !s.isRune);
      spellItems.forEach(s => {
        yearCounts[s.anno] = (yearCounts[s.anno] || 0) + 1;
      });

      const totalSpells = spellItems.length;
      const yearTabLabels = {
        "ALL": `Tutti (${totalSpells})`,
        "1": `I Anno (${yearCounts[1] || 0})`,
        "2": `II Anno (${yearCounts[2] || 0})`,
        "3": `III Anno (${yearCounts[3] || 0})`,
        "4": `IV Anno (${yearCounts[4] || 0})`,
        "5": `V Anno (${yearCounts[5] || 0})`,
        "6": `VI Anno (${yearCounts[6] || 0})`,
        "7": `VII Anno (${yearCounts[7] || 0})`,
        "0": `Altri (${yearCounts[0] || 0})`
      };

      yearTabs.forEach(tab => {
        const yr = tab.getAttribute("data-year");
        if (yearTabLabels[yr]) {
          tab.textContent = yearTabLabels[yr];
        }
      });

      if (yearSelect) {
        Array.from(yearSelect.options).forEach(opt => {
          const yr = opt.value;
          if (yearTabLabels[yr]) {
            opt.textContent = yearTabLabels[yr];
          }
        });
      }

      const duelYes = spellItems.filter(s => s.inDuello).length;
      const duelNo = spellItems.filter(s => !s.inDuello).length;
      duelSegBtns.forEach(btn => {
        const d = btn.getAttribute("data-duel");
        if (d === "ALL") btn.textContent = `Tutti (${totalSpells})`;
        if (d === "YES") btn.textContent = `⚔️ Da Duello: SÌ (${duelYes})`;
        if (d === "NO") btn.textContent = `⛔ Non da Duello: NO (${duelNo})`;
      });

      if (duelFilter) {
        Array.from(duelFilter.options).forEach(opt => {
          if (opt.value === "ALL") opt.textContent = `Duello: Qualsiasi (${totalSpells})`;
          if (opt.value === "YES") opt.textContent = `⚔️ Utilizzabile in Duello: SÌ (${duelYes})`;
          if (opt.value === "NO") opt.textContent = `⛔ Non da Duello / Rituale: NO (${duelNo})`;
        });
      }

      updateMacroButtonBadges();
    }

    // Update Global Statistics
    function updateStats() {
      statTotal.textContent = SPELLS_DATA.length;
      statDuel.textContent = SPELLS_DATA.filter(s => s.inDuello).length;
      statDark.textContent = SPELLS_DATA.filter(s => s.tipologia.includes("Maledizione") || s.tipologia.includes("Fattura")).length;
      statArith.textContent = SPELLS_DATA.filter(s => s.anno === 0 || s.tipologia.includes("Aritmantico") || s.tipologia.includes("Elementale") || s.tipologia.includes("Trasfigurazione") || s.tipologia.includes("Celeste") || s.tipologia.includes("Botanica")).length;
      updateFilterCounts();
    }

    // Helper per ricerca universale su ogni scheda (incantesimo o runa)
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
          activeMacroHint.innerHTML = `Visualizzazione: <strong class="text-amber-300">241 Incantesimi Didattici</strong>`;
        }
      } else {
        macroRunesBtn?.classList.remove("text-slate-400", "hover:text-indigo-300", "hover:bg-slate-900");
        macroRunesBtn?.classList.add("bg-indigo-600", "text-white", "shadow-md");

        macroSpellsBtn?.classList.remove("bg-amber-500", "text-slate-950", "shadow-md");
        macroSpellsBtn?.classList.add("text-slate-400", "hover:text-amber-300", "hover:bg-slate-900");

        if (spellSubFilters) spellSubFilters.classList.add("hidden");
        if (activeMacroHint) {
          activeMacroHint.innerHTML = `Visualizzazione: <strong class="text-indigo-300">25 Antiche Rune Futhark</strong>`;
        }
      }

      renderSpells();
    }

    // Highlighting helper
    function highlightText(text, query) {
      if (!query || query.trim().length === 0) return text;
      const clean = query.trim().replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
      const regex = new RegExp(`(${clean})`, 'gi');
      return text.replace(regex, '<mark class="bg-amber-400/40 text-amber-200 px-0.5 rounded font-semibold">$1</mark>');
    }

    // Filter Logic
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
    }

    // Render Cards
    function renderSpells() {
      const filtered = getFilteredSpells();
      resultsCountBadge.textContent = activeMacro === "spells" ? `${filtered.length} incantesimi trovati` : `${filtered.length} rune trovate`;

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
        } else if (spell.tipologia.includes("Rune") || spell.isRune) {
          typeBadgeClass = "bg-indigo-500/20 text-indigo-300 border-indigo-500/40";
        }

        // Duel / Runic badge
        let duelBadge;
        if (spell.isRune) {
          duelBadge = `<span class="inline-flex items-center gap-1 px-2.5 py-0.5 rounded-full text-[11px] font-bold bg-indigo-500/20 text-indigo-300 border border-indigo-500/40 shadow-sm">
                         <span>ᛟ</span> Futhark: Pos. ${spell.posizioneAlfabeto}
                       </span>`;
        } else {
          duelBadge = spell.inDuello
            ? `<span class="inline-flex items-center gap-1 px-2.5 py-0.5 rounded-full text-[11px] font-bold bg-emerald-500/15 text-emerald-300 border border-emerald-500/30 shadow-sm">
                 <span>⚔️</span> Duello: SÌ
               </span>`
            : `<span class="inline-flex items-center gap-1 px-2.5 py-0.5 rounded-full text-[11px] font-bold bg-slate-800 text-slate-400 border border-slate-700">
                 <span>⛔</span> Duello: NO
               </span>`;
        }

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
      modalLetterBreakdown.textContent = spell.isRune 
        ? `Posizione nell'Alfabeto: ${spell.posizioneAlfabeto} ➔ Valenza Magica: ${spell.valenza} (Canone: Valenza corrisponde alla Posizione)`
        : `${breakdown} = ${spell.sommaLettere} ➔ Riduzione: Valenza ${spell.valenza}`;
      modalArithNotes.textContent = spell.noteAritmantiche || "";

      // Elemento Runa Associata nel Modale
      const modalRuneBox = document.getElementById("modalRuneAssociation");
      const modalRunePos = document.getElementById("modalRunePosition");
      if (modalRuneBox && modalRunePos) {
        modalRunePos.textContent = `Valenza ${spell.valenza}`;
        modalRuneBox.innerHTML = spell.isRune
          ? `<strong>Runa Primaria dell'Alfabeto:</strong> ${spell.nome} (${spell.aett})<br><span class="text-xs text-amber-200/90">Incantesimi in risonanza: ${spell.incantesimiAssociati || spell.runeAssociate}</span>`
          : `<strong>Runa dell'Alfabeto Associata:</strong> <span class="text-amber-300">${spell.runeAssociate || "—"}</span>`;
      }

      // Bussola Magica (Guidami / Point Me) Setup
      isCompassActive = (spell.id === "guidami");
      if (wandPathElement) {
        wandPathElement.removeAttribute("transform");
        wandPathElement.style.transition = "";
      }
      const guidePath = document.getElementById("wandGuidePath");
      if (guidePath) {
        guidePath.removeAttribute("transform");
        guidePath.style.transition = "";
      }
      const spark = document.getElementById("wandSpark");
      if (spark) {
        spark.style.transition = "";
      }
      if (wandTrackLabel) {
        wandTrackLabel.innerHTML = isCompassActive
          ? '🧭 <span class="text-amber-300 font-semibold">Bussola Magica:</span> Muovi il mouse per orientare'
          : 'Traccia Dinamica';
      }
      if (replayWandAnimBtn) {
        replayWandAnimBtn.innerHTML = isCompassActive
          ? '<span>🧭</span> Punta al Nord'
          : '<span>🔄</span> Anima Gesto';
      }

      // Configura il tracciato del gesto
      const pathData = spell.movimentoSvg || "M 30,75 L 120,75";
      wandPathElement.setAttribute("d", pathData);
      if (guidePath) guidePath.setAttribute("d", pathData);

      // Mostra prima il modale affinché le dimensioni e il layout siano attivi
      spellModal.classList.remove("hidden");
      setTimeout(() => {
        spellModal.classList.remove("opacity-0");
        modalCard.classList.remove("scale-95");
        
        // Avvia l'animazione con una breve pausa per sincronizzarsi con l'apertura
        setTimeout(() => {
          animateWandPath();
        }, 120);
      }, 15);
    };

    let wandAnimId = null;

    function animateWandPath() {
      if (!wandPathElement) return;

      // Cancella eventuale animazione precedente in corso
      if (wandAnimId) {
        cancelAnimationFrame(wandAnimId);
        wandAnimId = null;
      }

      const spark = document.getElementById("wandSpark");
      const guidePath = document.getElementById("wandGuidePath");
      const d = wandPathElement.getAttribute("d");

      if (!d || d.trim() === "") {
        if (spark) spark.style.opacity = "0";
        return;
      }

      if (guidePath) guidePath.setAttribute("d", d);

      // Calcola la lunghezza esatta del tracciato
      let totalLen = 0;
      try {
        totalLen = wandPathElement.getTotalLength();
      } catch (err) {
        totalLen = 220;
      }

      const isStationary = !totalLen || totalLen <= 0.5;

      if (isStationary) {
        wandPathElement.style.strokeDasharray = "none";
        wandPathElement.style.strokeDashoffset = "0";
      } else {
        // Imposta stroke-dasharray esattamente sulla lunghezza reale
        wandPathElement.style.strokeDasharray = `${totalLen} ${totalLen}`;
        wandPathElement.style.strokeDashoffset = `${totalLen}`;
      }

      // Posizione iniziale della scintilla
      let startPoint = { x: 75, y: 75 };
      try {
        startPoint = wandPathElement.getPointAtLength(0);
      } catch (e) {}

      if (spark) {
        spark.setAttribute("cx", startPoint.x);
        spark.setAttribute("cy", startPoint.y);
        spark.style.transition = "none";
        spark.style.opacity = "1";
        spark.setAttribute("r", "6");
      }

      // Feedback visivo sul pulsante Anima Gesto
      if (replayWandAnimBtn) {
        replayWandAnimBtn.classList.add("ring-2", "ring-amber-400", "bg-amber-500/30");
      }

      // Durata fluida proporzionata (1.2s - 1.8s)
      const duration = isStationary ? 1200 : Math.min(Math.max(totalLen * 5.5, 1100), 1800);
      const startTime = performance.now();

      function step(now) {
        const elapsed = now - startTime;
        const progress = Math.min(elapsed / duration, 1);

        if (isStationary) {
          if (spark) {
            spark.setAttribute("cx", 75);
            spark.setAttribute("cy", 75);
            const pulse = 6 + Math.sin(progress * Math.PI) * 2.5;
            spark.setAttribute("r", pulse.toFixed(1));
          }
        } else {
          // Curva di accelerazione/decelerazione cubica fluida
          const ease = progress < 0.5
            ? 4 * progress * progress * progress
            : 1 - Math.pow(-2 * progress + 2, 3) / 2;

          const currentLen = ease * totalLen;
          wandPathElement.style.strokeDashoffset = `${Math.max(0, totalLen - currentLen)}`;

          if (spark) {
            try {
              const pt = wandPathElement.getPointAtLength(Math.min(currentLen, totalLen));
              spark.setAttribute("cx", pt.x);
              spark.setAttribute("cy", pt.y);
            } catch (e) {}
          }
        }

        if (progress < 1) {
          wandAnimId = requestAnimationFrame(step);
        } else {
          wandAnimId = null;
          wandPathElement.style.strokeDashoffset = "0";
          if (spark) {
            spark.style.transition = "opacity 0.6s ease, transform 0.3s ease";
            spark.style.opacity = "0.75";
            spark.setAttribute("r", "6");
          }
          if (replayWandAnimBtn) {
            replayWandAnimBtn.classList.remove("ring-2", "ring-amber-400", "bg-amber-500/30");
          }
        }
      }

      wandAnimId = requestAnimationFrame(step);
    }

    replayWandAnimBtn.addEventListener("click", () => {
      if (isCompassActive) {
        wandPathElement.removeAttribute("transform");
        const guidePath = document.getElementById("wandGuidePath");
        if (guidePath) guidePath.removeAttribute("transform");
        const spark = document.getElementById("wandSpark");
        if (spark) {
          spark.setAttribute("cx", "75");
          spark.setAttribute("cy", "25");
        }
      }
      animateWandPath();
    });

    // Compass Interactive Mouse Tracking (Guidami / Point Me)
    if (wandCanvasBox) {
      wandCanvasBox.addEventListener("mousemove", (e) => {
        if (!isCompassActive) return;
        const svg = document.getElementById("wandSvgCanvas");
        if (!svg) return;
        const rect = svg.getBoundingClientRect();
        const mouseX = ((e.clientX - rect.left) / rect.width) * 150;
        const mouseY = ((e.clientY - rect.top) / rect.height) * 150;

        const dx = mouseX - 75;
        const dy = mouseY - 75;
        if (Math.hypot(dx, dy) < 4) return;

        const angleRad = Math.atan2(dy, dx);
        const angleDeg = (angleRad * 180 / Math.PI) + 90;

        wandPathElement.setAttribute("transform", `rotate(${angleDeg.toFixed(1)} 75 75)`);
        const guidePath = document.getElementById("wandGuidePath");
        if (guidePath) guidePath.setAttribute("transform", `rotate(${angleDeg.toFixed(1)} 75 75)`);

        const spark = document.getElementById("wandSpark");
        if (spark) {
          const sparkX = 75 + 50 * Math.sin(angleDeg * Math.PI / 180);
          const sparkY = 75 - 50 * Math.cos(angleDeg * Math.PI / 180);
          spark.setAttribute("cx", sparkX.toFixed(1));
          spark.setAttribute("cy", sparkY.toFixed(1));
          spark.style.opacity = "1";
        }
      });

      wandCanvasBox.addEventListener("mouseleave", () => {
        if (!isCompassActive) return;
        wandPathElement.style.transition = "transform 0.45s cubic-bezier(0.34, 1.56, 0.64, 1)";
        const guidePath = document.getElementById("wandGuidePath");
        if (guidePath) guidePath.style.transition = "transform 0.45s cubic-bezier(0.34, 1.56, 0.64, 1)";
        const spark = document.getElementById("wandSpark");
        if (spark) spark.style.transition = "cx 0.45s ease-out, cy 0.45s ease-out";

        wandPathElement.setAttribute("transform", "rotate(0 75 75)");
        if (guidePath) guidePath.setAttribute("transform", "rotate(0 75 75)");
        if (spark) {
          spark.setAttribute("cx", "75");
          spark.setAttribute("cy", "25");
        }

        setTimeout(() => {
          wandPathElement.style.transition = "";
          if (guidePath) guidePath.style.transition = "";
          if (spark) spark.style.transition = "";
        }, 450);
      });
    }

    function closeModal() {
      if (wandAnimId) {
        cancelAnimationFrame(wandAnimId);
        wandAnimId = null;
      }
      isCompassActive = false;
      if (wandPathElement) {
        wandPathElement.removeAttribute("transform");
        wandPathElement.style.transition = "";
      }
      const guidePath = document.getElementById("wandGuidePath");
      if (guidePath) {
        guidePath.removeAttribute("transform");
        guidePath.style.transition = "";
      }
      const spark = document.getElementById("wandSpark");
      if (spark) {
        spark.style.transition = "";
      }
      if (wandTrackLabel) wandTrackLabel.textContent = "Traccia Dinamica";
      if (replayWandAnimBtn) replayWandAnimBtn.innerHTML = '<span>🔄</span> Anima Gesto';

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

    // Dizionario di Forzatura Canonica (Codex Arithmantiae & Bridget Wenlock)
    const CANONICAL_OVERRIDES = {
      "FINITE INCANTATEM": { valenza: 7, reason: "Valenza 7 forzata da Canone (Controincantesimo Supremo - Bridget Wenlock)", element: "Controincantesimo Supremo (Numero 7)" },
      "FINITE": { valenza: 7, reason: "Valenza 7 forzata da Canone (Controincantesimo - Bridget Wenlock)", element: "Controincantesimo (Numero 7)" },
      "INCENDIO": { valenza: 8, reason: "Valenza 8 forzata da Canone (Elemento Fuoco nel Codex Arithmantiae)", element: "Fuoco (Numero 8 - Formula Plasma)" },
      "AGUAMENTI": { valenza: 1, reason: "Valenza 1 forzata da Canone (Elemento Acqua nel Codex Arithmantiae)", element: "Acqua (Numero 1 - Formula Coerceo)" },
      "VENTUS": { valenza: 5, reason: "Valenza 5 forzata da Canone (Elemento Aria nel Codex Arithmantiae)", element: "Aria (Numero 5 - Formula Finge)" }
    };

    const VALENCE_RUNES_MAP = {
      1: "ᚠ Fehu (Pos. 1ª)",
      2: "ᚢ Uruz (Pos. 2ª)",
      3: "ᚦ Thurisaz (Pos. 3ª)",
      4: "ᚨ Ansuz (Pos. 4ª)",
      5: "ᚱ Raido (Pos. 5ª)",
      6: "ᚲ Kenaz (Pos. 6ª)",
      7: "ᚷ Gebo (Pos. 7ª)",
      8: "ᚹ Wunjo (Pos. 8ª)",
      9: "ᚺ Hagalaz (Pos. 9ª)"
    };

    // Calculator Tool Logic
    function calculateWordArithmancy(word) {
      const calcRunesElem = document.getElementById("calcRunes");
      if (!word) {
        calcNorm.textContent = "-";
        calcLetters.textContent = "-";
        calcSum.textContent = "0";
        calcValence.textContent = "-";
        calcOpposite.textContent = "-";
        calcFigure.textContent = "-";
        calcElement.textContent = "-";
        if (calcRunesElem) calcRunesElem.textContent = "-";
        return;
      }

      const rawClean = word.trim().toUpperCase();
      const clean = rawClean.split("").filter(c => PYTHAGOREAN[c]);
      if (clean.length === 0) return;

      const sum = clean.reduce((acc, c) => acc + PYTHAGOREAN[c], 0);
      let reduced = sum;
      while (reduced > 9) {
        reduced = String(reduced).split("").reduce((acc, d) => acc + Number(d), 0);
      }

      // Applicazione forzatura canonica
      let isOverridden = false;
      let overrideObj = CANONICAL_OVERRIDES[rawClean];
      if (overrideObj) {
        reduced = overrideObj.valenza;
        isOverridden = true;
      }

      const opposite = 5 - reduced + 5;

      calcNorm.textContent = clean.join("") + (isOverridden ? ` ⭐ [${overrideObj.reason}]` : "");
      calcLetters.textContent = clean.map(c => `${c}(${PYTHAGOREAN[c]})`).join(" + ");
      calcSum.textContent = sum;
      calcValence.textContent = isOverridden ? `${reduced} (Canone)` : reduced;
      calcOpposite.textContent = opposite;
      calcFigure.textContent = GEOMETRY_MAP[reduced] || "-";
      calcElement.textContent = (isOverridden && overrideObj.element) ? overrideObj.element : (ELEMENT_MAP[reduced] || `Simmetria speculare: ${opposite}`);
      if (calcRunesElem) {
        calcRunesElem.textContent = VALENCE_RUNES_MAP[reduced] || "-";
      }
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

      renderSpells();
    }

    if (duelFilter) {
      duelFilter.addEventListener("change", (e) => {
        setDuelFilter(e.target.value);
      });
    }

    duelSegBtns.forEach(btn => {
      btn.addEventListener("click", () => {
        setDuelFilter(btn.dataset.duel);
      });
    });

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
      updateMacroButtonBadges();
      renderSpells();
    });

    clearSearchBtn.addEventListener("click", () => {
      searchInput.value = "";
      searchQuery = "";
      clearSearchBtn.classList.add("hidden");
      updateMacroButtonBadges();
      renderSpells();
    });

    // Macro Filter Listeners
    macroSpellsBtn?.addEventListener("click", () => setMacroFilter("spells"));
    macroRunesBtn?.addEventListener("click", () => setMacroFilter("runes"));

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
      
      setMacroFilter("spells");
      setYearFilter("ALL");
      setDuelFilter("ALL");

      valPills.forEach(p => {
        p.classList.remove("bg-amber-500/20", "text-amber-300", "border-amber-500/30", "border");
        p.classList.add("bg-slate-800/80", "text-slate-300");
      });
      document.querySelector('.val-pill[data-val="ALL"]').classList.add("bg-amber-500/20", "text-amber-300", "border-amber-500/30", "border");

      updateMacroButtonBadges();
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
