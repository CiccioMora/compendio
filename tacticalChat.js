// tacticalChat.js - Consigliere Tattico & Grimorio di Azione per Hogwarts
// Analizza il campo di azione (Duello, Pozioni, Creature, Erbologia, Rune, Misto)
// e restituisce la mossa o combo ottimale con spiegazione, valenze e alternative tattiche.

(function() {
  "use strict";

  // --- Configuration & Quick Suggestions per Field ---
  const CHAT_FIELDS = {
    duel: {
      name: "Duello",
      icon: "⚔️",
      placeholder: "Descrivi la situazione di duello (es. 'L\'avversario usa Protego e mi attacca con fiamme')...",
      chips: [
        "⚔️ Combo Disarmo e Schianto Rapido",
        "🛡️ Superare o Abbattere un Protego",
        "🔥 Neutralizzare un attacco di Fuoco",
        "⚡ Attacco rapido con Valenza Opposta",
        "💨 Fuga ed Evasione da Accerchiamento",
        "🪄 Spezzare un incantesimo di Legame"
      ],
      chipsPhysical: [
        "🥊 Schivata e Disarmo Fisico del Polso",
        "🥋 Leva Articolare e Proiezione a Terra",
        "🦵 Spazzata Bassa alla Gamba d'Appoggio",
        "🧥 Parata con Mantello e Presa al Collo",
        "💨 Evasione Bassa da Pugno o Carica",
        "💥 Colpo Rapido al Plesso Solare"
      ],
      chipsHybridUserMagic: [
        "🪄 Bloccare la Carica Fisica con Glisseo e Impedimenta",
        "❄️ Inabilitazione Motoria con Gambemolli a Distanza",
        "⛓️ Incarceramus per Confinare l'Assalitore Fisico",
        "⚡ Stordimento Preventivo con Stupeficium",
        "💨 Arretramento Veloce con Carpe Retractum",
        "🛡️ Barriera d'Attrito per Impedire il Corpo a Corpo"
      ],
      chipsHybridEnemyMagic: [
        "🏃 Blitz Ravvicinato e Deviazione del Polso Armato",
        "📐 Evasione a Zig-Zag per Schivare gli Incantesimi",
        "💥 Disarmo Fisico della Bacchetta e Atterramento",
        "🧥 Accecamento con Mantello per Togliere la Mira",
        "🦵 Spazzata a Terra prima che Lanci l'Incanto",
        "🥋 Blocco Articolare del Braccio che Impugna la Bacchetta"
      ]
    },
    potions: {
      name: "Arte delle Pozioni",
      icon: "🧪",
      placeholder: "Descrivi il problema alchemico (es. 'Serve un antidoto rapido a veleno ingerito')...",
      chips: [
        "🧪 Antidoto Rapido a Veleno Ingerito",
        "💥 Pozione Tattica da Lancio in Duello",
        "🩹 Cura immediata di Ferite Profonde",
        "🧠 Pozione per Potenziare Riflessi e Mente",
        "😴 Pacificazione Silenziosa con Sonnifero",
        "🐺 Gestione Licantropia con Antilupo"
      ]
    },
    creatures: {
      name: "Creature Magiche",
      icon: "🐉",
      placeholder: "Quale creatura stai affrontando? (es. 'Come neutralizzare un Berretto Rosso o un Molliccio')...",
      chips: [
        "🐉 Neutralizzare un Molliccio",
        "👹 Difendersi da un Berretto Rosso",
        "🦅 Pacificare e Avvicinare un Ippogrifo",
        "👻 Respingere un Dissennatore",
        "🕷️ Allontanare un'Acromantula",
        "🐛 Raccogliere Succo da Horklump"
      ]
    },
    herbology: {
      name: "Erbologia Botanica",
      icon: "🌿",
      placeholder: "Quale pianta o rimedio botanico vuoi usare? (es. 'Come liberarsi dal Tranello del Diavolo')...",
      chips: [
        "🌿 Liberarsi dal Tranello del Diavolo",
        "🪴 Uso e Protezione dalla Mandragola",
        "🩸 Rimarginare con Essenza di Dittamo",
        "🥀 Neutralizzare una Tentacula Velenosa",
        "🌳 Scegliere un Legno Nobile per Difesa",
        "🫁 Respirare Sott'acqua con Algabranchia"
      ]
    },
    runes: {
      name: "Antiche Rune & Aritmanzia",
      icon: "ᛟ",
      placeholder: "Quale sigillo o calcolo di valenza ti serve? (es. 'Spezzare un sigillo a Valenza 4')...",
      chips: [
        "ᛟ Spezzare un Sigillo a Valenza 4",
        "🛡️ Creare un Cerchio di Protezione Runica",
        "🔢 Calcolare la Valenza Opposta di un Attacco",
        "⚡ Triade di Thoot per Legame Permanente",
        "🌊 Attivare la Matrice Elementale Acqua (Fehu)",
        "🔥 Runa Kenaz per Dissipare Freddo Oscuro"
      ]
    },
    all: {
      name: "Strategia Globale (Mista)",
      icon: "✨",
      placeholder: "Descrivi qualsiasi scenario combinato (es. 'Combo con Pozione, Pianta e Incantesimo')...",
      chips: [
        "⚔️ Combo Integrata: Pianta + Incantesimo + Pozione",
        "🛡️ Difesa Totale contro Mago Oscuro e Bestia",
        "🧪 Preparare il Terreno prima del Duello",
        "🪄 Disarmare e Cancellare la Memoria",
        "📐 Sovraccarico Aritmantico di Zona"
      ]
    }
  };

  // State
  let activeField = "duel";
  let activeMode = "combo";          // "single" | "combo"
  let activeSteps = 3;               // 2 | 3 | 4
  let duelOfficial = true;           // true (Ufficiale) | false (Non Ufficiale)
  let duelType = "magical";          // "magical" | "physical" | "hybrid"
  let duelHybridRole = "user_magic"; // "user_magic" | "enemy_magic"
  let chatHistory = [];
  let isProcessing = false;

  // Safe data getters
  function getSpells() {
    if (typeof window !== "undefined" && window.SPELLS_DATA && Array.isArray(window.SPELLS_DATA)) {
      return window.SPELLS_DATA;
    }
    return [];
  }

  function getMaterie() {
    if (typeof window !== "undefined" && window.materieData) {
      return window.materieData;
    }
    return { creature: [], piante: [], pozioni: [] };
  }

  // Helper: Create clickable HTML tag for a spell or item
  function formatEntityLink(name, type, id) {
    if (type === "spell" || type === "rune") {
      return `<button type="button" onclick="window.openSpellDetails('${id}')" class="inline-flex items-center gap-1 px-2 py-0.5 rounded bg-amber-500/15 hover:bg-amber-500/30 text-amber-300 border border-amber-500/30 text-[11px] font-code font-bold transition-all hover:scale-105 shadow-sm" title="Clicca per aprire la scheda didattica"><span>⚡</span> <span>${name}</span></button>`;
    } else if (type === "creature") {
      return `<button type="button" onclick="window.openItemDetails('creatures', '${id}')" class="inline-flex items-center gap-1 px-2 py-0.5 rounded bg-amber-600/15 hover:bg-amber-600/30 text-amber-300 border border-amber-600/30 text-[11px] font-semibold transition-all hover:scale-105 shadow-sm" title="Clicca per aprire la scheda creatura"><span>🐉</span> <span>${name}</span></button>`;
    } else if (type === "plant") {
      return `<button type="button" onclick="window.openItemDetails('plants', '${id}')" class="inline-flex items-center gap-1 px-2 py-0.5 rounded bg-emerald-600/15 hover:bg-emerald-600/30 text-emerald-300 border border-emerald-600/30 text-[11px] font-semibold transition-all hover:scale-105 shadow-sm" title="Clicca per aprire la scheda botanica"><span>🌿</span> <span>${name}</span></button>`;
    } else if (type === "potion") {
      return `<button type="button" onclick="window.openItemDetails('potions', '${id}')" class="inline-flex items-center gap-1 px-2 py-0.5 rounded bg-indigo-600/15 hover:bg-indigo-600/30 text-indigo-300 border border-indigo-600/30 text-[11px] font-semibold transition-all hover:scale-105 shadow-sm" title="Clicca per aprire la ricetta alchemica"><span>🧪</span> <span>${name}</span></button>`;
    }
    return `<strong>${name}</strong>`;
  }

  // --- ADAPTER FOR SINGLE MOVE OR COMBO (2, 3, 4 STEPS) ---
  function formatAdviceForModeAndSteps(advice, mode, requestedSteps, field, query) {
    if (!advice || !advice.bestMove || !Array.isArray(advice.bestMove.steps)) {
      return advice;
    }

    const q = (query || "").toLowerCase();
    const originalSteps = advice.bestMove.steps;

    if (mode === "single") {
      let chosenIdx = 0;
      if (originalSteps.length > 1) {
        const hasDmgQuery = /(?:ustio|brucia|ferit|danno|colp|tagli|fiamm|esplod|fulmin|stord|disarm)/i.test(q);
        const s1Text = (originalSteps[1].action + " " + originalSteps[1].details).toLowerCase();
        if (hasDmgQuery && /(?:ustio|brucia|ferit|danno|colp|tagli|fiamm|esplod|fulmin|stord|disarm)/i.test(s1Text)) {
          chosenIdx = 1;
        }
      }
      const base = originalSteps[chosenIdx] || originalSteps[0];
      const cleanAction = base.action.replace(/^(?:Fase\s+[^:]+:|Inizio\s+Tattico:|Attacco\s+Decisivo:)\s*/i, "");

      const singleStep = {
        num: 1,
        action: `Mossa Risolutiva: ${cleanAction}`,
        spellLink: base.spellLink,
        details: base.details
      };

      return {
        ...advice,
        mode: "single",
        stepsCount: 1,
        bestMove: {
          ...advice.bestMove,
          name: `Azione Singola: ${cleanAction}`,
          steps: [singleStep],
          rationale: `Risoluzione immediata in colpo singolo: ${advice.bestMove.rationale}`
        }
      };
    }

    // Mode === "combo"
    const targetCount = Math.max(2, Math.min(4, Number(requestedSteps) || 3));
    let newSteps = [];

    if (targetCount === 2) {
      newSteps = [
        { ...originalSteps[0], num: 1 },
        { ...(originalSteps[1] || originalSteps[0]), num: 2 }
      ];
    } else if (targetCount === 3) {
      if (originalSteps.length >= 3) {
        newSteps = [
          { ...originalSteps[0], num: 1 },
          { ...originalSteps[1], num: 2 },
          { ...originalSteps[2], num: 3 }
        ];
      } else {
        newSteps = [
          { ...originalSteps[0], num: 1 },
          { ...(originalSteps[1] || originalSteps[0]), num: 2 },
          {
            num: 3,
            action: "Neutralizzazione di Chiusura",
            spellLink: formatEntityLink("Expelliarmus", "spell", "expelliarmus"),
            details: "Approfitta dello sbilanciamento dell'avversario per sferrare un disarmo immediato o bloccare l'azione con un incantesimo di stordimento."
          }
        ];
      }
    } else if (targetCount === 4) {
      let s1 = { ...originalSteps[0], num: 1 };
      let s2 = { ...(originalSteps[1] || originalSteps[0]), num: 2 };
      let s3 = originalSteps[2]
        ? { ...originalSteps[2], num: 3 }
        : {
            num: 3,
            action: "Neutralizzazione di Chiusura",
            spellLink: formatEntityLink("Expelliarmus", "spell", "expelliarmus"),
            details: "Disarma o stordisci l'avversario approfittando della rottura della sua guardia difensiva."
          };

      let s4;
      if (originalSteps[3]) {
        s4 = { ...originalSteps[3], num: 4 };
      } else if (field === "duel") {
        s4 = {
          num: 4,
          action: "Confinamento Permanente e Messa in Sicurezza",
          spellLink: formatEntityLink("Petrificus Totalus", "spell", "petrificus-totalus") + " o " + formatEntityLink("Incarceramus", "spell", "incarceramus"),
          details: "Per scongiurare qualsiasi contrattacco fisico o recupero della bacchetta caduta, completa la sequenza con <strong>Petrificus Totalus (Valenza 8)</strong> per irrigidire completamente il corpo del rivale o <strong>Incarceramus (Valenza 6)</strong> per avvolgerlo in funi magiche indistruttibili."
        };
      } else if (field === "potions") {
        s4 = {
          num: 4,
          action: "Stabilizzazione Post-Trattamento e Monitoraggio",
          spellLink: formatEntityLink("Pozione Rinvigorente", "potion", "pot-rinvigorente"),
          details: "Dopo la somministrazione o l'azione primaria, fai assumere una dose di <strong>Pozione Rinvigorente</strong> per ripristinare la vitalità dei tessuti ed eliminare i residui di shock o affaticamento alchemico."
        };
      } else if (field === "creatures") {
        s4 = {
          num: 4,
          action: "Confinamento e Segnalazione di Sicurezza",
          spellLink: formatEntityLink("Impedimenta", "spell", "impedimenta") + " / " + formatEntityLink("Signo", "spell", "signo"),
          details: "Delimita l'area attorno all'esemplare con un perimetro di sicurezza incantato e contatta un Custode delle Creature Magiche per la custodia definitiva."
        };
      } else if (field === "herbology") {
        s4 = {
          num: 4,
          action: "Riposizionamento Conservativo e Sigillo Botanico",
          spellLink: formatEntityLink("Herbivicus", "spell", "herbivicus"),
          details: "Riponi il campione o l'esemplare in un contenitore sigillato con terra ricca di sostanze nutritive e stabilizza la temperatura ambientale per non alterarne le proprietà officinali."
        };
      } else if (field === "runes") {
        s4 = {
          num: 4,
          action: "Ancoraggio e Sigillatura del Nodo Runico",
          spellLink: formatEntityLink("Iùngo", "spell", "iungo") + " con " + formatEntityLink("Jera", "rune", "runa-jera"),
          details: "Incanala <strong>Iùngo</strong> per legare la matrice appena modificata al ciclo naturale rappresentato dalla runa <strong>Jera</strong>, garantendo stabilità eterna e protezione da futuri sovraccarichi."
        };
      } else {
        s4 = {
          num: 4,
          action: "Bonifica Ambientale e Verifica Anti-Traccia",
          spellLink: formatEntityLink("Finite Incantatem", "spell", "finite-incantatem"),
          details: "Esegui una scansione ad ampio raggio con <strong>Finite Incantatem</strong> per dissipare ogni residuo magico, fumo o tossina dispersa nell'aria, lasciando la zona priva di pericoli latenti."
        };
      }

      newSteps = [s1, s2, s3, s4];
    }

    return {
      ...advice,
      mode: "combo",
      stepsCount: targetCount,
      bestMove: {
        ...advice.bestMove,
        steps: newSteps
      }
    };
  }

  // --- KNOWLEDGE & HEURISTIC TACTICAL REASONING ENGINE ---
  function computeTacticalAdvice(field, query, options = {}) {
    const q = (query || "").toLowerCase();

    // Determine requested resolution mode and step count
    const fallbackMode = typeof activeMode !== "undefined" ? activeMode : "combo";
    const fallbackSteps = typeof activeSteps !== "undefined" ? activeSteps : 3;
    let reqMode = (options && options.mode) || fallbackMode;
    let reqSteps = Number((options && options.steps) || fallbackSteps);

    // Determine duel parameters (Official vs Unofficial, Magical / Physical / Hybrid)
    const fallbackOfficial = typeof duelOfficial !== "undefined" ? duelOfficial : true;
    const fallbackDuelType = typeof duelType !== "undefined" ? duelType : "magical";
    const fallbackHybridRole = typeof duelHybridRole !== "undefined" ? duelHybridRole : "user_magic";

    let reqOfficial = options && options.duelOfficial !== undefined ? !!options.duelOfficial : fallbackOfficial;
    let reqDuelType = (options && options.duelType) || fallbackDuelType;
    let reqHybridRole = (options && options.duelHybridRole) || fallbackHybridRole;

    // Natural language query overrides for mode (only if not explicitly set in options)
    if (!options || (!options.mode && !options.steps)) {
      if (/(?:mossa\s+singola|singola\s+mossa|solo\s+un[ao]\s+mossa|un\s+solo\s+colpo|colpo\s+singolo|singolo\s+incant|1\s+pass|un\s+pass)/i.test(q)) {
        reqMode = "single";
        reqSteps = 1;
      } else if (/(?:2\s+pass|due\s+pass|combo\s+(?:da|a)\s+2)/i.test(q)) {
        reqMode = "combo";
        reqSteps = 2;
      } else if (/(?:4\s+pass|quattro\s+pass|combo\s+(?:da|a)\s+4)/i.test(q)) {
        reqMode = "combo";
        reqSteps = 4;
      } else if (/(?:3\s+pass|tre\s+pass|combo\s+(?:da|a)\s+3)/i.test(q)) {
        reqMode = "combo";
        reqSteps = 3;
      }
    }

    // Natural language duel overrides (only if not explicitly set in options)
    if (!options || options.duelOfficial === undefined) {
      if (/(?:duello\s+ufficiale|sfida\s+ufficiale|torneo|regolamentar|ufficiale)/i.test(q) && !/(?:non\s+ufficiale|clandestin)/i.test(q)) {
        reqOfficial = true;
      } else if (/(?:non\s+ufficiale|clandestin|liber[oa]|senza\s+regol|fuori\s+legge|riss[ae]|strada)/i.test(q)) {
        reqOfficial = false;
      }
    }

    if (!options || !options.duelType) {
      if (/(?:ibrid|un\s+mago\s+e\s+un\s+babban|uno\s+mago\s+e\s+uno\s+no|tu\s+mago|lui\s+mago|io\s+mago|lui\s+fisico|io\s+fisico|senza\s+bacchetta\s+contro\s+mago|mago\s+contro\s+combattente)/i.test(q)) {
        reqDuelType = "hybrid";
        if (!options || !options.duelHybridRole) {
          if (/(?:io\s+mago|tu\s+mago|io\s+ho\s+la\s+bacchetta|avversario\s+(?:fisico|babbano|bruto|senza\s+magia|a\s+mani\s+nude)|nemico\s+(?:fisico|a\s+mani\s+nude))/i.test(q)) {
            reqHybridRole = "user_magic";
          } else if (/(?:io\s+fisico|tu\s+fisico|io\s+senza\s+bacchetta|io\s+disarmato|avversario\s+(?:mago|ha\s+la\s+bacchetta|usa\s+la\s+magia)|nemico\s+mago)/i.test(q)) {
            reqHybridRole = "enemy_magic";
          }
        }
      } else if (/(?:duello\s+fisic|scontro\s+fisic|corpo\s+a\s+corpo|a\s+mani\s+nude|senza\s+magia|pugni|calci|arti\s+marziali|lotta|sala\s+d'armi)/i.test(q) && !/(?:magi|incant|bacchett)/i.test(q)) {
        reqDuelType = "physical";
      } else if (/(?:magic|bacchett|incantesim|protego|duello\s+magico)/i.test(q) && !/(?:ibrid|fisic)/i.test(q)) {
        reqDuelType = "magical";
      }
    }

    function evaluateRawAdvice(field, query, q, reqOfficial, reqDuelType, reqHybridRole) {
      const spells = getSpells();
      const materie = getMaterie();

    // --- Intent & Effect Feature Extraction ---
    const isExplicitAttack = /(?:voglio|attacc|colpir|lanciar|infligg|provoc|bruciar|atterrar|abbatter|disarmar|far\s+cader|facendolo\s+cader|mandar.*(?:suolo|terra|tappeto))/i.test(q);
    const isExplicitDefense = /(?:difend|difesa|parar|scherm|neutralizz|estingu|spegner|salvar|proteg|antidot|subisc|avversario\s+(?:usa|ha\s+usato|attacca|mi\s+attacca)|mi\s+attacca)/i.test(q) && !q.includes("voglio attaccare");

    const hasBurn = /(?:bruciat|brucia|ustio|piaghe|vescic|scottatur)/i.test(q);
    const hasFire = /(?:fuoco|fiamm|incendi|termic)/i.test(q);
    const hasFall = /(?:cader|cadut|suolo|terra|tappeto|scivol|atterr|sbilanc|inciamp|sgambett|gambe.*moll)/i.test(q);
    const hasDisarm = /(?:disarm|togli.*bacchett|volar.*bacchett)/i.test(q);
    const hasStun = /(?:stord|schiant|sven|incoscient|addorment)/i.test(q);
    const hasImmobilize = /(?:immobil|pietrif|blocca|legar|funi|congel)/i.test(q);
    const hasBlind = /(?:accec|ciec|buio|fumo|oscur|nebbia|zucca|melofors)/i.test(q);
    const hasShield = /(?:protego|scudo|barriera)/i.test(q);
    const hasShieldBreak = (/(?:romper|abbatter|sfondar|superar|bypass|annullar)/i.test(q) && hasShield) || q.includes("superare o abbattere un protego") || q.includes("rompo un protego");
    const hasLift = /(?:sollev|aria|volar|sospend|levit|levicorpus)/i.test(q);
    const hasWater = /(?:acqua|bolla|sommerg|affog|ebublio|aguamenti)/i.test(q);
    const hasCut = /(?:tagli|recid|fendent|squarc|diffindo)/i.test(q);

    // 0. MULTIDISCIPLINARY COMBOS (field === "all" or queries mentioning mixed strategies)
    if (field === "all" && (q.includes("integrat") || q.includes("misto") || (q.includes("pianta") && q.includes("pozion")) || q.includes("tutte") || q.includes("combo integrata"))) {
      return {
        title: "Strategia Magistrale Integrata: Pianta + Incantesimo + Pozione",
        fieldLabel: "✨ Strategia Globale • Tattica Multidisciplinare",
        bestMove: {
          name: "Trittico di Sopraffazione: Fumo Alchemico ➔ Radici ➔ Schianto",
          steps: [
            {
              num: 1,
              action: "Fase Alchemica: Copertura e Disorientamento",
              spellLink: formatEntityLink("Pozione Fumogena", "potion", "pot-fumogena"),
              details: "Frangere a terra una fiala di <strong>Pozione Fumogena</strong>: crea all'istante una coltre impenetrabile che impedisce al nemico di mirare o prevedere i tuoi movimenti."
            },
            {
              num: 2,
              action: "Fase Botanica / Incanto: Intrappolamento al Terreno",
              spellLink: formatEntityLink("Herbivicus", "spell", "herbivicus"),
              details: "Attraverso il fumo, proietta <strong>Herbivicus</strong> sul terreno per accelerare all'istante la crescita delle radici e dell'erba circostante, avvinghiando le caviglie dell'avversario."
            },
            {
              num: 3,
              action: "Fase Arcana: Neutralizzazione Finale",
              spellLink: formatEntityLink("Stupeficium", "spell", "stupeficium"),
              details: "Con il bersaglio cieco e bloccato alle caviglie, scaglia <strong>Stupeficium (V7)</strong> per completare la vittoria senza subire contrattacchi."
            }
          ],
          rationale: "La combinazione di un reagente alchemico fisico (il fumo non è intercettato da un Protego ordinario), l'interazione biologica con l'ambiente e la scarica cinetica della bacchetta rende l'azione inarrestabile."
        },
        alternatives: [
          {
            title: "Piano B: Sigillo Runico Difensivo",
            desc: `In caso di contrattacco rapido, arretra all'interno di un cerchio runico attivato con ${formatEntityLink("Signo", "spell", "signo")} e la runa ${formatEntityLink("Algiz", "rune", "runa-algiz")} per assorbire qualsiasi maledizione a distanza.`
          },
          {
            title: "Piano C: Medimagia d'Urgenza",
            desc: `Se hai subito lesioni durante l'ingaggio, applica tre gocce di ${formatEntityLink("Dittamo", "plant", "p-dittamo")} sulle ferite per una cicatrizzazione immediata.`
          }
        ],
        warnings: "La coordinazione tra lancio di fiala ed incantesimo richiede massimo tempismo per non cadere vittime della propria stessa cortina di fumo."
      };
    }

    // 1. DUEL / COMBAT SCENARIOS
    if (field === "duel" || (field === "all" && (q.includes("duell") || q.includes("combatt") || q.includes("protego") || q.includes("attacc") || q.includes("scudo") || q.includes("disarm") || hasBurn || hasFall))) {
      
      const duelRegimeLabel = reqOfficial ? '⚖️ Ufficiale' : '🏴 Non Ufficiale';
      const duelFieldBadge = `⚔️ Duello • ${duelRegimeLabel} • 🪄 Magico`;
      const duelOfficialWarningSuffix = reqOfficial
        ? "Regole Ufficiali di Duello: incantesimi pienamente conformi al Codice Didattico di Hogwarts (⚔️ SÌ). Vietate arti oscure o lesioni permanenti."
        : "Duello Non Ufficiale / Scontro Libero: nessuna limitazione arbitrale. Ammesse magie d'impatto ambientale, trasfigurazioni pesanti e pozioni tattiche da lancio.";

      // A. DUELLO FISICO (Lotta corpo a corpo / Disarmati / Sala d'armi)
      if (reqDuelType === "physical") {
        const isDisarmIntent = hasDisarm || /(?:arma|polso|bacchetta|disarm|leva)/i.test(q);
        const officialRuleText = reqOfficial
          ? "⚖️ Duello Fisico Ufficiale: Regolamento da Sala d'Armi di Hogwarts. Vietati colpi proibiti (occhi, gola, colpi dopo la dichiarazione di resa). Vittoria all'atterramento netto o resa per leva articolare."
          : "🏴 Duello Fisico Libero (Non Ufficiale): Nessuna restrizione arbitrale. Sfrutta pareti, manto, oggetti contundenti ed evita l'accerchiamento.";

        if (isDisarmIntent) {
          return {
            title: `Duello Fisico: Disarmo da Presa e Atterramento (${reqOfficial ? 'Ufficiale' : 'Libero'})`,
            fieldLabel: `⚔️ Duello Fisico • ${reqOfficial ? '⚖️ Ufficiale' : '🏴 Non Ufficiale'}`,
            bestMove: {
              name: "Sequenza di Lotta: Evasione della Linea ➔ Leva Articolare al Polso ➔ Proiezione",
              steps: [
                {
                  num: 1,
                  action: "Evasione Angolata dalla Linea di Spinta",
                  spellLink: "<strong>Biomeccanica di Sala d'Armi</strong>",
                  details: "Schiva lateralmente di 45 gradi uscendo dalla traiettoria del pugno o dell'arma avversaria con baricentro ribassato, inducendo il rivale a sbilanciarsi sul proprio slancio a vuoto."
                },
                {
                  num: 2,
                  action: "Presa a Due Mani e Torsione a Leva Esterna",
                  spellLink: "<strong>Leva Articolare al Polso</strong>",
                  details: "Afferra l'articolazione del polso del braccio proteso con entrambe le mani: applica una torsione rotatoria verso l'esterno che forza l'apertura istantanea delle dita e disarma qualsiasi oggetto o bacchetta impugnata."
                },
                {
                  num: 3,
                  action: "Spazzata Circolare e Atterramento al Suolo",
                  spellLink: "<strong>Spazzata al Tallone</strong>",
                  details: "Mentre l'avversario cede al dolore articolare, aggancia la sua gamba d'appoggio da dietro con il collo del piede e spingi la spalla opposta: l'avversario stramazza a terra supino senza appigli."
                },
                {
                  num: 4,
                  action: "Immobilizzazione con Controllo Scapolare",
                  spellLink: "<strong>Leva al Suolo & Confinamento</strong>",
                  details: "Fissa il braccio dell'avversario al suolo posizionando il ginocchio dietro la scapola per impedire qualsiasi contrattacco fino alla resa formale."
                }
              ],
              rationale: "Nel combattimento corpo a corpo, la manipolazione della forza d'inerzia avversaria unita a leve articolari chiuse consente di neutralizzare avversari di qualsiasi stazza senza l'ausilio di incantesimi."
            },
            alternatives: [
              {
                title: "Piano B: Parata con Mantello e Avvolgimento Visivo",
                desc: "Usa il lembo pesante del mantello da mago per intercettare il colpo e avvolgerlo attorno al capo del rivale, togliendogli la vista prima di una spazzata bassa."
              },
              {
                title: "Piano C: Gomitata d'Incontro al Costato",
                desc: "Se l'avversario chiude a sorpresa la distanza in clinch, abbassa il gomito e percuoti le costole fluttuanti per rompere la presa e riguadagnare il controllo."
              }
            ],
            warnings: officialRuleText
          };
        }

        // Generic physical duel scenario (strike / knockdown / brawling)
        return {
          title: `Duello Fisico: Intercettazione e Proiezione Baricentrica (${reqOfficial ? 'Ufficiale' : 'Libero'})`,
          fieldLabel: `⚔️ Duello Fisico • ${reqOfficial ? '⚖️ Ufficiale' : '🏴 Non Ufficiale'}`,
          bestMove: {
            name: "Sequenza Difensiva e Proiezione: Parata d'Avambraccio ➔ Percussione al Plesso ➔ Atterramento sull'Anca",
            steps: [
              {
                num: 1,
                action: "Deflessione Dinamica del Colpo",
                spellLink: "<strong>Parata d'Avambraccio Esterno</strong>",
                details: "Defletti verso l'esterno il colpo o la carica dell'avversario con l'avambraccio flesso ad angolo retto, proteggendo il mento e aprendo la guardia centrale del rivale."
              },
              {
                num: 2,
                action: "Percussione Controllata al Plesso Solare",
                spellLink: "<strong>Percussione Cinetica</strong>",
                details: "Penetra nella guardia aperta con un colpo dritto al plesso solare per contrarre il diaframma dell'avversario e mozzargli momentaneamente il fiato."
              },
              {
                num: 3,
                action: "Proiezione sull'Anca e Atterramento",
                spellLink: "<strong>Proiezione Baricentrica</strong>",
                details: "Posiziona l'anca sotto il baricentro del rivale, tira il braccio agganciato e sollevalo proiettandolo a terra a gambe all'aria."
              },
              {
                num: 4,
                action: "Messa in Sicurezza e Distanza di Guardia",
                spellLink: "<strong>Guardia Tattica</strong>",
                details: "Arretra di due passi mantenendo la posizione di guardia di sala d'armi, ordinando all'avversario al suolo di dichiarare la resa."
              }
            ],
            rationale: "La deflessione esterna rompe l'equilibrio del busto avversario; la successiva proiezione baricentrica usa il peso del contendente contro sé stesso garantendo un atterramento pulito."
          },
          alternatives: [
            {
              title: "Piano B: Schivata Circolare e Spinta alle Spalle",
              desc: "Effettua un perno rotatorio sul piede anteriore mentre il rivale carica, spingendolo energicamente tra le scapole per mandarlo a sbattere contro il terreno o la parete."
            },
            {
              title: "Piano C: Blocco Doppio d'Avambraccio in Clinch",
              desc: "Se l'avversario tenta una presa a due mani, serra i doveri avambracci a cuneo per aprire la sua presa e arretra di scatto."
            }
          ],
          warnings: officialRuleText
        };
      }

      // B. DUELLO IBRIDO: TU MAGO VS NEMICO FISICO
      if (reqDuelType === "hybrid" && reqHybridRole === "user_magic") {
        return {
          title: `Duello Ibrido: Controllo e Neutralizzazione a Distanza (Tu Mago vs Nemico Fisico)`,
          fieldLabel: `⚡ Duello Ibrido • Tu Mago vs Nemico Fisico • ${reqOfficial ? '⚖️ Ufficiale' : '🏴 Non Ufficiale'}`,
          bestMove: {
            name: "Sequenza di Arresto Carica: Intercettazione (Glisseo / Impedimenta) ➔ Legame (Incarceramus / Gambemolli) ➔ Schianto",
            steps: [
              {
                num: 1,
                action: "Arresto Immediato della Carica Fisica",
                spellLink: formatEntityLink("Glisseo", "spell", "glisseo") + " o " + formatEntityLink("Impedimenta", "spell", "impedimenta"),
                details: "Mentre l'avversario corre per chiudere la distanza, incanala <strong>Glisseo (V6 - Terra)</strong> sul pavimento per annullare l'attrito e farlo crollare a terra sul proprio slancio, oppure proietta <strong>Impedimenta (V3)</strong> per congelare la sua avanzata cinetica a mezz'aria."
              },
              {
                num: 2,
                action: "Inabilitazione Motoria a Bersaglio Bloccato",
                spellLink: formatEntityLink("Locomotor Wibbly", "spell", "locomotor-wibbly") + " o " + formatEntityLink("Incarceramus", "spell", "incarceramus"),
                details: "Mentre il contendente tenta faticosamente di rialzarsi o avanzare, scaglia <strong>Locomotor Wibbly (V2)</strong> per liquefare i muscoli delle sue gambe come gelatina, o <strong>Incarceramus (V6)</strong> per avvolgerlo con robuste funi magiche."
              },
              {
                num: 3,
                action: "Neutralizzazione Definitiva a Distanza di Sicurezza",
                spellLink: formatEntityLink("Stupeficium", "spell", "stupeficium") + " o " + formatEntityLink("Petrificus Totalus", "spell", "petrificus-totalus"),
                details: "Senza mai avvicinarti a meno di 3 metri, completa lo scontro con <strong>Stupeficium (V7)</strong> per addormentare/stordire il contendente, azzerando ogni minaccia fisica."
              },
              {
                num: 4,
                action: "Confinamento Runico di Sicurezza",
                spellLink: formatEntityLink("Signo", "spell", "signo"),
                details: "Traccia con la bacchetta un cerchio runico di guardia attorno all'avversario per prevenire qualsiasi interferenza o reazione improvvisa."
              }
            ],
            rationale: "La magia gode di portata e velocità supersonica: non permettere mai al contendente fisico di entrare a distanza di presa (sotto 1.5 metri). Neutralizzarlo da lontano azzera il pericolo al 100%."
          },
          alternatives: [
            {
              title: "Piano B: Barriera di Fumo con Fumos",
              desc: `Se la carica è rapida, emetti ${formatEntityLink("Fumos", "spell", "fumos")} (V5) e arretra diagonalmente: il nemico fisico non potrà vedere la tua sagoma e andrà a vuoto.`
            },
            {
              title: "Piano C: Disorientamento con Melofors",
              desc: `Incastra una pesante zucca sulla testa dell'avversario con ${formatEntityLink("Melofors", "spell", "melofors")} (V4): privato della vista e sbilanciato dal peso della zucca, il bruto cesserà l'attacco.`
            }
          ],
          warnings: reqOfficial
            ? "⚖️ Duello Ibrido Ufficiale: È severamente vietato scagliare sortilegi laceranti (es. Diffindo) o maledizioni lesive permanenti su un avversario che combatte a mani nude. Usare solo incantesimi di contenimento e stordimento non cruenti."
            : "🏴 Duello Ibrido Libero (Non Ufficiale): Se l'avversario fisico impugna armi da taglio o ha forza sovrumana, puoi usare incanti cinetici pesanti come Bombarda sul terreno per sbalzarlo indietro."
        };
      }

      // C. DUELLO IBRIDO: TU FISICO VS NEMICO MAGO
      if (reqDuelType === "hybrid" && reqHybridRole === "enemy_magic") {
        return {
          title: `Duello Ibrido: Tattica di Blitz e Neutralizzazione Bacchetta (Tu Fisico vs Nemico Mago)`,
          fieldLabel: `⚡ Duello Ibrido • Tu Fisico vs Nemico Mago • ${reqOfficial ? '⚖️ Ufficiale' : '🏴 Non Ufficiale'}`,
          bestMove: {
            name: "Strategia Anti-Mago: Corsa Evasiva a Zig-Zag ➔ Blitz Ravvicinato ➔ Deviazione e Disarmo del Polso Armato",
            steps: [
              {
                num: 1,
                action: "Rottura della Linea di Puntamento con Movimento Evasivo",
                spellLink: "<strong>Schivata a Spirale / Zig-Zag</strong>",
                details: "Un mago deve puntare la bacchetta dritto verso di te per colpire. Non correre in linea retta: muoviti a zig-zag con frequenti cambi di livello e baricentro ribassato per togliere al rivale il tempo di collimare la mira."
              },
              {
                num: 2,
                action: "Blitz Ravvicinato ed Intercettazione del Polso Armato",
                spellLink: "<strong>Deflessione d'Avambraccio Anti-Bacchetta</strong>",
                details: "Chiudi fulmineamente la distanza entrando sotto il raggio di puntamento (<1 metro): prima che il mago completi la pronuncia della formula, colpisci dal basso verso l'alto il suo avambraccio armato con il palmo della mano, facendo sparare la scintilla a vuoto verso il soffitto."
              },
              {
                num: 3,
                action: "Torsione Articolare, Disarmo e Spazzata al Mago",
                spellLink: "<strong>Torsione a Leva & Caduta Bacchetta</strong>",
                details: "Afferra saldamente il polso armato del rivale e torcilo verso l'interno costringendolo ad aprire le dita e far cadere la bacchetta al suolo; contemporaneamente falcia la sua gamba d'appoggio per farlo crollare a terra supino."
              },
              {
                num: 4,
                action: "Calcio di Allontanamento Bacchetta e Controllo a Terra",
                spellLink: "<strong>Allontanamento Bacchetta & Leva</strong>",
                details: "Calcia istantaneamente la bacchetta caduta ad almeno 5 metri di distanza e fissa il mago a terra con una presa di leva, ordinandogli la resa."
              }
            ],
            rationale: "Il tempo di emissione di un incantesimo richiede formulazione mentale, allineamento fisico della bacchetta e pronuncia fonetica. A distanza inferiore a 1 metro, la velocità biomeccanica di una presa o di un pugno è più rapida dell'attivazione magica."
          },
          alternatives: [
            {
              title: "Piano B: Lancio del Mantello per Accecare la Mira",
              desc: "Togliti il mantello e lancialo sul viso del mago: privato della visuale, l'avversario non oserà lanciare alla cieca e ti darà 2 secondi per chiudere la distanza e placcarlo."
            },
            {
              title: "Piano C: Sfruttamento di Ripari Ambientali e Imboscata",
              desc: "Se il mago si trova a distanza maggiore di 5 metri, riparati dietro colonne o tavoli solidi per fargli scaricare gli incanti contro gli ostacoli, quindi scatta nell'intervallo tra due lanci."
            }
          ],
          warnings: reqOfficial
            ? "⚖️ Duello Ibrido Ufficiale: Secondo il codice di sfida mista, il disarmo e l'allontanamento della bacchetta decretano la vittoria immediata del contendente fisico. È vietato colpire ulteriormente il mago disarmato."
            : "🏴 Duello Ibrido Libero (Non Ufficiale): Priorità assoluta distruggere o scagliare lontano la bacchetta: un mago a terra può tentare un incantesimo di contatto non verbale se riesce a toccare il legno della bacchetta!"
        };
      }
      
      // Scenario 1: BURN / FIRE + FALL / KNOCKDOWN (e.g. "voglio attaccare il mio avversario provocandogli bruciature e facendolo cadere al suolo")
      if ((hasBurn || hasFire) && hasFall && (isExplicitAttack || !isExplicitDefense)) {
        return {
          title: "Strategia di Duello: Atterramento al Suolo e Attacco Ustionante",
          fieldLabel: "⚔️ Duello Magico • Combo Offensiva di Controllo & Danno",
          bestMove: {
            name: "Sequenza Tattica: Sbilanciamento Rapido (Glisseo) ➔ Piaghe Termiche (Exulcero / Incendio)",
            steps: [
              {
                num: 1,
                action: "Annullamento dell'Attrito e Atterramento Immediato",
                spellLink: formatEntityLink("Glisseo", "spell", "glisseo"),
                details: "Inizia incanalando <strong>Glisseo (Valenza 6 - Terra)</strong> direttamente sulla porzione di pavimento sotto i piedi dell'avversario. Annulla istantaneamente il coefficiente d'attrito: il rivale perde aderenza e stramazza rovinosamente a terra supino, perdendo la linea di mira e l'assetto per erigere uno scudo."
              },
              {
                num: 2,
                action: "Attacco Ustionante al Bersaglio a Terra",
                spellLink: formatEntityLink("Exulcero", "spell", "exulcero") + " o " + formatEntityLink("Incendio", "spell", "incendio"),
                details: "Mentre l'avversario è steso al suolo e tenta disperatamente di rialzarsi, scaglia <strong>Exulcero (Valenza 4 - Maledictio VI Anno)</strong>: la stoccata provoca bruciature cutanee dolorose e piaghe simili a bruciature di sigaro sul torso del rivale, oppure usa <strong>Incendio (Valenza 1)</strong> per scatenare getti di fiamme che incendiano le vesti costringendolo a rotolare nel panico."
              },
              {
                num: 3,
                action: "Disarmo di Chiusura a Bersaglio Indifeso",
                spellLink: formatEntityLink("Expelliarmus", "spell", "expelliarmus"),
                details: "Approfitta dell'attimo in cui il bersaglio è a terra in preda al bruciore per sferrare un netto <strong>Expelliarmus (Valenza 2)</strong> al polso della mano armata, strappandogli la bacchetta prima che possa tentare una replica."
              }
            ],
            rationale: "La combinazione di mobilità annullata (Glisseo V6 / Terra) e danno termico immediato (Exulcero V4 o Incendio V1) garantisce che il secondo colpo vada a segno al 100%: un bersaglio steso a terra non ha appoggio per schivare né equilibrio per sostenere un Protego ortogonale."
          },
          alternatives: [
            {
              title: "Piano B (Sequenza Inversa: Danno Termico ➔ Spinta Cinetica)",
              desc: `Colpisci a sorpresa con ${formatEntityLink("Exulcero", "spell", "exulcero")} (V4) per infliggere fitte ustionanti, seguito all'istante da ${formatEntityLink("Flipendo", "spell", "flipendo")} (V1) al torace per scaraventare l'avversario all'indietro facendolo schiantare a gambe all'aria.`
            },
            {
              title: "Piano C (Variante Liquefazione Muscolare: Gambemolli)",
              desc: `Applica ${formatEntityLink("Locomotor Wibbly", "spell", "locomotor-wibbly")} (V2) per rendere le gambe del rivale come gelatina facendolo crollare al suolo, e subito dopo scaglia ${formatEntityLink("Incendio", "spell", "incendio")} (V1) sul mantello per completare l'obiettivo.`
            }
          ],
          warnings: "Tutti gli incantesimi della combo (Glisseo, Exulcero, Incendio, Flipendo, Expelliarmus) sono pienamente abilitati in duello formale (⚔️ SÌ). Le bruciature da Exulcero vanno trattate a fine scontro con essenza di Dittamo; è rigorosamente proibito infierire con ulteriori fiamme su un avversario già disarmato e al tappeto."
        };
      }

      // Scenario 2: BLIND / SMOKE + DISARM
      if (hasBlind && (hasDisarm || isExplicitAttack)) {
        return {
          title: "Strategia di Duello: Accecamento Tattico e Disarmo Rapido",
          fieldLabel: "⚔️ Duello Magico • Tattica Offensiva Elusiva",
          bestMove: {
            name: "Doppietta di Furtività: Cortina Visiva ➔ Disarmo Diretto",
            steps: [
              {
                num: 1,
                action: "Occultamento della Visuale Avversaria",
                spellLink: formatEntityLink("Obscuro", "spell", "obscuro") + " o " + formatEntityLink("Fumos", "spell", "fumos"),
                details: "Incanala <strong>Obscuro (V8)</strong> per bendare istantaneamente gli occhi dell'avversario o <strong>Fumos (V5)</strong> per avvolgerlo in una coltre fumogena: privato del contatto visivo, il rivale non può puntare la bacchetta."
              },
              {
                num: 2,
                action: "Disarmo con Angolo di Puntamento Imprevisto",
                spellLink: formatEntityLink("Expelliarmus", "spell", "expelliarmus"),
                details: "Muoviti lateralmente rispetto al fumo e lancia <strong>Expelliarmus (V2)</strong> guidato dalla voce o dalla sagoma dell'avversario per strappargli la bacchetta."
              },
              {
                num: 3,
                action: "Blocco Cinetico Finale",
                spellLink: formatEntityLink("Petrificus Totalus", "spell", "petrificus-totalus"),
                details: "Senza attendere che il fumo si diradi, completa con la pietrificazione per congelare il corpo della vittima al suolo."
              }
            ],
            rationale: "La rottura del canale ottico impedisce all'avversario di alzare scudi direzionali come Protego, che richiedono l'intercettazione visiva del raggio nemico."
          },
          alternatives: [
            {
              title: "Piano B: Zucca Trasfigurativa Disorientante",
              desc: `Usa ${formatEntityLink("Melofors", "spell", "melofors")} (V4) per incastrare una pesante zucca sulla testa dell'avversario togliendogli la vista, poi disarmalo con calma.`
            },
            {
              title: "Piano C: Fiala Fumogena Alchemica",
              desc: `Frantuma a terra una ${formatEntityLink("Pozione Fumogena", "potion", "pot-fumogena")} per creare una barriera fisica di fumo opaco non dissolvibile da incanti ordinari.`
            }
          ],
          warnings: "Obscuro ed Expelliarmus sono regolari in duello (⚔️ SÌ). Non lanciare sortilegi cinetici pesanti nel fumo se non sei sicuro della posizione degli arbitri di duello."
        };
      }

      // Scenario 3: PROTEGO / SHIELD BREAKER
      if (hasShieldBreak || hasShield) {
        return {
          title: "Strategia di Duello: Superamento e Neutralizzazione di Protego",
          fieldLabel: "⚔️ Duello Magico • Anti-Scudo",
          bestMove: {
            name: "Combo di Destabilizzazione Ambientale e Disarmo",
            steps: [
              {
                num: 1,
                action: "Bypass Geometrico dal Basso",
                spellLink: formatEntityLink("Glisseo", "spell", "glisseo"),
                details: "Il <em>Protego</em> crea uno scudo cinetico frontale ma lascia scoperto il suolo e il piano d'appoggio. Usa <strong>Glisseo (V6)</strong> sul pavimento sotto i piedi dell'avversario per annullare l'attrito e far cadere il bersaglio, interrompendo la concentrazione dello scudo."
              },
              {
                num: 2,
                action: "Molestia Periferica Simultanea",
                spellLink: formatEntityLink("Avis", "spell", "avis") + " & " + formatEntityLink("Oppugno", "spell", "oppugno"),
                details: "Evoca uno stormo di uccelli (V9) e scagliali a tenaglia con Oppugno (V5) dai lati o da dietro: uno scudo frontale non può intercettare 20 vettori d'attacco contemporanei."
              },
              {
                num: 3,
                action: "Chiusura con Disarmo Diretto",
                spellLink: formatEntityLink("Expelliarmus", "spell", "expelliarmus"),
                details: "Nell'istante in cui l'avversario barcolla o si volta per deviare lo stormo, sferra <strong>Expelliarmus (V2)</strong> al torso per disarmarlo definitivamente."
              }
            ],
            rationale: "La sequenza Glisseo (V6 - Elemento Terra/Esagono) ➔ Expelliarmus (V2 - Angolo/Cinetica) sfrutta la caduta della barriera direzionale senza sprecare energia nel tentare di forzare lo scudo a piena potenza."
          },
          alternatives: [
            {
              title: "Piano B: Sfondamento da Sovraccarico Concussivo",
              desc: `Punta con ${formatEntityLink("Bombarda", "spell", "bombarda")} (V3) o ${formatEntityLink("Reducto", "spell", "reducto")} (V9) non allo scudo, ma alle pareti o al soffitto immediatamente sopra o dietro l'avversario: la pioggia di calcinacci pesanti travolgerà il mago escludendo il raggio di protezione.`
            },
            {
              title: "Piano C: Annullamento Aritmantico di Simmetria",
              desc: `Se l'avversario mantiene un Protego a Valenza 2 (Angolo/Dualità), scaglia un incantesimo ad altissima risonanza opposta di Valenza 8 come ${formatEntityLink("Wunjo", "rune", "runa-wunjo")} o ${formatEntityLink("Plasma", "spell", "plasma")} (Elemento Fuoco/Ottagono) per frantumare la matrice geometrica della cupola.`
            }
          ],
          warnings: "Regola di Duello: Expelliarmus, Glisseo, Avis e Oppugno sono pienamente abilitati in duello ufficiale (⚔️ SÌ). Mantieni sempre la linea di visuale libera e fai attenzione a non colpire giudici o spettatori con detriti."
        };
      }

      // Scenario 4: DEFENSIVE COUNTER TO FIRE ATTACK
      if ((hasFire || hasBurn) && (isExplicitDefense || q.includes("mi attacca") || q.includes("contro") || q.includes("estinguere") || q.includes("neutralizzare un attacco di fuoco"))) {
        return {
          title: "Strategia di Duello: Neutralizzazione Fuoco ed Estinzione Magica",
          fieldLabel: "⚔️ Duello Magico • Contro-Elementale Difensiva",
          bestMove: {
            name: "Contro-Azione Idro-Cinetica e Schianto",
            steps: [
              {
                num: 1,
                action: "Estinzione e Schermo di Vapore",
                spellLink: formatEntityLink("Aguamenti", "spell", "aguamenti"),
                details: "Emetti un getto violento d'acqua (V1 - Elemento Acqua/Circonferenza) per intercettare il dardo di fuoco. L'impatto termico genera all'istante una fitta nube di vapore acqueo che occulta la tua sagoma all'avversario."
              },
              {
                num: 2,
                action: "Inversione e Confinamento in Bolla",
                spellLink: formatEntityLink("Ebublio", "spell", "ebublio"),
                details: "Sfrutta l'acqua nebulizzata nell'aria per incanalare <strong>Ebublio (V6)</strong>, intrappolando l'avversario in una gigantesca bolla d'acqua che spegnerà qualsiasi scintilla residua della sua bacchetta."
              },
              {
                num: 3,
                action: "Neutralizzazione con Schianto",
                spellLink: formatEntityLink("Stupeficium", "spell", "stupeficium"),
                details: "Mentre l'avversario è avvolto dalla bolla acquatica, scaglia uno <strong>Stupeficium (V7)</strong>: l'acqua amplificherà la conducibilità dell'energia cinetica garantendo lo svenimento istantaneo."
              }
            ],
            rationale: "La progressione V1 (Acqua pura) ➔ V6 (Terra/Sostegno) ➔ V7 (Ettagono/Opposizione) copre l'intero spettro elementale spegnendo il calore avversario e trasformando la sua stessa arma in una trappola conduttiva."
          },
          alternatives: [
            {
              title: "Piano B: Fenditura d'Aria Deflettente",
              desc: `Usa ${formatEntityLink("Ventus", "spell", "ventus")} con un fendente orizzontale a salire per deflettere le fiamme verso l'alto, seguito da ${formatEntityLink("Flipendo", "spell", "flipendo")} (V1) per colpire l'avversario sbilanciato.`
            },
            {
              title: "Piano C: Schivata con Barriera di Ghiaccio",
              desc: `Congela all'istante l'umidità circostante tramite ${formatEntityLink("Glisseo", "spell", "glisseo")} combinato a una trasfigurazione di pietra inanimata per assorbire l'ondata termica.`
            }
          ],
          warnings: "Attenzione: in caso di Fuoco Maledetto (Ardemonio), Aguamenti è inefficace; in tal caso l'unica soluzione canonica è la smaterializzazione rapida o il controincanto universale Finite Incantatem eseguito all'unisono da più maghi."
        };
      }

      // Scenario 5: FALL / KNOCKDOWN ONLY (ATTACK)
      if (hasFall && (isExplicitAttack || !isExplicitDefense) && !hasBurn && !hasFire) {
        return {
          title: "Strategia di Duello: Atterramento al Suolo e Imprigionamento",
          fieldLabel: "⚔️ Duello Magico • Controllo Cinetico",
          bestMove: {
            name: "Catena di Atterramento e Neutralizzazione a Terra",
            steps: [
              {
                num: 1,
                action: "Sgretolamento della Postura a Terra",
                spellLink: formatEntityLink("Flipendo", "spell", "flipendo") + " o " + formatEntityLink("Glisseo", "spell", "glisseo"),
                details: "Colpisci il torso con una scarica di <strong>Flipendo (V1)</strong> per scagliarlo all'indietro a terra, oppure usa <strong>Glisseo (V6)</strong> sotto i suoi piedi per farlo cadere sul suolo liscio."
              },
              {
                num: 2,
                action: "Congelamento Motorio a Terra",
                spellLink: formatEntityLink("Petrificus Totalus", "spell", "petrificus-totalus"),
                details: "Mentre è schienato al suolo, scaglia <strong>Petrificus Totalus (V2)</strong>: braccia e gambe si saldano bloccando qualsiasi tentativo di rimettersi in piedi."
              },
              {
                num: 3,
                action: "Chiusura con Disarmo",
                spellLink: formatEntityLink("Expelliarmus", "spell", "expelliarmus"),
                details: "Strappa la bacchetta al bersaglio pietrificato con <strong>Expelliarmus (V2)</strong>."
              }
            ],
            rationale: "La Valenza 1 (Flipendo - impulso elementale) seguita da Valenza 2 (Petrificus Totalus) ed Expelliarmus (V2) condivide la risonanza pitagorica riducendo il tempo di latenza tra i colpi."
          },
          alternatives: [
            {
              title: "Piano B: Maledizione Gambemolli",
              desc: `Colpisci con ${formatEntityLink("Locomotor Wibbly", "spell", "locomotor-wibbly")} (V2) per fargli cedere le ginocchia e farlo accasciare a terra.`
            },
            {
              title: "Piano C: Legaccio con Incarceramus",
              desc: `Usa ${formatEntityLink("Incarceramus", "spell", "incarceramus")} (V6) per avvolgere gambe e busto con corde incantate mentre cade.`
            }
          ],
          warnings: "Non colpire con incantesimi lesivi un bersaglio già al suolo e impossibilitato a difendersi."
        };
      }

      // Scenario 6: BURN / FIRE ONLY (ATTACK)
      if ((hasBurn || hasFire) && (isExplicitAttack || !isExplicitDefense)) {
        return {
          title: "Strategia di Duello: Attacco Piro-Cinetico e Bruciature",
          fieldLabel: "⚔️ Duello Magico • Offensiva Termica",
          bestMove: {
            name: "Incursione di Fiamme e Piaghe Ustionanti",
            steps: [
              {
                num: 1,
                action: "Attacco Termico Primario",
                spellLink: formatEntityLink("Exulcero", "spell", "exulcero") + " o " + formatEntityLink("Incendio", "spell", "incendio"),
                details: "Scaglia <strong>Exulcero (V4)</strong> per causare bruciature e piaghe dolorose istantanee che costringono il rivale a rompere la guardia, o lancia una fiammata con <strong>Incendio (V1)</strong> mirando alla veste per distrarlo con il fuoco."
              },
              {
                num: 2,
                action: "Disarmo Rapido su Bersaglio Dolorante",
                spellLink: formatEntityLink("Expelliarmus", "spell", "expelliarmus"),
                details: "Mentre l'avversario ritrae la mano o batte sul mantello per spegnere le fiamme, scaglia <strong>Expelliarmus (V2)</strong> al polso per sottrargli l'arma."
              },
              {
                num: 3,
                action: "Stordimento di Sicurezza",
                spellLink: formatEntityLink("Stupeficium", "spell", "stupeficium"),
                details: "Chiudi con <strong>Stupeficium (V7)</strong> per mandare il rivale al tappeto in stato di incoscienza."
              }
            ],
            rationale: "Il dolore acuto da bruciatura rompe istantaneamente la concentrazione mentale necessaria per deviare gli incanti in arrivo."
          },
          alternatives: [
            {
              title: "Piano B: Fiammata Spinta con Ventus",
              desc: `Scaglia ${formatEntityLink("Incendio", "spell", "incendio")} (V1) abbinato a un fendente d'aria di ${formatEntityLink("Ventus", "spell", "ventus")} per espandere il raggio termico su un fronte largo.`
            },
            {
              title: "Piano C: Pozione Sputafuoco",
              desc: `Trattieni un sorso di ${formatEntityLink("Pozione Sputafuoco", "potion", "pot-sputafuoco")} ed espellilo in avanti creando un muro di fiamme inestinguibili.`
            }
          ],
          warnings: "Le bruciature da Exulcero o Incendio richiedono il trattamento con Essenza di Dittamo o balsamo antiscottature a fine duello."
        };
      }

      // Scenario C: Fast Disarm & Immobilize Combo
      if (q.includes("disarm") || q.includes("immobilizz") || q.includes("rapido") || q.includes("combo") || q.includes("schiant") || q.includes("bloccare")) {
        return {
          title: "Strategia di Duello: Combo Classica Disarmo e Blocco Totale",
          fieldLabel: "⚔️ Duello Magico • Tattica Offensiva",
          bestMove: {
            name: "Trittico di Neutralizzazione Rapida (Disarmo ➔ Blocco ➔ Schianto)",
            steps: [
              {
                num: 1,
                action: "Attacco d'Inizio: Disarmo Immediato",
                spellLink: formatEntityLink("Expelliarmus", "spell", "expelliarmus"),
                details: "Scaglia il raggio scarlatto (V2) mirando direttamente all'avambraccio dell'avversario. Se va a segno, la bacchetta nemica vola via privando il rivale di qualsiasi replica."
              },
              {
                num: 2,
                action: "Impedimento Motorio Istantaneo",
                spellLink: formatEntityLink("Petrificus Totalus", "spell", "petrificus-totalus"),
                details: "Senza soluzione di continuità, lancia <strong>Petrificus Totalus (V2)</strong>: braccia e gambe del bersaglio si saldano all'istante e la vittima cade rigida a terra come un asse di legno."
              },
              {
                num: 3,
                action: "Assicurazione di Neutralizzazione",
                spellLink: formatEntityLink("Incarceramus", "spell", "incarceramus"),
                details: "Evoca spesse funi incantate (V6) per avvolgere il corpo pietrificato, impedendo la liberazione anche in caso di contro-incanto anticipato."
              }
            ],
            rationale: "La sequenza V2 (Expelliarmus) e V2 (Petrificus Totalus) condivide la stessa Valenza Aritmantica 2 (Angolo/Dualità), consentendo al mago di mantenere inalterata la risonanza del catalizzatore senza pause di riallineamento geometrico!"
          },
          alternatives: [
            {
              title: "Piano B: Distrazione Visiva e Calcio Cinetico",
              desc: `Inizia con ${formatEntityLink("Obscuro", "spell", "obscuro")} (V8) o ${formatEntityLink("Fumos", "spell", "fumos")} per bendare/accecare il rivale, seguito subito da ${formatEntityLink("Stupeficium", "spell", "stupeficium")} (V7) al petto.`
            },
            {
              title: "Piano C: Atterramento con Levicorpus",
              desc: `Usa ${formatEntityLink("Levicorpus", "spell", "levicorpus")} (V2) per sollevare l'avversario a mezz'aria per la caviglia lasciandolo indifeso, quindi richiedi la resa o procedi al disarmo a distanza ravvicinata.`
            }
          ],
          warnings: "In duello competitivo scolastico è rigorosamente vietato infierire su un avversario già disarmato o immobilizzato da Petrificus Totalus."
        };
      }

      // Scenario D: Counter-curse / Unbinding
      if (q.includes("contro") || q.includes("liberar") || q.includes("scioglier") || q.includes("annullar") || q.includes("malediz")) {
        return {
          title: "Strategia di Duello: Protocollo di Controincanto e Dissoluzione",
          fieldLabel: "⚔️ Duello Magico • Contromagia Difensiva",
          bestMove: {
            name: "Sequenza di Dissoluzione e Ripristino Cinetico",
            steps: [
              {
                num: 1,
                action: "Dissoluzione Universale degli Effetti",
                spellLink: formatEntityLink("Finite Incantatem", "spell", "finite-incantatem"),
                details: "Esegui un fendente orizzontale netto e deciso pronunciando <em>Finite Incantatem</em> (V6). Scioglie all'istante fatture minori, legami cinetici, alterazioni visive e incanti di disturbo in corso."
              },
              {
                num: 2,
                action: "Rilascio Specifico da Vincoli Corporei",
                spellLink: formatEntityLink("Liberacorpus", "spell", "liberacorpus"),
                details: "Se l'alleato o tu stesso siete vittime di Levicorpus o sospensioni aeree, <strong>Liberacorpus (V2)</strong> interrompe il vettore gravitazionale ripristinando il contatto a terra."
              },
              {
                num: 3,
                action: "Schermo di Barriera Immediato",
                spellLink: formatEntityLink("Protego", "spell", "protego"),
                details: "Non rimanere fermo dopo la dissoluzione: alza immediatamente un <strong>Protego (V2)</strong> per impedire che l'avversario approfitti della finestra di vulnerabilità."
              }
            ],
            rationale: "Finite Incantatem opera sulla Valenza 6 (Esagono di Terra/Stabilità), che ridistribuisce e disperde la coerenza magica delle trame eteree avversarie."
          },
          alternatives: [
            {
              title: "Piano B: Rescissione da Intrappolamento Aritmantico",
              desc: `Per legami runici o trappole avanzate, applica ${formatEntityLink("Rescindo Captio", "spell", "rescindo-captio")} con movimento a spirale inversa per spezzare il vincolo rituale.`
            },
            {
              title: "Piano C: Contro-Illusione Sensoriale",
              desc: `Se la minaccia deriva da miraggi o alterazioni sensoriali (come Illuficium), esegui ${formatEntityLink("Illusìndum", "spell", "illuficium")} con rotazione completa a 360° sopra il capo.`
            }
          ],
          warnings: "Il controincantesimo richiede che l'intensità volitiva di chi lo pronuncia sia pari o superiore a quella dell'incantatore originale."
        };
      }
    }

    // 2. POTIONS SCENARIOS
    if (field === "potions" || (field === "all" && (q.includes("pozion") || q.includes("alchim") || q.includes("veleno") || q.includes("antidoto") || q.includes("infuso") || q.includes("calderon") || ((hasBurn || q.includes("bruciat") || q.includes("ustion")) && !isExplicitAttack)))) {
      if (hasBurn || q.includes("bruciatur") || q.includes("ustion") || q.includes("scottatur")) {
        return {
          title: "Protocollo Alchemico: Trattamento Medimagico delle Ustioni",
          fieldLabel: "🧪 Arte delle Pozioni • Medimagia Riparatrice",
          bestMove: {
            name: "Cicatrizzazione Epidermica e Terapia Termica Rapida",
            steps: [
              {
                num: 1,
                action: "Cicatrizzazione Istantanea delle Piaghe",
                spellLink: formatEntityLink("Essenza di Dittamo", "plant", "p-dittamo"),
                details: "Applicare 3 gocce di <strong>Essenza di Dittamo</strong> direttamente sulla cute lesa: fumo argenteo si leverà dalla ferita e uno strato di pelle nuova e sana si riformerà all'istante sigillando le bruciature."
              },
              {
                num: 2,
                action: "Bendaggio Sterile Lenitivo",
                spellLink: formatEntityLink("Garza di Ortica", "potion", "pot-garza-ortica"),
                details: "Applicare la <strong>Garza di Ortica</strong> a trama rada per proteggere l'epidermide in rigenerazione da infezioni senza alterare l'azione dei principi attivi."
              },
              {
                num: 3,
                action: "Terapia Reintegrativa Fisiologica",
                spellLink: formatEntityLink("Pozione Rigeneratrice", "potion", "pot-rigeneratrice"),
                details: "Somministrare per via orale per reintegrare i liquidi e i sali persi dallo shock termico dell'ustione."
              }
            ],
            rationale: "L'Essenza di Dittamo arresta il processo necrotico delle cellule colpite da calore o maledizioni lesive (come Exulcero), mentre la Garza di Ortica evita il rigetto cutaneo."
          },
          alternatives: [
            {
              title: "Piano B: Pasta Cancellalividi & Scottature",
              desc: "Per scottature superficiali da calderone, applicare la pasta densa a base di calendula e murtlap per lenire il rossore."
            },
            {
              title: "Piano C: Infuso di Mandragola Lenitiva",
              desc: "In caso di ustioni chimiche o caustiche da pus di Bubotubero, risciacquare con infuso di radice di Mandragola per neutralizzare l'acidità magica."
            }
          ],
          warnings: "L'Essenza di Dittamo è altamente infiammabile prima dell'applicazione: tenere lontano da candele o calderoni accesi."
        };
      }

      if (q.includes("veleno") || q.includes("antidoto") || q.includes("tossic") || q.includes("avvelen")) {
        return {
          title: "Protocollo Alchemico d'Emergenza: Neutralizzazione Veleni",
          fieldLabel: "🧪 Arte delle Pozioni • Medimagia Alchemica",
          bestMove: {
            name: "Terapia Sequenziale Anti-Tossica e Rigenerazione",
            steps: [
              {
                num: 1,
                action: "Neutralizzazione Alcaloide Immediata",
                spellLink: formatEntityLink("Antidoto ai Veleni Comuni", "potion", "pot-antidoto-veleni-comuni"),
                details: "Somministrare immediatamente per via orale: contiene bezoar polverizzato, bacche di vischio e corno di unicorno. Neutralizza i veleni comuni di livello I e II (come punture di Doxy, morsi di Fwooper o tossine da ingestione)."
              },
              {
                num: 2,
                action: "Bendaggio Sterile senza Rigetto",
                spellLink: formatEntityLink("Garza di Ortica", "potion", "pot-garza-ortica"),
                details: "Se l'avvelenamento ha provocato piaghe o corrosioni dermiche, applica la <strong>Garza di Ortica</strong> a trama rada: filtra le impurità magiche senza assorbire i principi attivi curativi e previene il rigetto tissutale."
              },
              {
                num: 3,
                action: "Ripristino Forze e Tonicità Cardiorespiratoria",
                spellLink: formatEntityLink("Pozione Rigeneratrice", "potion", "pot-rigeneratrice"),
                details: "Completata la decontaminazione, fare ingerire una dose di Pozione Rigeneratrice per ristabilire i valori vitali e arrestare il deperimento muscolare."
              }
            ],
            rationale: "L'Antidoto ai Veleni Comuni agisce sulle molecole tossiche libere nel circolo sanguigno, mentre la Garza di Ortica protegge la barriera cutanea senza interferire farmacologicamente."
          },
          alternatives: [
            {
              title: "Piano B: Rimedio Istantaneo con Bezoar Puro",
              desc: "In assenza di fiale già pronte, spingere direttamente un bezoar grezzo (calcolo gastrico di capra) giù per la gola del paziente: salverà dalla maggior parte dei veleni comuni vegetali e minerali."
            },
            {
              title: "Piano C: Infuso di Radice di Mandragola",
              desc: `Per veleni che causano torpore muscolare profondo o principio di pietrificazione, somministrare una dose calda di infuso di Mandragola cotta a vapore.`
            }
          ],
          warnings: "Non somministrare mai pozioni rigeneratrici prima che l'antidoto abbia completamente neutralizzato la tossina primaria, per evitare di accelerare l'assorbimento del veleno!"
        };
      }

      if (q.includes("lancio") || q.includes("duello") || q.includes("combatt") || q.includes("esplosiv") || q.includes("fuoco")) {
        return {
          title: "Tattica Alchemica da Duello: Preparazioni da Lancio",
          fieldLabel: "🧪 Arte delle Pozioni • Uso Tattico Offensivo",
          bestMove: {
            name: "Doppietta di Fiale a Impatto Tattico (Cortina & Esplosione)",
            steps: [
              {
                num: 1,
                action: "Accecamento e Fumo Coprente Istantaneo",
                spellLink: formatEntityLink("Pozione Fumogena", "potion", "pot-fumogena"),
                details: "Lancia una fiala a frammentazione ai piedi del rivale: all'impatto libera un fumo nero e acre che inibisce la vista dell'avversario rompendo la linea di puntamento della bacchetta."
              },
              {
                num: 2,
                action: "Innesco a Detonazione Cinetica",
                spellLink: formatEntityLink("Pozione Esplosiva", "potion", "pot-esplosiva"),
                details: "Scaglia subito dopo una boccetta di <strong>Pozione Esplosiva</strong>: sviluppa un'onda d'urto ad alta pressione che abbatte coperture fisiche e fa cadere a terra il bersaglio."
              }
            ],
            rationale: "I composti chimici volatili non sono incantesimi diretti, pertanto oltrepassano le maglie di un Protego ordinario che scherma solo le maledizioni a frequenza eterea."
          },
          alternatives: [
            {
              title: "Piano B: Fiala Soporifera a Diffusione d'Aria",
              desc: `In spazi chiusi, frantuma una dose di Pozione Soporifera abbinata all'incantesimo ${formatEntityLink("Ventus", "spell", "ventus")} per saturare la stanza e addormentare il bersaglio senza violenza.`
            },
            {
              title: "Piano C: Pozione Aguzzaingegno per Riflessi",
              desc: `Bevi una fiala di ${formatEntityLink("Pozione Aguzzaingegno", "potion", "pot-aguzzaingegno")} prima dell'inizio dello scontro: aumenta la velocità di calcolo aritmantico e i riflessi di parata della bacchetta.`
            }
          ],
          warnings: "La Pozione Esplosiva è altamente instabile: maneggiare rigorosamente con guanti in pelle di drago e non conservare vicino a fonti di calore."
        };
      }

      // Default Potion advice
      return {
        title: "Consulenza Alchemica: Preparazione e Utilizzo Pozioni",
        fieldLabel: "🧪 Arte delle Pozioni • Preparazione Rapida",
        bestMove: {
          name: "Protocollo Alchemico d'Elite",
          steps: [
            {
              num: 1,
              action: "Verifica Temperatura e Calderone",
              spellLink: formatEntityLink("Pozione Aguzzaingegno", "potion", "pot-aguzzaingegno"),
              details: "Per massimizzare concentrazione e memoria delle ricette complesse, assumere prima della sessione per velocizzare i tempi di calcolo degli ingredienti."
            },
            {
              num: 2,
              action: "Filtraggio Senza Perdite",
              spellLink: formatEntityLink("Garza di Ortica", "potion", "pot-garza-ortica"),
              details: "Usa la Garza di Ortica sul beccuccio di travaso: elimina le scorie saline trattenendo il 100% dei principi attivi nobili."
            }
          ],
          rationale: "Il successo nell'Arte delle Pozioni dipende dalla precisione assoluta dei tagli e dal controllo rigoroso della fiamma del calderone."
        },
        alternatives: [
          {
            title: "Piano B: Sostituzione d'Emergenza degli Ingredienti",
            desc: "Se manca radice di asfodelo, è possibile bilanciare con succo di fagiolo sopoforo schiacciato con lama d'argento piatto per favorire il rilascio rapido."
          },
          {
            title: "Piano C: Conservazione Protetta",
            desc: "Conservare le fiale in vetri d'ambra sigillati con cera alchemica per impedire l'ossidazione alla luce solare."
          }
        ],
        warnings: "Seguire sempre con rigore il numero e la direzione dei giri di cucchiaio specificati nel ricettario didattico."
      };
    }

    // 3. CREATURES SCENARIOS
    if (field === "creatures" || (field === "all" && (q.includes("creatur") || q.includes("mostr") || q.includes("besti") || q.includes("berretto") || q.includes("molliccio") || q.includes("dissennator") || q.includes("acromantula") || q.includes("ippogrifo")))) {
      if (q.includes("molliccio") || q.includes("boggart") || q.includes("paura")) {
        return {
          title: "Tattica di Difesa: Neutralizzazione del Molliccio (Boggart)",
          fieldLabel: "🐉 Cura delle Creature Magiche • Difesa DCAO",
          bestMove: {
            name: "Protocollo di Umorismo & Risonanza Ridicola",
            steps: [
              {
                num: 1,
                action: "Visualizzazione della Forma Comica",
                spellLink: formatEntityLink("Riddikulus", "spell", "riddikulus"),
                details: "Prima di pronunciare la formula, visualizza mentalmente con precisione chirurgica la forma comica e umiliante in cui costringere la tua peggiore paura (es. vestiti da nonna, zampe coi pattini a rotelle)."
              },
              {
                num: 2,
                action: "Scatto di Risata Catartica",
                spellLink: formatEntityLink("Riddikulus", "spell", "riddikulus"),
                details: "Puntamento deciso della bacchetta gridando <em>Riddikulus!</em> (V3 - Triangolo/Creazione). L'esplosione di risate frantuma la coerenza fisica della creatura costringendola alla fuga."
              }
            ],
            rationale: "Il Molliccio è un non-essere parassita che si nutre del rilascio biochimico del terrore; la risata rompe la sua matrice dimensionale disperdendolo all'istante."
          },
          alternatives: [
            {
              title: "Piano B: Lavoro di Gruppo",
              desc: "Affrontare il Molliccio in compagnia di altri maghi: la creatura entra in confusione nel non sapere quale forma assumere tra le paure simultanee dei presenti."
            },
            {
              title: "Piano C: Confinamento Fisico",
              desc: `Se colti impreparati, chiudere immediatamente l'armadio o il baule e sigillare i cardini con ${formatEntityLink("Colloportus", "spell", "colloportus")}.`
            }
          ],
          warnings: "Non affrontare mai un Molliccio se si è sopraffatti da stanchezza estrema o panico incontrollato."
        };
      }

      if (q.includes("berretto") || q.includes("red cap") || q.includes("palude")) {
        return {
          title: "Tattica di Combattimento: Neutralizzazione Berretto Rosso",
          fieldLabel: "🐉 Creature Magiche • Classe XXX (Mago Capace)",
          bestMove: {
            name: "Arresto Cinetico e Disarmo della Clava",
            steps: [
              {
                num: 1,
                action: "Arresto della Carica Bruta",
                spellLink: formatEntityLink("Impedimenta", "spell", "impedimenta"),
                details: "Lancia <strong>Impedimenta (V1)</strong> sul Berretto Rosso: congela all'istante la sua carica d'assalto e riduce l'impeto della clava ferrata."
              },
              {
                num: 2,
                action: "Puntamento Agli Arti Inferiori",
                spellLink: formatEntityLink("Locomotor Mortis", "spell", "locomotor-mortis"),
                details: "Sferra un <strong>Locomotor Mortis (V2)</strong> mirando alle gambe della creatura per saldarle e farla stramazzare nel fango."
              },
              {
                num: 3,
                action: "Frantumazione dell'Arma",
                spellLink: formatEntityLink("Reducto", "spell", "reducto"),
                details: "Punta la bacchetta alla clava ferrata con <strong>Reducto (V9)</strong>: senza la sua arma, il Berretto Rosso perde ogni coraggio e si ritira nei cunicoli sotterranei."
              }
            ],
            rationale: "I Berretti Rossi si annidano nei campi di battaglia dove è stato versato sangue; la loro ferocia si basa unicamente sulla sorpresa e sull'arma contundente."
          },
          alternatives: [
            {
              title: "Piano B: Cortina di Fumo Evasiva",
              desc: `Usa ${formatEntityLink("Fumos", "spell", "fumos")} per rompere il contatto visivo ed uscire dalla zona acquitrinosa dove la creatura è agile.`
            },
            {
              title: "Piano C: Soluzione Botanica Repellente",
              desc: "Lanciare una manciata di foglie triturate di Pianta della Puzza o zolfo magico: l'olfatto iper-sensibile della bestia la farà scappare."
            }
          ],
          warnings: "Se sei ferito, allontanati subito: l'odore di sangue fresco raddoppia l'aggressività e la forza fisica del Berretto Rosso!"
        };
      }

      if (q.includes("ippogrifo") || q.includes("pacificare") || q.includes("avvicinare")) {
        return {
          title: "Etichetta e Pacificazione: Avvicinamento dell'Ippogrifo",
          fieldLabel: "🐉 Cura delle Creature Magiche • Classe XXX",
          bestMove: {
            name: "Cerimoniale di Rispetto e Inchino Oculare",
            steps: [
              {
                num: 1,
                action: "Contatto Visivo Fisso senza Sbattere Ciglia",
                spellLink: formatEntityLink("Ippogrifo", "creature", "c-ippogrifo"),
                details: "Gli Ippogrifi sono creature fiere e nobili. Fissali direttamente negli occhi senza battere ciglio: mostrare esitazione o battere le palpebre può essere interpretato come debolezza o inganno."
              },
              {
                num: 2,
                action: "Inchino Solenne e Attesa di Risposta",
                spellLink: formatEntityLink("Ippogrifo", "creature", "c-ippogrifo"),
                details: "Chinati lentamente a 45 gradi mantenendo lo sguardo fermo. Non muovere un passo finché l'Ippogrifo non ricambia l'inchino piegando le zampe anteriori."
              },
              {
                num: 3,
                action: "Carezza al Becco e Confidenza",
                spellLink: formatEntityLink("Ippogrifo", "creature", "c-ippogrifo"),
                details: "Solo dopo che ha ricambiato l'inchino, avanza a passi lenti e distendi il palmo della mano per accarezzargli la sommità del becco."
              }
            ],
            rationale: "Il canone di Cura delle Creature Magiche prescrive che l'orgoglio dell'Ippogrifo è sacro: offenderlo o urlare scatena un fendente letale di artigli anteriori."
          },
          alternatives: [
            {
              title: "Piano B: Offerta di Cibo Preliminare",
              desc: "In caso di nervosismo della bestia, lanciare a terra un furetto decongelato o carne cruda per gratificarla prima del contatto."
            },
            {
              title: "Piano C: Ritirata Lenta Indietro",
              desc: "Se l'Ippogrifo grugnisce o arruffa le penne senza inchinarsi, indietreggiare lentamente senza voltarsi mai di spalle."
            }
          ],
          warnings: "Non insultare MAI un Ippogrifo e non avvicinarsi mai di corsa o con movimenti bruschi."
        };
      }

      if (q.includes("dissennator") || q.includes("patronus") || q.includes("dementor")) {
        return {
          title: "Tattica di Difesa: Respingimento del Dissennatore",
          fieldLabel: "🐉 Creature Magiche • Classe XXXXX (Pericolo Estremo)",
          bestMove: {
            name: "Evocazione del Guardiano di Luce Positiva",
            steps: [
              {
                num: 1,
                action: "Concentrazione sul Ricordo Più Potente",
                spellLink: formatEntityLink("Expecto Patronum", "spell", "expecto-patronum"),
                details: "Fissa nella mente il ricordo più felice e puro della tua vita, colmandoti dell'energia vitale di quel momento."
              },
              {
                num: 2,
                action: "Rilascio del Patronus Corporeo",
                spellLink: formatEntityLink("Expecto Patronum", "spell", "expecto-patronum"),
                details: "Traccia la spirale orizzontale proiettando <strong>Expecto Patronum (V4)</strong>: un guardiano argenteo incorporeo caricherà il Dissennatore costringendolo alla ritirata immediata."
              }
            ],
            rationale: "I Dissennatori si nutrono di speranza e felicità umana; il Patronus è pura energia positiva incorporea che non possono consumare né scalfire."
          },
          alternatives: [
            {
              title: "Piano B: Terapia Immediata Post-Attacco",
              desc: "Dopo un incontro ravvicinato, ingerire immediatamente tavolette di puro Cioccolato Magico di Mielandia per ripristinare il calore interno e scacciare la depressione."
            },
            {
              title: "Piano C: Fuga Eterea Veloce",
              desc: `Se incapaci di evocare un Patronus corporeo, usare ${formatEntityLink("Fumos", "spell", "fumos")} e fuggire verso zone soleggiate o calorose.`
            }
          ],
          warnings: "Nessun incantesimo elementale comune (fuoco, acqua, schianto) ha effetto su un Dissennatore: solo il Patronus può respingerlo."
        };
      }

      // Default Creature advice
      return {
        title: "Strategia di Gestione e Contenimento Creature",
        fieldLabel: "🐉 Cura delle Creature Magiche • Protocollo di Sicurezza",
        bestMove: {
          name: "Pacificazione Metodica e Contenimento Silenzioso",
          steps: [
            {
              num: 1,
              action: "Controllo Visivo e Postura Non Minacciosa",
              spellLink: formatEntityLink("Horklump", "creature", "c-horklump"),
              details: "Avvicinarsi con cautela, mantenendo il baricentro basso e la bacchetta puntata verso il basso senza movimenti a scatto."
            },
            {
              num: 2,
              action: "Blocco Motorio Indolore",
              spellLink: formatEntityLink("Immobulus", "spell", "immobulus"),
              details: "Se la creatura diventa ostile, applicare <strong>Immobulus</strong> o <strong>Incarceramus</strong> per immobilizzarla senza causarle danni permanenti."
            }
          ],
          rationale: "Il Ministero della Magia impone il rispetto delle specie tutelate: la neutralizzazione deve sempre privilegiare la pacificazione rispetto alla violenza letale."
        },
        alternatives: [
          {
            title: "Piano B: Esca Cibo / Distrazione Specifica",
            desc: "Usare carne cruda per creature carnivore (come Thestral) o vermi di legno per Asticelli per distrarre la bestia in sicurezza."
          },
          {
            title: "Piano C: Barriera di Confinamento",
            desc: `Tracciare un cerchio di confinamento con ${formatEntityLink("Cave Inimicum", "spell", "cave-inimicum")} o ${formatEntityLink("Protego Totalum", "spell", "protego-totalum")}.`
          }
        ],
        warnings: "Verificare sempre la Classificazione Ministeriale della creatura prima di intervenire (da X innocuo a XXXXX ammazzamaghi)."
      };
    }

    // 4. HERBOLOGY SCENARIOS
    if (field === "herbology" || (field === "all" && (q.includes("piant") || q.includes("erbolog") || q.includes("tranello") || q.includes("mandragola") || q.includes("dittamo") || q.includes("tentacula") || q.includes("radic")))) {
      if (q.includes("tranello") || q.includes("diavolo") || q.includes("devil")) {
        return {
          title: "Protocollo Botanico di Sopravvivenza: Tranello del Diavolo",
          fieldLabel: "🌿 Erbologia Botanica • Coltura Pericolosa",
          bestMove: {
            name: "Rilassamento e Invocazione Solare Termica",
            steps: [
              {
                num: 1,
                action: "Arresto Immediato di Ogni Resistenza Fisica",
                spellLink: formatEntityLink("Tranello del Diavolo", "plant", "p-mandragola"),
                details: "Smetti di dimenarti: la pianta reagisce alla tensione muscolare stritolando con forza proporzionale alla resistenza. Rilassare completamente il corpo rallenta la costrizione."
              },
              {
                num: 2,
                action: "Luce e Calore Concentrato",
                spellLink: formatEntityLink("Lumos Solem", "spell", "lumos-solem") + " o " + formatEntityLink("Incendio", "spell", "incendio"),
                details: "Emetti un raggio abbagliante di pura luce solare con <strong>Lumos Solem (V2)</strong> o fiamme con <strong>Incendio (V1)</strong> direttamente sui nodi radicali: la pianta ritirerà i viticci all'istante!"
              }
            ],
            rationale: "Il Tranello del Diavolo prospera nell'ombra buia e umida; la sua fisiologia vegetale è intollerante ai raggi solari concentrati e al calore del fuoco."
          },
          alternatives: [
            {
              title: "Piano B: Recisione Mirata",
              desc: `Se assistito da un compagno, scagliare ${formatEntityLink("Diffindo", "spell", "diffindo")} (V1) alla base dei fusti guida per allentare la morsa.`
            },
            {
              title: "Piano C: Fiala Termica da Tasca",
              desc: "Frantumare una capsula di Fuoco dell'Alchimista sul terreno per creare una barriera termica invalicabile per i viticci."
            }
          ],
          warnings: "Chi lotta contro il Tranello del Diavolo viene strangolato in meno di 60 secondi: la disciplina mentale è indispensabile per la sopravvivenza."
        };
      }

      if (q.includes("mandragola") || q.includes("pietrific") || q.includes("grido")) {
        return {
          title: "Protocollo di Sicurezza: Manipolazione della Mandragola",
          fieldLabel: "🌿 Erbologia Botanica • Pianta Antropomorfa",
          bestMove: {
            name: "Travaso e Protezione Acustica Assoluta",
            steps: [
              {
                num: 1,
                action: "Isolamento Acustico Sigillato",
                spellLink: formatEntityLink("Mandragola", "plant", "p-mandragola"),
                details: "Indossa paraorecchie imbottiti di pelo di Fwooper verificando che aderiscano ermeticamente prima di toccare il vaso."
              },
              {
                num: 2,
                action: "Estrazione e Travaso Rapido",
                spellLink: formatEntityLink("Mandragola", "plant", "p-mandragola"),
                details: "Afferrare con decisione il ciuffo di foglie ed estrarre la radice umanoide, inserendola immediatamente nel nuovo terriccio concimato con sterco di drago."
              }
            ],
            rationale: "Il pianto della Mandragola giovane fa svenire per ore; il grido dell'esemplare adulto è letale e fulminante per chiunque lo ascolti senza protezione."
          },
          alternatives: [
            {
              title: "Piano B: Cura da Pietrificazione",
              desc: "Quando mature, le radici cotte e distillate formano il Decotto di Mandragola, l'unico rimedio in grado di risvegliare chi è stato pietrificato da sguardi malefici o incantesimi oscuri."
            },
            {
              title: "Piano C: Incantesimo Silenziatore",
              desc: `Applicare ${formatEntityLink("Silencio", "spell", "silencio")} attorno all'area di coltivazione per ridurre la propagazione dell'onda sonora.`
            }
          ],
          warnings: "Non sfilare mai i paraorecchie finché la radice non è completamente interrata e ricoperta dal terriccio magico."
        };
      }

      if (q.includes("tentacula") || q.includes("mordace") || q.includes("carnivor")) {
        return {
          title: "Protocollo di Difesa: Neutralizzazione Tentacula Velenosa",
          fieldLabel: "🌿 Erbologia Botanica • Pianta Carnivora Classe C",
          bestMove: {
            name: "Recisione Mirata dei Tentacoli e Stordimento",
            steps: [
              {
                num: 1,
                action: "Interruzione dell'Attacco Flessibile",
                spellLink: formatEntityLink("Diffindo", "spell", "diffindo"),
                details: "Scagliare <strong>Diffindo (V1)</strong> con fendente diagonale sui viticci dentati che cercano di mordere per reciderli alla base."
              },
              {
                num: 2,
                action: "Repulsione Vegetale di Zona",
                spellLink: formatEntityLink("Tentacula Velenosa", "plant", "p-tentacula-velenosa"),
                details: "Applicare <strong>Protego Herbivorum</strong> per respingere le spine acuminate e i succhi caustici secreti dalla bocca della pianta."
              }
            ],
            rationale: "La Tentacula Velenosa morde e inietta una tossina paralizzante; recidere i tentacoli toglie ogni potere offensivo al fusto centrale."
          },
          alternatives: [
            {
              title: "Piano B: Allontanamento con Calore",
              desc: `Usare ${formatEntityLink("Incendio", "spell", "incendio")} per costringere la pianta a ritrarsi, stando attenti a non bruciare le foglie che contengono linfa preziosa.`
            },
            {
              title: "Piano C: Succo Diserbante",
              desc: "Spruzzare linfa diserbante per inibire i recettori sensoriali dei fiori carnivori."
            }
          ],
          warnings: "Il morso della Tentacula provoca spasmi muscolari e gonfiore grave: tenere a portata di mano essenza di Dittamo."
        };
      }

      // Default Herbology
      return {
        title: "Tattica di Gestione Botanica & Raccolta",
        fieldLabel: "🌿 Erbologia Botanica • Colture Speciali",
        bestMove: {
          name: "Estrazione Protetta e Raccolta Principi Attivi",
          steps: [
            {
              num: 1,
              action: "Protezione con Guanti di Drago",
              spellLink: formatEntityLink("Dittamo", "plant", "p-dittamo"),
              details: "Indossare sempre guanti in pelle di drago spessi per evitare dermatiti causate da spine velenose o peli urticanti."
            },
            {
              num: 2,
              action: "Taglio Netto alla Base",
              spellLink: formatEntityLink("Diffindo", "spell", "diffindo"),
              details: "Eseguire un taglio chirurgico con lama sterilizzata o con <strong>Diffindo (V1)</strong> per non danneggiare la radice madre e permettere la ricrescita."
            }
          ],
          rationale: "Le piante magiche trattengono la carica eterea nei tessuti linfatici; un taglio rozzo disperde la potenza attiva dell'estratto alchemico."
        },
        alternatives: [
          {
            title: "Piano B: Idro-Nutrizione Accelerata",
            desc: `Applicare ${formatEntityLink("Aguamenti", "spell", "aguamenti")} combinato a concime di Mooncalf per accelerare la fioritura di 3 settimane.`
          },
          {
            title: "Piano C: Conservazione in Garza",
            desc: "Avvolgere i germogli in garze sterili umide per conservare la freschezza per oltre 48 ore senza deperimento."
          }
        ],
        warnings: "Alcune specie esotiche rilasciano spore soporifere durante il taglio: lavorare sempre in serre ben aerate."
      };
    }

    // 5. RUNES & ARITHMANCY SCENARIOS
    if (field === "runes" || (field === "all" && (q.includes("runa") || q.includes("valenza") || q.includes("aritm") || q.includes("futhark") || q.includes("sigillo") || q.includes("aett")))) {
      // Numerical valence query: e.g. "valenza 4" or "spezzare un sigillo"
      const valenceMatch = q.match(/valenza\s*([1-9])/);
      const targetVal = valenceMatch ? parseInt(valenceMatch[1]) : 4;
      const oppVal = 10 - targetVal; // Canon Pythagorean symmetry (or 10 - V)

      return {
        title: `Strategia Aritmantica: Risoluzione e Annullamento Valenza ${targetVal}`,
        fieldLabel: "ᛟ Antiche Rune & Aritmanzia • Calcolo di Simmetria",
        bestMove: {
          name: `Spezzamento di Matrice tramite Valenza Opposta (V${targetVal} ➔ V${oppVal})`,
          steps: [
            {
              num: 1,
              action: `Identificazione della Geometria Attiva (Valenza ${targetVal})`,
              spellLink: formatEntityLink("Signo", "spell", "signo"),
              details: `Un incantesimo o sigillo di <strong>Valenza ${targetVal}</strong> vibra secondo una figura geometrica chiusa (es. Quadrato/Stabilità se V4, Triangolo se V3).`
            },
            {
              num: 2,
              action: `Invocazione della Valenza Opposta di Simmetria: V${oppVal}`,
              spellLink: formatEntityLink("Finite Incantatem", "spell", "finite-incantatem"),
              details: `Per dissolvere la tensione senza contraccolpo, incanala un incantesimo a <strong>Valenza ${oppVal}</strong> (es. Finite Incantatem se V6, oppure Wunjo se V8). La somma ${targetVal} + ${oppVal} = 10 riduce la polarità all'unità monadica 1, collassando il sigillo.`
            },
            {
              num: 3,
              action: "Tracciamento dell'Annullatore nell'Etere",
              spellLink: formatEntityLink("Persìgno", "spell", "persigno"),
              details: "Usa <strong>Persìgno</strong> muovendo la punta della bacchetta per disegnare il glifo runico corrispondente alla valenza calcolata direttamente sul perimetro del sigillo avversario."
            }
          ],
          rationale: `Nel Liber Septimus del Codex Arithmantiae, due forze a valenza complementare (${targetVal} e ${oppVal}) si annullano perfettamente creando una transizione a somma 10 (riduzione pitagorica 1, Monade di quiete).`
        },
        alternatives: [
          {
            title: "Piano B: Sostituzione con Triade di Thoot",
            desc: "Se il sigillo è permanente, applicare un legame a 3 rune dello stesso Aett con l'incantesimo Iùngo per riorientare il flusso magico verso terra."
          },
          {
            title: "Piano C: Sovraccarico Elementale",
            desc: `Applicare la runa dell'Elemento Fuoco (Kenaz) per bruciare il supporto materiale su cui è inciso il glifo runico.`
          }
        ],
        warnings: "Un calcolo errato della valenza opposta non dissolve il sigillo, ma provoca un contraccolpo aritmantico (Backlash) sulla bacchetta dell'incantatore."
      };
    }

    // 6. GENERAL / SEMANTIC FALLBACK SEARCH ACROSS ENTIRE COMPENDIUM
    const stopWords = new Set([
      "voglio", "vorrei", "posso", "devo", "come", "cosa", "quale", "quali",
      "il", "lo", "la", "i", "gli", "le", "un", "uno", "una",
      "di", "a", "da", "in", "con", "su", "per", "tra", "fra",
      "e", "ed", "o", "od", "ma", "che", "cui", "chi",
      "mio", "mia", "miei", "mie", "tuo", "tua", "suo", "sua",
      "avversario", "avversari", "nemico", "nemici", "bersaglio",
      "fare", "far", "modo", "meglio", "migliore"
    ]);

    const cleanTokens = q.replace(/[^\w\sàèéìòù]/gi, ' ').split(/\s+/).filter(w => w.length >= 3 && !stopWords.has(w));

    function scoreItem(item, isSpell) {
      let score = 0;
      const text = `${item.nome} ${item.formula || ''} ${item.descrizione} ${item.duelloNote || ''} ${item.tipologia || ''} ${item.utilizziMagici || ''}`.toLowerCase();
      cleanTokens.forEach(tok => {
        if (item.nome.toLowerCase().includes(tok)) score += 12;
        if (item.formula && item.formula.toLowerCase().includes(tok)) score += 14;
        if (item.duelloNote && item.duelloNote.toLowerCase().includes(tok)) score += 8;
        if (item.descrizione.toLowerCase().includes(tok)) score += 4;
        if (item.tipologia && item.tipologia.toLowerCase().includes(tok)) score += 6;
      });
      if (isSpell) {
        if ((isExplicitAttack || field === "duel") && item.inDuello) score += 15;
        if ((isExplicitAttack || field === "duel") && !item.inDuello) score -= 20;
      }
      return score;
    }

    const matchingSpells = spells
      .map(s => ({ item: s, score: scoreItem(s, true) }))
      .filter(x => x.score > 0)
      .sort((a, b) => b.score - a.score)
      .map(x => x.item);

    const matchingCreatures = materie.creature
      .map(c => ({ item: c, score: scoreItem(c, false) }))
      .filter(x => x.score > 0)
      .sort((a, b) => b.score - a.score)
      .map(x => x.item);

    const matchingPotions = materie.pozioni
      .map(p => ({ item: p, score: scoreItem(p, false) }))
      .filter(x => x.score > 0)
      .sort((a, b) => b.score - a.score)
      .map(x => x.item);

    // Build synthesized custom advice
    const spellA = matchingSpells[0] || spells.find(s => s.id === "expelliarmus") || spells[0];
    const spellB = matchingSpells[1] || (spellA.id === "expelliarmus" ? spells.find(s => s.id === "stupeficium") : spells.find(s => s.id === "expelliarmus")) || spells[1];
    const potionAlt = matchingPotions[0];
    const creatureAlt = matchingCreatures[0];

    return {
      title: `Consiglio Tattico: Risoluzione Operativa per "${query.slice(0, 40)}..."`,
      fieldLabel: `${CHAT_FIELDS[field] ? CHAT_FIELDS[field].icon + ' ' + CHAT_FIELDS[field].name : '✨ Strategia Globale'}`,
      bestMove: {
        name: `Combo Consigliata con ${spellA.nome}`,
        steps: [
          {
            num: 1,
            action: `Inizio Tattico: ${spellA.nome} (Formula: ${spellA.formula})`,
            spellLink: formatEntityLink(spellA.nome, spellA.isRune ? "rune" : "spell", spellA.id),
            details: `Inizia l'azione incanalando <strong>${spellA.formula}</strong> (Valenza ${spellA.valenza}): ${spellA.duelloNote || spellA.descrizione.slice(0, 150) + '...'}`
          },
          {
            num: 2,
            action: `Chiusura o Sinergia con ${spellB.nome}`,
            spellLink: formatEntityLink(spellB.nome, spellB.isRune ? "rune" : "spell", spellB.id),
            details: `Coordina immediatamente il secondo colpo con <strong>${spellB.formula}</strong> (Valenza ${spellB.valenza}): sfrutta la finestra aperta dal primo incantesimo per completare l'obiettivo.`
          }
        ],
        rationale: `L'abbinamento tra ${spellA.nome} (V${spellA.valenza}) e ${spellB.nome} (V${spellB.valenza}) garantisce un flusso continuo di energia senza dispersioni, coprendo sia la fase di apertura che quella di neutralizzazione.`
      },
      alternatives: [
        {
          title: potionAlt ? `Piano B (Soluzione Alchemica: ${potionAlt.nome})` : "Piano B: Approccio Elusivo di Posizionamento",
          desc: potionAlt 
            ? `Integra la pozione ${formatEntityLink(potionAlt.nome, 'potion', potionAlt.id)} (${potionAlt.tempoPreparazione}): ${potionAlt.descrizione.slice(0, 140)}...`
            : `Usa un incantesimo di movimento come ${formatEntityLink('Carpe Retractum', 'spell', 'carpe-retractum')} o ${formatEntityLink('Ascendio', 'spell', 'ascendio')} per cambiare asse di combattimento prima del secondo lancio.`
        },
        {
          title: creatureAlt ? `Piano C (Interazione Creatura: ${creatureAlt.nome})` : "Piano C: Difesa Statica e Contro-Azione",
          desc: creatureAlt
            ? `Se la situazione coinvolge ${formatEntityLink(creatureAlt.nome, 'creature', creatureAlt.id)} (Classe ${creatureAlt.classificazione}): ${creatureAlt.descrizione.slice(0, 140)}...`
            : `Alza una barriera temporanea con ${formatEntityLink('Protego', 'spell', 'protego')} o usa ${formatEntityLink('Finite Incantatem', 'spell', 'finite-incantatem')} per azzerare gli incanti nemici prima di contrattaccare.`
        }
      ],
      warnings: `Verifica sempre che gli incantesimi scelti siano autorizzati per il contesto specifico (Duello: ${spellA.inDuello ? '⚔️ Abilitato' : '⛔ Non da duello'}).`
    };
    }

    const rawAdvice = evaluateRawAdvice(field, query, q, reqOfficial, reqDuelType, reqHybridRole);
    return formatAdviceForModeAndSteps(rawAdvice, reqMode, reqSteps, field, query);
  }

  // --- GEMINI API FALLBACK CLIENT (OPTIONAL POWER-USER INTEGRATION) ---
  async function callGeminiApi(apiKey, field, query, options = {}) {
    const fieldName = CHAT_FIELDS[field] ? CHAT_FIELDS[field].name : "Mondo Magico";
    const mode = (options && options.mode) || activeMode || "combo";
    const steps = Number((options && options.steps) || activeSteps || 3);
    const modeInstruction = mode === "single"
      ? "L'utente richiede una MOSSA SINGOLA (1 solo incantesimo o azione decisiva immediata, senza passaggi multipli)."
      : `L'utente richiede una COMBO TATTICA a esattamente ${steps} passaggi sequenziali numerati.`;

    const systemPrompt = `Sei il Grimorio Tattico di Hogwarts, un esperto maestro di duelli magici, alchimia delle pozioni, creature ed erbologia dell'Arcane GDR.
L'utente ti chiede una mossa o combo tattica nel campo "${fieldName}".
${modeInstruction}
Fornisci SEMPRE:
1. "${mode === 'single' ? 'Mossa Risolutiva Singola Consigliata' : 'Combo Ottimale Consigliata (' + steps + ' Passaggi)'}": con formule esatte (es. Expelliarmus, Aguamenti, Glisseo), Valenza Magica (1-9), e spiegazione chiara del perché funziona.
2. "Razionale Tattico & Valenza": spiegazione della logica magica o aritmantica della sequenza.
3. "Alternative Tattiche": Piano B (alternativa elusiva o sfondamento) e Piano C (soluzione con pozione, pianta o runa).
4. "Avvertenze & Regole di Duello": se gli incantesimi sono da duello (Sì/No) e controindicazioni.
Rispondi in italiano con tono epico, professionale e didattico. Usa elenchi puntati chiari.`;

    const url = `https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key=${encodeURIComponent(apiKey)}`;
    const payload = {
      contents: [
        {
          role: "user",
          parts: [
            { text: `${systemPrompt}\n\nDomanda dell'utente: "${query}"` }
          ]
        }
      ],
      generationConfig: {
        temperature: 0.3,
        maxOutputTokens: 1000
      }
    };

    const res = await fetch(url, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(payload)
    });

    if (!res.ok) {
      throw new Error(`Gemini API error: ${res.status}`);
    }

    const data = await res.json();
    const candidate = data?.candidates?.[0]?.content?.parts?.[0]?.text;
    if (!candidate) throw new Error("Risposta vuota dall'API Gemini");
    return candidate;
  }

  // --- RENDER ASSISTANT MESSAGE HTML ---
  function renderAssistantResponseHtml(advice) {
    if (typeof advice === "string") {
      // Direct text / Gemini response: parse basic markdown
      let formatted = advice
        .replace(/\*\*(.*?)\*\*/g, '<strong class="text-amber-300 font-semibold">$1</strong>')
        .replace(/\*(.*?)\*/g, '<em class="text-slate-300">$1</em>')
        .replace(/\n\n/g, '</p><p class="mt-2 text-slate-300">')
        .replace(/\n- /g, '<br>• ');

      return `
        <div class="chat-message assistant-msg p-4 rounded-2xl bg-slate-900/90 border border-amber-500/35 text-xs text-slate-200 shadow-xl space-y-2 chat-bubble-enter">
          <div class="flex items-center justify-between border-b border-slate-800/80 pb-2">
            <span class="text-amber-300 font-bold font-magic flex items-center gap-1.5">
              <span>🪄</span> Grimorio Tattico (Gemini AI)
            </span>
            <span class="text-[10px] px-2 py-0.5 rounded-full bg-indigo-500/15 text-indigo-300 border border-indigo-500/30">Risposta Dinamica</span>
          </div>
          <div class="text-xs text-slate-200 leading-relaxed space-y-2">
            <p>${formatted}</p>
          </div>
        </div>
      `;
    }

    // Structured Advice from Tactical Engine
    const isSingle = advice.mode === "single";
    const stepsCount = advice.stepsCount || (advice.bestMove && advice.bestMove.steps ? advice.bestMove.steps.length : 1);

    const modeBadge = isSingle
      ? `<span class="text-[10px] px-2 py-0.5 rounded-full bg-amber-500/20 text-amber-300 border border-amber-500/40 whitespace-nowrap font-bold flex items-center gap-1 shadow-sm"><span>⚡</span> Mossa Singola</span>`
      : `<span class="text-[10px] px-2 py-0.5 rounded-full bg-amber-500/20 text-amber-300 border border-amber-500/40 whitespace-nowrap font-bold flex items-center gap-1 shadow-sm"><span>🔗</span> Combo (${stepsCount} Passaggi)</span>`;

    const sectionTitle = isSingle
      ? `<span>⚡</span> Mossa Risolutiva Singola Consigliata:`
      : `<span>🎯</span> Combo Ottimale Consigliata (${stepsCount} Passaggi):`;

    const stepsHtml = advice.bestMove.steps.map(s => `
      <div class="flex items-start gap-2.5 p-2.5 rounded-xl bg-slate-900/80 border border-slate-800/80">
        <span class="w-5 h-5 rounded-full ${isSingle ? 'bg-amber-500/20 text-amber-300 border-amber-500/40' : 'bg-emerald-500/20 text-emerald-300 border-emerald-500/40'} border flex items-center justify-center font-bold text-[10px] shrink-0 mt-0.5">
          ${s.num}
        </span>
        <div class="space-y-1 w-full">
          <div class="flex items-center gap-2 flex-wrap">
            <span class="font-bold text-white text-[12px]">${s.action}:</span>
            ${s.spellLink}
          </div>
          <p class="text-slate-300 text-[11px] leading-relaxed">${s.details}</p>
        </div>
      </div>
    `).join("");

    const altHtml = advice.alternatives.map(alt => `
      <div class="p-2.5 rounded-xl bg-slate-950/70 border border-slate-800/80 space-y-1">
        <div class="font-bold text-sky-300 flex items-center gap-1.5 text-[11px]">
          <span>◈</span> ${alt.title}
        </div>
        <p class="text-slate-400 text-[11px] leading-relaxed">${alt.desc}</p>
      </div>
    `).join("");

    return `
      <div class="chat-message assistant-msg p-4 sm:p-5 rounded-2xl bg-slate-900/95 border border-amber-500/35 text-xs text-slate-200 shadow-2xl space-y-3.5 chat-bubble-enter">
        <!-- Header -->
        <div class="flex items-center justify-between border-b border-slate-800 pb-2.5 flex-wrap gap-2">
          <div class="flex items-center gap-2">
            <span class="text-base">🪄</span>
            <span class="font-magic font-bold text-white text-sm sm:text-base tracking-wide">${advice.title}</span>
          </div>
          <div class="flex items-center gap-1.5 flex-wrap">
            ${modeBadge}
            <span class="text-[10px] px-2 py-0.5 rounded-full bg-slate-800 text-slate-300 border border-slate-700 whitespace-nowrap font-medium">
              ${advice.fieldLabel}
            </span>
          </div>
        </div>

        <!-- Mossa o Combo Ottimale -->
        <div class="space-y-2">
          <div class="text-[11px] uppercase tracking-wider font-bold ${isSingle ? 'text-amber-400' : 'text-emerald-400'} flex items-center gap-1.5">
            ${sectionTitle}
          </div>
          <div class="p-3 rounded-xl bg-slate-950/90 border ${isSingle ? 'border-amber-500/40' : 'border-emerald-500/30'} space-y-2">
            <div class="font-magic font-bold ${isSingle ? 'text-amber-300' : 'text-emerald-300'} text-xs">${advice.bestMove.name}</div>
            <div class="space-y-2 pt-1">
              ${stepsHtml}
            </div>
          </div>
        </div>

        <!-- Razionale Tattico -->
        <div class="p-3 rounded-xl bg-slate-950/60 border border-amber-500/20 space-y-1">
          <div class="font-semibold text-amber-300 flex items-center gap-1.5 text-[11px]">
            <span>💡</span> Razionale Tattico & Aritmantico:
          </div>
          <p class="text-slate-300 text-[11px] leading-relaxed">${advice.bestMove.rationale}</p>
        </div>

        <!-- Alternative Tattiche -->
        <div class="space-y-2">
          <div class="text-[11px] uppercase tracking-wider font-bold text-sky-400 flex items-center gap-1.5">
            <span>🔄</span> Alternative Tattiche (Piano B & C):
          </div>
          <div class="grid grid-cols-1 sm:grid-cols-2 gap-2">
            ${altHtml}
          </div>
        </div>

        <!-- Avvertenze & Canone -->
        <div class="text-[10px] text-slate-400 border-t border-slate-800/80 pt-2 flex items-start gap-1.5">
          <span class="text-amber-400 font-bold shrink-0">⚠️ Avvertenze:</span>
          <span>${advice.warnings}</span>
        </div>
      </div>
    `;
  }

  // --- UI CONTROLLER ---
  function initTacticalChat() {
    const drawer = document.getElementById("tacticalChatDrawer");
    const card = document.getElementById("tacticalChatCard");
    const openBtn = document.getElementById("openTacticalChatBtn");
    const fabBtn = document.getElementById("fabTacticalChatBtn");
    const closeBtn = document.getElementById("closeTacticalChatBtn");
    const backdrop = document.getElementById("tacticalChatBackdrop");
    const chatForm = document.getElementById("chatForm");
    const chatInput = document.getElementById("chatInput");
    const sendBtn = document.getElementById("chatSendBtn");
    const messagesContainer = document.getElementById("chatMessagesContainer");
    const clearBtn = document.getElementById("clearChatBtn");
    const chipsContainer = document.getElementById("chatSuggestionChips");
    const chipsScrollLeftBtn = document.getElementById("chipsScrollLeftBtn");
    const chipsScrollRightBtn = document.getElementById("chipsScrollRightBtn");
    const fieldSelector = document.getElementById("chatFieldSelector");
    const fieldPills = document.querySelectorAll(".chat-field-pill");
    const activeFieldLabel = document.getElementById("activeChatFieldLabel");
    const toggleApiKeyBtn = document.getElementById("toggleChatApiKey");
    const apiKeyRow = document.getElementById("apiKeyConfigRow");
    const apiKeyInput = document.getElementById("geminiApiKeyInput");
    const saveApiKeyBtn = document.getElementById("saveApiKeyBtn");
    const sampleBtn = document.getElementById("chatVoiceOrSampleBtn");
    const modeBtns = document.querySelectorAll(".chat-mode-btn");
    const comboStepsContainer = document.getElementById("comboStepsContainer");
    const stepBtns = document.querySelectorAll(".chat-step-btn");
    const duelConfigBar = document.getElementById("duelConfigBar");
    const duelOfficialBtns = document.querySelectorAll(".duel-official-btn");
    const duelTypeBtns = document.querySelectorAll(".duel-type-btn");
    const duelHybridRoleContainer = document.getElementById("duelHybridRoleContainer");
    const duelRoleBtns = document.querySelectorAll(".duel-role-btn");

    if (!drawer || !chatForm) return;

    // Load saved API key
    if (apiKeyInput) {
      apiKeyInput.value = localStorage.getItem("hogwarts_gemini_api_key") || "";
    }

    // Toggle API key row
    toggleApiKeyBtn?.addEventListener("click", () => {
      apiKeyRow?.classList.toggle("hidden");
    });

    saveApiKeyBtn?.addEventListener("click", () => {
      const val = apiKeyInput ? apiKeyInput.value.trim() : "";
      if (val) {
        localStorage.setItem("hogwarts_gemini_api_key", val);
        alert("Chiave API salvata! Il Grimorio utilizzerà Gemini per le risposte espanse.");
      } else {
        localStorage.removeItem("hogwarts_gemini_api_key");
        alert("Chiave rimossa. Il Grimorio torna al motore offline integrato (100% autonomo).");
      }
      apiKeyRow?.classList.add("hidden");
    });

    // Duel Configuration Helpers
    function updateDuelConfigUI() {
      if (!duelConfigBar) return;
      if (activeField === "duel") {
        duelConfigBar.classList.remove("hidden");
      } else {
        duelConfigBar.classList.add("hidden");
      }

      duelOfficialBtns.forEach(btn => {
        const isOfficial = btn.dataset.official === "true";
        const isActive = isOfficial === duelOfficial;
        btn.classList.toggle("active", isActive);
        btn.classList.toggle("bg-amber-500", isActive);
        btn.classList.toggle("text-slate-950", isActive);
        btn.classList.toggle("font-bold", isActive);
        btn.classList.toggle("text-slate-400", !isActive);
      });

      duelTypeBtns.forEach(btn => {
        const isCurrent = btn.dataset.type === duelType;
        btn.classList.toggle("active", isCurrent);
        btn.classList.toggle("bg-amber-500", isCurrent);
        btn.classList.toggle("text-slate-950", isCurrent);
        btn.classList.toggle("font-bold", isCurrent);
        btn.classList.toggle("text-slate-400", !isCurrent);
      });

      if (duelHybridRoleContainer) {
        if (activeField === "duel" && duelType === "hybrid") {
          duelHybridRoleContainer.classList.remove("hidden");
        } else {
          duelHybridRoleContainer.classList.add("hidden");
        }
      }

      duelRoleBtns.forEach(btn => {
        const isCurrent = btn.dataset.role === duelHybridRole;
        btn.classList.toggle("active", isCurrent);
        btn.classList.toggle("bg-amber-500", isCurrent);
        btn.classList.toggle("text-slate-950", isCurrent);
        btn.classList.toggle("font-bold", isCurrent);
        btn.classList.toggle("text-slate-400", !isCurrent);
      });

      updateInputPlaceholder();
      renderSuggestionChips();
    }

    duelOfficialBtns.forEach(btn => {
      btn.addEventListener("click", () => {
        duelOfficial = btn.dataset.official === "true";
        updateDuelConfigUI();
      });
    });

    duelTypeBtns.forEach(btn => {
      btn.addEventListener("click", () => {
        const t = btn.dataset.type;
        if (t && ["magical", "physical", "hybrid"].includes(t)) {
          duelType = t;
          updateDuelConfigUI();
        }
      });
    });

    duelRoleBtns.forEach(btn => {
      btn.addEventListener("click", () => {
        const r = btn.dataset.role;
        if (r && ["user_magic", "enemy_magic"].includes(r)) {
          duelHybridRole = r;
          updateDuelConfigUI();
        }
      });
    });

    // Resolution Mode and Steps Helpers
    function updateInputPlaceholder() {
      if (!chatInput) return;
      const fieldData = CHAT_FIELDS[activeField] || CHAT_FIELDS.duel;
      if (activeField === "duel") {
        if (duelType === "magical") {
          chatInput.placeholder = activeMode === "single"
            ? `Descrivi l'azione di duello magico ${duelOfficial ? '(ufficiale)' : '(libero)'}... (1 mossa)`
            : `Descrivi la situazione di duello magico ${duelOfficial ? '(ufficiale)' : '(libero)'}... (combo a ${activeSteps} passi)`;
        } else if (duelType === "physical") {
          chatInput.placeholder = activeMode === "single"
            ? `Descrivi lo scontro corpo a corpo / lotta fisica... (1 mossa)`
            : `Descrivi la situazione di lotta corpo a corpo... (combo a ${activeSteps} passi)`;
        } else if (duelType === "hybrid") {
          if (duelHybridRole === "user_magic") {
            chatInput.placeholder = `Tu usi la magia vs avversario fisico (descrivi la carica nemica)...`;
          } else {
            chatInput.placeholder = `Tu combatti fisicamente vs mago con bacchetta (descrivi l'azione di blitz)...`;
          }
        }
      } else {
        if (activeMode === "single") {
          chatInput.placeholder = `Descrivi l'azione (fornirò la singola mossa migliore per ${fieldData.name})...`;
        } else {
          chatInput.placeholder = `Descrivi la situazione (fornirò una combo a ${activeSteps} passaggi per ${fieldData.name})...`;
        }
      }
    }

    function updateModeUI() {
      modeBtns.forEach(btn => {
        const isCurrent = btn.dataset.mode === activeMode;
        btn.classList.toggle("active", isCurrent);
        btn.classList.toggle("bg-amber-500", isCurrent);
        btn.classList.toggle("text-slate-950", isCurrent);
        btn.classList.toggle("shadow-sm", isCurrent);
        btn.classList.toggle("font-bold", isCurrent);
        btn.classList.toggle("text-slate-400", !isCurrent);
      });

      if (comboStepsContainer) {
        if (activeMode === "single") {
          comboStepsContainer.classList.add("opacity-30", "pointer-events-none");
        } else {
          comboStepsContainer.classList.remove("opacity-30", "pointer-events-none");
        }
      }

      updateInputPlaceholder();
    }

    function updateStepsUI() {
      stepBtns.forEach(btn => {
        const stepsNum = parseInt(btn.dataset.steps, 10);
        const isCurrent = stepsNum === activeSteps;
        btn.classList.toggle("active", isCurrent);
        btn.classList.toggle("bg-amber-500", isCurrent);
        btn.classList.toggle("text-slate-950", isCurrent);
        btn.classList.toggle("font-bold", isCurrent);
        btn.classList.toggle("text-slate-400", !isCurrent);
      });

      updateInputPlaceholder();
    }

    modeBtns.forEach(btn => {
      btn.addEventListener("click", () => {
        const newMode = btn.dataset.mode;
        if (newMode && (newMode === "single" || newMode === "combo")) {
          activeMode = newMode;
          updateModeUI();
        }
      });
    });

    stepBtns.forEach(btn => {
      btn.addEventListener("click", () => {
        const steps = parseInt(btn.dataset.steps, 10);
        if (steps >= 2 && steps <= 4) {
          activeSteps = steps;
          if (activeMode === "single") {
            activeMode = "combo";
            updateModeUI();
          }
          updateStepsUI();
        }
      });
    });

    // Horizontal Scroll Helpers & Navigation Arrows
    function updateScrollArrows() {
      if (!chipsContainer || !chipsScrollLeftBtn || !chipsScrollRightBtn) return;
      const maxScroll = chipsContainer.scrollWidth - chipsContainer.clientWidth;
      if (maxScroll <= 4) {
        chipsScrollLeftBtn.style.opacity = "0";
        chipsScrollLeftBtn.style.pointerEvents = "none";
        chipsScrollRightBtn.style.opacity = "0";
        chipsScrollRightBtn.style.pointerEvents = "none";
        return;
      }

      const atStart = chipsContainer.scrollLeft <= 6;
      const atEnd = chipsContainer.scrollLeft >= maxScroll - 6;

      chipsScrollLeftBtn.style.opacity = atStart ? "0" : "0.95";
      chipsScrollLeftBtn.style.pointerEvents = atStart ? "none" : "auto";

      chipsScrollRightBtn.style.opacity = atEnd ? "0" : "0.95";
      chipsScrollRightBtn.style.pointerEvents = atEnd ? "none" : "auto";
    }

    chipsScrollLeftBtn?.addEventListener("click", () => {
      chipsContainer?.scrollBy({ left: -220, behavior: "smooth" });
    });

    chipsScrollRightBtn?.addEventListener("click", () => {
      chipsContainer?.scrollBy({ left: 220, behavior: "smooth" });
    });

    chipsContainer?.addEventListener("scroll", updateScrollArrows);

    // Converts vertical mouse wheel to smooth horizontal scroll
    function enableHorizontalWheelScroll(element) {
      if (!element) return;
      element.addEventListener("wheel", (e) => {
        if (Math.abs(e.deltaY) > Math.abs(e.deltaX) && e.deltaY !== 0) {
          e.preventDefault();
          element.scrollLeft += e.deltaY * 1.2;
          updateScrollArrows();
        }
      }, { passive: false });
    }

    // Enables mouse click-and-drag horizontal scroll
    function enableDragToScroll(element) {
      if (!element) return;
      let isDown = false;
      let startX = 0;
      let initialScroll = 0;
      let hasDragged = false;

      element.addEventListener("mousedown", (e) => {
        if (e.button !== 0) return;
        isDown = true;
        hasDragged = false;
        startX = e.pageX - element.offsetLeft;
        initialScroll = element.scrollLeft;
      });

      window.addEventListener("mouseup", () => {
        if (!isDown) return;
        isDown = false;
        setTimeout(() => { hasDragged = false; }, 50);
      });

      element.addEventListener("mousemove", (e) => {
        if (!isDown) return;
        e.preventDefault();
        const x = e.pageX - element.offsetLeft;
        const walk = (x - startX) * 1.4;
        if (Math.abs(walk) > 5) {
          hasDragged = true;
        }
        element.scrollLeft = initialScroll - walk;
        updateScrollArrows();
      });

      // Capture phase click handler: suppress click if dragged
      element.addEventListener("click", (e) => {
        if (hasDragged) {
          e.preventDefault();
          e.stopPropagation();
          hasDragged = false;
        }
      }, true);
    }

    // Initialize horizontal scroll handlers
    enableHorizontalWheelScroll(chipsContainer);
    enableDragToScroll(chipsContainer);
    enableHorizontalWheelScroll(fieldSelector);
    enableDragToScroll(fieldSelector);

    // Render suggestion chips
    function renderSuggestionChips() {
      if (!chipsContainer) return;
      const fieldData = CHAT_FIELDS[activeField] || CHAT_FIELDS.duel;
      let chipsToRender = fieldData.chips;

      if (activeField === "duel") {
        if (duelType === "physical") {
          chipsToRender = fieldData.chipsPhysical || fieldData.chips;
        } else if (duelType === "hybrid") {
          if (duelHybridRole === "user_magic") {
            chipsToRender = fieldData.chipsHybridUserMagic || fieldData.chips;
          } else {
            chipsToRender = fieldData.chipsHybridEnemyMagic || fieldData.chips;
          }
        }
      }

      chipsContainer.innerHTML = chipsToRender.map(chip => `
        <button type="button" class="chat-chip px-2.5 py-1 rounded-full bg-slate-900/90 hover:bg-slate-800 text-slate-300 hover:text-amber-300 border border-slate-700/80 hover:border-amber-500/40 text-[11px] font-medium transition whitespace-nowrap shrink-0">
          ${chip}
        </button>
      `).join("");

      chipsContainer.querySelectorAll(".chat-chip").forEach(chipBtn => {
        chipBtn.addEventListener("click", () => {
          if (chatInput) {
            chatInput.value = chipBtn.textContent.trim();
            handleChatSubmit();
          }
        });
      });

      chipsContainer.scrollLeft = 0;
      setTimeout(updateScrollArrows, 30);
    }

    // Update active field
    function setField(field) {
      if (!CHAT_FIELDS[field]) field = "duel";
      activeField = field;

      fieldPills.forEach(pill => {
        if (pill.dataset.field === field) {
          pill.className = "chat-field-pill px-2.5 py-1 rounded-lg text-xs font-semibold whitespace-nowrap transition bg-amber-500 text-slate-950 shadow-sm font-magic";
        } else {
          pill.className = "chat-field-pill px-2.5 py-1 rounded-lg text-xs font-semibold whitespace-nowrap transition bg-slate-900 text-slate-400 hover:text-amber-300 border border-slate-800 font-magic";
        }
      });

      if (activeFieldLabel) {
        activeFieldLabel.innerHTML = `Selezionato: <strong class="text-amber-300">${CHAT_FIELDS[field].name}</strong>`;
      }

      updateDuelConfigUI();
    }

    fieldPills.forEach(pill => {
      pill.addEventListener("click", () => setField(pill.dataset.field));
    });

    // Sample button fills random suggestion
    sampleBtn?.addEventListener("click", () => {
      const fieldData = CHAT_FIELDS[activeField] || CHAT_FIELDS.duel;
      const randomChip = fieldData.chips[Math.floor(Math.random() * fieldData.chips.length)];
      if (chatInput) {
        chatInput.value = randomChip;
        chatInput.focus();
      }
    });

    // Open/Close Drawer
    function openChat(field) {
      if (field) setField(field);
      drawer.style.display = "flex";
      drawer.classList.add("active");
      drawer.classList.remove("hidden");
      setTimeout(() => {
        drawer.classList.remove("opacity-0");
        card?.classList.remove("translate-x-4");
      }, 10);

      // Welcome message on first open
      if (chatHistory.length === 0) {
        appendWelcomeMessage();
      }

      renderSuggestionChips();
      setTimeout(updateScrollArrows, 80);
      setTimeout(() => chatInput?.focus(), 150);
    }

    function closeChat() {
      drawer.classList.add("opacity-0");
      card?.classList.add("translate-x-4");
      setTimeout(() => {
        drawer.classList.remove("active");
        drawer.classList.add("hidden");
        drawer.style.display = "none";
      }, 250);
    }

    openBtn?.addEventListener("click", () => openChat());
    fabBtn?.addEventListener("click", () => openChat());
    closeBtn?.addEventListener("click", closeChat);
    backdrop?.addEventListener("click", closeChat);

    window.openTacticalChat = openChat;
    window.closeTacticalChat = closeChat;
    window.toggleTacticalChat = () => {
      if (drawer.classList.contains("active")) closeChat();
      else openChat();
    };

    // Scroll to bottom
    function scrollToBottom() {
      if (messagesContainer) {
        messagesContainer.scrollTop = messagesContainer.scrollHeight;
      }
    }

    // Append welcome message
    function appendWelcomeMessage() {
      if (!messagesContainer) return;
      const welcome = document.createElement("div");
      welcome.className = "chat-message assistant-welcome p-4 rounded-2xl bg-slate-900/80 border border-amber-500/20 text-xs text-slate-300 space-y-2 chat-bubble-enter";
      welcome.innerHTML = `
        <div class="flex items-center gap-2 text-amber-300 font-magic font-bold text-sm">
          <span>⚡</span> Benvenuto nel Grimorio Tattico di Hogwarts
        </div>
        <p class="leading-relaxed">
          Sono il tuo consigliere di duello e strategia magica. Indica il <strong>campo di azione</strong> (Duello, Pozioni, Creature, Erbologia o Rune) e descrivi l'obiettivo o la situazione che stai affrontando.
        </p>
        <p class="text-slate-400 text-[11px] leading-relaxed">
          Analizzerò il database delle <strong>562 voci didattiche</strong> per comporre la <strong>mossa o combo migliore</strong> (con formule, gesti e valenze) e formulare tutte le <strong>alternative tattiche</strong> disponibili!
        </p>
      `;
      messagesContainer.appendChild(welcome);
      scrollToBottom();
    }

    // Append user message
    function appendUserMessage(text) {
      if (!messagesContainer) return;
      const userBubble = document.createElement("div");
      userBubble.className = "chat-message user-msg flex justify-end chat-bubble-enter";
      const modeTag = activeMode === "single"
        ? "⚡ Mossa Singola"
        : `🔗 Combo (${activeSteps} Passi)`;

      let duelTag = "";
      if (activeField === "duel") {
        const off = duelOfficial ? "⚖️ Ufficiale" : "🏴 Non Ufficiale";
        let typ = "🪄 Magico";
        if (duelType === "physical") typ = "🥊 Fisico";
        else if (duelType === "hybrid") {
          typ = duelHybridRole === "user_magic" ? "⚡ Ibrido (Tu Mago)" : "⚡ Ibrido (Tu Fisico)";
        }
        duelTag = ` • ${off} • ${typ}`;
      }

      userBubble.innerHTML = `
        <div class="max-w-[85%] p-3 rounded-2xl bg-gradient-to-r from-amber-600 to-amber-700 text-slate-950 font-medium text-xs shadow-md space-y-0.5">
          <div class="text-[10px] font-bold uppercase tracking-wider text-amber-950/90 flex items-center justify-between gap-2 border-b border-amber-950/20 pb-0.5">
            <span>${CHAT_FIELDS[activeField].icon} ${CHAT_FIELDS[activeField].name}${duelTag}</span>
            <span class="px-1.5 py-0.2 bg-amber-950/20 rounded font-semibold text-[9px] shrink-0">${modeTag}</span>
          </div>
          <div class="leading-relaxed text-slate-950 font-semibold pt-0.5">${text.replace(/</g, "&lt;").replace(/>/g, "&gt;")}</div>
        </div>
      `;
      messagesContainer.appendChild(userBubble);
      scrollToBottom();
    }

    // Append loading spinner
    function appendLoadingBubble() {
      if (!messagesContainer) return null;
      const loading = document.createElement("div");
      loading.id = "chatLoadingBubble";
      loading.className = "chat-message assistant-loading p-3.5 rounded-2xl bg-slate-900/70 border border-slate-800 text-xs text-amber-400 flex items-center gap-2.5 chat-bubble-enter";
      loading.innerHTML = `
        <span class="w-2 h-2 rounded-full bg-amber-400 animate-ping"></span>
        <span class="font-magic font-bold tracking-wide">Il Grimorio sta calcolando le valenze e la combo ottimale...</span>
      `;
      messagesContainer.appendChild(loading);
      scrollToBottom();
      return loading;
    }

    function removeLoadingBubble() {
      const el = document.getElementById("chatLoadingBubble");
      if (el) el.remove();
    }

    // Submit handler
    async function handleChatSubmit(e) {
      if (e) e.preventDefault();
      if (!chatInput) return;
      const text = chatInput.value.trim();
      if (!text || isProcessing) return;

      chatInput.value = "";
      isProcessing = true;
      if (sendBtn) sendBtn.disabled = true;

      const chatOpts = {
        mode: activeMode,
        steps: activeSteps,
        duelOfficial,
        duelType,
        duelHybridRole
      };

      appendUserMessage(text);
      chatHistory.push({ role: "user", text, field: activeField, ...chatOpts });

      const loader = appendLoadingBubble();

      try {
        const apiKey = localStorage.getItem("hogwarts_gemini_api_key");
        let responseHtml = "";

        if (apiKey) {
          try {
            const geminiRaw = await callGeminiApi(apiKey, activeField, text, chatOpts);
            responseHtml = renderAssistantResponseHtml(geminiRaw);
          } catch (apiErr) {
            console.warn("Gemini API call failed, falling back to offline tactical engine:", apiErr);
            const offlineAdvice = computeTacticalAdvice(activeField, text, chatOpts);
            responseHtml = renderAssistantResponseHtml(offlineAdvice);
          }
        } else {
          // Instant offline tactical evaluation
          // Small realistic thinking delay (150ms) for magical immersion
          await new Promise(r => setTimeout(r, 160));
          const offlineAdvice = computeTacticalAdvice(activeField, text, chatOpts);
          responseHtml = renderAssistantResponseHtml(offlineAdvice);
        }

        removeLoadingBubble();

        const assistantBubble = document.createElement("div");
        assistantBubble.innerHTML = responseHtml;
        messagesContainer?.appendChild(assistantBubble);
        scrollToBottom();

        chatHistory.push({ role: "assistant", advice: responseHtml });
      } catch (err) {
        removeLoadingBubble();
        console.error("Chat Error:", err);
        const errBubble = document.createElement("div");
        errBubble.className = "p-3 rounded-xl bg-rose-950/80 border border-rose-800 text-rose-300 text-xs";
        errBubble.textContent = "Errore durante l'elaborazione magica. Riprova con un'altra richiesta.";
        messagesContainer?.appendChild(errBubble);
      } finally {
        isProcessing = false;
        if (sendBtn) sendBtn.disabled = false;
      }
    }

    chatForm.addEventListener("submit", handleChatSubmit);

    // Enter to submit (Shift+Enter for newline)
    chatInput?.addEventListener("keydown", (e) => {
      if (e.key === "Enter" && !e.shiftKey) {
        e.preventDefault();
        handleChatSubmit();
      }
    });

    // Clear history
    clearBtn?.addEventListener("click", () => {
      chatHistory = [];
      if (messagesContainer) {
        messagesContainer.innerHTML = "";
      }
      appendWelcomeMessage();
    });

    // Init UI State & Default Field
    updateModeUI();
    updateStepsUI();
    updateDuelConfigUI();
    setField("duel");
  }

  // Export methods globally for integration and tests
  if (typeof window !== "undefined") {
    window.TacticalChat = {
      computeTacticalAdvice,
      formatAdviceForModeAndSteps,
      CHAT_FIELDS,
      getActiveMode: () => activeMode,
      setActiveMode: (m) => { activeMode = m; },
      getActiveSteps: () => activeSteps,
      setActiveSteps: (s) => { activeSteps = s; },
      getDuelOfficial: () => duelOfficial,
      setDuelOfficial: (o) => { duelOfficial = o; },
      getDuelType: () => duelType,
      setDuelType: (t) => { duelType = t; },
      getDuelHybridRole: () => duelHybridRole,
      setDuelHybridRole: (r) => { duelHybridRole = r; }
    };
  }

  // Auto-init on DOM readiness
  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", initTacticalChat);
  } else {
    initTacticalChat();
  }

})();
