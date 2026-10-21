// app.js - Logica Applicativa e Interattività del Portale Unificato di Hogwarts
// Integra le 5 Macro-Discipline: Incantesimi, Rune, Creature, Piante e Pozioni

function initPortal() {

  // --- Macro Configurations & Metadata ---
  const MACRO_CONFIG = {
    spells: {
      name: "Incantesimi",
      icon: "🪄",
      hint: '<strong class="text-amber-300">268 Incantesimi Didattici</strong> (Valenza, Movimenti Bacchetta, Duello)',
      activeClass: "bg-amber-500 text-slate-950 shadow-lg shadow-amber-500/20 border border-amber-400 ring-2 ring-amber-400/40",
      inactiveClass: "text-slate-300 hover:text-amber-300 bg-slate-900/90 hover:bg-slate-800/90 border border-slate-700/80",
      hasYear: true,
      hasDuel: true,
      hasValence: true,
      secondaryIcon: "🏷️",
      secondaryLabel: "Tipologia Incantesimo:",
      secondaryOptions: [
        { label: "Tutte le Tipologie", value: "ALL" },
        { label: "⚔️ Offensivo / Attacco", value: "Offensivo" },
        { label: "🛡️ Difensivo / Scudo", value: "Difensivo" },
        { label: "⚡ Schiantesimo", value: "Schiantesimo" },
        { label: "⚠️ Fattura", value: "Fattura" },
        { label: "☠️ Maledizione / M. Oscura", value: "Maledizione" },
        { label: "🌿 Curativo / Medimagia", value: "Curativo" },
        { label: "🪄 Trasfigurazione", value: "Trasfigurazione" },
        { label: "🔥 Elementale (4 Elementi)", value: "Elementale" },
        { label: "📐 Aritmantico / Tracciatura", value: "Aritmantico" },
        { label: "✨ Utilità & Cinetica", value: "Utilità" }
      ]
    },
    runes: {
      name: "Antiche Rune",
      icon: "ᛟ",
      hint: '<strong class="text-indigo-300">25 Antiche Rune Futhark</strong> (Significato, Aett, Simboli)',
      activeClass: "bg-indigo-600 text-white shadow-lg shadow-indigo-600/20 border border-indigo-400 ring-2 ring-indigo-400/40",
      inactiveClass: "text-slate-300 hover:text-indigo-300 bg-slate-900/90 hover:bg-slate-800/90 border border-slate-700/80",
      hasYear: false,
      hasDuel: false,
      hasValence: false,
      secondaryIcon: "ᛟ",
      secondaryLabel: "Aett Runico:",
      secondaryOptions: [
        { label: "Tutti gli Aett Futhark", value: "ALL" },
        { label: "Primo Aett (Freyr)", value: "Freyr" },
        { label: "Secondo Aett (Heimdall)", value: "Heimdall" },
        { label: "Terzo Aett (Tiwaz)", value: "Tiwaz" }
      ]
    },
    creatures: {
      name: "Creature Magiche",
      icon: "🐉",
      hint: '<strong class="text-amber-400">74 Creature Magiche</strong> (Classificazione Ministeriale, Habitat, Dieta)',
      activeClass: "bg-amber-600 text-white shadow-lg shadow-amber-600/20 border border-amber-400 ring-2 ring-amber-400/40",
      inactiveClass: "text-slate-300 hover:text-amber-300 bg-slate-900/90 hover:bg-slate-800/90 border border-slate-700/80",
      hasYear: true,
      hasDuel: false,
      hasValence: false,
      secondaryIcon: "⚖️",
      secondaryLabel: "Classificazione Ministeriale:",
      secondaryOptions: [
        { label: "Tutte le Classi (X - XXXXX)", value: "ALL" },
        { label: "X — Noioso", value: "X" },
        { label: "XX — Innocuo / Addomesticabile", value: "XX" },
        { label: "XXX — Mago Capace", value: "XXX" },
        { label: "XXXX — Pericoloso / Specialista", value: "XXXX" },
        { label: "XXXXX — Noto Ammazzamaghi", value: "XXXXX" }
      ]
    },
    plants: {
      name: "Erbologia & Piante",
      icon: "🌿",
      hint: '<strong class="text-emerald-400">57 Piante & Colture Botaniche</strong> (Parti Usate, Proprietà, Coltivazione)',
      activeClass: "bg-emerald-600 text-white shadow-lg shadow-emerald-600/20 border border-emerald-400 ring-2 ring-emerald-400/40",
      inactiveClass: "text-slate-300 hover:text-emerald-300 bg-slate-900/90 hover:bg-slate-800/90 border border-slate-700/80",
      hasYear: true,
      hasDuel: false,
      hasValence: false,
      secondaryIcon: "🌱",
      secondaryLabel: "Tipologia Botanica:",
      secondaryOptions: [
        { label: "Tutte le Tipologie", value: "ALL" },
        { label: "Piante da Rimedio", value: "Piante da Rimedio" },
        { label: "Piante Velenose", value: "Piante Velenose" },
        { label: "Piante Antropomorfe", value: "Piante Antropomorfe" },
        { label: "Alteratrici di Stato", value: "Alteratrici di Stato" },
        { label: "Alberi Nobili & Legnami", value: "Alberi Nobili" },
        { label: "Piante Maestre & Avanzate", value: "Piante Maestre" },
        { label: "Famiglia delle Fagiole", value: "Fagiole" },
        { label: "Strumentazione Magica", value: "Strumentazione" },
        { label: "Formule Botaniche", value: "Formule Botaniche" },
        { label: "Anatomia Botanica", value: "Anatomia Botanica" },
        { label: "Tecniche di Difesa & Bonifica", value: "Bonifica" }
      ]
    },
    potions: {
      name: "Arte delle Pozioni",
      icon: "🧪",
      hint: '<strong class="text-indigo-400">138 Pozioni & Preparazioni Alchemiche</strong> (Ingredienti, Procedimenti, Effetti)',
      activeClass: "bg-indigo-600 text-white shadow-lg shadow-indigo-600/20 border border-indigo-400 ring-2 ring-indigo-400/40",
      inactiveClass: "text-slate-300 hover:text-indigo-300 bg-slate-900/90 hover:bg-slate-800/90 border border-slate-700/80",
      hasYear: true,
      hasDuel: false,
      hasValence: false,
      secondaryIcon: "⚗️",
      secondaryLabel: "Tipologia Alchemica:",
      secondaryOptions: [
        { label: "Tutte le Tipologie", value: "ALL" },
        { label: "Curativa / Medimagica", value: "Curativa" },
        { label: "Di Trasformazione", value: "Trasformante" },
        { label: "Alteratrice di Stato", value: "Alteratrice" },
        { label: "Veleno / Tossico", value: "Veleno" },
        { label: "Antidoto", value: "Antidoto" },
        { label: "Filtro d'Amore / Emotivo", value: "Filtro" },
        { label: "Elisir", value: "Elisir" },
        { label: "Sonnifero / Soporifera", value: "Soporifera" },
        { label: "Per Oggetti / Tattica", value: "Oggetti" },
        { label: "Cosmetica / Aspetto", value: "Cosmetica" },
        { label: "Veterinaria Magica", value: "Veterinaria" },
        { label: "Magia Oscura / Proibita", value: "Oscura" }
      ]
    }
  };

  // --- Application State ---
  let activeMacro = "spells"; // "spells" | "runes" | "creatures" | "plants" | "potions"
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

  // --- DOM Elements ---
  const macroSpellsBtn = document.getElementById("macroSpellsBtn");
  const macroRunesBtn = document.getElementById("macroRunesBtn");
  const macroCreaturesBtn = document.getElementById("macroCreaturesBtn");
  const macroPlantsBtn = document.getElementById("macroPlantsBtn");
  const macroPotionsBtn = document.getElementById("macroPotionsBtn");

  const macroSpellsText = document.getElementById("macroSpellsText");
  const macroRunesText = document.getElementById("macroRunesText");
  const macroCreaturesText = document.getElementById("macroCreaturesText");
  const macroPlantsText = document.getElementById("macroPlantsText");
  const macroPotionsText = document.getElementById("macroPotionsText");
  const activeMacroHint = document.getElementById("activeMacroHint");

  const secondaryFilterSelect = document.getElementById("secondaryFilterSelect");
  const secondaryFilterLabel = document.getElementById("secondaryFilterLabel");
  const secondaryFilterIcon = document.getElementById("secondaryFilterIcon");
  const secondaryFilterText = document.getElementById("secondaryFilterText");

  const yearTabsSection = document.getElementById("yearTabsSection");
  const yearTabsContainer = document.getElementById("yearTabsContainer");
  const duelAndValenceContainer = document.getElementById("duelAndValenceContainer");
  const duelSegBtns = document.querySelectorAll(".duel-seg-btn");
  const valPills = document.querySelectorAll(".val-pill");

  const spellsGrid = document.getElementById("spellsGrid");
  const noResultsState = document.getElementById("noResultsState");
  const searchInput = document.getElementById("searchInput");
  const clearSearchBtn = document.getElementById("clearSearchBtn");
  const resultsCountBadge = document.getElementById("resultsCountBadge");
  const resetAllFiltersBtn = document.getElementById("resetAllFiltersBtn");

  // Stats Elements in Hero Banner
  const statTotal = document.getElementById("statTotal");
  const statRunes = document.getElementById("statRunes");
  const statCreatures = document.getElementById("statCreatures");
  const statPlants = document.getElementById("statPlants");
  const statPotions = document.getElementById("statPotions");
  const statGrandTotal = document.getElementById("statGrandTotal");
  const statDuel = document.getElementById("statDuel");
  const statDark = document.getElementById("statDark");

  // Spell Modal Elements
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
  const wandTrackLabel = document.getElementById("wandTrackLabel");
  let isCompassActive = false;
  let wandAnimId = null;

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

  // Detailed Item Modal Elements (Creature, Piante, Pozioni)
  const itemModal = document.getElementById("itemModal");
  const itemModalCard = document.getElementById("itemModalCard");
  const itemModalCloseBtn = document.getElementById("itemModalCloseBtn");
  const itemModalBackdrop = document.getElementById("itemModalBackdrop");
  const itemModalBadgeCategory = document.getElementById("itemModalBadgeCategory");
  const itemModalBadgeYear = document.getElementById("itemModalBadgeYear");
  const itemModalBadgeSpecial = document.getElementById("itemModalBadgeSpecial");
  const itemModalTitle = document.getElementById("itemModalTitle");
  const itemModalSubtitle = document.getElementById("itemModalSubtitle");
  const itemModalContentBody = document.getElementById("itemModalContentBody");

  // --- Helper: Retrieve Dataset by Macro ---
  function getDatasetForMacro(macro) {
    if (macro === "spells") {
      return (window.SPELLS_DATA || []).filter(s => !s.isRune);
    } else if (macro === "runes") {
      return (window.SPELLS_DATA || []).filter(s => s.isRune);
    } else if (macro === "creatures") {
      return window.materieData?.creature || [];
    } else if (macro === "plants") {
      return window.materieData?.piante || [];
    } else if (macro === "potions") {
      return window.materieData?.pozioni || [];
    }
    return [];
  }

  // --- Helper: Universal Search Matching ---
  function matchesSearch(item, macro, query) {
    if (!query || query.trim() === "") return true;
    const q = query.trim().toLowerCase();

    if (macro === "spells" || macro === "runes") {
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

    if (macro === "creatures") {
      const corpus = [
        item.nome,
        item.nomeAlternativo,
        item.descrizione,
        item.habitat,
        item.dieta,
        item.tratti,
        item.utilizziMagici,
        item.regolamentazione,
        item.commerciabilita,
        item.classificazione,
        item.classificazioneLabel
      ].filter(Boolean).join(" ").toLowerCase();
      return corpus.includes(q);
    }

    if (macro === "plants") {
      const corpus = [
        item.nome,
        item.nomeBotanico,
        item.nomeAlternativo,
        item.descrizione,
        item.partiUtilizzate,
        item.proprieta,
        item.coltivazioneCura,
        item.usiPozionistici,
        item.tipologia
      ].filter(Boolean).join(" ").toLowerCase();
      return corpus.includes(q);
    }

    if (macro === "potions") {
      const corpus = [
        item.nome,
        item.nomeAlternativo,
        item.descrizione,
        item.coloreFinale,
        item.tempoPreparazione,
        item.metodoAssunzione,
        item.tipologia,
        item.avvertenze,
        item.inventoreOrigine,
        ...(item.ingredienti || []),
        ...(item.preparazione || [])
      ].filter(Boolean).join(" ").toLowerCase();
      return corpus.includes(q);
    }

    return true;
  }

  // --- Highlighting Helper ---
  function highlightText(text, query) {
    if (!text) return "";
    if (!query || query.trim().length === 0) return text;
    const clean = query.trim().replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
    const regex = new RegExp(`(${clean})`, 'gi');
    return text.replace(regex, '<mark class="bg-amber-400/40 text-amber-200 px-0.5 rounded font-semibold">$1</mark>');
  }

  // --- Update Macro Badges during Live Search ---
  function updateMacroButtonBadges() {
    const q = searchQuery.trim().toLowerCase();

    ["spells", "runes", "creatures", "plants", "potions"].forEach(m => {
      const dataset = getDatasetForMacro(m);
      const count = q === "" ? dataset.length : dataset.filter(item => matchesSearch(item, m, q)).length;
      const textElem = document.getElementById(`macro${m.charAt(0).toUpperCase() + m.slice(1)}Text`);
      if (textElem) {
        textElem.textContent = `${MACRO_CONFIG[m].name} (${count})`;
      }
    });
  }

  // --- Global Stats Update ---
  function updateStats() {
    const spells = (window.SPELLS_DATA || []).filter(s => !s.isRune);
    const runes = (window.SPELLS_DATA || []).filter(s => s.isRune);
    const creatures = window.materieData?.creature || [];
    const plants = window.materieData?.piante || [];
    const potions = window.materieData?.pozioni || [];

    if (statTotal) statTotal.textContent = spells.length;
    if (statRunes) statRunes.textContent = runes.length;
    if (statCreatures) statCreatures.textContent = creatures.length;
    if (statPlants) statPlants.textContent = plants.length;
    if (statPotions) statPotions.textContent = potions.length;
    if (statGrandTotal) statGrandTotal.textContent = spells.length + runes.length + creatures.length + plants.length + potions.length;
    if (statDuel) statDuel.textContent = spells.filter(s => s.inDuello).length;
    if (statDark) statDark.textContent = spells.filter(s => (s.tipologia || '').includes("Maledizione") || (s.tipologia || '').includes("Fattura")).length;

    updateMacroButtonBadges();
  }

  // --- Secondary Filter Dropdown Update ---
  function updateSecondaryFilterOptions() {
    if (!secondaryFilterSelect) return;
    const cfg = MACRO_CONFIG[activeMacro];
    if (!cfg) return;

    if (secondaryFilterIcon) secondaryFilterIcon.textContent = cfg.secondaryIcon;
    if (secondaryFilterText) secondaryFilterText.textContent = cfg.secondaryLabel;

    secondaryFilterSelect.innerHTML = cfg.secondaryOptions.map(opt => {
      const isSelected = (activeType === opt.value) ? "selected" : "";
      return `<option value="${opt.value}" ${isSelected}>${opt.label}</option>`;
    }).join("");
  }

  // --- Dynamic Year Tabs Rendering ---
  function renderYearTabs() {
    if (!yearTabsContainer) return;
    const cfg = MACRO_CONFIG[activeMacro];
    if (!cfg.hasYear) {
      if (yearTabsSection) yearTabsSection.classList.add("hidden");
      return;
    }
    if (yearTabsSection) yearTabsSection.classList.remove("hidden");

    const dataset = getDatasetForMacro(activeMacro);
    const total = dataset.length;

    // Count per year
    const yearCounts = {};
    dataset.forEach(item => {
      yearCounts[item.anno] = (yearCounts[item.anno] || 0) + 1;
    });

    const yearsToDisplay = [
      { label: `Tutti (${total})`, value: "ALL" },
      { label: `I Anno (${yearCounts[1] || 0})`, value: "1" },
      { label: `II Anno (${yearCounts[2] || 0})`, value: "2" },
      { label: `III Anno (${yearCounts[3] || 0})`, value: "3" },
      { label: `IV Anno (${yearCounts[4] || 0})`, value: "4" },
      { label: `V Anno (${yearCounts[5] || 0})`, value: "5" },
      { label: `VI Anno (${yearCounts[6] || 0})`, value: "6" },
      { label: `VII Anno (${yearCounts[7] || 0})`, value: "7" }
    ];

    if (yearCounts[0] !== undefined && yearCounts[0] > 0) {
      yearsToDisplay.push({ label: `Altri (${yearCounts[0]})`, value: "0" });
    }

    yearTabsContainer.innerHTML = yearsToDisplay.map(y => {
      const isSelected = (activeYear === y.value);
      const cls = isSelected
        ? "year-tab px-3 py-1.5 rounded-lg text-xs font-semibold transition whitespace-nowrap bg-amber-500 text-slate-950 shadow-md"
        : "year-tab px-3 py-1.5 rounded-lg text-xs font-semibold transition whitespace-nowrap bg-slate-800 text-slate-300 hover:bg-slate-700";
      return `<button type="button" data-year="${y.value}" class="${cls}">${y.label}</button>`;
    }).join("");

    yearTabsContainer.querySelectorAll(".year-tab").forEach(tab => {
      tab.addEventListener("click", () => {
        activeYear = tab.dataset.year;
        renderYearTabs();
        renderCards();
      });
    });
  }

  // --- Macro Filter Switching ---
  function setMacroFilter(macro) {
    activeMacro = macro;
    activeYear = "ALL";
    activeType = "ALL";
    activeDuel = "ALL";
    activeValence = "ALL";

    // Update Macro Button highlight styles
    ["spells", "runes", "creatures", "plants", "potions"].forEach(m => {
      const btn = document.getElementById(`macro${m.charAt(0).toUpperCase() + m.slice(1)}Btn`);
      if (!btn) return;
      const cfg = MACRO_CONFIG[m];
      const isCurrent = (m === activeMacro);
      btn.className = `macro-btn p-3.5 rounded-xl text-xs sm:text-sm font-magic font-bold transition-all duration-200 flex flex-col items-center justify-center gap-1 ${
        isCurrent ? cfg.activeClass : cfg.inactiveClass
      }`;
    });

    // Update Stat Cards highlight in Hero Banner
    document.querySelectorAll(".stat-card").forEach(card => {
      const target = card.dataset.statMacro;
      if (target === activeMacro) {
        card.classList.add("ring-2", "ring-amber-400", "bg-amber-950/40");
      } else {
        card.classList.remove("ring-2", "ring-amber-400", "bg-amber-950/40");
      }
    });

    // Sync URL hash
    if (window.history && window.history.replaceState) {
      window.history.replaceState(null, null, '#' + macro);
    }

    // Update Macro Context Hint
    if (activeMacroHint) {
      activeMacroHint.innerHTML = `Visualizzazione: ${MACRO_CONFIG[macro].hint}`;
    }

    // Toggle Duel and Valence Controls (strictly hidden for non-spells!)
    if (duelAndValenceContainer) {
      if (MACRO_CONFIG[macro].hasDuel || MACRO_CONFIG[macro].hasValence) {
        duelAndValenceContainer.classList.remove("hidden");
        duelAndValenceContainer.style.display = "flex";
      } else {
        duelAndValenceContainer.classList.add("hidden");
        duelAndValenceContainer.style.display = "none";
      }
    }

    // Reset Duel Segmented Controls to 'ALL'
    duelSegBtns.forEach(btn => {
      if (btn.dataset.duel === "ALL") {
        btn.classList.add("bg-amber-500/20", "text-amber-300", "border", "border-amber-500/40");
        btn.classList.remove("text-slate-400");
      } else {
        btn.classList.remove("bg-amber-500/20", "text-amber-300", "border", "border-amber-500/40");
        btn.classList.add("text-slate-400");
      }
    });

    // Reset Valence Pills to 'ALL'
    valPills.forEach(p => {
      if (p.dataset.val === "ALL") {
        p.classList.add("bg-amber-500/20", "text-amber-300", "border-amber-500/30", "border");
        p.classList.remove("bg-slate-800/80", "text-slate-300");
      } else {
        p.classList.remove("bg-amber-500/20", "text-amber-300", "border-amber-500/30", "border");
        p.classList.add("bg-slate-800/80", "text-slate-300");
      }
    });

    updateSecondaryFilterOptions();
    renderYearTabs();
    renderCards();
  }

  // --- Filtering Logic ---
  function getFilteredItems() {
    const dataset = getDatasetForMacro(activeMacro);
    const q = searchQuery.trim().toLowerCase();

    return dataset.filter(item => {
      // 1. Year filter
      if (MACRO_CONFIG[activeMacro].hasYear && activeYear !== "ALL") {
        if (String(item.anno) !== String(activeYear)) return false;
      }

      // 2. Secondary filter
      if (activeType !== "ALL") {
        if (activeMacro === "spells") {
          const t = (item.tipologia || "").toLowerCase();
          const qTarget = activeType.toLowerCase();
          if (activeType === "Utilità") {
            if (!t.includes("utilità") && !t.includes("cinetic") && !t.includes("locomozione") && !t.includes("pulizia") && !t.includes("riparazione") && !t.includes("ottico") && !t.includes("levitazione")) return false;
          } else if (activeType === "Offensivo") {
            if (!t.includes("offensivo") && !t.includes("schiantesimo") && !t.includes("attacco") && !t.includes("esplosiv") && !t.includes("disarmo")) return false;
          } else if (activeType === "Difensivo") {
            if (!t.includes("difensivo") && !t.includes("scudo") && !t.includes("protezione") && !t.includes("contro-incant") && !t.includes("controincant")) return false;
          } else if (activeType === "Curativo") {
            if (!t.includes("curativo") && !t.includes("medimagia") && !t.includes("chirurgico")) return false;
          } else if (activeType === "Maledizione") {
            if (!t.includes("maledizione") && !t.includes("oscura")) return false;
          } else {
            if (!t.includes(qTarget)) return false;
          }
        } else if (activeMacro === "runes") {
          if (!item.aett || !item.aett.toLowerCase().includes(activeType.toLowerCase())) return false;
        } else if (activeMacro === "creatures") {
          if (item.classificazione !== activeType) return false;
        } else if (activeMacro === "plants") {
          if (!item.tipologia || !item.tipologia.toLowerCase().includes(activeType.toLowerCase())) return false;
        } else if (activeMacro === "potions") {
          const typeStr = (item.tipologia || "") + " " + (item.nomeAlternativo || "");
          if (!typeStr.toLowerCase().includes(activeType.toLowerCase())) return false;
        }
      }

      // 3. Duel filter (only for spells)
      if (activeMacro === "spells") {
        if (activeDuel === "YES" && !item.inDuello) return false;
        if (activeDuel === "NO" && item.inDuello) return false;
      }

      // 4. Valence filter (only for spells)
      if (activeMacro === "spells") {
        if (activeValence !== "ALL" && item.valenza !== Number(activeValence)) return false;
      }

      // 5. Search query
      if (q && !matchesSearch(item, activeMacro, q)) return false;

      return true;
    });
  }

  // --- Card Generators ---

  function renderSpellCardHtml(spell) {
    let typeBadgeClass = "bg-amber-500/10 text-amber-300 border-amber-500/30";
    const tipologia = spell.tipologia || "";
    if (tipologia.includes("Offensivo") || tipologia.includes("Schiantesimo")) {
      typeBadgeClass = "bg-rose-500/10 text-rose-300 border-rose-500/30";
    } else if (tipologia.includes("Difensivo")) {
      typeBadgeClass = "bg-sky-500/10 text-sky-300 border-sky-500/30";
    } else if (tipologia.includes("Maledizione")) {
      typeBadgeClass = "bg-purple-500/15 text-purple-300 border-purple-500/30";
    } else if (tipologia.includes("Curativo")) {
      typeBadgeClass = "bg-emerald-500/10 text-emerald-300 border-emerald-500/30";
    } else if (tipologia.includes("Elementale")) {
      typeBadgeClass = "bg-orange-500/10 text-orange-300 border-orange-500/30";
    } else if (tipologia.includes("Trasfigurazione")) {
      typeBadgeClass = "bg-teal-500/10 text-teal-300 border-teal-500/30";
    } else if (tipologia.includes("Rune") || spell.isRune) {
      typeBadgeClass = "bg-indigo-500/20 text-indigo-300 border-indigo-500/40";
    }

    let duelBadge;
    if (spell.isRune) {
      duelBadge = `<span class="inline-flex items-center gap-1 px-2.5 py-0.5 rounded-full text-[11px] font-bold bg-indigo-500/20 text-indigo-300 border border-indigo-500/40 shadow-sm">
                     <span>ᛟ</span> Futhark: Pos. ${spell.posizioneAlfabeto}
                   </span>`;
    } else {
      duelBadge = spell.inDuello
        ? `<span class="inline-flex items-center gap-1 px-2.5 py-0.5 rounded-full text-[11px] font-bold bg-emerald-500/15 text-emerald-300 border border-emerald-500/30 shadow-sm">
             <span>⚔️</span> Duello: Sì
           </span>`
        : `<span class="inline-flex items-center gap-1 px-2.5 py-0.5 rounded-full text-[11px] font-bold bg-slate-800 text-slate-400 border border-slate-700">
             <span>⛔</span> Duello: No
           </span>`;
    }

    const tipoShort = tipologia.split('/')[0].trim();
    const figura = spell.figuraGeometrica || '';
    const figuraShort = figura.split('(')[0].trim();

    return `
      <div class="glass-card rounded-2xl p-5 flex flex-col justify-between cursor-pointer group" onclick="openSpellDetails('${spell.id}')">
        <div>
          <div class="flex items-center justify-between gap-2 mb-3">
            <span class="px-2.5 py-0.5 rounded-md text-xs font-semibold bg-slate-800/90 text-amber-300 border border-slate-700">
              ${spell.annoLabel || 'Didattica'}
            </span>
            ${duelBadge}
          </div>

          <h3 class="text-lg font-bold font-magic text-slate-100 group-hover:text-amber-300 transition-colors line-clamp-1 mb-1">
            ${highlightText(spell.nome, searchQuery)}
          </h3>

          <div class="flex items-center gap-2 mb-3">
            <span class="font-code text-xs px-2.5 py-1 rounded-lg bg-amber-500/10 border border-amber-500/25 text-amber-200 font-bold tracking-wide">
              ⚡ ${highlightText(spell.formula, searchQuery)}
            </span>
            <span class="text-xs px-2 py-0.5 rounded border ${typeBadgeClass} truncate max-w-[150px]">
              ${tipoShort}
            </span>
          </div>

          <p class="text-xs text-slate-300 line-clamp-3 leading-relaxed mb-4">
            ${highlightText(spell.descrizione, searchQuery)}
          </p>
        </div>

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
            <div class="text-[11px] text-sky-400 font-medium truncate max-w-[120px]" title="${figura}">
              ${figuraShort}
            </div>
          </div>

          <div class="text-[11px] text-slate-400 line-clamp-1 italic bg-slate-950/40 px-2 py-1 rounded">
            🪄 ${highlightText(spell.movimento, searchQuery)}
          </div>

          <div class="pt-1 flex items-center justify-end text-xs text-amber-400 font-semibold group-hover:translate-x-1 transition-transform">
            <span>Consulta Scheda & Gesto →</span>
          </div>
        </div>
      </div>
    `;
  }

  function renderCreatureCardHtml(item) {
    let classColor = 'bg-slate-800 text-slate-300 border-slate-700';
    if (item.classificazione === 'X') classColor = 'bg-slate-800/80 text-slate-300 border-slate-700';
    else if (item.classificazione === 'XX') classColor = 'bg-emerald-950/70 text-emerald-300 border-emerald-800/60';
    else if (item.classificazione === 'XXX') classColor = 'bg-sky-950/70 text-sky-300 border-sky-800/60';
    else if (item.classificazione === 'XXXX') classColor = 'bg-purple-950/70 text-purple-300 border-purple-800/60';
    else if (item.classificazione === 'XXXXX') classColor = 'bg-rose-950/80 text-rose-300 border-rose-800/80 animate-pulse';

    return `
      <div class="glass-card rounded-2xl p-5 flex flex-col justify-between cursor-pointer group" onclick="openItemDetails('creatures', '${item.id}')">
        <div>
          <div class="flex items-center justify-between gap-2 mb-3">
            <span class="px-2.5 py-1 rounded-full text-[11px] font-semibold bg-amber-950/60 text-amber-300 border border-amber-800/60">
              ${item.annoLabel}
            </span>
            <span class="px-2.5 py-1 rounded-full text-[11px] font-bold border ${classColor}">
              Classe: ${item.classificazione}
            </span>
          </div>

          <h3 class="font-magic text-lg font-bold text-white mb-1 tracking-wide group-hover:text-amber-400 transition-colors line-clamp-1">
            ${highlightText(item.nome, searchQuery)}
          </h3>
          <p class="text-xs text-amber-500/80 italic mb-2 line-clamp-1">${item.nomeAlternativo || 'Bestiario di Hogwarts'}</p>
          <p class="text-xs text-slate-300 line-clamp-3 mb-4 leading-relaxed">
            ${highlightText(item.descrizione, searchQuery)}
          </p>
        </div>

        <div>
          <div class="pt-3 border-t border-slate-800/80 flex items-center justify-between text-[11px] text-slate-400">
            <span class="truncate max-w-[180px]"><i class="text-amber-500 mr-1">📍</i>${item.habitat || 'Globale'}</span>
            <span class="text-amber-400 font-semibold group-hover:translate-x-1 transition-transform flex items-center gap-1">Consulta Scheda →</span>
          </div>
        </div>
      </div>
    `;
  }

  function renderPlantCardHtml(item) {
    return `
      <div class="glass-card rounded-2xl p-5 flex flex-col justify-between cursor-pointer group" onclick="openItemDetails('plants', '${item.id}')">
        <div>
          <div class="flex items-center justify-between gap-2 mb-3">
            <span class="px-2.5 py-1 rounded-full text-[11px] font-semibold bg-emerald-950/60 text-emerald-300 border border-emerald-800/60">
              ${item.annoLabel}
            </span>
            <span class="px-2 py-0.5 rounded text-[10px] font-medium bg-slate-800/80 text-emerald-300 border border-slate-700 truncate max-w-[150px]">
              ${item.tipologia || 'Erbologia'}
            </span>
          </div>

          <h3 class="font-magic text-lg font-bold text-white mb-1 tracking-wide group-hover:text-emerald-400 transition-colors line-clamp-1">
            ${highlightText(item.nome, searchQuery)}
          </h3>
          <p class="text-xs text-emerald-500/80 italic mb-2 line-clamp-1">${item.nomeBotanico || item.nomeAlternativo || 'Specie Botanica'}</p>
          <p class="text-xs text-slate-300 line-clamp-3 mb-4 leading-relaxed">
            ${highlightText(item.descrizione, searchQuery)}
          </p>
        </div>

        <div>
          <div class="pt-3 border-t border-slate-800/80 flex items-center justify-between text-[11px] text-slate-400">
            <span class="truncate max-w-[180px]"><i class="text-emerald-500 mr-1">🌿</i>${item.partiUtilizzate ? item.partiUtilizzate.split(',')[0] : 'Tessuti vegetali'}</span>
            <span class="text-emerald-400 font-semibold group-hover:translate-x-1 transition-transform flex items-center gap-1">Dettagli Botanici →</span>
          </div>
        </div>
      </div>
    `;
  }

  function renderPotionCardHtml(item) {
    const ingCount = item.ingredienti ? item.ingredienti.length : 0;
    return `
      <div class="glass-card rounded-2xl p-5 flex flex-col justify-between cursor-pointer group" onclick="openItemDetails('potions', '${item.id}')">
        <div>
          <div class="flex items-center justify-between gap-2 mb-3">
            <span class="px-2.5 py-1 rounded-full text-[11px] font-semibold bg-indigo-950/60 text-indigo-300 border border-indigo-800/60">
              ${item.annoLabel}
            </span>
            <span class="px-2 py-0.5 rounded text-[10px] font-medium bg-slate-800/80 text-amber-300 border border-slate-700 truncate max-w-[150px]">
              ${item.tipologia || 'Pozione'}
            </span>
          </div>

          <h3 class="font-magic text-lg font-bold text-white mb-1 tracking-wide group-hover:text-amber-400 transition-colors line-clamp-1">
            ${highlightText(item.nome, searchQuery)}
          </h3>
          <p class="text-xs text-amber-500/80 italic mb-2 line-clamp-1">${item.nomeAlternativo || 'Manuale di Pozioni'}</p>
          <p class="text-xs text-slate-300 line-clamp-3 mb-3 leading-relaxed">
            ${highlightText(item.descrizione, searchQuery)}
          </p>
        </div>

        <div>
          <div class="pt-2 mb-2 flex items-center gap-2 text-[11px] text-slate-400">
            <span class="w-2.5 h-2.5 rounded-full bg-amber-500 shrink-0"></span>
            <span class="truncate">${item.coloreFinale || 'Trasparente'}</span>
          </div>
          <div class="pt-2 border-t border-slate-800/80 flex items-center justify-between text-[11px] text-slate-400">
            <span>🧪 ${ingCount} ingredienti</span>
            <span class="text-amber-400 font-semibold group-hover:translate-x-1 transition-transform flex items-center gap-1">Ricetta & Formula →</span>
          </div>
        </div>
      </div>
    `;
  }

  // --- Render Cards Controller ---
  function renderCards() {
    const filtered = getFilteredItems();

    let label = "voci trovate";
    if (activeMacro === "spells") label = "incantesimi trovati";
    else if (activeMacro === "runes") label = "rune trovate";
    else if (activeMacro === "creatures") label = "creature trovate";
    else if (activeMacro === "plants") label = "specie botaniche trovate";
    else if (activeMacro === "potions") label = "pozioni trovate";

    if (resultsCountBadge) {
      resultsCountBadge.textContent = `${filtered.length} ${label}`;
    }

    if (filtered.length === 0) {
      spellsGrid.innerHTML = "";
      if (noResultsState) {
        noResultsState.classList.remove("hidden");
        noResultsState.style.display = "block";
      }
      return;
    }

    if (noResultsState) {
      noResultsState.classList.add("hidden");
      noResultsState.style.display = "none";
    }

    if (activeMacro === "spells" || activeMacro === "runes") {
      spellsGrid.innerHTML = filtered.map(s => renderSpellCardHtml(s)).join("");
    } else if (activeMacro === "creatures") {
      spellsGrid.innerHTML = filtered.map(c => renderCreatureCardHtml(c)).join("");
    } else if (activeMacro === "plants") {
      spellsGrid.innerHTML = filtered.map(p => renderPlantCardHtml(p)).join("");
    } else if (activeMacro === "potions") {
      spellsGrid.innerHTML = filtered.map(pot => renderPotionCardHtml(pot)).join("");
    }
  }

  // --- Open Detailed Spell/Rune Modal ---
  window.openSpellDetails = function(spellId) {
    const spell = (window.SPELLS_DATA || []).find(s => s.id === spellId);
    if (!spell) return;

    modalTitle.textContent = spell.nome;
    modalFormula.textContent = spell.formula;
    modalEtymology.textContent = spell.etimologia || "";
    modalDesc.textContent = spell.descrizione;
    modalMovement.textContent = spell.movimento;

    let badgesHtml = `
      <span class="px-3 py-1 rounded-full text-xs font-bold bg-amber-500/20 text-amber-300 border border-amber-500/40">
        ${spell.annoLabel || 'Didattica'}
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
    } else if (!spell.isRune) {
      badgesHtml += `
        <span class="px-3 py-1 rounded-full text-xs font-bold bg-rose-500/20 text-rose-300 border border-rose-500/40">
          ⛔ Non Utilizzabile in Duello
        </span>
      `;
    }
    modalBadges.innerHTML = badgesHtml;

    modalDuelTactics.innerHTML = `<strong>Tattica di Duello:</strong> ${spell.duelloNote || 'Nessuna specifica per il duello magico.'}`;

    modalValenceNum.textContent = spell.valenza;
    modalValenceSum.textContent = `Somma: ${spell.sommaLettere}`;
    modalOppositeNum.textContent = spell.valenzaOpposta;
    modalRepeatMax.textContent = spell.ripetibile ? `${spell.maxRipetizioni} volte` : "1 volta";
    modalRepeatStatus.textContent = spell.ripetibile ? "Incanto Ripetibile" : "Irripetibile";
    modalGeometry.textContent = spell.figuraGeometrica;

    const letters = spell.formula.toUpperCase().split("").filter(c => PYTHAGOREAN[c]);
    const breakdown = letters.map(c => `${c}=${PYTHAGOREAN[c]}`).join(" + ");
    modalLetterBreakdown.textContent = spell.isRune 
      ? `Posizione nell'Alfabeto: ${spell.posizioneAlfabeto} ➔ Valenza Magica: ${spell.valenza} (Canone: Valenza corrisponde alla Posizione)`
      : `${breakdown} = ${spell.sommaLettere} ➔ Riduzione: Valenza ${spell.valenza}`;
    modalArithNotes.textContent = spell.noteAritmantiche || "";

    const modalRuneBox = document.getElementById("modalRuneAssociation");
    const modalRunePos = document.getElementById("modalRunePosition");
    if (modalRuneBox && modalRunePos) {
      modalRunePos.textContent = `Valenza ${spell.valenza}`;
      modalRuneBox.innerHTML = spell.isRune
        ? `<strong>Runa Primaria dell'Alfabeto:</strong> ${spell.nome} (${spell.aett})<br><span class="text-xs text-amber-200/90">Incantesimi in risonanza: ${spell.incantesimiAssociati || spell.runeAssociate}</span>`
        : `<strong>Runa dell'Alfabeto Associata:</strong> <span class="text-amber-300">${spell.runeAssociate || "—"}</span>`;
    }

    isCompassActive = (spell.id === "guidami" || (spell.formula && spell.formula.toLowerCase() === "guidami"));
    const compassRose = document.getElementById("compassRoseDecor");
    const needleGroup = document.getElementById("wandNeedleGroup");

    if (needleGroup) {
      needleGroup.removeAttribute("transform");
      needleGroup.style.transition = "";
    }
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

    if (compassRose) {
      if (isCompassActive) compassRose.classList.remove("hidden");
      else compassRose.classList.add("hidden");
    }

    if (wandTrackLabel) {
      wandTrackLabel.innerHTML = isCompassActive
        ? '🧭 <span class="text-amber-300 font-semibold">Bussola Magica:</span> Segue il puntatore del mouse'
        : 'Traccia Dinamica';
    }
    if (replayWandAnimBtn) {
      replayWandAnimBtn.innerHTML = isCompassActive
        ? '<span>🧭</span> Punta al Nord'
        : '<span>🔄</span> Anima Gesto';
    }

    const pathData = spell.movimentoSvg || "M 30,75 L 120,75";
    wandPathElement.setAttribute("d", pathData);
    if (guidePath) guidePath.setAttribute("d", pathData);

    spellModal.style.display = "flex";
    spellModal.classList.add("active");
    spellModal.classList.remove("hidden");
    setTimeout(() => {
      spellModal.classList.remove("opacity-0");
      modalCard.classList.remove("scale-95");
      setTimeout(() => {
        animateWandPath();
      }, 120);
    }, 15);
  };

  function animateWandPath() {
    if (!wandPathElement) return;

    if (wandAnimId) {
      cancelAnimationFrame(wandAnimId);
      wandAnimId = null;
    }

    const spark = document.getElementById("wandSpark");
    const guidePath = document.getElementById("wandGuidePath");
    const needleGroup = document.getElementById("wandNeedleGroup");

    if (isCompassActive) {
      wandPathElement.style.strokeDasharray = "none";
      wandPathElement.style.strokeDashoffset = "0";
      if (guidePath) {
        guidePath.style.strokeDasharray = "none";
        guidePath.style.strokeDashoffset = "0";
      }
      if (needleGroup) {
        needleGroup.style.transition = "";
        needleGroup.setAttribute("transform", "rotate(0 75 75)");
      }
      if (spark) {
        spark.setAttribute("cx", "75");
        spark.setAttribute("cy", "25");
        spark.style.opacity = "1";
        spark.setAttribute("r", "6");
      }
      return;
    }
    const d = wandPathElement.getAttribute("d");

    if (!d || d.trim() === "") {
      if (spark) spark.style.opacity = "0";
      return;
    }

    if (guidePath) guidePath.setAttribute("d", d);

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
      wandPathElement.style.strokeDasharray = `${totalLen} ${totalLen}`;
      wandPathElement.style.strokeDashoffset = `${totalLen}`;
    }

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

    if (replayWandAnimBtn) {
      replayWandAnimBtn.classList.add("ring-2", "ring-amber-400", "bg-amber-500/30");
    }

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
          try {
            const endPt = wandPathElement.getPointAtLength(totalLen);
            spark.setAttribute("cx", endPt.x);
            spark.setAttribute("cy", endPt.y);
          } catch (e) {}
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

  replayWandAnimBtn?.addEventListener("click", () => {
    if (isCompassActive) {
      const needleGroup = document.getElementById("wandNeedleGroup");
      if (needleGroup) {
        needleGroup.style.transition = "transform 0.5s cubic-bezier(0.34, 1.56, 0.64, 1)";
        needleGroup.setAttribute("transform", "rotate(0 75 75)");
        setTimeout(() => {
          if (needleGroup) needleGroup.style.transition = "";
        }, 500);
      }
      return;
    }
    animateWandPath();
  });

  // Compass mouse follower for Guidami
  window.addEventListener("mousemove", (e) => {
    if (!isCompassActive) return;
    if (!spellModal || spellModal.classList.contains("hidden")) return;

    const svg = document.getElementById("wandSvgCanvas");
    if (!svg) return;
    const rect = svg.getBoundingClientRect();
    const centerX = rect.left + rect.width / 2;
    const centerY = rect.top + rect.height / 2;

    const dx = e.clientX - centerX;
    const dy = e.clientY - centerY;
    if (Math.hypot(dx, dy) < 2) return;

    const angleRad = Math.atan2(dy, dx);
    const angleDeg = (angleRad * 180 / Math.PI) + 90;

    const needleGroup = document.getElementById("wandNeedleGroup");
    if (needleGroup) {
      needleGroup.style.transition = "";
      needleGroup.setAttribute("transform", `rotate(${angleDeg.toFixed(1)} 75 75)`);
    }
  });

  function closeSpellModal() {
    if (wandAnimId) {
      cancelAnimationFrame(wandAnimId);
      wandAnimId = null;
    }
    isCompassActive = false;
    const compassRose = document.getElementById("compassRoseDecor");
    if (compassRose) compassRose.classList.add("hidden");

    spellModal.classList.add("opacity-0");
    modalCard.classList.add("scale-95");
    setTimeout(() => {
      spellModal.classList.remove("active");
      spellModal.classList.add("hidden");
      spellModal.style.display = "none";
    }, 250);
  }

  closeModalBtn?.addEventListener("click", closeSpellModal);
  spellModal?.addEventListener("click", (e) => {
    if (e.target === spellModal) closeSpellModal();
  });

  // --- Detailed Item Modal (Creature, Piante, Pozioni) ---
  window.openItemDetails = function(macro, id) {
    let dataset = [];
    if (macro === "creatures") dataset = window.materieData?.creature || [];
    else if (macro === "plants") dataset = window.materieData?.piante || [];
    else if (macro === "potions") dataset = window.materieData?.pozioni || [];

    const item = dataset.find(x => x.id === id);
    if (!item) return;

    itemModalTitle.textContent = item.nome;
    itemModalSubtitle.textContent = item.nomeBotanico || item.nomeAlternativo || "";
    if (itemModalBadgeYear) itemModalBadgeYear.textContent = item.annoLabel || (item.anno === 0 ? "Altri Anni" : `${item.anno}° Anno`);

    if (macro === "creatures") {
      itemModalBadgeCategory.textContent = "Creatura Magica";
      itemModalBadgeCategory.className = "px-3 py-1 rounded-full text-xs font-semibold bg-amber-950/80 text-amber-300 border border-amber-800";
      itemModalBadgeSpecial.textContent = `Classe ${item.classificazione} — ${item.classificazioneLabel}`;
      itemModalBadgeSpecial.className = "px-3 py-1 rounded-full text-xs font-semibold bg-purple-950/80 text-purple-300 border border-purple-800";

      itemModalContentBody.innerHTML = `
        <div class="space-y-4 text-sm text-slate-300 leading-relaxed">
          <div class="bg-slate-900/60 p-4 rounded-xl border border-slate-800">
            <h4 class="font-magic text-amber-400 font-bold mb-1">Descrizione & Comportamento</h4>
            <p>${item.descrizione}</p>
          </div>
          <div class="grid grid-cols-1 md:grid-cols-2 gap-3">
            <div class="bg-slate-900/60 p-3.5 rounded-xl border border-slate-800">
              <span class="text-amber-500 font-bold block mb-1">📍 Habitat & Diffusione</span>
              <p class="text-xs text-slate-300">${item.habitat || 'Sconosciuto'}</p>
            </div>
            <div class="bg-slate-900/60 p-3.5 rounded-xl border border-slate-800">
              <span class="text-amber-500 font-bold block mb-1">🍖 Dieta & Nutrizione</span>
              <p class="text-xs text-slate-300">${item.dieta || 'Carnivoro / Onnivoro'}</p>
            </div>
          </div>
          <div class="bg-slate-900/60 p-4 rounded-xl border border-slate-800">
            <h4 class="font-magic text-amber-400 font-bold mb-1">Utilizzi Magici & Alchemici</h4>
            <p class="text-xs text-slate-300">${item.utilizziMagici || 'Nessun utilizzo noto.'}</p>
          </div>
          <div class="bg-slate-900/60 p-4 rounded-xl border border-slate-800">
            <h4 class="font-magic text-amber-400 font-bold mb-1">Regolamentazione Ministeriale & Commercio</h4>
            <p class="text-xs text-slate-300">${item.regolamentazione || 'Norme ordinarie del Ministero della Magia.'}</p>
            <p class="text-[11px] text-amber-500 mt-2"><strong>Status Beni:</strong> ${item.commerciabilita || 'Non specificato'}</p>
          </div>
        </div>
      `;
    } else if (macro === "plants") {
      itemModalBadgeCategory.textContent = "Erbologia & Botanica";
      itemModalBadgeCategory.className = "px-3 py-1 rounded-full text-xs font-semibold bg-emerald-950/80 text-emerald-300 border border-emerald-800";
      itemModalBadgeSpecial.textContent = item.tipologia || "Specie Botanica";
      itemModalBadgeSpecial.className = "px-3 py-1 rounded-full text-xs font-semibold bg-teal-950/80 text-teal-300 border border-teal-800";

      itemModalContentBody.innerHTML = `
        <div class="space-y-4 text-sm text-slate-300 leading-relaxed">
          <div class="bg-slate-900/60 p-4 rounded-xl border border-slate-800">
            <h4 class="font-magic text-emerald-400 font-bold mb-1">Profilo Botanico</h4>
            <p>${item.descrizione}</p>
          </div>
          <div class="grid grid-cols-1 md:grid-cols-2 gap-3">
            <div class="bg-slate-900/60 p-3.5 rounded-xl border border-slate-800">
              <span class="text-emerald-500 font-bold block mb-1">🌿 Parti Utilizzate</span>
              <p class="text-xs text-slate-300">${item.partiUtilizzate || 'Fogliame, radici o corteccia'}</p>
            </div>
            <div class="bg-slate-900/60 p-3.5 rounded-xl border border-slate-800">
              <span class="text-emerald-500 font-bold block mb-1">✨ Proprietà Magiche</span>
              <p class="text-xs text-slate-300">${item.proprieta || 'Terapeutiche o trasmutative'}</p>
            </div>
          </div>
          <div class="bg-slate-900/60 p-4 rounded-xl border border-slate-800">
            <h4 class="font-magic text-emerald-400 font-bold mb-1">Protocollo di Coltivazione & Cura</h4>
            <p class="text-xs text-slate-300">${item.coltivazioneCura || 'Coltivazione in serra a parametri standard.'}</p>
          </div>
          <div class="bg-slate-900/60 p-4 rounded-xl border border-slate-800">
            <h4 class="font-magic text-emerald-400 font-bold mb-1">Applicazioni Pozionistiche & Medimagiche</h4>
            <p class="text-xs text-slate-300">${item.usiPozionistici || 'Ingrediente per pozioni e decotti officinali.'}</p>
          </div>
        </div>
      `;
    } else if (macro === "potions") {
      itemModalBadgeCategory.textContent = "Pozione Avanzata";
      itemModalBadgeCategory.className = "px-3 py-1 rounded-full text-xs font-semibold bg-indigo-950/80 text-indigo-300 border border-indigo-800";
      itemModalBadgeSpecial.textContent = item.tipologia || "Pozione";
      itemModalBadgeSpecial.className = "px-3 py-1 rounded-full text-xs font-semibold bg-amber-950/80 text-amber-300 border border-amber-800";

      const ingredientiList = (item.ingredienti || []).map(ing => `<li class="flex items-center gap-2"><span class="text-amber-500">✦</span> ${ing}</li>`).join("");
      const preparazioneList = (item.preparazione || []).map(step => `<li class="mb-1.5">${step}</li>`).join("");

      itemModalContentBody.innerHTML = `
        <div class="space-y-4 text-sm text-slate-300 leading-relaxed">
          <div class="bg-slate-900/60 p-4 rounded-xl border border-slate-800">
            <h4 class="font-magic text-amber-400 font-bold mb-1">Descrizione & Effetti</h4>
            <p>${item.descrizione}</p>
          </div>
          <div class="grid grid-cols-1 md:grid-cols-3 gap-2 text-xs">
            <div class="bg-slate-900/60 p-2.5 rounded-lg border border-slate-800">
              <span class="text-amber-500 font-bold block">🎨 Colore Finale:</span>
              <span>${item.coloreFinale || 'Trasparente'}</span>
            </div>
            <div class="bg-slate-900/60 p-2.5 rounded-lg border border-slate-800">
              <span class="text-amber-500 font-bold block">⏱️ Tempo Stima:</span>
              <span>${item.tempoPreparazione || 'Non specificato'}</span>
            </div>
            <div class="bg-slate-900/60 p-2.5 rounded-lg border border-slate-800">
              <span class="text-amber-500 font-bold block">🥄 Assunzione:</span>
              <span>${item.metodoAssunzione || 'Ingestione'}</span>
            </div>
          </div>
          <div class="bg-slate-900/60 p-4 rounded-xl border border-slate-800">
            <h4 class="font-magic text-amber-400 font-bold mb-2">Ingredienti Necessari (${(item.ingredienti || []).length})</h4>
            <ul class="text-xs text-slate-300 space-y-1">
              ${ingredientiList || '<li>Nessun ingrediente elencato.</li>'}
            </ul>
          </div>
          <div class="bg-slate-900/60 p-4 rounded-xl border border-slate-800">
            <h4 class="font-magic text-amber-400 font-bold mb-2">Procedimento di Preparazione (${(item.preparazione || []).length} passaggi)</h4>
            <ol class="text-xs text-slate-300 space-y-1.5 list-decimal pl-4">
              ${preparazioneList || '<li>Seguire le istruzioni del Maestro Pozionista.</li>'}
            </ol>
          </div>
          ${item.avvertenze ? `
          <div class="bg-amber-950/30 p-3.5 rounded-xl border border-amber-800/60">
            <h4 class="font-magic text-amber-400 font-bold mb-1">⚠️ Precauzioni & Avvertenze</h4>
            <p class="text-xs text-amber-200/90">${item.avvertenze}</p>
          </div>
          ` : ''}
          ${item.inventoreOrigine ? `
          <div class="text-[11px] text-slate-400 italic">
            <strong>Origine & Note Storiche:</strong> ${item.inventoreOrigine}
          </div>
          ` : ''}
        </div>
      `;
    }

    itemModal.style.display = "flex";
    itemModal.classList.add("active");
    itemModal.classList.remove("hidden");
    setTimeout(() => {
      itemModal.classList.remove("opacity-0");
      if (itemModalCard) itemModalCard.classList.remove("scale-95");
    }, 15);
  };

  function closeItemModal() {
    if (!itemModal) return;
    itemModal.classList.add("opacity-0");
    if (itemModalCard) itemModalCard.classList.add("scale-95");
    setTimeout(() => {
      itemModal.classList.remove("active");
      itemModal.classList.add("hidden");
      itemModal.style.display = "none";
    }, 250);
  }

  itemModalCloseBtn?.addEventListener("click", closeItemModal);
  itemModalBackdrop?.addEventListener("click", closeItemModal);

  // --- Calculator Tool Logic ---
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

  calcInput?.addEventListener("input", (e) => {
    calculateWordArithmancy(e.target.value);
  });

  document.querySelectorAll(".calc-sample").forEach(btn => {
    btn.addEventListener("click", () => {
      if (calcInput) {
        calcInput.value = btn.dataset.word;
        calculateWordArithmancy(btn.dataset.word);
      }
    });
  });

  openCalculatorBtn?.addEventListener("click", () => {
    calculatorModal.style.display = "flex";
    calculatorModal.classList.add("active");
    calculatorModal.classList.remove("hidden");
    setTimeout(() => {
      calculatorModal.classList.remove("opacity-0");
      calcCard.classList.remove("scale-95");
    }, 10);
    calcInput?.focus();
  });

  function closeCalculator() {
    calculatorModal.classList.add("opacity-0");
    calcCard.classList.add("scale-95");
    setTimeout(() => {
      calculatorModal.classList.remove("active");
      calculatorModal.classList.add("hidden");
      calculatorModal.style.display = "none";
    }, 250);
  }
  closeCalcBtn?.addEventListener("click", closeCalculator);
  calculatorModal?.addEventListener("click", (e) => {
    if (e.target === calculatorModal) closeCalculator();
  });

  // --- Duel Segmented Filter ---
  duelSegBtns.forEach(btn => {
    btn.addEventListener("click", () => {
      activeDuel = btn.dataset.duel;
      duelSegBtns.forEach(b => {
        if (b.dataset.duel === activeDuel) {
          b.classList.add("bg-amber-500/20", "text-amber-300", "border", "border-amber-500/40");
          b.classList.remove("text-slate-400");
        } else {
          b.classList.remove("bg-amber-500/20", "text-amber-300", "border", "border-amber-500/40");
          b.classList.add("text-slate-400");
        }
      });
      renderCards();
    });
  });

  // --- Valence Pills Filter ---
  valPills.forEach(pill => {
    pill.addEventListener("click", () => {
      valPills.forEach(p => {
        p.classList.remove("bg-amber-500/20", "text-amber-300", "border-amber-500/30", "border");
        p.classList.add("bg-slate-800/80", "text-slate-300");
      });
      pill.classList.remove("bg-slate-800/80", "text-slate-300");
      pill.classList.add("bg-amber-500/20", "text-amber-300", "border-amber-500/30", "border");

      activeValence = pill.dataset.val;
      renderCards();
    });
  });

  // --- Secondary Filter Event ---
  secondaryFilterSelect?.addEventListener("change", (e) => {
    activeType = e.target.value;
    renderCards();
  });

  // --- Search Input Events ---
  searchInput?.addEventListener("input", (e) => {
    searchQuery = e.target.value;
    if (searchQuery.trim() !== "") {
      clearSearchBtn?.classList.remove("hidden");
    } else {
      clearSearchBtn?.classList.add("hidden");
    }
    updateMacroButtonBadges();
    renderCards();
  });

  clearSearchBtn?.addEventListener("click", () => {
    if (searchInput) searchInput.value = "";
    searchQuery = "";
    clearSearchBtn?.classList.add("hidden");
    updateMacroButtonBadges();
    renderCards();
  });

  // --- Macro Filter Button Listeners ---
  macroSpellsBtn?.addEventListener("click", () => setMacroFilter("spells"));
  macroRunesBtn?.addEventListener("click", () => setMacroFilter("runes"));
  macroCreaturesBtn?.addEventListener("click", () => setMacroFilter("creatures"));
  macroPlantsBtn?.addEventListener("click", () => setMacroFilter("plants"));
  macroPotionsBtn?.addEventListener("click", () => setMacroFilter("potions"));

  // --- Reset All Filters ---
  function resetAllFilters() {
    activeYear = "ALL";
    activeType = "ALL";
    activeDuel = "ALL";
    activeValence = "ALL";
    searchQuery = "";
    if (searchInput) searchInput.value = "";
    if (clearSearchBtn) clearSearchBtn.classList.add("hidden");

    setMacroFilter("spells");
  }

  resetAllFiltersBtn?.addEventListener("click", resetAllFilters);
  document.getElementById("resetFiltersBtn")?.addEventListener("click", resetAllFilters);

  // --- Global Keyboard ESC Listener ---
  window.addEventListener("keydown", (e) => {
    if (e.key === "Escape") {
      closeSpellModal();
      closeItemModal();
      closeCalculator();
    }
  });

  // --- Hero Stat Cards Click Listeners ---
  document.querySelectorAll(".stat-card").forEach(card => {
    card.addEventListener("click", () => {
      const targetMacro = card.dataset.statMacro;
      if (targetMacro) {
        setMacroFilter(targetMacro);
        const catalogSec = document.getElementById("catalogSection");
        if (catalogSec) {
          catalogSec.scrollIntoView({ behavior: "smooth" });
        }
      }
    });
    card.addEventListener("keydown", (e) => {
      if (e.key === "Enter" || e.key === " ") {
        e.preventDefault();
        card.click();
      }
    });
  });

  // Expose global methods
  window.setMacroFilter = setMacroFilter;
  window.resetAllFilters = resetAllFilters;

  // --- Initial Boot ---
  updateStats();

  const initialHash = (typeof window !== "undefined" && window.location && window.location.hash)
    ? window.location.hash.replace("#", "").toLowerCase()
    : "";
  const validMacros = ["spells", "runes", "creatures", "plants", "potions"];
  if (validMacros.includes(initialHash)) {
    setMacroFilter(initialHash);
  } else if (initialHash === "creature") {
    setMacroFilter("creatures");
  } else if (initialHash === "piante") {
    setMacroFilter("plants");
  } else if (initialHash === "pozioni") {
    setMacroFilter("potions");
  } else {
    setMacroFilter("spells");
  }

}

// Robust execution whether script is evaluated before or after DOMContentLoaded
if (document.readyState === "loading") {
  document.addEventListener("DOMContentLoaded", initPortal);
} else {
  initPortal();
}
