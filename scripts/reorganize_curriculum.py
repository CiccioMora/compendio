# -*- coding: utf-8 -*-
import json
import re

BASE_DIR = '/Users/andreamorachioli/.gemini/antigravity/scratch/portale-incantesimi'

# 1. Carica spellsData.js
with open(f'{BASE_DIR}/spellsData.js', 'r', encoding='utf-8') as f:
    text = f.read()

start = text.find('[')
end = text.rfind(']') + 1
spells = json.loads(text[start:end])

# Mappatura esplicita per i 21 incantesimi precedentemente in anno 0
year_map = {
    'transfiguro': 1,
    'muto': 2,
    'finite-incantatem': 2,
    'verto': 3,
    'signo': 3,
    'coerceo': 3,
    'finge': 3,
    'adultero': 4,
    'plasma': 4,
    'dominum': 4,
    'significo': 4,
    'plansigno': 4,
    'fersigno': 4,
    'detecto': 4,
    'phi-porta': 5,
    'phi-revelio': 5,
    'evanesco': 5,
    'ivanesco': 5,
    'obstringo-circulum': 6,
    'muffliato': 6,
    'protego-totalum': 7
}

roman_labels = {
    1: 'I Anno',
    2: 'II Anno',
    3: 'III Anno',
    4: 'IV Anno',
    5: 'V Anno',
    6: 'VI Anno',
    7: 'VII Anno'
}

for s in spells:
    if s['id'] in year_map:
        s['anno'] = year_map[s['id']]
    # Normalizza annoLabel per tutti gli incantesimi a formato pulito ed esplicito
    s['annoLabel'] = roman_labels[s['anno']]

# Ordina gli incantesimi per anno e poi per nome
spells.sort(key=lambda x: (x['anno'], x['nome']))

# Riscrivi spellsData.js
new_spells_data = (
    "// spellsData.js - Archivio Completo dei 154 Incantesimi suddiviso per Anni (I - VII Anno)\n"
    "// Sincronizzato con il Programma Ufficiale di Studio di Arcane GDR e Trattati Didattici\n\n"
    f"const SPELLS_DATA = {json.dumps(spells, ensure_ascii=False, indent=2)};\n\n"
    "if (typeof module !== 'undefined' && module.exports) {\n"
    "  module.exports = SPELLS_DATA;\n"
    "}\n"
)

with open(f'{BASE_DIR}/spellsData.js', 'w', encoding='utf-8') as f:
    f.write(new_spells_data)

print(f"spellsData.js aggiornato: {len(spells)} incantesimi.")
for y in range(1, 8):
    cnt = len([s for s in spells if s['anno'] == y])
    print(f"  {roman_labels[y]}: {cnt}")
