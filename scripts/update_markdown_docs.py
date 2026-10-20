# -*- coding: utf-8 -*-
"""
Rigenera docs/compendio_incantesimi.md e l'artifact compendio_incantesimi.md
garantendo la completa sincronizzazione dei 144 incantesimi,
suddivisi per anno con la specifica:
- VI Anno: Maledictio (Yashiro Isana Mortem) & Liber Sextus (Hawstein)
- VII Anno: Oltre il Mago (Yashiro Isana Mortem) & Liber Septimus (Hawstein)
"""

import json

BASE_DIR = '/Users/andreamorachioli/.gemini/antigravity/scratch/portale-incantesimi'
ARTIFACT_DIR = '/Users/andreamorachioli/.gemini/antigravity/brain/3a4f7fa7-8206-4f51-b303-aa9b9d9eaf5c'

with open(f'{BASE_DIR}/spellsData.js', 'r', encoding='utf-8') as f:
    text = f.read()

start = text.find('[')
end = text.rfind(']') + 1
spells = json.loads(text[start:end])

# Gruppi per anno
by_year = {}
for s in spells:
    y = s['anno']
    by_year.setdefault(y, []).append(s)

year_titles = {
    1: ("I ANNO — FONDAMENTI DI DIFESA, CINETICA E INCANTESIMI GENERALI", "Fondamenti didattici, disarmo, mobilità e sortilegi cardine del primo anno a Hogwarts."),
    2: ("II ANNO — FATTURE, TRASFIGURAZIONE INANIMATA E CREATURE", "Fatture di impatto, gestione delle creature magiche e trasfigurazioni su oggetti inanimati."),
    3: ("III ANNO — ELEMENTI DI GELO, IMPATTO E LOCOMOZIONE", "Magia del ghiaccio, locomozione corporea, difesa contro mollicci e orientamento tattico."),
    4: ("IV ANNO — TATTICHE DI DIFESA, DISTRUZIONE E MEDIMAGIA", "Sortilegi balistici da breccia, estrazione di elementi, rimedi medici d'urgenza ed evocazioni."),
    5: ("V ANNO — PREPARAZIONE AI G.U.F.O., ESPLOSIVI E TATTICHE AVANZATE", "Approfondimento delle maledizioni da combattimento, sortilegi esplosivi ed esami ministeriali."),
    6: ("VI ANNO — M.A.G.O. I: INCANTESIMI, TRASFIGURAZIONE, D.C.A.O. (MALEDICTIO) & LIBER SEXTUS", "Didattica ufficiale di VI Anno da 'Arcane GDR' e trattati: Incantesimi (Confundo, Deletrius, Descendo, Silencio, Rallegrante, Carpe Retractum, Obliterato), Trasfigurazione Pratica (Crinus Muto, Pullus, Densaugeo, Paperate, Piscofors, Entomorphis, Furitum, Geminio, Inflatus), D.C.A.O. (Maledictio: Titillando, Exulcero, Monstrum, Dismundo, Locomotor Mortis, Locomotor Wibbly, Dolohov, Sectumsempra, Vulnera Sanentur, Caccole, Balbutio, Flagrante, Morsmordre, Patronus, Languelingua, Infelicità Eterna, Stalker), Reparifarge e Codex Arithmantiae (Liber Sextus: Emineo, Emineo Puteus, Transatio Objecto)."),
    7: ("VII ANNO — M.A.G.O. II: INCANTESIMI, D.C.A.O. SUPERIORE (OLTRE IL MAGO), ANIMAGIA & LIBER SEPTIMUS", "Didattica ufficiale di VII Anno da 'Arcane GDR' e trattati: Incantesimi (Passaporta / Portus, Prior Incantatio, Incantesimo Proteus, Cave Inimicum, Partis Temporus, Incantesimo Fidelius, Adduco Maxima, Obliviate), D.C.A.O. Superiore (Maledizioni Senza Perdono: Avada Kedavra, Crucio, Imperio; Fiendfyre / Ardemonio, Patronus Messaggero), Trasfigurazione Teoria (Animaleus Nobodyx, Homine Reverto) e Codex Arithmantiae (Liber Septimus: Nodum Solvo, Abscondas, Fermo, In Fine Laqueo, Quae Reversa, Deminatio Gravitas, Magnes Lathos Addicis, Protegis Hoc Incantementum, Rotas Sator, Capio Memoriam)."),
    0: ("ARITMANZIA OPERATIVA: LIBER I-V & SCIENZE TRASFIGURATIVE", "Grimorio operativo dei trattati di Zeno & Glaphira Hawstein (Signo e le 9 figure, formule elementali Coerceo/Finge/Adultero/Plasma, varchi aurei Phi Porta/Phi Revelio) e Trasfigurazione sistematica di Yashiro Isana Mortem.")
}

year_order = [1, 2, 3, 4, 5, 6, 7, 0]

md = []
md.append("# Compendium Magicum: Portale della Conoscenza degli Incantesimi")
md.append("*Classificazione Accademica Metodologica per Anni di Studio (Hogwarts & Ministero della Magia)*\n")
md.append("> [!NOTE]")
md.append(f"> Il presente compendio unifica l'intero corpus magico di **{len(spells)} incantesimi catalogati**, integrando le fonti didattiche ufficiali:")
md.append("> - **Programma di Studio Arcane GDR**: Incantesimi, Trasfigurazione e Difesa Contro le Arti Oscure (*I-VII Anno*).")
md.append("> - **Codex Arithmantiae** (*Zeno & Glaphira Hawstein*): *Liber I-V* (Aritmanzia di Base), *Liber VI* (Spazio e Traslazione — VI Anno), *Liber VII* (Rituali, Sigilli e Trappole — VII Anno).")
md.append("> - **Difesa Contro le Arti Oscure** (*Yashiro Isana Mortem*): **Maledictio** (*VI Anno*) e **Oltre il Mago** (*VII Anno*).")
md.append(">\n> 🔗 **[Apri il Portale Web Interattivo Completo (154 Incantesimi)](file:///Users/andreamorachioli/.gemini/antigravity/brain/3a4f7fa7-8206-4f51-b303-aa9b9d9eaf5c/portale_incantesimi.html)** oppure visualizza il progetto in locale: **[index.html](file:///Users/andreamorachioli/.gemini/antigravity/scratch/portale-incantesimi/index.html)**.\n")
md.append("---\n## 1. Fondamenti del Calcolo Aritmantico della Valenza Magica\n")
md.append("Secondo il *Codex Arithmantiae* (Liber Primus, Cap. IV), ogni formula magica racchiude un potenziale numerico intrinseco denominato **Valenza Magica**, calcolato tramite la **Tavola Pitagorica**:\n")
md.append("| 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |")
md.append("|---|---|---|---|---|---|---|---|---|")
md.append("| A | B | C | D | E | F | G | H | I |")
md.append("| J | K | L | M | N | O | P | Q | R |")
md.append("| S | T | U | V | W | X | Y | Z |   |\n")
md.append("### Struttura in Sette Libri del Codex Arithmantiae (*Zeno & Glaphira Hawstein*):")
md.append("- **Liber I — I Fondamenti dell'Arte**: introduzione teorica, livelli d'azione (T.L.A.), valenza magica pitagorica, numeri speciali e Bridget Wenlock (il sacro numero 7).")
md.append("- **Liber II — Numero e Anima**: numerologia, aritmomanzia e onomanzia, archetipi, numero del carattere, destino, cuore e ruota di Pitagora.")
md.append("- **Liber III — Incantesimi**: incanti ripetibili e irripetibili, controincanti aritmantici, formule elementali (*Coerceo*, *Finge*, *Adultero*, *Plasma*), difese statiche di zona (*Protego Totalum*, *Muffliato*), piante elementali e incantesimo *Proteus*.")
md.append("- **Liber IV — Geometria Magica**: figure geometriche e incantesimo segnante *Signo*, quadrati magici di Agrippa e Sator, sezione aurea e varchi proporzionali (*Phi Porta*, *Phi Revelio*).")
md.append("- **Liber V — La Cabala**: sephirot, vie di saggezza ed evoluzione esoterica caldea.")
md.append("- **Liber VI — Spazio e Traslazione (VI Anno / Sesto Anno)**: pozzi comunicanti (*Emineo*, *Emineo Puteus*), smaterializzazione, passaporta (*Portus*), triangolo traslatore (*Transatio Objecto*), giratempo e memoria delle bacchette (*Prior Incantatem*).")
md.append("- **Liber VII — Rituali, Sigilli e Trappole (VII Anno / Settimo Anno)**: rituali di passaggio e iniziazione, ricordi silenti (*Capio Memoriam*), sigilli aritmantici (*Deminatio Gravitas*, *Magnes Lathos Addicis*, *Protegis Hoc Incantementum*), rottura dei sigilli (*Nodum Solvo*), trappole geometriche (*Abscondas*, *Fermo*, *In Fine Laqueo*, *Quae Reversa*).\n")
md.append("### Struttura Didattica di Difesa Contro le Arti Oscure (*Yashiro Isana Mortem*):")
md.append("- **VI Anno — Maledictio**: studio approfondito della natura delle maledizioni, indole oscura, fatture complesse (*Titillando*, *Exulcero*, *Monstrum*, *Dismundo*), famiglia delle pastoie (*Locomotor Mortis*, *Locomotor Wibbly*), Maledizione di Dolohov (*Dolohoferio*), Maledizione Dissanguante (*Sectumsempra*) e contro-canto (*Vulnera Sanentur*), Sortilegio dell'Infelicità Eterna, demone spia (*Stalker Convocatus*).")
md.append("- **VII Anno — Oltre il Mago**: studio delle forze occulte supreme e della storia oscura: Maledizioni Senza Perdono (*Avada Kedavra*, *Crucio*, *Imperio*), Evocazione del Marchio Nero (*Morsmordre*), Maledizione della Fiamma Mutaforma (*Fiendfyre* / Ardemonio) e Contro-incanto Fendi-Fiamma (*Partis Temporus*), Horcrux e metodologie di distruzione, Legilimanzia e Occlumanzia applicate.\n")
md.append("### Regole Fondamentali:")
md.append("1. **Calcolo della Valenza**: si sommano i valori numerici delle singole lettere della formula e si riduce a cifra singola (intervallo 1-9).")
md.append("2. **Principio di Ripetizione**: un incantesimo ripetibile può essere reiterato efficacemente fino a un numero massimo di volte pari alla sua valenza magica.")
md.append("3. **Valenza Opposta di Simmetria**: nei controincantesimi e nei sigilli la valenza opposta si ricava rispetto al numero cardine 5 con la formula: `Valenza Opposta = 5 - Valenza + 5`")
md.append("4. **Tavola Operativa delle Figure (Incantesimo Signo)**:")
md.append("   - **1**: Circonferenza *(Acqua / Coerceo)*")
md.append("   - **2**: Angolo *(Dualismo)*")
md.append("   - **3**: Triangolo equilatero *(Unificazione)*")
md.append("   - **4**: Quadrato *(Risoluzione / Immanenza)*")
md.append("   - **5**: Pentagono regolare *(Aria / Finge)*")
md.append("   - **6**: Esagono regolare *(Terra / Adultero)*")
md.append("   - **7**: Ettagono regolare *(Opposizione / Massima Energia)*")
md.append("   - **8**: Ottagono regolare *(Fuoco / Plasma)*")
md.append("   - **9**: Ellisse *(Reincarnazione / Dinamismo estremo)*\n")
md.append("---\n## 2. Catalogazione degli Incantesimi Suddivisa per Anni\n")

for y in year_order:
    title, desc = year_titles[y]
    curr_spells = by_year.get(y, [])
    md.append(f"### {title} ({len(curr_spells)} Formule)")
    md.append(f"*{desc}*\n")
    md.append("| Nome | Formula | Valenza | Tipologia | Duello | Movimento Bacchetta | Sintesi Effetto |")
    md.append("|---|---|:---:|---|:---:|---|---|")
    for s in curr_spells:
        nome = s['nome']
        formula = f"`{s['formula']}`"
        val = f"**{s['valenza']}** *(Opp. {s['valenzaOpposta']})*"
        tipo = s['tipologia']
        duello = "**SÌ**" if s['inDuello'] else "NO"
        mov = s['movimento'].replace('|', '/')
        eff = s['descrizione'].replace('|', '/')
        if len(eff) > 130:
            eff = eff[:127] + "..."
        md.append(f"| **{nome}** | {formula} | {val} | {tipo} | {duello} | {mov} | {eff} |")
    md.append("\n")

md.append("---\n## 3. Matrice Strategica di Duello e Regole di Trasfigurazione\n")
md.append(f"- **Incantesimi Abilitati al Duello**: {sum(1 for s in spells if s['inDuello'])} formule ad attivazione istantanea o tattica.")
md.append(f"- **Incantesimi Non da Duello / Rituali**: {sum(1 for s in spells if not s['inDuello'])} formule per uso cerimoniale, sigilli, varchi o studio d'aula.\n")
md.append("### Principi di Trasfigurazione e Leggi di Gamp")
md.append("1. **I Cinque Divieti di Gamp**: Denaro, Cibo, Vita, Informazioni, Amore non possono essere creati dal nulla.")
md.append("2. **I Cinque Parametri Fondamentali della Trasfigurazione**: Spazio (volume), Struttura (conformazione), Colore, Tonalità (dettagli e riflessi) ed Essenza (identità permanente).")
md.append("3. **Gerarchia di Trasfigurazione Inanimata**: Transfiguro (forma) -> Muto (materia) -> Verto (totale simultaneo).")
md.append("4. **Classificazione delle Evanescenze**: Evanesco (inanimati e liquidi nel Non-Essere) e Ivanesco (piante e creature viventi evocate).\n")
md.append("---\n## 4. Strumenti Integrati nel Portale Web\n")
md.append("- **Visualizzatore Vettoriale SVG**: traccia dinamica e animata in tempo reale della traiettoria di bacchetta.")
md.append("- **Calcolatore Dinamico di Valenza**: calcola all'istante somma pitagorica, valenza, valenza opposta, figura geometrica operativa ed elemento naturale per qualsiasi formula o nome inserito.")
md.append("- **Filtri di Ricerca Multidimensionale**: per anno di corso, tipologia, compatibilità al duello e valenza magica da 1 a 9.\n")
md.append("> **Accedi ai File:**")
md.append(f"> - [portale_incantesimi.html](file://{ARTIFACT_DIR}/portale_incantesimi.html) (Versione Artifact)")
md.append(f"> - [index.html](file://{BASE_DIR}/index.html) (Versione Workspace)")

full_md = "\n".join(md)

with open(f'{BASE_DIR}/docs/compendio_incantesimi.md', 'w', encoding='utf-8') as f:
    f.write(full_md)

with open(f'{ARTIFACT_DIR}/compendio_incantesimi.md', 'w', encoding='utf-8') as f:
    f.write(full_md)

print("Documento docs/compendio_incantesimi.md e artifact compendio_incantesimi.md rigenerati con successo!")
