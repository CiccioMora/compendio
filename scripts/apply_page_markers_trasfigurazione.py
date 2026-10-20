# -*- coding: utf-8 -*-
import json

BASE_DIR = '/Users/andreamorachioli/.gemini/antigravity/scratch/portale-incantesimi'

# 1. Carica spellsData.js
with open(f'{BASE_DIR}/spellsData.js', 'r', encoding='utf-8') as f:
    text = f.read()

start = text.find('[')
end = text.rfind(']') + 1
spells = json.loads(text[start:end])

# Pagina 83 del Manuale di Trasfigurazione ("INCANTESIMO DI ESTENSIONE IRRICONOSCIBILE") avvia il VI Anno
for s in spells:
    if s['id'] == 'adduco-maxima':
        s['anno'] = 6
        s['annoLabel'] = 'VI Anno'
        s['descrizione'] = (
            "Apre il programma didattico di VI Anno nel Manuale di Trasfigurazione (Pagina 83) e trattato nella teoria dei Trasporti di Incantesimi. "
            "Sofisticata distorsione dello spazio-tempo: genera una piega dimensionale interna permanente lasciando intatto il perimetro visibile esterno "
            "(es. Stanza delle Necessità o borse senza fondo)."
        )

spells.sort(key=lambda x: (x['anno'], x['nome']))

# Salva spellsData.js
new_spells_data = (
    "// spellsData.js - Archivio Completo dei 154 Incantesimi suddiviso per Anni (I - VII Anno)\n"
    "// Sincronizzato con il Programma Ufficiale di Studio di Arcane GDR, Codex Arithmantiae e Manuali Docenti\n\n"
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
    print(f"  Anno {y}: {c}")

print(f"Totale Incantesimi: {len(spells)}")
