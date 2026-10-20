import json

with open('/Users/andreamorachioli/.gemini/antigravity/scratch/portale-incantesimi/spellsData.js', 'r', encoding='utf-8') as f:
    text = f.read()

start = text.find('const SPELLS_DATA = ') + len('const SPELLS_DATA = ')
end = text.rfind(';\n\nif (typeof')
spells = json.loads(text[start:end])

years = {
    1: 'I ANNO — FONDAMENTI DI DIFESA, INCANTESIMI GENERALI E DUELLO',
    2: 'II ANNO — FATTURE, TRASFIGURAZIONE INANIMATA, CINETICA E CREATURE',
    3: 'III ANNO — TRASFIGURAZIONE ANIMATA, GELO, IMPATTO, DISPERSIONE E LOCOMOZIONE',
    4: 'IV ANNO — EVOCAZIONI, TATTICHE AVANZATE, MEDIMAGIA E DIFESE DI ZONA',
    5: 'V ANNO — TRASFIGURAZIONE UMANA, DISTRUZIONE, FATTURE COMPLESSE E MALEDIZIONI',
    6: 'M.A.G.O. & ARTI OSCURE — MALEDIZIONI SENZA PERDONO, ANATEMI E PRATICHE CORRETTIVE',
    0: 'GRIMORIO ARITMANTICO & SCIENZE TRASFIGURATIVE (HAWSTEIN & MORTEM)'
}

lines = []
lines.append('# Compendium Magicum: Portale della Conoscenza degli Incantesimi')
lines.append('*Classificazione Accademica Metodologica per Anni di Studio (Hogwarts & Ministero della Magia)*\n')
lines.append('> [!NOTE]')
lines.append('> Il presente compendio unifica le conoscenze teorico-pratiche tratte dal **Codex Arithmantiae** (*Zeno & Glaphira Hawstein*), dal **Manuale di Difesa Contro le Arti Oscure** (*Gellert Mortem, Kaido Flarehelm*), da **Exorcismis Occultis** e **Maledictio** (*Yashiro Isana Mortem*), dal **Manuale Completo di Trasfigurazione** (*Yashiro Isana Mortem*) e dalla dispensa **Incantesimi**.')
lines.append('> ')
lines.append('> 🔗 **[Apri il Portale Web Interattivo Completo (129 Incantesimi)](file:///Users/andreamorachioli/.gemini/antigravity/brain/3a4f7fa7-8206-4f51-b303-aa9b9d9eaf5c/portale_incantesimi.html)** oppure visualizza il progetto in locale: **[index.html](file:///Users/andreamorachioli/.gemini/antigravity/scratch/portale-incantesimi/index.html)**.\n')
lines.append('---')
lines.append('## 1. Fondamenti del Calcolo Aritmantico della Valenza Magica\n')
lines.append('Secondo il *Codex Arithmantiae* (Liber Primus, Cap. IV), ogni formula magica racchiude un potenziale numerico intrinseco denominato **Valenza Magica**, calcolato tramite la **Tavola Pitagorica**:\n')
lines.append('| 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |')
lines.append('|---|---|---|---|---|---|---|---|---|')
lines.append('| A | B | C | D | E | F | G | H | I |')
lines.append('| J | K | L | M | N | O | P | Q | R |')
lines.append('| S | T | U | V | W | X | Y | Z |   |\n')
lines.append('### Regole Fondamentali:')
lines.append('1. **Calcolo della Valenza**: si sommano i valori numerici delle singole lettere della formula e si riduce a cifra singola (intervallo 1-9).')
lines.append('2. **Principio di Ripetizione**: un incantesimo ripetibile può essere reiterato efficacemente fino a un numero massimo di volte pari alla sua valenza magica (oltre tale soglia la reiterazione è vana).')
lines.append('3. **Valenza Opposta di Simmetria**: nei controincantesimi e nei sigilli la valenza opposta si ricava rispetto al numero cardine 5 con la formula: `Valenza Opposta = 5 - Valenza + 5`')
lines.append('4. **Tavola Operativa delle Figure (Incantesimo Signo)**:')
lines.append('   - **1**: Circonferenza *(Acqua / Coerceo)*')
lines.append('   - **2**: Angolo *(Dualismo)*')
lines.append('   - **3**: Triangolo equilatero *(Unificazione)*')
lines.append('   - **4**: Quadrato *(Risoluzione / Immanenza)*')
lines.append('   - **5**: Pentagono regolare *(Aria / Finge)*')
lines.append('   - **6**: Esagono regolare *(Terra / Adultero)*')
lines.append('   - **7**: Ettagono regolare *(Opposizione / Massima Energia)*')
lines.append('   - **8**: Ottagono regolare *(Fuoco / Plasma)*')
lines.append('   - **9**: Ellisse *(Reincarnazione / Dinamismo estremo)*\n')
lines.append('---')
lines.append('## 2. Catalogazione degli Incantesimi Suddivisa per Anni')

for yr, title in years.items():
    yr_spells = [s for s in spells if s['anno'] == yr]
    if not yr_spells:
        continue
    lines.append(f'\n### {title}\n')
    lines.append('| Nome | Formula | Valenza | Tipologia | Duello | Movimento Bacchetta | Sintesi Effetto |')
    lines.append('|---|---|:---:|---|:---:|---|---|')
    for s in yr_spells:
        duel_str = '**SÌ**' if s['inDuello'] else 'NO'
        formula_code = '`' + s['formula'] + '`'
        desc_clean = s['descrizione'].replace('|', '/').replace('\n', ' ')
        desc_snippet = desc_clean[:115] + '...' if len(desc_clean) > 115 else desc_clean
        mov_snippet = s['movimento'].replace('|', '/').replace('\n', ' ')
        nome_str = '**' + s['nome'] + '**'
        val_str = f"**{s['valenza']}** *(Opp. {s['valenzaOpposta']})*"
        lines.append(f"| {nome_str} | {formula_code} | {val_str} | {s['tipologia']} | {duel_str} | {mov_snippet} | {desc_snippet} |")

lines.append('\n---\n')
lines.append('## 3. Matrice Strategica di Duello e Regole di Trasfigurazione\n')
lines.append('### Principi di Trasfigurazione e Leggi di Gamp')
lines.append('1. **I Cinque Divieti di Gamp**: Denaro, Cibo, Vita, Informazioni, Amore non possono essere creati dal nulla.')
lines.append('2. **I Cinque Parametri Fondamentali della Trasfigurazione**: Spazio (volume), Struttura (conformazione), Colore, Tonalità (dettagli e riflessi) ed Essenza (identità permanente).')
lines.append('3. **Gerarchia di Trasfigurazione Inanimata**: Transfiguro (forma) -> Muto (materia) -> Verto (totale simultaneo).')
lines.append('4. **Classificazione delle Evanescenze**: Evanesco (inanimati e liquidi nel Non-Essere) e Ivanesco (piante e creature viventi evocate).\n')
lines.append('---')
lines.append('## 4. Strumenti Integrati nel Portale Web\n')
lines.append('- **Visualizzatore Vettoriale SVG**: traccia dinamica e animata in tempo reale della traiettoria di bacchetta.')
lines.append('- **Calcolatore Dinamico di Valenza**: calcola all\'istante somma pitagorica, valenza, valenza opposta, figura geometrica operativa ed elemento naturale per qualsiasi formula o nome inserito.')
lines.append('- **Filtri di Ricerca Multidimensionale**: per anno di corso, tipologia, compatibilità al duello e valenza magica da 1 a 9.\n')
lines.append('> **Accedi ai File:**')
lines.append('> - [portale_incantesimi.html](file:///Users/andreamorachioli/.gemini/antigravity/brain/3a4f7fa7-8206-4f51-b303-aa9b9d9eaf5c/portale_incantesimi.html) (Versione Artifact)')
lines.append('> - [index.html](file:///Users/andreamorachioli/.gemini/antigravity/scratch/portale-incantesimi/index.html) (Versione Workspace)')

output_text = '\n'.join(lines)
with open('/Users/andreamorachioli/.gemini/antigravity/brain/3a4f7fa7-8206-4f51-b303-aa9b9d9eaf5c/compendio_incantesimi.md', 'w', encoding='utf-8') as f:
    f.write(output_text)

print('Markdown file generated successfully without shell escapes!')
