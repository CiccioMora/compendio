// tacticalChat.js - Consigliere Tattico & Grimorio di Azione per Hogwarts
// Analizza il campo di azione (Duello, Pozioni, Creature, Erbologia, Rune, Misto)
// e restituisce la mossa o combo ottimale con spiegazione, valenze e alternative tattiche.

(function() {
  "use strict";

  // --- Configuration & Quick Suggestions per Field ---
  const CHAT_FIELDS = {
    duel: {
      name: "Duello Magico",
      icon: "⚔️",
      placeholder: "Descrivi la situazione di duello (es. 'L\'avversario usa Protego e mi attacca con fiamme')...",
      chips: [
        "⚔️ Combo Disarmo e Schianto Rapido",
        "🛡️ Superare o Abbattere un Protego",
        "🔥 Neutralizzare un attacco di Fuoco",
        "⚡ Attacco rapido con Valenza Opposta",
        "💨 Fuga ed Evasione da Accerchiamento",
        "🪄 Spezzare un incantesimo di Legame"
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

  // --- KNOWLEDGE & HEURISTIC TACTICAL REASONING ENGINE ---
  function computeTacticalAdvice(field, query) {
    const q = (query || "").toLowerCase();
    const spells = getSpells();
    const materie = getMaterie();

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
    if (field === "duel" || (field === "all" && (q.includes("duell") || q.includes("combatt") || q.includes("protego") || q.includes("attacc") || q.includes("scudo") || q.includes("disarm")))) {
      
      // Scenario A: Protego / Shield Breaker
      if (q.includes("protego") || q.includes("scudo") || q.includes("barriera") || q.includes("abbatter") || q.includes("sfondar") || q.includes("superare")) {
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

      // Scenario B: Fire Attack / Neutralizing Fire
      if (q.includes("fuoco") || q.includes("incendio") || q.includes("fiamma") || q.includes("brucia")) {
        return {
          title: "Strategia di Duello: Neutralizzazione Fuoco ed Estinzione Magica",
          fieldLabel: "⚔️ Duello Magico • Contro-Elementale",
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
    if (field === "potions" || (field === "all" && (q.includes("pozion") || q.includes("alchim") || q.includes("veleno") || q.includes("antidoto") || q.includes("infuso") || q.includes("calderon")))) {
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
    // Scan all spells for matching terms in name, formula, or duelloNote
    const matchingSpells = spells.filter(s => {
      const corpus = `${s.nome} ${s.formula} ${s.descrizione} ${s.duelloNote || ''} ${s.tipologia}`.toLowerCase();
      return q.split(/\s+/).some(word => word.length > 3 && corpus.includes(word));
    }).slice(0, 3);

    const matchingCreatures = materie.creature.filter(c => {
      const corpus = `${c.nome} ${c.descrizione} ${c.utilizziMagici || ''}`.toLowerCase();
      return q.split(/\s+/).some(word => word.length > 3 && corpus.includes(word));
    }).slice(0, 2);

    const matchingPotions = materie.pozioni.filter(p => {
      const corpus = `${p.nome} ${p.descrizione} ${p.tipologia}`.toLowerCase();
      return q.split(/\s+/).some(word => word.length > 3 && corpus.includes(word));
    }).slice(0, 2);

    // Build synthesized custom advice
    const spellA = matchingSpells[0] || spells.find(s => s.id === "expelliarmus") || spells[0];
    const spellB = matchingSpells[1] || spells.find(s => s.id === "stupeficium") || spells[1];
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

  // --- GEMINI API FALLBACK CLIENT (OPTIONAL POWER-USER INTEGRATION) ---
  async function callGeminiApi(apiKey, field, query) {
    const fieldName = CHAT_FIELDS[field] ? CHAT_FIELDS[field].name : "Mondo Magico";
    const systemPrompt = `Sei il Grimorio Tattico di Hogwarts, un esperto maestro di duelli magici, alchimia delle pozioni, creature ed erbologia dell'Arcane GDR.
L'utente ti chiede una mossa o combo tattica nel campo "${fieldName}".
Fornisci SEMPRE:
1. "Mossa o Combo Migliore (Scelta Ottimale)": con step numerati, formule esatte (es. Expelliarmus, Aguamenti, Glisseo), Valenza Magica (1-9), e spiegazione chiara del perché funziona.
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
    const stepsHtml = advice.bestMove.steps.map(s => `
      <div class="flex items-start gap-2.5 p-2.5 rounded-xl bg-slate-900/80 border border-slate-800/80">
        <span class="w-5 h-5 rounded-full bg-emerald-500/20 text-emerald-300 border border-emerald-500/40 flex items-center justify-center font-bold text-[10px] shrink-0 mt-0.5">
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
        <div class="flex items-center justify-between border-b border-slate-800 pb-2.5">
          <div class="flex items-center gap-2">
            <span class="text-base">🪄</span>
            <span class="font-magic font-bold text-white text-sm sm:text-base tracking-wide">${advice.title}</span>
          </div>
          <span class="text-[10px] px-2 py-0.5 rounded-full bg-amber-500/15 text-amber-300 border border-amber-500/30 whitespace-nowrap font-medium">
            ${advice.fieldLabel}
          </span>
        </div>

        <!-- Mossa o Combo Ottimale -->
        <div class="space-y-2">
          <div class="text-[11px] uppercase tracking-wider font-bold text-emerald-400 flex items-center gap-1.5">
            <span>🎯</span> Mossa o Combo Ottimale Consigliata:
          </div>
          <div class="p-3 rounded-xl bg-slate-950/90 border border-emerald-500/30 space-y-2">
            <div class="font-magic font-bold text-emerald-300 text-xs">${advice.bestMove.name}</div>
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
    const fieldPills = document.querySelectorAll(".chat-field-pill");
    const activeFieldLabel = document.getElementById("activeChatFieldLabel");
    const toggleApiKeyBtn = document.getElementById("toggleChatApiKey");
    const apiKeyRow = document.getElementById("apiKeyConfigRow");
    const apiKeyInput = document.getElementById("geminiApiKeyInput");
    const saveApiKeyBtn = document.getElementById("saveApiKeyBtn");
    const sampleBtn = document.getElementById("chatVoiceOrSampleBtn");

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

    // Render suggestion chips
    function renderSuggestionChips() {
      if (!chipsContainer) return;
      const fieldData = CHAT_FIELDS[activeField] || CHAT_FIELDS.duel;
      chipsContainer.innerHTML = fieldData.chips.map(chip => `
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

      if (chatInput) {
        chatInput.placeholder = CHAT_FIELDS[field].placeholder;
      }

      renderSuggestionChips();
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
      userBubble.innerHTML = `
        <div class="max-w-[85%] p-3 rounded-2xl bg-gradient-to-r from-amber-600 to-amber-700 text-slate-950 font-medium text-xs shadow-md space-y-0.5">
          <div class="text-[10px] font-bold uppercase tracking-wider text-amber-950/80">${CHAT_FIELDS[activeField].icon} ${CHAT_FIELDS[activeField].name}</div>
          <div class="leading-relaxed text-slate-950 font-semibold">${text.replace(/</g, "&lt;").replace(/>/g, "&gt;")}</div>
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

      appendUserMessage(text);
      chatHistory.push({ role: "user", text, field: activeField });

      const loader = appendLoadingBubble();

      try {
        const apiKey = localStorage.getItem("hogwarts_gemini_api_key");
        let responseHtml = "";

        if (apiKey) {
          try {
            const geminiRaw = await callGeminiApi(apiKey, activeField, text);
            responseHtml = renderAssistantResponseHtml(geminiRaw);
          } catch (apiErr) {
            console.warn("Gemini API call failed, falling back to offline tactical engine:", apiErr);
            const offlineAdvice = computeTacticalAdvice(activeField, text);
            responseHtml = renderAssistantResponseHtml(offlineAdvice);
          }
        } else {
          // Instant offline tactical evaluation
          // Small realistic thinking delay (150ms) for magical immersion
          await new Promise(r => setTimeout(r, 160));
          const offlineAdvice = computeTacticalAdvice(activeField, text);
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

    // Init with default chips
    setField("duel");
  }

  // Auto-init on DOM readiness
  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", initTacticalChat);
  } else {
    initTacticalChat();
  }

})();
