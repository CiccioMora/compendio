# -*- coding: utf-8 -*-
"""
Sincronizzazione Integrale del Compendio con il Programma di Studio Ufficiale di Arcane GDR:
- Trasfigurazione (VI e VII Anno)
- Difesa contro le Arti Oscure (VI e VII Anno)
- Incantesimi (VI e VII Anno)
- Codex Arithmantiae (Liber VI al VI Anno, Liber VII al VII Anno)
"""

import json
import re

BASE_DIR = '/Users/andreamorachioli/.gemini/antigravity/scratch/portale-incantesimi'
ARTIFACT_DIR = '/Users/andreamorachioli/.gemini/antigravity/brain/3a4f7fa7-8206-4f51-b303-aa9b9d9eaf5c'

# Carica spellsData.js attuale
with open(f'{BASE_DIR}/spellsData.js', 'r', encoding='utf-8') as f:
    text = f.read()

start = text.find('[')
end = text.rfind(']') + 1
spells = json.loads(text[start:end])
by_id = {s['id']: s for s in spells}

# 1. Riassegnazioni al VI ANNO (Arcane GDR)
moves_to_6 = [
    # INCANTESIMI (VI ANNO)
    ("rallegrante", "VI Anno (Incantesimi)", "Incluso nel programma ministeriale di VI Anno (Incantesimi - Sortilegi)."),
    ("silencio", "VI Anno (Incantesimi)", "Incluso nel programma ministeriale di VI Anno (Incantesimi - Incantesimo Ammutolente)."),
    ("carpe-retractum", "VI Anno (Incantesimi)", "Incluso nel programma ministeriale di VI Anno (Incantesimi - Incantesimo Afferra e Tira)."),
    ("deletrius", "VI Anno (Incantesimi)", "Incluso nel programma ministeriale di VI Anno (Incantesimi - Incantesimo di Cancellazione)."),
    ("descendo", "VI Anno (Incantesimi)", "Incluso nel programma ministeriale di VI Anno (Incantesimi - Descendo)."),
    # TRASFIGURAZIONE PRATICA (VI ANNO)
    ("crinus-muto", "VI Anno (Trasfigurazione)", "Incluso nel programma di VI Anno (Trasfigurazione Pratica - Crinus Muto)."),
    ("pullus", "VI Anno (Trasfigurazione)", "Incluso nel programma di VI Anno (Trasfigurazione Pratica - Pullus)."),
    ("densaugeo", "VI Anno (Trasfigurazione)", "Incluso nel programma di VI Anno (Trasfigurazione Pratica - Densaugeo)."),
    ("paperante", "VI Anno (Trasfigurazione)", "Incluso nel programma di VI Anno (Trasfigurazione Pratica - Paperate)."),
    ("piscofors", "VI Anno (Trasfigurazione)", "Incluso nel programma di VI Anno (Trasfigurazione Pratica - Piscofors)."),
    ("entomorphis", "VI Anno (Trasfigurazione)", "Incluso nel programma di VI Anno (Trasfigurazione Pratica - Entomorphis)."),
    ("furitum", "VI Anno (Trasfigurazione)", "Incluso nel programma di VI Anno (Trasfigurazione Pratica - Furitum)."),
    ("inflatus", "VI Anno (Trasfigurazione)", "Incluso nel programma di VI Anno (Trasfigurazione Pratica - Inflatus)."),
    # DCAO (VI ANNO)
    ("expecto-patronum", "VI Anno (D.C.A.O. - Sortilegi)", "Incluso nel programma didattico di VI Anno (D.C.A.O. - Incanto Patronus)."),
    ("languelingua", "VI Anno (D.C.A.O. - Maledictio)", "Incluso nel programma didattico di VI Anno (D.C.A.O. - Maledizione Languelingua)."),
    ("morsmordre", "VI Anno (D.C.A.O. - Teoria)", "Incluso nel programma didattico di VI Anno (D.C.A.O. - Morsmordre [Teoria]).")
]

for sid, label, prefix in moves_to_6:
    if sid in by_id:
        by_id[sid]['anno'] = 6
        by_id[sid]['annoLabel'] = label
        if prefix not in by_id[sid]['descrizione']:
            by_id[sid]['descrizione'] = f"{prefix} {by_id[sid]['descrizione']}"

# 2. Riassegnazioni al VII ANNO (Arcane GDR)
moves_to_7 = [
    # INCANTESIMI (VII ANNO)
    ("portus", "VII Anno (Incantesimi - Famiglia Trasporti)", "Incluso nel programma di VII Anno (Incantesimi - Famiglia dei Trasporti: Passaporta). Trattato anche nel Liber Sextus del Codex Arithmantiae."),
    ("adduco-maxima", "VII Anno (Incantesimi & Trasfigurazione)", "Incluso nel programma di VII Anno (Incantesimi - Incantesimo Estensivo Irriconoscibile) e studiato come teoria in Trasfigurazione di VI Anno."),
    ("obliviate", "VII Anno (Incantesimi)", "Incluso nel programma ministeriale di VII Anno (Incantesimi - Incantesimo di cancellazione della Memoria)."),
    # TRASFIGURAZIONE TEORIA (VII ANNO)
    ("animaleus-nobodyx", "VII Anno (Trasfigurazione - Teoria Animagia)", "Incluso nel programma di VII Anno (Trasfigurazione Teoria - Incantesimo Animaleus Nobodyx [Teoria]). Formula di sicurezza per il disvelamento delle trasfigurazioni umane."),
    ("reverto", "VII Anno (Trasfigurazione - Teoria Homine Reverto)", "Incluso nel programma di VII Anno (Trasfigurazione Teoria - Pozione/Controincanto Homine Reverto [Teoria]).")
]

for sid, label, prefix in moves_to_7:
    if sid in by_id:
        by_id[sid]['anno'] = 7
        by_id[sid]['annoLabel'] = label
        if prefix not in by_id[sid]['descrizione']:
            by_id[sid]['descrizione'] = f"{prefix} {by_id[sid]['descrizione']}"

# 3. Nuove formule da aggiungere dal Programma di Studio di Arcane GDR
new_spells_data = [
    # VI ANNO - INCANTESIMI
    {
        "id": "confundo",
        "anno": 6,
        "annoLabel": "VI Anno (Incantesimi)",
        "nome": "Incantesimo di Confusione (Confundo)",
        "formula": "Confundo",
        "ripetibile": True,
        "tipologia": "Magia Mentale / Confusione",
        "inDuello": True,
        "duelloNote": "Utilizzabile in duello. Causa istantaneo disorientamento e confusione nella mente del bersaglio, facendogli fallire la mira, esitare o attaccare alleati.",
        "movimento": "Puntamento ondulatorio della bacchetta verso le tempie del bersaglio con una rapida rotazione del polso.",
        "movimentoSvg": "M 40,75 C 55,45 65,105 80,75 C 95,45 105,105 120,75",
        "descrizione": "Incluso nel programma ministeriale di VI Anno (Incantesimi - Incantesimo di Confusione). Offusca la lucidità, inganna la percezione spaziale e altera temporaneamente il giudizio razionale dell'avversario o di oggetti magici senzienti (come il Calice di Fuoco).",
        "etimologia": "Dal verbo latino confundere (mescolare, disorientare, confondere).",
        "valenza": 2,
        "sommaLettere": 38,
        "valenzaOpposta": 8,
        "maxRipetizioni": 2,
        "figuraGeometrica": "Angolo / Linea (Dualismo)",
        "noteAritmantiche": "Valenza Magica 2 (somma pitagorica 38 ridotta a 2). Valenza opposta di simmetria: 8. Figura operativa per Signo: Angolo / Linea (Dualismo). Limite di reiterazione efficace: 2 volta/e."
    },
    {
        "id": "obliterato",
        "anno": 6,
        "annoLabel": "VI Anno (Incantesimi)",
        "nome": "Incantesimo Obliterante (Obliterato)",
        "formula": "Obliterato",
        "ripetibile": False,
        "tipologia": "Modifica Ambientale / Occultamento Tracce",
        "inDuello": False,
        "duelloNote": "Non da duello. Impiegato per cancellare orme, impronte di ruote o segni di calpestio sul terreno o sulla neve per depistare inseguitori.",
        "movimento": "Movimento a tergicristallo orizzontale a sfiorare la superficie del terreno.",
        "movimentoSvg": "M 30,85 Q 75,55 120,85 M 35,95 Q 75,65 115,95",
        "descrizione": "Incluso nel programma ministeriale di VI Anno (Incantesimi - Incantesimo Obliterante). Cancella istantaneamente orme, calpestii o tracce fisiche su neve, sabbia, fango o polvere, ripristinando la superficie originale senza lasciare segni di alterazione.",
        "etimologia": "Dal latino obliterare (cancellare, sopprimere ogni memoria visiva).",
        "valenza": 9,
        "sommaLettere": 45,
        "valenzaOpposta": 1,
        "maxRipetizioni": 1,
        "figuraGeometrica": "Ellisse (Reincarnazione / Dinamismo estremo)",
        "noteAritmantiche": "Valenza Magica 9 (somma pitagorica 45 ridotta a 9). Valenza opposta di simmetria: 1. Figura operativa per Signo: Ellisse (Reincarnazione / Dinamismo estremo). Limite di reiterazione efficace: 1 volta/e."
    },
    # VI ANNO - TRASFIGURAZIONE & DCAO
    {
        "id": "geminio",
        "anno": 6,
        "annoLabel": "VI Anno (Trasfigurazione & D.C.A.O.)",
        "nome": "Incantesimo / Maledizione di Duplicazione (Geminio)",
        "formula": "Geminio",
        "ripetibile": False,
        "tipologia": "Trasfigurazione / Maledizione Duplicante",
        "inDuello": False,
        "duelloNote": "Non da duello ordinario. Quando imposto come maledizione (Maledizione Gemini), fa moltiplicare esponenzialmente e roventemente l'oggetto toccato fino a schiacciare o soffocare gli intrusi (es. camere blindate della Gringott).",
        "movimento": "Pressione perpendicolare sulla superficie dell'oggetto seguita da un rapido doppio tocco a rimbalzo.",
        "movimentoSvg": "M 55,75 A 20,20 0 1,1 54,75 M 95,75 A 20,20 0 1,1 94,75",
        "descrizione": "Incluso nel programma di VI Anno (Trasfigurazione Pratica & D.C.A.O. - Maledizione Gemini [Teoria]). Duplica qualsiasi oggetto inanimato creando una replica esatta all'apparenza, ma priva di valore autentico e destinata col tempo a decadere e degradarsi.",
        "etimologia": "Dal latino geminare (raddoppiare, moltiplicare).",
        "valenza": 9,
        "sommaLettere": 45,
        "valenzaOpposta": 1,
        "maxRipetizioni": 1,
        "figuraGeometrica": "Ellisse (Reincarnazione / Dinamismo estremo)",
        "noteAritmantiche": "Valenza Magica 9 (somma pitagorica 45 ridotta a 9). Valenza opposta di simmetria: 1. Figura operativa per Signo: Ellisse (Reincarnazione / Dinamismo estremo). Limite di reiterazione efficace: 1 volta/e."
    },
    # VI ANNO - DCAO (MALEDICTIO)
    {
        "id": "mucus-ad-nauseam",
        "anno": 6,
        "annoLabel": "VI Anno (Maledictio - D.C.A.O.)",
        "nome": "Maledizione delle Caccole (Mucus ad Nauseam)",
        "formula": "Mucus ad Nauseam",
        "ripetibile": True,
        "tipologia": "Maledizione / Debilitazione Respiratoria",
        "inDuello": True,
        "duelloNote": "Utilizzabile in duello. Provoca un attacco istantaneo di raffreddore magico acuto con copiosa rinorrea verdastra che toglie il respiro e spezza il puntamento.",
        "movimento": "Gesto ondulatorio rapido dal naso dell'incantatore verso il bersaglio con un colpo secco discendente.",
        "movimentoSvg": "M 45,40 Q 60,85 75,60 Q 90,85 105,40 L 75,115",
        "descrizione": "Descritta in Maledictio e inclusa nel programma di VI Anno (D.C.A.O. - Maledizione delle caccole). Provoca un colamento ininterrotto di muco denso e starnuti convulsi che debilitano l'avversario e rendono impossibile la corretta pronuncia verbale.",
        "etimologia": "Dal latino mucus (muco) e ad nauseam (fino alla nausea, a oltranza).",
        "valenza": 3,
        "sommaLettere": 39,
        "valenzaOpposta": 7,
        "maxRipetizioni": 3,
        "figuraGeometrica": "Triangolo equilatero (Unificazione)",
        "noteAritmantiche": "Valenza Magica 3 (somma pitagorica 39 ridotta a 3). Valenza opposta di simmetria: 7. Figura operativa per Signo: Triangolo equilatero (Unificazione). Limite di reiterazione efficace: 3 volta/e."
    },
    {
        "id": "balbutio",
        "anno": 6,
        "annoLabel": "VI Anno (Maledictio - D.C.A.O.)",
        "nome": "Maledizione Balbuziente (Balbutio)",
        "formula": "Balbutio",
        "ripetibile": False,
        "tipologia": "Maledizione / Inibizione Verbale",
        "inDuello": True,
        "duelloNote": "Molto efficace in duello contro maghi che non padroneggiano il lancio non-verbale: blocca la favella e fa balbettare convulsamente il bersaglio rendendo nulli gli incantesimi verbali.",
        "movimento": "Doppio scatto orizzontale a zig-zag serrato all'altezza della gola.",
        "movimentoSvg": "M 40,75 L 60,65 L 75,85 L 90,65 L 110,75",
        "descrizione": "Descritta in Maledictio e inserita nel programma di VI Anno (D.C.A.O. - Maledizione Balbuziente). Provoca un'improvvisa forma grave di balbuzie spasmodica che impedisce l'articolazione sillabica corretta delle formule magiche.",
        "etimologia": "Dal latino balbutire (balbettare, inciampare nelle parole).",
        "valenza": 1,
        "sommaLettere": 28,
        "valenzaOpposta": 9,
        "maxRipetizioni": 1,
        "figuraGeometrica": "Circonferenza (Elemento Acqua)",
        "noteAritmantiche": "Valenza Magica 1 (somma pitagorica 28 ridotta a 1). Valenza opposta di simmetria: 9. Figura operativa per Signo: Circonferenza (Elemento Acqua). Limite di reiterazione efficace: 1 volta/e."
    },
    {
        "id": "flagrante",
        "anno": 6,
        "annoLabel": "VI Anno (Maledictio - D.C.A.O.)",
        "nome": "Maledizione Flagrante (Flagrante)",
        "formula": "Flagrante",
        "ripetibile": False,
        "tipologia": "Maledizione Difensiva / Ustione da Contatto",
        "inDuello": False,
        "duelloNote": "Non da duello. Viene applicata segretamente su tesori, maniglie o reliquie: all'istante del contatto fisico, il metallo arde di calore rovente provocando ustioni gravi.",
        "movimento": "Spirale stretta sulla superficie dell'oggetto culminante con una pressione incandescente della punta.",
        "movimentoSvg": "M 75,75 m -35,0 a 35,35 0 1,0 70,0 a 35,35 0 1,0 -70,0 M 75,50 L 75,100 M 50,75 L 100,75",
        "descrizione": "Descritta in Maledictio e inclusa nel programma di VI Anno (D.C.A.O. - Maledizione Flagrante). Incanta oggetti e forzieri rendendoli roventi al tocco pur non mostrando alcun segno esteriore visibile (nessun fumo né fiamma apparente).",
        "etimologia": "Dal participio latino flagrans / flagrantis (che brucia, ardente, fiammeggiante).",
        "valenza": 3,
        "sommaLettere": 39,
        "valenzaOpposta": 7,
        "maxRipetizioni": 1,
        "figuraGeometrica": "Triangolo equilatero (Unificazione)",
        "noteAritmantiche": "Valenza Magica 3 (somma pitagorica 39 ridotta a 3). Valenza opposta di simmetria: 7. Figura operativa per Signo: Triangolo equilatero (Unificazione). Limite di reiterazione efficace: 1 volta/e."
    },
    # VII ANNO - DCAO SUPERIORE
    {
        "id": "patronus-messaggero",
        "anno": 7,
        "annoLabel": "VII Anno (D.C.A.O. Superiore)",
        "nome": "Incanto Patronus Messaggero (Expecto Patronum Vocalis)",
        "formula": "Expecto Patronum",
        "ripetibile": False,
        "tipologia": "Incanto Protettivo Superiore / Messaggero Vocale",
        "inDuello": False,
        "duelloNote": "Non da combattimento diretto. Invenzione riservata all'Ordine della Fenice (ideata da Albus Silente): il Patronus assume consistenza corporea o semitrasparente e parla con la voce stessa dell'evocatore per recapitare comunicazioni segrete a prova di intercettazione.",
        "movimento": "Ampio cerchio fluido dal cuore verso l'esterno, accompagnato da un sussurro mentale del messaggio da trasmettere.",
        "movimentoSvg": "M 75,45 C 50,45 35,65 35,85 C 35,110 65,120 75,130 C 85,120 115,110 115,85 C 115,65 100,45 75,45 Z",
        "descrizione": "Incluso nel programma didattico di VII Anno (D.C.A.O. - Incanto Patronus Messaggero). Variante avanzatissima ideata da Silente: il Patronus si muove istantaneamente attraverso qualsiasi distanza e ostacolo, manifestandosi davanti al destinatario e ripetendo il messaggio con la voce dell'incantatore prima di dissolversi.",
        "etimologia": "Dal latino patronus (protettore, difensore).",
        "valenza": 6,
        "sommaLettere": 69,
        "valenzaOpposta": 4,
        "maxRipetizioni": 1,
        "figuraGeometrica": "Esagono regolare (Elemento Terra / Equilibrio)",
        "noteAritmantiche": "Valenza Magica 6 (somma pitagorica 69 ridotta a 6). Valenza opposta di simmetria: 4. Figura operativa per Signo: Esagono regolare (Elemento Terra / Equilibrio). Limite di reiterazione efficace: 1 volta/e."
    }
]

for ns in new_spells_data:
    if ns['id'] in by_id:
        by_id[ns['id']].update(ns)
    else:
        spells.append(ns)
        by_id[ns['id']] = ns

# Ordinamento rigoroso per anno: 1, 2, 3, 4, 5, 6, 7, poi 0
def sort_key(s):
    y = s['anno']
    order_val = 99 if y == 0 else y
    return (order_val, s['nome'])

spells.sort(key=sort_key)

js_content = """// spellsData.js - Archivio Completo degli Incantesimi suddiviso per Anni
// Fonti Didattiche Ufficiali:
// - Programma di Studio Arcane GDR: Incantesimi, Trasfigurazione, Difesa Contro le Arti Oscure (I-VII Anno)
// - Codex Arithmantiae (Zeno & Glaphira Hawstein): Liber I-V (Aritmanzia di Base), Liber VI (Spazio e Traslazione), Liber VII (Rituali, Sigilli e Trappole)
// - Trattati di D.C.A.O.: Maledictio & Oltre il Mago (Yashiro Isana Mortem)

const SPELLS_DATA = """ + json.dumps(spells, ensure_ascii=False, indent=2) + """;

if (typeof module !== "undefined" && module.exports) {
  module.exports = SPELLS_DATA;
}
"""

with open(f'{BASE_DIR}/spellsData.js', 'w', encoding='utf-8') as f:
    f.write(js_content)

print(f"Salvati {len(spells)} incantesimi in spellsData.js!")

# Conteggi
counts = {}
for s in spells:
    counts[s['anno']] = counts.get(s['anno'], 0) + 1
duel_yes = sum(1 for s in spells if s['inDuello'])
duel_no = sum(1 for s in spells if not s['inDuello'])
total = len(spells)

print(f"Statistiche: Totale={total}, Anni={counts}, Duello: SÌ={duel_yes}, NO={duel_no}")

# 4. Aggiorna index.html
with open(f'{BASE_DIR}/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Badge eroico
html = re.sub(r'\b\d+\s+Incantesimi\s+Codificati\b', f'{total} Incantesimi Codificati', html)

# Select Anno
old_year_opts = re.compile(r'<select id="yearSelect"[\s\S]*?</select>')
new_year_opts = f'''<select id="yearSelect" class="w-full px-3 py-2.5 rounded-xl bg-slate-950/90 border border-slate-700 text-xs text-slate-200 focus:outline-none focus:border-amber-500 transition">
            <option value="ALL">Tutti gli Anni ({total})</option>
            <option value="1">I Anno — Fondamenti & Cinetica ({counts.get(1, 0)})</option>
            <option value="2">II Anno — Fatture & Inanimati ({counts.get(2, 0)})</option>
            <option value="3">III Anno — Gelo & Locomozione ({counts.get(3, 0)})</option>
            <option value="4">IV Anno — Tattiche & Medimagia ({counts.get(4, 0)})</option>
            <option value="5">V Anno — G.U.F.O. & Esplosivi ({counts.get(5, 0)})</option>
            <option value="6">VI Anno — M.A.G.O. I: Maledictio, Trasfigurazione, Incantesimi & Lib. VI ({counts.get(6, 0)})</option>
            <option value="7">VII Anno — M.A.G.O. II: Oltre il Mago, Trasporti, Animagia & Lib. VII ({counts.get(7, 0)})</option>
            <option value="0">Aritmanzia — Hawstein: Liber I-V & Trattati Operativi ({counts.get(0, 0)})</option>
          </select>'''
html = old_year_opts.sub(new_year_opts, html)

# Select Duello
old_duel_opts = re.compile(r'<select id="duelFilter"[\s\S]*?</select>')
new_duel_opts = f'''<select id="duelFilter" class="w-full px-3 py-2.5 rounded-xl bg-slate-950/90 border border-slate-700 text-xs text-slate-200 focus:outline-none focus:border-amber-500 transition">
            <option value="ALL">Duello: Qualsiasi ({total})</option>
            <option value="YES">⚔️ Utilizzabile in Duello: SÌ ({duel_yes})</option>
            <option value="NO">⛔ Non da Duello / Rituale: NO ({duel_no})</option>
          </select>'''
html = old_duel_opts.sub(new_duel_opts, html)

# Badge risultati
html = re.sub(r'id="resultsCountBadge"[^>]*>[\s\S]*?</span>', f'id="resultsCountBadge" class="text-amber-400 font-code font-semibold">{total} incantesimi trovati</span>', html)

# Quick Tabs
old_tabs = re.compile(r'<div class="flex items-center gap-1\.5 overflow-x-auto pb-1\.5 scrollbar-none" id="yearTabsContainer">[\s\S]*?</div>')
new_tabs = f'''<div class="flex items-center gap-1.5 overflow-x-auto pb-1.5 scrollbar-none" id="yearTabsContainer">
            <button data-year="ALL" class="year-tab px-3 py-1.5 rounded-lg text-xs font-semibold transition whitespace-nowrap bg-amber-500 text-slate-950 shadow-md">
              Tutti ({total})
            </button>
            <button data-year="1" class="year-tab px-3 py-1.5 rounded-lg text-xs font-semibold transition whitespace-nowrap bg-slate-800 text-slate-300 hover:bg-slate-700">
              I Anno ({counts.get(1, 0)})
            </button>
            <button data-year="2" class="year-tab px-3 py-1.5 rounded-lg text-xs font-semibold transition whitespace-nowrap bg-slate-800 text-slate-300 hover:bg-slate-700">
              II Anno ({counts.get(2, 0)})
            </button>
            <button data-year="3" class="year-tab px-3 py-1.5 rounded-lg text-xs font-semibold transition whitespace-nowrap bg-slate-800 text-slate-300 hover:bg-slate-700">
              III Anno ({counts.get(3, 0)})
            </button>
            <button data-year="4" class="year-tab px-3 py-1.5 rounded-lg text-xs font-semibold transition whitespace-nowrap bg-slate-800 text-slate-300 hover:bg-slate-700">
              IV Anno ({counts.get(4, 0)})
            </button>
            <button data-year="5" class="year-tab px-3 py-1.5 rounded-lg text-xs font-semibold transition whitespace-nowrap bg-slate-800 text-slate-300 hover:bg-slate-700">
              V Anno ({counts.get(5, 0)})
            </button>
            <button data-year="6" class="year-tab px-3 py-1.5 rounded-lg text-xs font-semibold transition whitespace-nowrap bg-slate-800 text-slate-300 hover:bg-slate-700">
              VI Anno ({counts.get(6, 0)})
            </button>
            <button data-year="7" class="year-tab px-3 py-1.5 rounded-lg text-xs font-semibold transition whitespace-nowrap bg-slate-800 text-slate-300 hover:bg-slate-700">
              VII Anno ({counts.get(7, 0)})
            </button>
            <button data-year="0" class="year-tab px-3 py-1.5 rounded-lg text-xs font-semibold transition whitespace-nowrap bg-slate-800 text-slate-300 hover:bg-slate-700">
              Aritmanzia ({counts.get(0, 0)})
            </button>
          </div>'''
html = old_tabs.sub(new_tabs, html)

# Segmented controls
old_duel_seg = re.compile(r'<div class="inline-flex rounded-xl bg-slate-950 p-1 border border-slate-800 shadow-inner" id="duelSegmentedGroup">[\s\S]*?</div>')
new_duel_seg = f'''<div class="inline-flex rounded-xl bg-slate-950 p-1 border border-slate-800 shadow-inner" id="duelSegmentedGroup">
              <button data-duel="ALL" class="duel-seg-btn px-3 py-1.5 rounded-lg text-xs font-semibold bg-amber-500/20 text-amber-300 border border-amber-500/40 transition">
                Tutti ({total})
              </button>
              <button data-duel="YES" class="duel-seg-btn px-3 py-1.5 rounded-lg text-xs font-semibold text-slate-400 hover:text-emerald-300 hover:bg-slate-800/80 transition">
                ⚔️ Da Duello: SÌ ({duel_yes})
              </button>
              <button data-duel="NO" class="duel-seg-btn px-3 py-1.5 rounded-lg text-xs font-semibold text-slate-400 hover:text-rose-300 hover:bg-slate-800/80 transition">
                ⛔ Non da Duello: NO ({duel_no})
              </button>
            </div>'''
html = old_duel_seg.sub(new_duel_seg, html)

with open(f'{BASE_DIR}/index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Aggiornato index.html!")

# 5. Standalone HTML
with open(f'{BASE_DIR}/style.css', 'r', encoding='utf-8') as f:
    css_content = f.read()

with open(f'{BASE_DIR}/app.js', 'r', encoding='utf-8') as f:
    app_js = f.read()

standalone = html
standalone = standalone.replace('<link rel="stylesheet" href="style.css">', f'<style>\n{css_content}\n</style>')
standalone = standalone.replace('<script src="spellsData.js"></script>', f'<script>\n{js_content}\n</script>')
standalone = standalone.replace('<script src="app.js"></script>', f'<script>\n{app_js}\n</script>')

with open(f'{BASE_DIR}/dist/portale_standalone.html', 'w', encoding='utf-8') as f:
    f.write(standalone)

with open(f'{ARTIFACT_DIR}/portale_incantesimi.html', 'w', encoding='utf-8') as f:
    f.write(standalone)

print("Rigenerati dist/portale_standalone.html e artifact portale_incantesimi.html!")
