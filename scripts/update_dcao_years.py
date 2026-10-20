# -*- coding: utf-8 -*-
"""
Script di sincronizzazione del Compendio degli Incantesimi:
- Difesa Contro le Arti Oscure:
  * VI Anno: Maledictio (Yashiro Isana Mortem)
  * VII Anno: Oltre il Mago (Yashiro Isana Mortem)
- Aritmanzia:
  * VI Anno: Liber Sextus (Zeno & Glaphira Hawstein - Spazio e Traslazione)
  * VII Anno: Liber Septimus (Zeno & Glaphira Hawstein - Rituali, Sigilli e Trappole)
- Aggiornamento dataset, filtri UI, standalone bundle, documentazione e artifact.
"""

import json
import re
import os

BASE_DIR = '/Users/andreamorachioli/.gemini/antigravity/scratch/portale-incantesimi'
ARTIFACT_DIR = '/Users/andreamorachioli/.gemini/antigravity/brain/3a4f7fa7-8206-4f51-b303-aa9b9d9eaf5c'

# 1. Carica spellsData.js
with open(f'{BASE_DIR}/spellsData.js', 'r', encoding='utf-8') as f:
    text = f.read()

start = text.find('[')
end = text.rfind(']') + 1
spells = json.loads(text[start:end])

by_id = {s['id']: s for s in spells}

# Aggiorna incantesimi di Maledictio per il VI Anno
maledictio_ids = [
    'titillando', 'exulcero', 'monstrum', 'dismundo',
    'locomotor-mortis', 'locomotor-wibbly', 'dolohoferio',
    'sectumsempra', 'vulnera-sanentur', 'infelicita-eterna',
    'stalker-convocatus'
]

for mid in maledictio_ids:
    if mid in by_id:
        by_id[mid]['anno'] = 6
        by_id[mid]['annoLabel'] = 'VI Anno (Maledictio)'
        desc = by_id[mid]['descrizione']
        if 'Maledictio' not in desc:
            by_id[mid]['descrizione'] = f"Trattato nel manuale di D.C.A.O. Maledictio (Y. I. Mortem, VI Anno). {desc}"

# Aggiorna Trasfigurazione M.A.G.O. nel VI Anno
trasf_mago_ids = ['animaleus-nobodyx', 'reverto', 'reparifarge']
for tid in trasf_mago_ids:
    if tid in by_id:
        by_id[tid]['anno'] = 6
        by_id[tid]['annoLabel'] = 'VI Anno (Trasfigurazione M.A.G.O.)'

# Aggiorna Oltre il Mago nel VII Anno
oltre_ids = ['avada-kedavra', 'crucio', 'imperio', 'morsmordre']
for oid in oltre_ids:
    if oid in by_id:
        by_id[oid]['anno'] = 7
        by_id[oid]['annoLabel'] = 'VII Anno (Oltre il Mago)'
        desc = by_id[oid]['descrizione']
        if 'Oltre il Mago' not in desc:
            by_id[oid]['descrizione'] = f"Trattato nel testo di D.C.A.O. superiore Oltre il Mago (Y. I. Mortem, VII Anno). {desc}"

# Aggiungi Fiendfyre (Ardemonio) e Partis Temporus a VII Anno (Oltre il Mago)
fiendfyre_obj = {
    "id": "fiendfyre",
    "anno": 7,
    "annoLabel": "VII Anno (Oltre il Mago)",
    "nome": "Maledizione della Fiamma Mutaforma (Ardemonio / Fiendfyre)",
    "formula": "Fiendfyre",
    "ripetibile": False,
    "tipologia": "Magia Oscura Suprema / Fuoco Maledetto",
    "inDuello": True,
    "duelloNote": "Estremamente distruttivo ed illegale. Evoca colossali fiamme maledette zoomorfe (draghi, chimere, serpenti) che inseguono la vita, divorano qualsiasi barriera magica e possono distruggere anche gli Horcrux.",
    "movimento": "Vortice ascendente della bacchetta che culmina in un fendente d'aria espansivo accompagnato da un ruggito primordiale.",
    "movimentoSvg": "M 75,125 C 45,100 45,70 75,50 C 105,30 85,15 75,15 C 65,15 45,30 75,50 C 105,70 105,100 75,125 Z",
    "descrizione": "Trattata nel testo di D.C.A.O. superiore Oltre il Mago e in Maledictio (Y. I. Mortem, VII Anno). Genera un fuoco maledetto immenso e quasi inestinguibile (non cedevole ad Aguamenti o acqua normale) che assume le sembianze di gigantesche chimere, draghi e rapaci che cacciano ogni forma vivente. È una delle rarissime sostanze magiche capaci di distruggere gli Horcrux.",
    "etimologia": "Dall'inglese fiend (demone, spirito maligno) e fyre (fuoco arcaico); in italiano Ardemonio (ardere + demonio).",
    "valenza": 2,
    "sommaLettere": 56,
    "valenzaOpposta": 8,
    "maxRipetizioni": 1,
    "figuraGeometrica": "Angolo / Linea (Dualismo)",
    "noteAritmantiche": "Valenza Magica 2 (somma pitagorica 56 ridotta a 2). Valenza opposta di simmetria: 8. Figura operativa per Signo: Angolo / Linea (Dualismo). Limite di reiterazione efficace: 1 volta/e."
}

partis_obj = {
    "id": "partis-temporus",
    "anno": 7,
    "annoLabel": "VII Anno (Oltre il Mago)",
    "nome": "Incantesimo Fendi-Fiamma (Partis Temporus)",
    "formula": "Partis Temporus",
    "ripetibile": False,
    "tipologia": "Difensivo Avanzato / Controllo Elementale Magico",
    "inDuello": True,
    "duelloNote": "Utilizzabile in duello contro barriere di fuoco o colate di fuoco magico per fendere le fiamme e creare un varco sicuro di passaggio.",
    "movimento": "Fendente verticale netto dall'alto in basso con rapida separazione orizzontale a braccia aperte.",
    "movimentoSvg": "M 75,30 L 75,120 M 75,75 L 35,75 M 75,75 L 115,75",
    "descrizione": "Trattato nel testo di D.C.A.O. superiore Oltre il Mago (Y. I. Mortem, VII Anno). Formula di alta difesa contro magie ignee oscure: permette all'incantatore di aprire una breccia o un corridoio di sicurezza attraverso barriere di fuoco magico ostili (incluso l'Ardemonio parzialmente circoscritto).",
    "etimologia": "Dal latino partire (dividere, spartire) e tempus/temporis (tempo, tregua temporanea).",
    "valenza": 3,
    "sommaLettere": 66,
    "valenzaOpposta": 7,
    "maxRipetizioni": 1,
    "figuraGeometrica": "Triangolo equilatero (Unificazione)",
    "noteAritmantiche": "Valenza Magica 3 (somma pitagorica 66 ridotta a 3). Valenza opposta di simmetria: 7. Figura operativa per Signo: Triangolo equilatero (Unificazione). Limite di reiterazione efficace: 1 volta/e."
}

if "fiendfyre" not in by_id:
    spells.append(fiendfyre_obj)
    by_id["fiendfyre"] = fiendfyre_obj
else:
    by_id["fiendfyre"].update(fiendfyre_obj)

if "partis-temporus" not in by_id:
    spells.append(partis_obj)
    by_id["partis-temporus"] = partis_obj
else:
    by_id["partis-temporus"].update(partis_obj)

# Ordinamento rigoroso per anno: 1, 2, 3, 4, 5, 6, 7, poi 0 (trattati/rituali)
def sort_key(s):
    y = s['anno']
    order_val = 99 if y == 0 else y
    return (order_val, s['nome'])

spells.sort(key=sort_key)

js_content = """// spellsData.js - Archivio Completo degli Incantesimi suddiviso per Anni
// Fonti Didattiche Ufficiali:
// - Codex Arithmantiae (Zeno & Glaphira Hawstein): Liber I-V (Aritmanzia di Base e Trattati Operativi), Liber VI (Spazio e Traslazione, VI Anno), Liber VII (Rituali, Sigilli e Trappole, VII Anno)
// - Difesa Contro le Arti Oscure: Maledictio (Yashiro Isana Mortem, VI Anno), Oltre il Mago (Yashiro Isana Mortem, VII Anno)
// - Manuale di Trasfigurazione & Dispense di Incantesimi

const SPELLS_DATA = """ + json.dumps(spells, ensure_ascii=False, indent=2) + """;

if (typeof module !== "undefined" && module.exports) {
  module.exports = SPELLS_DATA;
}
"""

with open(f'{BASE_DIR}/spellsData.js', 'w', encoding='utf-8') as f:
    f.write(js_content)

print(f"Salvati {len(spells)} incantesimi in spellsData.js!")

# Calcolo statistiche
counts = {}
for s in spells:
    counts[s['anno']] = counts.get(s['anno'], 0) + 1
duel_yes = sum(1 for s in spells if s['inDuello'])
duel_no = sum(1 for s in spells if not s['inDuello'])
total = len(spells)

print(f"Statistiche: Totale={total}, Anni={counts}, Duello: SÌ={duel_yes}, NO={duel_no}")

# 2. Aggiorna index.html
with open(f'{BASE_DIR}/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Aggiorna badge eroico
html = re.sub(r'\b\d+\s+Incantesimi\s+Codificati\b', f'{total} Incantesimi Codificati', html)

# Aggiorna dropdown Anno
old_year_opts = re.compile(r'<select id="yearSelect"[\s\S]*?</select>')
new_year_opts = f'''<select id="yearSelect" class="w-full px-3 py-2.5 rounded-xl bg-slate-950/90 border border-slate-700 text-xs text-slate-200 focus:outline-none focus:border-amber-500 transition">
            <option value="ALL">Tutti gli Anni ({total})</option>
            <option value="1">I Anno — Fondamenti & Cinetica ({counts.get(1, 0)})</option>
            <option value="2">II Anno — Fatture & Inanimati ({counts.get(2, 0)})</option>
            <option value="3">III Anno — Gelo, Impatto & Locomozione ({counts.get(3, 0)})</option>
            <option value="4">IV Anno — Tattiche & Medimagia ({counts.get(4, 0)})</option>
            <option value="5">V Anno — Umana, Esplosivi & Maledizioni ({counts.get(5, 0)})</option>
            <option value="6">VI Anno — Maledictio & Liber Sextus ({counts.get(6, 0)})</option>
            <option value="7">VII Anno — Oltre il Mago & Liber Septimus ({counts.get(7, 0)})</option>
            <option value="0">Aritmanzia — Hawstein: Liber I-V & Trattati Operativi ({counts.get(0, 0)})</option>
          </select>'''
html = old_year_opts.sub(new_year_opts, html)

# Aggiorna dropdown Duello
old_duel_opts = re.compile(r'<select id="duelFilter"[\s\S]*?</select>')
new_duel_opts = f'''<select id="duelFilter" class="w-full px-3 py-2.5 rounded-xl bg-slate-950/90 border border-slate-700 text-xs text-slate-200 focus:outline-none focus:border-amber-500 transition">
            <option value="ALL">Duello: Qualsiasi ({total})</option>
            <option value="YES">⚔️ Utilizzabile in Duello: SÌ ({duel_yes})</option>
            <option value="NO">⛔ Non da Duello / Rituale: NO ({duel_no})</option>
          </select>'''
html = old_duel_opts.sub(new_duel_opts, html)

# Aggiorna resultsCountBadge
html = re.sub(r'id="resultsCountBadge"[^>]*>[\s\S]*?</span>', f'id="resultsCountBadge" class="text-amber-400 font-code font-semibold">{total} incantesimi trovati</span>', html)

# Aggiorna Quick Year Tabs
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
              VI Anno / Maledictio & Lib. VI ({counts.get(6, 0)})
            </button>
            <button data-year="7" class="year-tab px-3 py-1.5 rounded-lg text-xs font-semibold transition whitespace-nowrap bg-slate-800 text-slate-300 hover:bg-slate-700">
              VII Anno / Oltre il Mago & Lib. VII ({counts.get(7, 0)})
            </button>
            <button data-year="0" class="year-tab px-3 py-1.5 rounded-lg text-xs font-semibold transition whitespace-nowrap bg-slate-800 text-slate-300 hover:bg-slate-700">
              Aritmanzia / Liber I-V ({counts.get(0, 0)})
            </button>
          </div>'''
html = old_tabs.sub(new_tabs, html)

# Aggiorna Duel Segmented Controls
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

# 3. Costruisci il portale standalone monolitico
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

print("Rigenerato dist/portale_standalone.html e artifact portale_incantesimi.html!")
