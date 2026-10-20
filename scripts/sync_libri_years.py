# -*- coding: utf-8 -*-
import json

BASE_DIR = '/Users/andreamorachioli/.gemini/antigravity/scratch/portale-incantesimi'

# 1. Carica spellsData.js
with open(f'{BASE_DIR}/spellsData.js', 'r', encoding='utf-8') as f:
    text = f.read()

start = text.find('[')
end = text.rfind(']') + 1
spells = json.loads(text[start:end])

# Corrispondenza diretta e rigorosa dei Libri agli Anni di Studio:
# Liber I   -> I Anno (1° anno)
# Liber II  -> II Anno (2° anno)
# Liber III -> III Anno (3° anno)
# Liber IV  -> IV Anno (4° anno)
# Liber V   -> V Anno (5° anno)
# Liber VI  -> VI Anno (6° anno / Sesto Anno)
# Liber VII -> VII Anno (7° anno / Settimo Anno)

libri_and_curriculum_map = {
    # --- I ANNO (Liber I & Fondamenti) ---
    'signo': 1,               # Codex Arithmantiae: Liber I (Tracciamento fondamentale)
    'coerceo': 1,            # Codex Arithmantiae: Liber I (TLA Elemento 1 - Acqua)
    'transfiguro': 1,        # Manuale Trasfigurazione: Livello I Morfologica

    # --- II ANNO (Liber II & Controincanti) ---
    'finge': 2,              # Codex Arithmantiae: Liber II (TLA Elemento 5 - Aria)
    'muto': 2,               # Manuale Trasfigurazione: Livello II Materica
    'finite-incantatem': 2,  # D.C.A.O. / Incantesimi: Controincantesimo Generale

    # --- III ANNO (Liber III & Elementi Avanzati) ---
    'adultero': 3,           # Codex Arithmantiae: Liber III (TLA Elemento 6 - Terra)
    'plasma': 3,             # Codex Arithmantiae: Liber III (TLA Elemento 8 - Fuoco)
    'verto': 3,              # Manuale Trasfigurazione: Livello III Totale

    # --- IV ANNO (Liber IV, Marchiatura & Varchi) ---
    'phi-porta': 4,          # Codex Arithmantiae: Liber IV (Varchi Proporzionali Aurei)
    'dominum': 4,            # Difesa Statica Contenitori
    'significo': 4,          # Manuale Trasfigurazione: Marchiatura Inanimata
    'plansigno': 4,          # Manuale Trasfigurazione: Marchiatura Vegetale
    'fersigno': 4,           # Manuale Trasfigurazione: Marchiatura Viventi
    'detecto': 4,            # Manuale Trasfigurazione: Diagnostica Rifrazione

    # --- V ANNO (Liber V & Evanescenza G.U.F.O.) ---
    'phi-revelio': 5,        # Codex Arithmantiae: Liber V (Crittografia Magica Celante)
    'evanesco': 5,           # Manuale Trasfigurazione: Evanescenza Inanimati (G.U.F.O.)
    'ivanesco': 5,           # Manuale Trasfigurazione: Evanescenza Viventi (G.U.F.O.)

    # --- VI ANNO (Liber VI & Sesto Anno) ---
    'obstringo-circulum': 6, # Arcane GDR VI Anno: Teoria Trasfigurazione Circolare
    'muffliato': 6,          # Sortilegi Mezzosangue / D.C.A.O.

    # --- VII ANNO (Liber VII & Settimo Anno) ---
    'protego-totalum': 7     # Difesa Statica Superiore di Zona
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
    if s['id'] in libri_and_curriculum_map:
        s['anno'] = libri_and_curriculum_map[s['id']]
    s['annoLabel'] = roman_labels[s['anno']]

spells.sort(key=lambda x: (x['anno'], x['nome']))

# Salva spellsData.js
new_spells_data = (
    "// spellsData.js - Archivio Completo dei 154 Incantesimi suddiviso per Anni (I - VII Anno)\n"
    "// Sincronizzato con il Programma Ufficiale di Studio di Arcane GDR e Trattati Didattici (Liber I-VII)\n\n"
    f"const SPELLS_DATA = {json.dumps(spells, ensure_ascii=False, indent=2)};\n\n"
    "if (typeof module !== 'undefined' && module.exports) {\n"
    "  module.exports = SPELLS_DATA;\n"
    "}\n"
)

with open(f'{BASE_DIR}/spellsData.js', 'w', encoding='utf-8') as f:
    f.write(new_spells_data)

counts = {}
for y in range(1, 8):
    c = len([s for s in spells if s['anno'] == y])
    counts[y] = c
    print(f"  {roman_labels[y]}: {c}")

print(f"Totale Incantesimi: {len(spells)}")
