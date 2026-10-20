# -*- coding: utf-8 -*-
"""
sync_all_portal.py
Sincronizza completamente:
1. app.js (aggiunge conteggio dinamico dei filtri per anno e duello)
2. index.html (aggiorna contatori statici e badge)
3. docs/compendio_incantesimi.md (aggiorna conteggi e tabelle per i 200 elementi)
4. dist/portale_standalone.html (rigenera file standalone completo con JS e dati inlined)
5. Artifacts nel brain directory
"""

import json
import re

BASE_DIR = '/Users/andreamorachioli/.gemini/antigravity/scratch/portale-incantesimi'
ARTIFACT_DIR = '/Users/andreamorachioli/.gemini/antigravity/brain/3a4f7fa7-8206-4f51-b303-aa9b9d9eaf5c'

# Carica dati
with open(f'{BASE_DIR}/spellsData.js', 'r', encoding='utf-8') as f:
    text = f.read()

spells = json.loads(text[text.find('['):text.rfind(']')+1])
total_entries = len(spells)
runes_count = len([s for s in spells if s.get('isRune')])
spells_count = total_entries - runes_count
duel_yes = len([s for s in spells if s.get('inDuello')])
duel_no = len([s for s in spells if not s.get('inDuello') and not s.get('isRune')])

year_counts = {}
for s in spells:
    year_counts[s['anno']] = year_counts.get(s['anno'], 0) + 1

print(f"Totale: {total_entries} (Incantesimi: {spells_count}, Rune: {runes_count})")
print(f"Per anno: {year_counts}")
print(f"Duello SÌ: {duel_yes}, Duello NO: {duel_no}")

# 1. Aggiorna app.js per conteggio dinamico
with open(f'{BASE_DIR}/app.js', 'r', encoding='utf-8') as f:
    app_js = f.read()

# Inietta updateFilterCounts se non presente
if "function updateFilterCounts()" not in app_js:
    target_needle = "    function updateStats() {"
    replacement_code = """    function updateFilterCounts() {
      const yearCounts = {};
      SPELLS_DATA.forEach(s => {
        yearCounts[s.anno] = (yearCounts[s.anno] || 0) + 1;
      });

      const yearTabLabels = {
        "ALL": `Tutti (${SPELLS_DATA.length})`,
        "1": `I Anno (${yearCounts[1] || 0})`,
        "2": `II Anno (${yearCounts[2] || 0})`,
        "3": `III Anno (${yearCounts[3] || 0})`,
        "4": `IV Anno (${yearCounts[4] || 0})`,
        "5": `V Anno (${yearCounts[5] || 0})`,
        "6": `VI Anno (${yearCounts[6] || 0})`,
        "7": `VII Anno (${yearCounts[7] || 0})`,
        "0": `Altri (${yearCounts[0] || 0})`,
        "8": `Antiche Rune (${yearCounts[8] || 0})`
      };

      yearTabs.forEach(tab => {
        const yr = tab.getAttribute("data-year");
        if (yearTabLabels[yr]) {
          tab.textContent = yearTabLabels[yr];
        }
      });

      if (yearSelect) {
        Array.from(yearSelect.options).forEach(opt => {
          const yr = opt.value;
          if (yearTabLabels[yr]) {
            opt.textContent = yearTabLabels[yr];
          }
        });
      }

      const duelYes = SPELLS_DATA.filter(s => s.inDuello).length;
      const duelNo = SPELLS_DATA.filter(s => !s.inDuello && !s.isRune).length;
      const totalSpells = SPELLS_DATA.filter(s => !s.isRune).length;
      duelSegBtns.forEach(btn => {
        const d = btn.getAttribute("data-duel");
        if (d === "ALL") btn.textContent = `Tutti (${totalSpells})`;
        if (d === "YES") btn.textContent = `⚔️ Da Duello: SÌ (${duelYes})`;
        if (d === "NO") btn.textContent = `⛔ Non da Duello: NO (${duelNo})`;
      });

      if (duelFilter) {
        Array.from(duelFilter.options).forEach(opt => {
          if (opt.value === "ALL") opt.textContent = `Duello: Qualsiasi (${totalSpells})`;
          if (opt.value === "YES") opt.textContent = `⚔️ Utilizzabile in Duello: SÌ (${duelYes})`;
          if (opt.value === "NO") opt.textContent = `⛔ Non da Duello / Rituale: NO (${duelNo})`;
        });
      }
    }

    // Update Global Statistics
    function updateStats() {
      statTotal.textContent = SPELLS_DATA.length;
      statDuel.textContent = SPELLS_DATA.filter(s => s.inDuello).length;
      statDark.textContent = SPELLS_DATA.filter(s => s.tipologia.includes("Maledizione") || s.tipologia.includes("Fattura")).length;
      statArith.textContent = SPELLS_DATA.filter(s => s.anno === 0 || s.tipologia.includes("Aritmantico") || s.tipologia.includes("Elementale") || s.tipologia.includes("Trasfigurazione") || s.tipologia.includes("Celeste") || s.tipologia.includes("Botanica")).length;
      updateFilterCounts();
    }"""
    app_js = app_js.replace(
        "    // Update Global Statistics\n    function updateStats() {\n      statTotal.textContent = SPELLS_DATA.length;\n      statDuel.textContent = SPELLS_DATA.filter(s => s.inDuello).length;\n      statDark.textContent = SPELLS_DATA.filter(s => s.tipologia.includes(\"Maledizione\") || s.tipologia.includes(\"Fattura\")).length;\n      statArith.textContent = SPELLS_DATA.filter(s => s.anno === 0 || s.tipologia.includes(\"Aritmantico\") || s.tipologia.includes(\"Elementale\") || s.tipologia.includes(\"Trasfigurazione\")).length;\n    }",
        replacement_code
    )

with open(f'{BASE_DIR}/app.js', 'w', encoding='utf-8') as f:
    f.write(app_js)

print("app.js aggiornato con logica dinamica dei filtri.")

# 2. Aggiorna index.html
with open(f'{BASE_DIR}/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Aggiornamento dropdown yearSelect
html = re.sub(r'<option value="ALL">Tutti \([0-9]+\)</option>', f'<option value="ALL">Tutti ({total_entries})</option>', html)
html = re.sub(r'<option value="1">I Anno \([0-9]+\)</option>', f'<option value="1">I Anno ({year_counts.get(1, 0)})</option>', html)
html = re.sub(r'<option value="2">II Anno \([0-9]+\)</option>', f'<option value="2">II Anno ({year_counts.get(2, 0)})</option>', html)
html = re.sub(r'<option value="3">III Anno \([0-9]+\)</option>', f'<option value="3">III Anno ({year_counts.get(3, 0)})</option>', html)
html = re.sub(r'<option value="4">IV Anno \([0-9]+\)</option>', f'<option value="4">IV Anno ({year_counts.get(4, 0)})</option>', html)
html = re.sub(r'<option value="5">V Anno \([0-9]+\)</option>', f'<option value="5">V Anno ({year_counts.get(5, 0)})</option>', html)
html = re.sub(r'<option value="6">VI Anno \([0-9]+\)</option>', f'<option value="6">VI Anno ({year_counts.get(6, 0)})</option>', html)
html = re.sub(r'<option value="7">VII Anno \([0-9]+\)</option>', f'<option value="7">VII Anno ({year_counts.get(7, 0)})</option>', html)
html = re.sub(r'<option value="0">Altri \([0-9]+\)</option>', f'<option value="0">Altri ({year_counts.get(0, 0)})</option>', html)
html = re.sub(r'<option value="8">Antiche Rune \([0-9]+\)</option>', f'<option value="8">Antiche Rune ({year_counts.get(8, 0)})</option>', html)

# Aggiornamento duelFilter
html = re.sub(r'<option value="ALL">Duello: Qualsiasi \([0-9]+\)</option>', f'<option value="ALL">Duello: Qualsiasi ({spells_count})</option>', html)
html = re.sub(r'<option value="YES">⚔️ Utilizzabile in Duello: SÌ \([0-9]+\)</option>', f'<option value="YES">⚔️ Utilizzabile in Duello: SÌ ({duel_yes})</option>', html)
html = re.sub(r'<option value="NO">⛔ Non da Duello / Rituale: NO \([0-9]+\)</option>', f'<option value="NO">⛔ Non da Duello / Rituale: NO ({duel_no})</option>', html)

# Aggiornamento Year Quick Tabs
html = re.sub(r'data-year="ALL"([^>]*)>\s*Tutti \([0-9]+\)', f'data-year="ALL"\\1>\n              Tutti ({total_entries})', html)
html = re.sub(r'data-year="1"([^>]*)>\s*I Anno \([0-9]+\)', f'data-year="1"\\1>\n              I Anno ({year_counts.get(1, 0)})', html)
html = re.sub(r'data-year="2"([^>]*)>\s*II Anno \([0-9]+\)', f'data-year="2"\\1>\n              II Anno ({year_counts.get(2, 0)})', html)
html = re.sub(r'data-year="3"([^>]*)>\s*III Anno \([0-9]+\)', f'data-year="3"\\1>\n              III Anno ({year_counts.get(3, 0)})', html)
html = re.sub(r'data-year="4"([^>]*)>\s*IV Anno \([0-9]+\)', f'data-year="4"\\1>\n              IV Anno ({year_counts.get(4, 0)})', html)
html = re.sub(r'data-year="5"([^>]*)>\s*V Anno \([0-9]+\)', f'data-year="5"\\1>\n              V Anno ({year_counts.get(5, 0)})', html)
html = re.sub(r'data-year="6"([^>]*)>\s*VI Anno \([0-9]+\)', f'data-year="6"\\1>\n              VI Anno ({year_counts.get(6, 0)})', html)
html = re.sub(r'data-year="7"([^>]*)>\s*VII Anno \([0-9]+\)', f'data-year="7"\\1>\n              VII Anno ({year_counts.get(7, 0)})', html)
html = re.sub(r'data-year="0"([^>]*)>\s*Altri \([0-9]+\)', f'data-year="0"\\1>\n              Altri ({year_counts.get(0, 0)})', html)
html = re.sub(r'data-year="8"([^>]*)>\s*Antiche Rune \([0-9]+\)', f'data-year="8"\\1>\n              Antiche Rune ({year_counts.get(8, 0)})', html)

# Aggiornamento duelSegmentedGroup
html = re.sub(r'data-duel="ALL"([^>]*)>\s*Tutti \([0-9]+\)', f'data-duel="ALL"\\1>\n                Tutti ({spells_count})', html)
html = re.sub(r'data-duel="YES"([^>]*)>\s*⚔️ Da Duello: SÌ \([0-9]+\)', f'data-duel="YES"\\1>\n                ⚔️ Da Duello: SÌ ({duel_yes})', html)
html = re.sub(r'data-duel="NO"([^>]*)>\s*⛔ Non da Duello: NO \([0-9]+\)', f'data-duel="NO"\\1>\n                ⛔ Non da Duello: NO ({duel_no})', html)

# Results badge
html = re.sub(r'<span id="resultsCountBadge"[^>]*>[0-9]+ incantesimi trovati</span>', f'<span id="resultsCountBadge" class="text-amber-400 font-code font-semibold">{total_entries} incantesimi trovati</span>', html)

with open(f'{BASE_DIR}/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("index.html aggiornato.")

# 3. Aggiorna dist/portale_standalone.html
with open(f'{BASE_DIR}/style.css', 'r', encoding='utf-8') as f:
    css_content = f.read()

# Ricarica spellsData.js e app.js aggiornati
with open(f'{BASE_DIR}/spellsData.js', 'r', encoding='utf-8') as f:
    spells_data_content = f.read()

with open(f'{BASE_DIR}/app.js', 'r', encoding='utf-8') as f:
    app_js_content = f.read()

# Creazione standalone
standalone_html = html
standalone_html = standalone_html.replace(
    '<link rel="stylesheet" href="style.css">',
    f'<style>\n{css_content}\n</style>'
)
standalone_html = standalone_html.replace(
    '<script src="spellsData.js"></script>',
    f'<script>\n{spells_data_content}\n</script>'
)
standalone_html = standalone_html.replace(
    '<script src="app.js"></script>',
    f'<script>\n{app_js_content}\n</script>'
)

with open(f'{BASE_DIR}/dist/portale_standalone.html', 'w', encoding='utf-8') as f:
    f.write(standalone_html)

with open(f'{ARTIFACT_DIR}/portale_incantesimi.html', 'w', encoding='utf-8') as f:
    f.write(standalone_html)

print("dist/portale_standalone.html e artifact portale_incantesimi.html rigenerati.")

# 4. Aggiorna docs/compendio_incantesimi.md
with open(f'{BASE_DIR}/docs/compendio_incantesimi.md', 'r', encoding='utf-8') as f:
    comp_md = f.read()

# Aggiorna intestazione e statistiche generali
comp_md = re.sub(r'179 voci catalogate \(154 incantesimi \+ 25 rune', f'{total_entries} voci catalogate ({spells_count} incantesimi + {runes_count} rune', comp_md)
comp_md = re.sub(r'181 voci catalogate \(156 incantesimi \+ 25 rune', f'{total_entries} voci catalogate ({spells_count} incantesimi + {runes_count} rune', comp_md)
comp_md = re.sub(r'\(179 Voci \(Incantesimi & Rune\)\)', f'({total_entries} Voci (Incantesimi & Rune))', comp_md)
comp_md = re.sub(r'\(181 Voci \(Incantesimi & Rune\)\)', f'({total_entries} Voci (Incantesimi & Rune))', comp_md)

# Genera sezioni o schede riepilogative per tutti i 200 elementi
table_rows = []
for s in spells:
    tipo = s.get('tipologia', '-')
    formula = s.get('formula', '-')
    val = s.get('valenza', '-')
    opp = s.get('valenzaOpposta', '-')
    nome = s.get('nome', '-')
    anno_lbl = s.get('annoLabel', '-')
    duel = "⚔️ SÌ" if s.get('inDuello') else ("ᛟ Runa" if s.get('isRune') else "⛔ NO")
    rune = s.get('runeAssociate', '-')
    table_rows.append(f"| **{anno_lbl}** | **{nome}** | `{formula}` | **{val}** | {opp} | {tipo} | {duel} | {rune} |")

compendium_header = f"""# Compendium Magicum: Portale della Conoscenza delle Nozioni Pratiche
*Classificazione Accademica Metodologica per Anni di Studio (Hogwarts & Arcane GDR)*

> [!NOTE]
> Il presente compendio unifica l'intero corpus magico di **{total_entries} voci catalogate ({spells_count} incantesimi pratici + {runes_count} rune dell'Antico Futhark)**, integrando le fonti didattiche ufficiali:
> - **Programma di Studio Arcane GDR**: Incantesimi, Trasfigurazione, Astronomia, Erbologia e Difesa Contro le Arti Oscure (*I-VII Anno*).
> - **Astronomia Magica** (*Mary C. Silente & Trattato I-V Anno*): *Guidami*, *Alheia Croma*, *Apokros*, *Lux Perfluo*, *Astralis Cartae Dominium*, *Astra Invoco*, *Stellaris Revela*, *Stellaris Obscura*, *Caelus Memorium*, *Cometae Vocatum*, *Sidera Sentio*, *Orbis Caeli*, *Rituale Meteorio*.
> - **Erbologia Pratica** (*Nicholas Kelleher*): *Aguamenti*, *Herbivicus*, *Trimere*, *Protego Herbivorum*, *Repello Inimicum*, *Reparo Herbalis*, *Sistamina*.
> - **Codex Arithmantiae** (*Zeno & Glaphira Hawstein*): *Liber VI* (Spazio e Traslazione — VI Anno), *Liber VII* (Rituali, Sigilli e Trappole — VII Anno) e formule elementali/operative.
> - **Difesa Contro le Arti Oscure** (*Yashiro Isana Mortem*): **Maledictio** (*VI Anno*) e **Oltre il Mago** (*VII Anno*).
> - **Formule Senza Anno (Altri)**: Controincanti generali, difese statiche di zona, trasfigurazione fondamentale e trattati aritmantici non vincolati ad un'annata scolastica.
>
> 🔗 **[Apri il Portale Web Interattivo Completo ({total_entries} Voci)](file:///Users/andreamorachioli/.gemini/antigravity/brain/3a4f7fa7-8206-4f51-b303-aa9b9d9eaf5c/portale_incantesimi.html)** oppure visualizza il progetto in locale: **[index.html](file:///Users/andreamorachioli/.gemini/antigravity/scratch/portale-incantesimi/index.html)**.

---
## 1. Fondamenti del Calcolo Aritmantico della Valenza Magica

Secondo il *Codex Arithmantiae* (Liber Primus, Cap. IV), ogni formula magica racchiude un potenziale numerico intrinseco denominato **Valenza Magica**, calcolato tramite la **Tavola Pitagorica**:

| 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
|---|---|---|---|---|---|---|---|---|
| A | B | C | D | E | F | G | H | I |
| J | K | L | M | N | O | P | Q | R |
| S | T | U | V | W | X | Y | Z |   |

### 1.1 Canone di Associazione Incantesimi ⟷ Alfabeto Runico
> [!IMPORTANT]
> **Regola Fondamentale di Corrispondenza**:  
> *«Le rune si associano agli incantesimi in questo modo: la valenza dell'incantesimo deve corrispondere alla posizione della runa nell'alfabeto runico.»*  
> 
> Nel Futhark Antico (24 rune articolate nei 3 Aettir di 8 glifi ciascuno, più la Runa Bianca centrale), la corrispondenza si applica direttamente sulle posizioni 1–9 e tramite riduzione teosofica su base 9 per le posizioni 10–24:
> - **Valenza 1**: ᚠ **Fehu** (Pos. 1ª), ᚾ **Nauthiz** (Pos. 10ª $\\rightarrow 1$), ᛖ **Ehwaz** (Pos. 19ª $\\rightarrow 1$)
> - **Valenza 2**: ᚢ **Uruz** (Pos. 2ª), ᛁ **Isa** (Pos. 11ª $\\rightarrow 2$), ᛗ **Mannaz** (Pos. 20ª $\\rightarrow 2$)
> - **Valenza 3**: ᚦ **Thurisaz** (Pos. 3ª), ᛃ **Jera** (Pos. 12ª $\\rightarrow 3$), ᛚ **Laguz** (Pos. 21ª $\\rightarrow 3$)
> - **Valenza 4**: ᚨ **Ansuz** (Pos. 4ª), ᛇ **Eihwaz** (Pos. 13ª $\\rightarrow 4$), ᛜ **Inguz** (Pos. 22ª $\\rightarrow 4$)
> - **Valenza 5**: ᚱ **Raido** (Pos. 5ª), ᛈ **Perthr** (Pos. 14ª $\\rightarrow 5$), ᛟ **Othila** (Pos. 23ª $\\rightarrow 5$), ○ **Runa Bianca** (Centro del Wyrd)
> - **Valenza 6**: ᚲ **Kenaz** (Pos. 6ª), ᛉ **Algiz** (Pos. 15ª $\\rightarrow 6$), ᛞ **Dagaz** (Pos. 24ª $\\rightarrow 6$)
> - **Valenza 7**: ᚷ **Gebo** (Pos. 7ª), ᛋ **Sowilo** (Pos. 16ª $\\rightarrow 7$)
> - **Valenza 8**: ᚹ **Wunjo** (Pos. 8ª), ᛏ **Teiwaz** (Pos. 17ª $\\rightarrow 8$)
> - **Valenza 9**: ᚺ **Hagalaz** (Pos. 9ª), ᛒ **Berkana** (Pos. 18ª $\\rightarrow 9$)

---

## 2. Tavola Generale dei {total_entries} Incantesimi e Rune

| Anno | Nome Incanto | Formula | Valenza | Opposto | Tipologia | Duello | Rune Associate |
|:---:|---|---|:---:|:---:|---|:---:|---|
""" + "\n".join(table_rows) + "\n\n"

with open(f'{BASE_DIR}/docs/compendio_incantesimi.md', 'w', encoding='utf-8') as f:
    f.write(compendium_header)

with open(f'{ARTIFACT_DIR}/compendio_incantesimi.md', 'w', encoding='utf-8') as f:
    f.write(compendium_header)

print("docs/compendio_incantesimi.md e artifact compendio_incantesimi.md aggiornati.")
