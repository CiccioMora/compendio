# -*- coding: utf-8 -*-
"""
scripts/fix_rune_association.py
Aggiorna la corrispondenza delle Rune dell'Alfabeto per tutti gli incantesimi e per le rune.
Canone: la valenza dell'incantesimo (1..9) corrisponde esclusivamente alla singola runa
che occupa quella precisa posizione nell'alfabeto runico (Posizioni 1..9).
Nessuna estensione modulare alle rune successive (10..24).
"""

import json
import re

BASE_DIR = '/Users/andreamorachioli/.gemini/antigravity/scratch/portale-incantesimi'
ARTIFACT_DIR = '/Users/andreamorachioli/.gemini/antigravity/brain/3a4f7fa7-8206-4f51-b303-aa9b9d9eaf5c'

VALENCE_RUNES_MAP = {
    1: "ᚠ Fehu (Pos. 1ª)",
    2: "ᚢ Uruz (Pos. 2ª)",
    3: "ᚦ Thurisaz (Pos. 3ª)",
    4: "ᚨ Ansuz (Pos. 4ª)",
    5: "ᚱ Raido (Pos. 5ª)",
    6: "ᚲ Kenaz (Pos. 6ª)",
    7: "ᚷ Gebo (Pos. 7ª)",
    8: "ᚹ Wunjo (Pos. 8ª)",
    9: "ᚺ Hagalaz (Pos. 9ª)"
}

# 1. Carica spellsData.js
with open(f'{BASE_DIR}/spellsData.js', 'r', encoding='utf-8') as f:
    text = f.read()

start_idx = text.find('[')
end_idx = text.rfind(']') + 1
spells = json.loads(text[start_idx:end_idx])

# Calcola incantesimi per valenza
spells_by_valence = {}
for s in spells:
    if not s.get('isRune'):
        v = s.get('valenza')
        spells_by_valence.setdefault(v, []).append(s.get('formula') or s.get('nome'))

# Aggiorna incantesimi
spells_updated = 0
runes_updated = 0

for s in spells:
    if not s.get('isRune'):
        val = s.get('valenza')
        s['runeAssociate'] = VALENCE_RUNES_MAP.get(val, "ᚠ Fehu (Pos. 1ª)")
        spells_updated += 1
    else:
        # È una voce di runa
        pos = s.get('posizioneNum')
        if pos and pos in VALENCE_RUNES_MAP:
            s['runeAssociate'] = VALENCE_RUNES_MAP[pos]
            sample_spells = spells_by_valence.get(pos, [])[:5]
            total_v_spells = len(spells_by_valence.get(pos, []))
            s['incantesimiAssociati'] = f"Valenza {pos} ({total_v_spells} incantesimi didattici, es. {', '.join(sample_spells)})"
        else:
            s['runeAssociate'] = f"{s.get('formula', s.get('nome'))} (Pos. {s.get('posizioneAlfabeto', '-')})"
            s['incantesimiAssociati'] = "Nessuno (Posizione alfabetica oltre le 9 valenze degli incantesimi didattici)"
        runes_updated += 1

# Riscrivi spellsData.js
new_spells_data_content = f"""// spellsData.js - Archivio Completo dei {len(spells)} Incantesimi e Rune dell'Antico Futhark
// Sincronizzato con il Programma Ufficiale di Studio di Arcane GDR, Trattati Didattici, Astronomia, Erbologia e Codex Arithmantiae

const SPELLS_DATA = {json.dumps(spells, ensure_ascii=False, indent=2)};
"""

with open(f'{BASE_DIR}/spellsData.js', 'w', encoding='utf-8') as f:
    f.write(new_spells_data_content)

print(f"spellsData.js aggiornato: {spells_updated} incantesimi e {runes_updated} rune.")

# 2. Aggiorna app.js
with open(f'{BASE_DIR}/app.js', 'r', encoding='utf-8') as f:
    app_js = f.read()

# Aggiorna label modale: "Rune dell'Alfabeto Associate:" -> "Runa dell'Alfabeto Associata:"
app_js = app_js.replace(
    '<strong>Rune dell\'Alfabeto Associate:</strong>',
    '<strong>Runa dell\'Alfabeto Associata:</strong>'
)

# Aggiorna VALENCE_RUNES_MAP in app.js
old_map_pattern = r'const VALENCE_RUNES_MAP = \{[\s\S]*?1: "ᚠ Fehu \(Pos\. 1ª\)[^}]*?\};'
new_map_code = """const VALENCE_RUNES_MAP = {
      1: "ᚠ Fehu (Pos. 1ª)",
      2: "ᚢ Uruz (Pos. 2ª)",
      3: "ᚦ Thurisaz (Pos. 3ª)",
      4: "ᚨ Ansuz (Pos. 4ª)",
      5: "ᚱ Raido (Pos. 5ª)",
      6: "ᚲ Kenaz (Pos. 6ª)",
      7: "ᚷ Gebo (Pos. 7ª)",
      8: "ᚹ Wunjo (Pos. 8ª)",
      9: "ᚺ Hagalaz (Pos. 9ª)"
    };"""

app_js = re.sub(old_map_pattern, new_map_code, app_js)

with open(f'{BASE_DIR}/app.js', 'w', encoding='utf-8') as f:
    f.write(app_js)

print("app.js aggiornato.")

# 3. Aggiorna index.html
with open(f'{BASE_DIR}/index.html', 'r', encoding='utf-8') as f:
    index_html = f.read()

index_html = index_html.replace(
    '<span class="text-slate-400">Rune Futhark (Valenza = Posizione):</span>',
    '<span class="text-slate-400">Runa Futhark (Valenza = Posizione):</span>'
)

with open(f'{BASE_DIR}/index.html', 'w', encoding='utf-8') as f:
    f.write(index_html)

print("index.html aggiornato.")

# 4. Aggiorna scripts/sync_all_portal.py per intestazione e tabella
with open(f'{BASE_DIR}/scripts/sync_all_portal.py', 'r', encoding='utf-8') as f:
    sync_py = f.read()

# Sostituisci tabella header e descrizione canone
sync_py = re.sub(
    r'\| Anno \| Nome Incanto \| Formula \| Valenza \| Opposto \| Tipologia \| Duello \| Rune Associate \|',
    '| Anno | Nome Incanto | Formula | Valenza | Opposto | Tipologia | Duello | Runa Associata |',
    sync_py
)

old_canon_block = r"""> Nel Futhark Antico \(24 rune articolate nei 3 Aettir di 8 glifi ciascuno, più la Runa Bianca centrale\), la corrispondenza si applica direttamente sulle posizioni 1–9 e tramite riduzione teosofica su base 9 per le posizioni 10–24:
> - \*\*Valenza 1\*\*: ᚠ \*\*Fehu\*\* \(Pos\. 1ª\), ᚾ \*\*Nauthiz\*\* \(Pos\. 10ª \$\\rightarrow 1\$\), ᛖ \*\*Ehwaz\*\* \(Pos\. 19ª \$\\rightarrow 1\$\)
> - \*\*Valenza 2\*\*: ᚢ \*\*Uruz\*\* \(Pos\. 2ª\), ᛁ \*\*Isa\*\* \(Pos\. 11ª \$\\rightarrow 2\$\), ᛗ \*\*Mannaz\*\* \(Pos\. 20ª \$\\rightarrow 2\$\)
> - \*\*Valenza 3\*\*: ᚦ \*\*Thurisaz\*\* \(Pos\. 3ª\), ᛃ \*\*Jera\*\* \(Pos\. 12ª \$\\rightarrow 3\$\), ᛚ \*\*Laguz\*\* \(Pos\. 21ª \$\\rightarrow 3\$\)
> - \*\*Valenza 4\*\*: ᚨ \*\*Ansuz\*\* \(Pos\. 4ª\), ᛇ \*\*Eihwaz\*\* \(Pos\. 13ª \$\\rightarrow 4\$\), ᛜ \*\*Inguz\*\* \(Pos\. 22ª \$\\rightarrow 4\$\)
> - \*\*Valenza 5\*\*: ᚱ \*\*Raido\*\* \(Pos\. 5ª\), ᛈ \*\*Perthr\*\* \(Pos\. 14ª \$\\rightarrow 5\$\), ᛟ \*\*Othila\*\* \(Pos\. 23ª \$\\rightarrow 5\$\), ○ \*\*Runa Bianca\*\* \(Centro del Wyrd\)
> - \*\*Valenza 6\*\*: ᚲ \*\*Kenaz\*\* \(Pos\. 6ª\), ᛉ \*\*Algiz\*\* \(Pos\. 15ª \$\\rightarrow 6\$\), ᛞ \*\*Dagaz\*\* \(Pos\. 24ª \$\\rightarrow 6\$\)
> - \*\*Valenza 7\*\*: ᚷ \*\*Gebo\*\* \(Pos\. 7ª\), ᛋ \*\*Sowilo\*\* \(Pos\. 16ª \$\\rightarrow 7\$\)
> - \*\*Valenza 8\*\*: ᚹ \*\*Wunjo\*\* \(Pos\. 8ª\), ᛏ \*\*Teiwaz\*\* \(Pos\. 17ª \$\\rightarrow 8\$\)
> - \*\*Valenza 9\*\*: ᚺ \*\*Hagalaz\*\* \(Pos\. 9ª\), ᛒ \*\*Berkana\*\* \(Pos\. 18ª \$\\rightarrow 9\$\)"""

new_canon_block = """> La corrispondenza è rigorosamente 1:1 tra la Valenza Aritmantica dell'incantesimo (1–9) e la posizione ordinale occupata dalla runa nell'Alfabeto Runico (Posizioni 1–9):
> - **Valenza 1**: ᚠ **Fehu** (Pos. 1ª)
> - **Valenza 2**: ᚢ **Uruz** (Pos. 2ª)
> - **Valenza 3**: ᚦ **Thurisaz** (Pos. 3ª)
> - **Valenza 4**: ᚨ **Ansuz** (Pos. 4ª)
> - **Valenza 5**: ᚱ **Raido** (Pos. 5ª)
> - **Valenza 6**: ᚲ **Kenaz** (Pos. 6ª)
> - **Valenza 7**: ᚷ **Gebo** (Pos. 7ª)
> - **Valenza 8**: ᚹ **Wunjo** (Pos. 8ª)
> - **Valenza 9**: ᚺ **Hagalaz** (Pos. 9ª)"""

sync_py = re.sub(old_canon_block, new_canon_block, sync_py)

with open(f'{BASE_DIR}/scripts/sync_all_portal.py', 'w', encoding='utf-8') as f:
    f.write(sync_py)

print("scripts/sync_all_portal.py aggiornato.")

# 5. Aggiorna gli script helper
for helper in ['scripts/integrate_runes_database.py', 'scripts/integrate_missing_manual_spells.py', 'scripts/sync_trasfigurazione_curriculum.py']:
    path = f'{BASE_DIR}/{helper}'
    try:
        with open(path, 'r', encoding='utf-8') as f:
            c = f.read()
        c = re.sub(r'VALENCE_TO_RUNES = \{[\s\S]*?1: "ᚠ Fehu \(Pos\. 1ª\)[^}]*?\}', 'VALENCE_TO_RUNES = ' + json.dumps(VALENCE_RUNES_MAP, ensure_ascii=False, indent=4), c)
        c = re.sub(r'VALENCE_RUNES_MAP = \{[\s\S]*?1: "ᚠ Fehu \(Pos\. 1ª\)[^}]*?\}', 'VALENCE_RUNES_MAP = ' + json.dumps(VALENCE_RUNES_MAP, ensure_ascii=False, indent=4), c)
        c = c.replace('<strong>Rune dell\'Alfabeto Associate:</strong>', '<strong>Runa dell\'Alfabeto Associata:</strong>')
        with open(path, 'w', encoding='utf-8') as f:
            f.write(c)
        print(f"{helper} aggiornato.")
    except Exception as e:
        print(f"Errore su {helper}: {e}")

print("Tutti i file sorgente sono stati preparati.")
