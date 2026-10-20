# -*- coding: utf-8 -*-
"""
Sincronizzazione finale del VII Anno (Incantesimi) da Arcane GDR:
- Teoria: Incantesimo Fidelius
- Sortilegi: Incantesimo Proteus, Prior Incantatio (spostato al VII Anno), Cave Inimicum, Partis Temporus
- Aggiornamento dataset (154 formule), UI, standalone, markdown e artifacts.
"""

import json
import re

BASE_DIR = '/Users/andreamorachioli/.gemini/antigravity/scratch/portale-incantesimi'
ARTIFACT_DIR = '/Users/andreamorachioli/.gemini/antigravity/brain/3a4f7fa7-8206-4f51-b303-aa9b9d9eaf5c'

with open(f'{BASE_DIR}/spellsData.js', 'r', encoding='utf-8') as f:
    text = f.read()

spells = json.loads(text[text.find('['):text.rfind(']')+1])
by_id = {s['id']: s for s in spells}

# 1. Sposta Prior Incantatem al VII Anno (Arcane GDR - VII Anno Sortilegi: Prior Incantatio)
if "prior-incantatem" in by_id:
    by_id["prior-incantatem"]["anno"] = 7
    by_id["prior-incantatem"]["annoLabel"] = "VII Anno (Incantesimi - Prior Incantatio)"
    by_id["prior-incantatem"]["nome"] = "Rivelazione della Memoria della Bacchetta (Prior Incantatio / Prior Incantatem)"
    by_id["prior-incantatem"]["descrizione"] = "Incluso nel programma didattico di VII Anno (Incantesimi - Sortilegi: Prior Incantatio). Trattato approfonditamente anche nel Liber Sextus del Codex Arithmantiae (Cap. VII: Le bacchette e l'aritmologia). Costringe una bacchetta a rilasciare l'ombra e l'eco degli ultimi sortilegi castati in ordine temporale inverso."

# 2. Aggiorna Partis Temporus
if "partis-temporus" in by_id:
    by_id["partis-temporus"]["annoLabel"] = "VII Anno (Incantesimi & D.C.A.O.)"
    by_id["partis-temporus"]["descrizione"] = "Incluso nel programma didattico di VII Anno (Incantesimi - Sortilegi: Partis Temporus & D.C.A.O. Superiore). Formula di alta difesa contro magie ignee oscure: permette all'incantatore di aprire una breccia o un corridoio di sicurezza attraverso barriere di fuoco magico ostili (incluso l'Ardemonio parzialmente circoscritto)."

# 3. Nuove formule del VII Anno (Arcane GDR)
new_seventh_spells = [
    {
        "id": "fidelius",
        "anno": 7,
        "annoLabel": "VII Anno (Incantesimi - Teoria Fidelius)",
        "nome": "Incantesimo di Occultamento Totale (Incantesimo Fidelius)",
        "formula": "Fidelius",
        "ripetibile": False,
        "tipologia": "Incanto di Occultamento Ermetico / Rituale dell'Anima",
        "inDuello": False,
        "duelloNote": "Rituale di protezione assoluta non da duello. Nasconde un segreto (come una dimora o una persona) all'interno dell'anima vivente di un Custode Segreto designato.",
        "movimento": "Punta della bacchetta a contatto con il petto del Custode Segreto, tracciando un quadrato ermetico ideale.",
        "movimentoSvg": "M 45,45 L 105,45 L 105,105 L 45,105 Z M 75,60 L 75,90 M 60,75 L 90,75",
        "descrizione": "Incluso nel programma didattico di VII Anno (Incantesimi - Teoria Incantesimo Fidelius). Sortilegio antico ed estremamente complesso che sigilla un'informazione nell'anima di una persona viva (il Custode Segreto). Il luogo protetto diventa invisibile, intangibile e introvabile a chiunque, a meno che il Custode non riveli volontariamente il segreto.",
        "etimologia": "Dal latino fidelis (fedele, leale).",
        "valenza": 4,
        "sommaLettere": 40,
        "valenzaOpposta": 6,
        "maxRipetizioni": 1,
        "figuraGeometrica": "Quadrato (Immanenza / Risoluzione)",
        "noteAritmantiche": "Valenza Magica 4 (somma pitagorica 40 ridotta a 4). Valenza opposta di simmetria: 6. Figura operativa per Signo: Quadrato (Immanenza / Risoluzione). Limite di reiterazione efficace: 1 volta/e."
    },
    {
        "id": "proteus",
        "anno": 7,
        "annoLabel": "VII Anno (Incantesimi - Sortilegi)",
        "nome": "Incantesimo Proteus (Proteus)",
        "formula": "Proteus",
        "ripetibile": False,
        "tipologia": "Incantesimo di Legame Simpatico / Modifica Multipla",
        "inDuello": False,
        "duelloNote": "Non utilizzabile in duello. Crea un legame magico indissolubile tra più repliche di un oggetto (es. le monete dell'Esercito di Silente o i Galeoni dei Mangiamorte): modificandone una, tutte le altre mutano all'istante.",
        "movimento": "Tracciare un esagono aereo sopra il prototipo e toccare a raggiera le repliche.",
        "movimentoSvg": "M 75,35 L 105,55 L 105,95 L 75,115 L 45,95 L 45,55 Z",
        "descrizione": "Incluso nel programma didattico di VII Anno (Incantesimi - Sortilegi: Incantesimo Proteus) e trattato nel Liber III del Codex Arithmantiae. Lega magicamente più oggetti a un originale: quando i tratti o le lettere dell'originale vengono alterati, tutte le copie riflettono istantaneamente la modifica.",
        "etimologia": "Dal dio marino greco Proteo, celebre per mutare forma a piacimento.",
        "valenza": 6,
        "sommaLettere": 33,
        "valenzaOpposta": 4,
        "maxRipetizioni": 1,
        "figuraGeometrica": "Esagono regolare (Elemento Terra / Equilibrio)",
        "noteAritmantiche": "Valenza Magica 6 (somma pitagorica 33 ridotta a 6). Valenza opposta di simmetria: 4. Figura operativa per Signo: Esagono regolare (Elemento Terra / Equilibrio). Limite di reiterazione efficace: 1 volta/e."
    },
    {
        "id": "cave-inimicum",
        "anno": 7,
        "annoLabel": "VII Anno (Incantesimi - Sortilegi)",
        "nome": "Incantesimo Difensivo d'Avvertimento (Cave Inimicum)",
        "formula": "Cave Inimicum",
        "ripetibile": False,
        "tipologia": "Difensivo Statico di Zona (I.D.S.) / Rivelazione Nemici",
        "inDuello": False,
        "duelloNote": "Non da duello. Sortilegio difensivo d'accampamento: avvolge un'area in una cupola invisibile che avverte gli occupanti dell'avvicinarsi di nemici o intrusi e ne dissimula la vista dall'esterno.",
        "movimento": "Puntare la bacchetta verso la volta celeste e tracciare un cerchio protettivo dall'alto verso il basso.",
        "movimentoSvg": "M 75,30 A 45,45 0 1,0 75,120 A 45,45 0 1,0 75,30 M 75,45 L 75,105 M 45,75 L 105,75",
        "descrizione": "Incluso nel programma didattico di VII Anno (Incantesimi - Sortilegi: Cave Inimicum). Uno dei cardini della difesa da campo avanzata: rende l'area protetta indistinguibile per chi guarda dall'esterno e fa vibrare la bacchetta dell'incantatore non appena un individuo ostile tenta di varcare il perimetro.",
        "etimologia": "Dal latino cave (guardati da, fai attenzione) e inimicum (il nemico).",
        "valenza": 5,
        "sommaLettere": 59,
        "valenzaOpposta": 5,
        "maxRipetizioni": 1,
        "figuraGeometrica": "Pentagono regolare (Elemento Aria / Etere)",
        "noteAritmantiche": "Valenza Magica 5 (somma pitagorica 59 ridotta a 5). Valenza opposta di simmetria: 5. Figura operativa per Signo: Pentagono regolare (Elemento Aria / Etere). Limite di reiterazione efficace: 1 volta/e."
    }
]

for ns in new_seventh_spells:
    if ns['id'] in by_id:
        by_id[ns['id']].update(ns)
    else:
        spells.append(ns)
        by_id[ns['id']] = ns

# Ordinamento
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
            <option value="7">VII Anno — M.A.G.O. II: Incantesimi, Oltre il Mago, Animagia & Lib. VII ({counts.get(7, 0)})</option>
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

# Standalone
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
