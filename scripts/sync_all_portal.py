# -*- coding: utf-8 -*-
"""
scripts/sync_all_portal.py
Sincronizza completamente:
1. app.js (statistiche, filtri dinamici per i 241 incantesimi e 25 rune)
2. index.html (macro filtri, dropdown, tab per anno e duello)
3. dist/portale_standalone.html (bundle autonomo con CSS e JS inlined)
4. docs/compendio_incantesimi.md (tavola sinottica e compendio 266 voci)
5. Artifacts portale_incantesimi.html e compendio_incantesimi.md
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
duel_yes = len([s for s in spells if s.get('inDuello') and not s.get('isRune')])
duel_no = len([s for s in spells if not s.get('inDuello') and not s.get('isRune')])

year_counts = {}
for s in spells:
    if not s.get('isRune'):
        year_counts[s['anno']] = year_counts.get(s['anno'], 0) + 1

print(f"Totale: {total_entries} (Incantesimi: {spells_count}, Rune: {runes_count})")
print(f"Per anno: {year_counts}")
print(f"Duello SÌ: {duel_yes}, Duello NO: {duel_no}")

# 1. Aggiorna app.js
with open(f'{BASE_DIR}/app.js', 'r', encoding='utf-8') as f:
    app_js = f.read()

# Aggiorna statistiche globali se presenti
app_js = re.sub(
    r'activeMacroHint\.innerHTML = `Visualizzazione: <strong class="text-amber-300">\$\{SPELLS_DATA\.filter\(s => !s\.isRune\)\.length\} Incantesimi Didattici</strong>`;',
    f'activeMacroHint.innerHTML = `Visualizzazione: <strong class="text-amber-300">{spells_count} Incantesimi Didattici</strong>`;',
    app_js
)
app_js = re.sub(
    r'activeMacroHint\.innerHTML = `Visualizzazione: <strong class="text-indigo-300">\$\{SPELLS_DATA\.filter\(s => s\.isRune\)\.length\} Antiche Rune Futhark</strong>`;',
    f'activeMacroHint.innerHTML = `Visualizzazione: <strong class="text-indigo-300">{runes_count} Antiche Rune Futhark</strong>`;',
    app_js
)

with open(f'{BASE_DIR}/app.js', 'w', encoding='utf-8') as f:
    f.write(app_js)

print("app.js sincronizzato.")

# 2. Aggiorna index.html
with open(f'{BASE_DIR}/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Aggiorna macro bottoni
html = re.sub(r'<span id="macroSpellsText">Incantesimi \([0-9]+\)</span>', f'<span id="macroSpellsText">Incantesimi ({spells_count})</span>', html)
html = re.sub(r'<span id="macroRunesText">Rune \([0-9]+\)</span>', f'<span id="macroRunesText">Rune ({runes_count})</span>', html)
html = re.sub(r'Visualizzazione: <strong class="text-amber-300">[0-9]+ Incantesimi Didattici</strong>', f'Visualizzazione: <strong class="text-amber-300">{spells_count} Incantesimi Didattici</strong>', html)

# Aggiornamento dropdown yearSelect
html = re.sub(r'<option value="ALL">Tutti gli Incantesimi \([0-9]+\)</option>', f'<option value="ALL">Tutti gli Incantesimi ({spells_count})</option>', html)
html = re.sub(r'<option value="ALL">Tutti \([0-9]+\)</option>', f'<option value="ALL">Tutti gli Incantesimi ({spells_count})</option>', html)
html = re.sub(r'<option value="1">I Anno \([0-9]+\)</option>', f'<option value="1">I Anno ({year_counts.get(1, 0)})</option>', html)
html = re.sub(r'<option value="2">II Anno \([0-9]+\)</option>', f'<option value="2">II Anno ({year_counts.get(2, 0)})</option>', html)
html = re.sub(r'<option value="3">III Anno \([0-9]+\)</option>', f'<option value="3">III Anno ({year_counts.get(3, 0)})</option>', html)
html = re.sub(r'<option value="4">IV Anno \([0-9]+\)</option>', f'<option value="4">IV Anno ({year_counts.get(4, 0)})</option>', html)
html = re.sub(r'<option value="5">V Anno \([0-9]+\)</option>', f'<option value="5">V Anno ({year_counts.get(5, 0)})</option>', html)
html = re.sub(r'<option value="6">VI Anno \([0-9]+\)</option>', f'<option value="6">VI Anno ({year_counts.get(6, 0)})</option>', html)
html = re.sub(r'<option value="7">VII Anno \([0-9]+\)</option>', f'<option value="7">VII Anno ({year_counts.get(7, 0)})</option>', html)
html = re.sub(r'<option value="0">Altri \([0-9]+\)</option>', f'<option value="0">Altri ({year_counts.get(0, 0)})</option>', html)


# Aggiornamento Year Quick Tabs
html = re.sub(r'data-year="ALL"([^>]*)>\s*Tutti \([0-9]+\)', f'data-year="ALL"\\1>\n              Tutti ({spells_count})', html)
html = re.sub(r'data-year="1"([^>]*)>\s*I Anno \([0-9]+\)', f'data-year="1"\\1>\n              I Anno ({year_counts.get(1, 0)})', html)
html = re.sub(r'data-year="2"([^>]*)>\s*II Anno \([0-9]+\)', f'data-year="2"\\1>\n              II Anno ({year_counts.get(2, 0)})', html)
html = re.sub(r'data-year="3"([^>]*)>\s*III Anno \([0-9]+\)', f'data-year="3"\\1>\n              III Anno ({year_counts.get(3, 0)})', html)
html = re.sub(r'data-year="4"([^>]*)>\s*IV Anno \([0-9]+\)', f'data-year="4"\\1>\n              IV Anno ({year_counts.get(4, 0)})', html)
html = re.sub(r'data-year="5"([^>]*)>\s*V Anno \([0-9]+\)', f'data-year="5"\\1>\n              V Anno ({year_counts.get(5, 0)})', html)
html = re.sub(r'data-year="6"([^>]*)>\s*VI Anno \([0-9]+\)', f'data-year="6"\\1>\n              VI Anno ({year_counts.get(6, 0)})', html)
html = re.sub(r'data-year="7"([^>]*)>\s*VII Anno \([0-9]+\)', f'data-year="7"\\1>\n              VII Anno ({year_counts.get(7, 0)})', html)
html = re.sub(r'data-year="0"([^>]*)>\s*Altri \([0-9]+\)', f'data-year="0"\\1>\n              Altri ({year_counts.get(0, 0)})', html)

# Aggiornamento duelSegmentedGroup
html = re.sub(r'data-duel="ALL"([^>]*)>\s*Tutti \([0-9]+\)', f'data-duel="ALL"\\1>\n                Tutti ({spells_count})', html)
html = re.sub(r'data-duel="YES"([^>]*)>\s*(?:⚔️ Da Duello: SÌ|Sì) \([0-9]+\)', f'data-duel="YES"\\1>\n                Sì ({duel_yes})', html)
html = re.sub(r'data-duel="NO"([^>]*)>\s*(?:⛔ Non da Duello: NO|No) \([0-9]+\)', f'data-duel="NO"\\1>\n                No ({duel_no})', html)

# Aggiornamento Header Stats Badges
dark_count = len([s for s in spells if not s.get('isRune') and ('Maledizione' in s.get('tipologia', '') or 'Fattura' in s.get('tipologia', ''))])
html = re.sub(r'<div id="statTotal"[^>]*>[0-9]+</div>\s*<div[^>]*>(?:Incantesimi Totali|Incantesimi)</div>', f'<div id="statTotal" class="text-2xl font-bold font-magic text-amber-400">{spells_count}</div>\n            <div class="text-[11px] uppercase tracking-wider text-slate-400 font-medium">Incantesimi</div>', html)
html = re.sub(r'<div id="statRunes"[^>]*>[0-9]+</div>\s*<div[^>]*>Antiche Rune</div>', f'<div id="statRunes" class="text-2xl font-bold font-magic text-indigo-400">{runes_count}</div>\n            <div class="text-[11px] uppercase tracking-wider text-slate-400 font-medium">Antiche Rune</div>', html)
html = re.sub(r'<div id="statDuel"[^>]*>[0-9]+</div>', f'<div id="statDuel" class="text-2xl font-bold font-magic text-emerald-400">{duel_yes}</div>', html)
html = re.sub(r'<div id="statDark"[^>]*>[0-9]+</div>', f'<div id="statDark" class="text-2xl font-bold font-magic text-rose-400">{dark_count}</div>', html)

# Results badge
html = re.sub(r'<span id="resultsCountBadge"[^>]*>[0-9]+ incantesimi trovati</span>', f'<span id="resultsCountBadge" class="text-amber-400 font-code font-semibold">{spells_count} incantesimi trovati</span>', html)

# Helper generazione singola card per pre-rendering immediato (First Paint istantaneo senza attesa JS)
def generate_card_html(spell):
    tipologia = spell.get('tipologia', '')
    is_rune = spell.get('isRune', False)
    
    # Type color badge
    type_badge_class = "bg-amber-500/10 text-amber-300 border-amber-500/30"
    if "Offensivo" in tipologia or "Schiantesimo" in tipologia:
        type_badge_class = "bg-rose-500/10 text-rose-300 border-rose-500/30"
    elif "Difensivo" in tipologia:
        type_badge_class = "bg-sky-500/10 text-sky-300 border-sky-500/30"
    elif "Maledizione" in tipologia:
        type_badge_class = "bg-purple-500/15 text-purple-300 border-purple-500/30"
    elif "Curativo" in tipologia:
        type_badge_class = "bg-emerald-500/10 text-emerald-300 border-emerald-500/30"
    elif "Elementale" in tipologia:
        type_badge_class = "bg-orange-500/10 text-orange-300 border-orange-500/30"
    elif "Trasfigurazione" in tipologia:
        type_badge_class = "bg-teal-500/10 text-teal-300 border-teal-500/30"
    elif "Rune" in tipologia or is_rune:
        type_badge_class = "bg-indigo-500/20 text-indigo-300 border-indigo-500/40"
        
    # Duel / Runic badge
    if is_rune:
        pos = spell.get("posizioneAlfabeto", "")
        duel_badge = f'<span class="inline-flex items-center gap-1 px-2.5 py-0.5 rounded-full text-[11px] font-bold bg-indigo-500/20 text-indigo-300 border border-indigo-500/40 shadow-sm"><span>ᛟ</span> Futhark: Pos. {pos}</span>'
    else:
        if spell.get('inDuello'):
            duel_badge = '<span class="inline-flex items-center gap-1 px-2.5 py-0.5 rounded-full text-[11px] font-bold bg-emerald-500/15 text-emerald-300 border border-emerald-500/30 shadow-sm"><span>⚔️</span> Duello: SÌ</span>'
        else:
            duel_badge = '<span class="inline-flex items-center gap-1 px-2.5 py-0.5 rounded-full text-[11px] font-bold bg-slate-800 text-slate-400 border border-slate-700"><span>⛔</span> Duello: NO</span>'

    tipo_short = tipologia.split('/')[0].strip() if tipologia else ''
    figura = spell.get('figuraGeometrica', '')
    figura_short = figura.split('(')[0].strip() if figura else ''

    return f'''
          <div class="glass-card rounded-2xl p-5 flex flex-col justify-between cursor-pointer group" onclick="openSpellDetails('{spell['id']}')">
            <div>
              <!-- Header info: Year & Duel -->
              <div class="flex items-center justify-between gap-2 mb-3">
                <span class="px-2.5 py-0.5 rounded-md text-xs font-semibold bg-slate-800/90 text-amber-300 border border-slate-700">
                  {spell.get('annoLabel', '')}
                </span>
                {duel_badge}
              </div>

              <!-- Spell Name -->
              <h3 class="text-lg font-bold font-magic text-slate-100 group-hover:text-amber-300 transition-colors line-clamp-1 mb-1">
                {spell.get('nome', '')}
              </h3>

              <!-- Formula Box -->
              <div class="flex items-center gap-2 mb-3">
                <span class="font-code text-xs px-2.5 py-1 rounded-lg bg-amber-500/10 border border-amber-500/25 text-amber-200 font-bold tracking-wide">
                  ⚡ {spell.get('formula', '')}
                </span>
                <span class="text-xs px-2 py-0.5 rounded border {type_badge_class} truncate max-w-[150px]">
                  {tipo_short}
                </span>
              </div>

              <!-- Description -->
              <p class="text-xs text-slate-300 line-clamp-3 leading-relaxed mb-4">
                {spell.get('descrizione', '')}
              </p>
            </div>

            <!-- Footer Arithmantic Summary -->
            <div class="border-t border-slate-800/80 pt-3 space-y-2">
              <div class="flex items-center justify-between text-xs">
                <div class="flex items-center gap-1.5">
                  <span class="text-slate-400">Valenza:</span>
                  <span class="font-code font-bold text-amber-400 bg-amber-950/60 px-1.5 py-0.5 rounded border border-amber-700/40">
                    V{spell.get('valenza', '')}
                  </span>
                  <span class="text-[11px] text-slate-400" title="Valenza opposta di simmetria">
                    (Opp. {spell.get('valenzaOpposta', '')})
                  </span>
                </div>
                <div class="text-[11px] text-sky-400 font-medium truncate max-w-[120px]" title="{figura}">
                  {figura_short}
                </div>
              </div>

              <!-- Wand Movement snippet -->
              <div class="text-[11px] text-slate-400 line-clamp-1 italic bg-slate-950/40 px-2 py-1 rounded">
                🪄 {spell.get('movimento', '')}
              </div>

              <div class="pt-1 flex items-center justify-end text-xs text-amber-400 font-semibold group-hover:translate-x-1 transition-transform">
                <span>Consulta Scheda & Gesto →</span>
              </div>
            </div>
          </div>'''

# Pre-renderizza tutte le schede iniziali degli incantesimi (escluse le rune dal default)
initial_spells = [s for s in spells if not s.get('isRune')]
cards_html = "".join(generate_card_html(s) for s in initial_spells)

# Inietta le schede in spellsGrid per rendere la lista immediatamente disponibile
grid_pattern = r'(<div id="spellsGrid"[^>]*>)[\s\S]*?(</div>\s*<!-- Empty State -->)'
html = re.sub(grid_pattern, r'\1' + cards_html + r'\n    \2', html)

with open(f'{BASE_DIR}/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print(f"index.html aggiornato con {len(initial_spells)} schede pre-renderizzate.")

# 3. Aggiorna dist/portale_standalone.html
with open(f'{BASE_DIR}/style.css', 'r', encoding='utf-8') as f:
    css_content = f.read()

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

compendium_header = f"""# Codex Arcane - Mondo Magico
*Classificazione Accademica Metodologica per Anni di Studio (Hogwarts & Arcane GDR)*

> [!NOTE]
> Il presente compendio unifica l'intero corpus magico di **{total_entries} voci catalogate ({spells_count} incantesimi pratici + {runes_count} rune dell'Antico Futhark)**, integrando le fonti didattiche ufficiali:
> - **Manuale di Studio Magico Incantesimi (Edizione 2026)** (*Yashiro Isana Mortem*): Tomi I-VII (I-VII Anno) completi di formule, gesti, etimologie e Chicche di Magia.
> - **Programma di Trasfigurazione** (*Yashiro Isana Mortem*): Principi di trasformazione inanimata, animata, umana ed evocazioni tecniche (*Avis*, *Serpensortia*, *Orchideus*, *Ebublio*, *Obscuro*, *Pulveris*, *Slugulus Eructo*).
> - **Astronomia Magica** (*Mary C. Silente & Trattato I-V Anno*): *Guidami*, *Alheia Croma*, *Apokros*, *Lux Perfluo*, *Astralis Cartae Dominium*, *Astra Invoco*, *Stellaris Revela*, *Stellaris Obscura*, *Caelus Memorium*, *Cometae Vocatum*, *Sidera Sentio*, *Orbis Caeli*, *Rituale Meteorio*.
> - **Erbologia Pratica** (*Nicholas Kelleher*): *Aguamenti*, *Herbivicus*, *Trimere*, *Protego Herbivorum*, *Repello Inimicum*, *Reparo Herbalis*, *Sistamina*.
> - **Codex Arithmantiae** (*Zeno & Glaphira Hawstein*): *Liber VI* (Spazio e Traslazione — VI Anno), *Liber VII* (Rituali, Sigilli e Trappole — VII Anno) e formule elementali/operative.
> - **Difesa Contro le Arti Oscure** (*Gellert Mortem & Yashiro Isana Mortem*): **Maledictio** (*VI Anno*), **Oltre il Mago** (*VII Anno*) e trattati anti-creature oscure (*Imposium*).
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
> La corrispondenza è rigorosamente 1:1 tra la Valenza Aritmantica dell'incantesimo (1–9) e la posizione ordinale occupata dalla runa nell'Alfabeto Runico (Posizioni 1–9):
> - **Valenza 1**: ᚠ **Fehu** (Pos. 1ª)
> - **Valenza 2**: ᚢ **Uruz** (Pos. 2ª)
> - **Valenza 3**: ᚦ **Thurisaz** (Pos. 3ª)
> - **Valenza 4**: ᚨ **Ansuz** (Pos. 4ª)
> - **Valenza 5**: ᚱ **Raido** (Pos. 5ª)
> - **Valenza 6**: ᚲ **Kenaz** (Pos. 6ª)
> - **Valenza 7**: ᚷ **Gebo** (Pos. 7ª)
> - **Valenza 8**: ᚹ **Wunjo** (Pos. 8ª)
> - **Valenza 9**: ᚺ **Hagalaz** (Pos. 9ª)

---

## 2. Tavola Generale dei {total_entries} Incantesimi e Rune

| Anno | Nome Incanto | Formula | Valenza | Opposto | Tipologia | Duello | Runa Associata |
|:---:|---|---|:---:|:---:|---|:---:|---|
""" + "\n".join(table_rows) + "\n\n"

with open(f'{BASE_DIR}/docs/compendio_incantesimi.md', 'w', encoding='utf-8') as f:
    f.write(compendium_header)

with open(f'{ARTIFACT_DIR}/compendio_incantesimi.md', 'w', encoding='utf-8') as f:
    f.write(compendium_header)

print("docs/compendio_incantesimi.md e artifact compendio_incantesimi.md aggiornati.")
