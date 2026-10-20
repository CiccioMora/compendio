# -*- coding: utf-8 -*-
"""
apply_altri_filter.py
Aggiorna spellsData.js impostando anno: 0 e annoLabel: "Altri" per i 21 incantesimi
senza riferimento legato all'anno accademico (formule generali, elementali, zone,
aritmanzia fondamentale e trasfigurazione di base).
Aggiorna index.html, dist/portale_standalone.html, gli artifact e la documentazione.
"""

import json
import re

BASE_DIR = '/Users/andreamorachioli/.gemini/antigravity/scratch/portale-incantesimi'
ARTIFACT_DIR = '/Users/andreamorachioli/.gemini/antigravity/brain/3a4f7fa7-8206-4f51-b303-aa9b9d9eaf5c'

# 1. Carica spellsData.js
with open(f'{BASE_DIR}/spellsData.js', 'r', encoding='utf-8') as f:
    text = f.read()

start = text.find('[')
end = text.rfind(']') + 1
spells = json.loads(text[start:end])

# I 21 incantesimi privi di anno di corso curricolare specifico
altri_spells = {
    "finite-incantatem", "plasma", "coerceo", "finge", "adultero",
    "dominum", "muffliato", "phi-revelio", "phi-porta", "signo",
    "evanesco", "ivanesco", "detecto", "fersigno", "plansigno",
    "significo", "protego-totalum", "obstringo-circulum", "muto",
    "transfiguro", "verto"
}

roman_labels = {
    0: "Altri",
    1: "I Anno",
    2: "II Anno",
    3: "III Anno",
    4: "IV Anno",
    5: "V Anno",
    6: "VI Anno",
    7: "VII Anno"
}

for s in spells:
    if s['id'] in altri_spells:
        s['anno'] = 0
        s['annoLabel'] = "Altri"
    else:
        s['annoLabel'] = roman_labels[s['anno']]

# Ordina: Anni 1-7 in sequenza, poi Altri (0) in coda, ordinati per nome
spells.sort(key=lambda x: (x['anno'] if x['anno'] > 0 else 99, x['nome']))

# Conteggi per anno
counts = {}
for s in spells:
    counts[s['anno']] = counts.get(s['anno'], 0) + 1

print("Conteggio incantesimi per categoria d'Anno:")
for y in [1, 2, 3, 4, 5, 6, 7, 0]:
    print(f"  {roman_labels[y]}: {counts.get(y, 0)}")
print(f"Totale: {len(spells)}")

# Scrivi spellsData.js
js_code = (
    "// spellsData.js - Archivio Completo dei 154 Incantesimi suddiviso per Anni (I - VII Anno e Altri)\n"
    "// Sincronizzato con il Programma Ufficiale di Studio di Arcane GDR, Trattati Didattici e Codex Arithmantiae\n\n"
    f"const SPELLS_DATA = {json.dumps(spells, ensure_ascii=False, indent=2)};\n\n"
    "if (typeof module !== 'undefined' && module.exports) {\n"
    "  module.exports = SPELLS_DATA;\n"
    "}\n"
)

with open(f'{BASE_DIR}/spellsData.js', 'w', encoding='utf-8') as f:
    f.write(js_code)
print("Salvato spellsData.js!")

# 2. Aggiorna index.html
with open(f'{BASE_DIR}/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Aggiorna select id="yearSelect"
new_year_select = f'''<select id="yearSelect" class="w-full px-3 py-2.5 rounded-xl bg-slate-950/90 border border-slate-700 text-xs text-slate-200 focus:outline-none focus:border-amber-500 transition">
            <option value="ALL">Tutti gli Anni ({len(spells)})</option>
            <option value="1">I Anno — Fondamenti & Cinetica ({counts.get(1, 0)})</option>
            <option value="2">II Anno — Fatture & Inanimati ({counts.get(2, 0)})</option>
            <option value="3">III Anno — Gelo & Locomozione ({counts.get(3, 0)})</option>
            <option value="4">IV Anno — Tattiche & Medimagia ({counts.get(4, 0)})</option>
            <option value="5">V Anno — Esplosivi & G.U.F.O. ({counts.get(5, 0)})</option>
            <option value="6">VI Anno — Sesto Anno: Maledizioni, Trasfigurazione & Incantesimi ({counts.get(6, 0)})</option>
            <option value="7">VII Anno — Settimo Anno: Incantesimi Superiori, Difesa & Arti Oscure ({counts.get(7, 0)})</option>
            <option value="0">Altri — Formule Senza Riferimento d\'Anno ({counts.get(0, 0)})</option>
          </select>'''

html = re.sub(
    r'<select id="yearSelect"[\s\S]*?</select>',
    new_year_select,
    html
)

# Aggiorna yearTabsContainer
new_year_tabs = f'''<div class="flex items-center gap-1.5 overflow-x-auto pb-1.5 scrollbar-none" id="yearTabsContainer">
            <button data-year="ALL" class="year-tab px-3 py-1.5 rounded-lg text-xs font-semibold transition whitespace-nowrap bg-amber-500 text-slate-950 shadow-md">
              Tutti ({len(spells)})
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
              Altri ({counts.get(0, 0)})
            </button>
          </div>'''

html = re.sub(
    r'<div class="flex items-center gap-1\.5 overflow-x-auto pb-1\.5 scrollbar-none" id="yearTabsContainer">[\s\S]*?</div>',
    new_year_tabs,
    html
)

with open(f'{BASE_DIR}/index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Salvato index.html!")

# 3. Genera dist/portale_standalone.html e artifact portale_incantesimi.html
with open(f'{BASE_DIR}/style.css', 'r', encoding='utf-8') as f:
    css_content = f.read()

with open(f'{BASE_DIR}/app.js', 'r', encoding='utf-8') as f:
    app_js = f.read()

standalone = html
standalone = standalone.replace('<link rel="stylesheet" href="style.css">', f'<style>\n{css_content}\n</style>')
standalone = standalone.replace('<script src="spellsData.js"></script>', f'<script>\n{js_code}\n</script>')
standalone = standalone.replace('<script src="app.js"></script>', f'<script>\n{app_js}\n</script>')

with open(f'{BASE_DIR}/dist/portale_standalone.html', 'w', encoding='utf-8') as f:
    f.write(standalone)

with open(f'{ARTIFACT_DIR}/portale_incantesimi.html', 'w', encoding='utf-8') as f:
    f.write(standalone)
print("Rigenerati dist/portale_standalone.html e artifact portale_incantesimi.html!")
