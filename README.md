# 🪄 Compendium Magicum — Portale della Conoscenza degli Incantesimi

[![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)](https://developer.mozilla.org/it/docs/Web/HTML)
[![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)](https://developer.mozilla.org/it/docs/Web/JavaScript)
[![Tailwind CSS](https://img.shields.io/badge/Tailwind_CSS-38B2AC?style=for-the-badge&logo=tailwind-css&logoColor=white)](https://tailwindcss.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-amber.svg?style=for-the-badge)](LICENSE)
[![Incantesimi](https://img.shields.io/badge/Incantesimi_Catalogati-144-blueviolet?style=for-the-badge)](#)

> **Portale Web interattivo e compendio accademico completo che suddivide e cataloga la conoscenza degli incantesimi per anni di studio (I-VII Anno, M.A.G.O., trattati di D.C.A.O. e Codex Arithmantiae).**
>
> Ogni scheda include: **Nome**, **Formula**, **Valenza Magica Pitagorica (1-9)**, **Valenza Opposta di Simmetria**, **Movimento della Bacchetta (con animazione vettoriale SVG)**, **Tipologia Magica**, **Idoneità ed Utilizzo in Duello** (con tattiche dedicate) ed **Etimologia**.

---

## 🌟 Caratteristiche Principali

- **📅 Suddivisione Accademica per Anni di Corso**:
  - **I Anno** (16 incantesimi): *Fondamenti di Difesa, Cinetica e Incantesimi Generali (Flipendo, Expelliarmus, Wingardium Leviosa, Lumos, Diffindo...)*
  - **II Anno** (14 incantesimi): *Fatture, Trasfigurazione Inanimata e Creature (Rictusempra, Tarantallegra, Engorgio, Reducio, Arania Exumai...)*
  - **III Anno** (16 incantesimi): *Elementi di Gelo, Impatto e Locomozione (Glacius, Carpe Retractum, Riddikulus, Ascendio, Immobulus...)*
  - **IV Anno** (20 incantesimi): *Tattiche di Difesa, Distruzione e Medimagia (Bombarda, Stupeficium Avanzato, Aguamenti, Episkey, Avis, Oppugno...)*
  - **V Anno** (22 incantesimi): *Preparazione ai G.U.F.O., Esplosivi e Maledizioni Comuni (Confringo, Expecto Patronum, Languelingua, Reducto, Furunculus, Densaugeo...)*
  - **VI Anno — D.C.A.O.: Maledictio & Aritmanzia: Liber Sextus** (19 incantesimi):
    - *D.C.A.O. ("Maledictio" - Y. I. Mortem)*: Titillando, Exulcero, Monstrum, Dismundo, Locomotor Mortis, Locomotor Wibbly, Maledizione di Dolohov (*Dolohoferio*), Maledizione Dissanguante (*Sectumsempra*), Canto Curativo (*Vulnera Sanentur*), Sortilegio dell'Infelicità Eterna, Demone Stalker (*Stalker Convocatus*).
    - *Aritmanzia ("Codex Arithmantiae: Liber Sextus - Spazio e Traslazione" - Z. & G. Hawstein)*: Emineo, Emineo Puteus, Portus, Transatio Objecto, Prior Incantatem.
    - *Trasfigurazione M.A.G.O.*: Animaleus Nobodyx, Reverto, Reparifarge.
  - **VII Anno — D.C.A.O. Superiore: Oltre il Mago & Aritmanzia: Liber Septimus** (16 incantesimi):
    - *D.C.A.O. Superiore ("Oltre il Mago" - Y. I. Mortem)*: Anatema che Uccide (*Avada Kedavra*), Maledizione Cruciatus (*Crucio*), Maledizione Imperius (*Imperio*), Evocazione del Marchio Nero (*Morsmordre*), Maledizione della Fiamma Mutaforma (*Fiendfyre* / Ardemonio), Incantesimo Fendi-Fiamma (*Partis Temporus*).
    - *Aritmanzia ("Codex Arithmantiae: Liber Septimus - Rituali, Sigilli e Trappole" - Z. & G. Hawstein)*: Nodum Solvo, Abscondas, Fermo, In Fine Laqueo, Quae Reversa, Deminatio Gravitas, Magnes Lathos Addicis, Protegis Hoc Incantementum, Rotas Sator, Capio Memoriam.
  - **Grimorio Aritmantico Operativo (Liber I-V & Trattati)** (21 formule): *Trattati operativi di Zeno & Glaphira Hawstein: Signo e le 9 Figure Geometriche, Coerceo, Plasma, Finge, Adultero, Phi Porta, Phi Revelio, Sigilli di Controvalenza e Trasfigurazione Metodica.*

- **⚔️ Filtro e Valutazione Tattica per il Duello Magico**:
  - **93 Incantesimi Abilitati al Duello**: catalogati con finestra di lancio rapido, tempo di caricamento verbale/non verbale e contromisure.
  - **51 Incantesimi Non da Duello**: formule di utilità domestica, riparazione, scasso (*Alohomora*), sigilli lenti (*Colloportus*), pozzi comunicanti o trasfigurazioni complesse d'aula.
  - Segmented buttons e commutatore rapido *"Solo Duello"* nella barra di navigazione.
  - Segmented buttons e commutatore rapido *"Solo Duello"* nella barra di navigazione.

- **🔍 Ricerca Testuale Full-Text in Tempo Reale**:
  - Filtro dinamico istantaneo su **Nome**, **Formula**, **Testo della Descrizione** e **Gesto della bacchetta**.
  - Evidenziazione visiva automatica (`<mark>`) dei termini cercati.

- **📐 Valenza Magica e Principi del Codex Arithmantiae**:
  - Calcolo della valenza magica tramite **Tavola Pitagorica** (riduzione $1-9$).
  - **Valenza Opposta di Simmetria col 5** per i controincantesimi ($\text{Valenza Opposta} = 5 - \text{Valenza} + 5$).
  - **Regola di Reiterazione**: numero massimo di lanci ripetibili consecutivi prima della saturazione o dispersione magica.
  - Tavola delle figure geometriche per l'incantesimo *Signo* (cerchio, angolo, triangolo, quadrato, pentagono, esagono, ettagono, ottagono, ellisse).

- **🪄 Gesto della Bacchetta con Animazione SVG**:
  - Ogni incantesimo dispone della riproduzione vettoriale animata del tracciato gestuale con pulsante per riavviare l'animazione.

- **🧮 Calcolatore Aritmantico Interattivo Integrato**:
  - Modale integrata per inserire qualsiasi parola o formula magica e calcolarne in tempo reale: lettere normalizzate, somma pitagorica, valenza ridotta, opposto di simmetria, figura geometrica ed elemento associato.

---

## 🗂️ Struttura del Progetto

```text
portale-incantesimi/
├── index.html              # Entrypoint dell'applicazione web (compatibile GitHub Pages)
├── spellsData.js           # Database completo dei 144 incantesimi strutturato in JSON/JS
├── app.js                  # Logica applicativa, gestione filtri, ricerca e modali
├── style.css               # Regole grafiche avanzate, font magici e animazioni SVG
├── dist/
│   └── portale_standalone.html  # Versione monolitica a singolo file (apribile offline senza server)
├── docs/
│   └── compendio_incantesimi.md # Trattato accademico completo in Markdown
├── scripts/                # Script di compilazione e validazione dei dati
│   ├── generate_data.py
│   ├── build_full_database.py
│   └── update_portal_ui.py
├── LICENSE                 # Licenza MIT
└── README.md               # Documentazione del repository
```

---

## 🚀 Come Pubblicare su GitHub e GitHub Pages

### 1. Inizializzare il Repository Git Locale

Apri il terminale nella cartella del progetto ed esegui:

```bash
cd /Users/andreamorachioli/.gemini/antigravity/scratch/portale-incantesimi

# Inizializza il repository
git init

# Aggiungi tutti i file
git add .

# Crea il primo commit
git commit -m "feat: rilascio iniziale del portale della conoscenza degli incantesimi"
```

### 2. Collegare il Repository Remoto su GitHub

1. Vai su [GitHub](https://github.com/new) e crea un nuovo repository pubblico (es. `portale-incantesimi`).
2. Collega il repository remoto e carica il codice:

```bash
# Imposta il branch principale su main
git branch -M main

# Aggiungi l'origine remota (sostituisci con il tuo username GitHub)
git remote add origin https://github.com/CiccioMora/compendio.git
git push -u origin main
```

### 3. Attivare GitHub Pages (Sito Web Online Gratis)

1. Nel tuo repository su GitHub, vai su **Settings** > **Pages** (nel menu laterale sinistro).
2. Sotto **Build and deployment** > **Branch**:
   - Seleziona il branch: `main`
   - Seleziona la cartella: `/ (root)`
3. Clicca su **Save**.
4. Dopo circa 1-2 minuti, il tuo portale sarà accessibile pubblicamente all'indirizzo:
   👉 **`https://CiccioMora.github.io/compendio/`**

---

## 💻 Utilizzo in Locale

Non è richiesto alcun ambiente Node o build step:
1. Clona il repository:
   ```bash
   git clone https://github.com/CiccioMora/compendio.git
   cd compendio
   ```
2. Fai doppio clic su `index.html` per aprirlo direttamente in qualsiasi browser (Google Chrome, Firefox, Safari, Edge).
3. In alternativa, puoi utilizzare un qualsiasi server statico locale:
   ```bash
   npx serve .
   # oppure
   python3 -m http.server 8080
   ```

---

## 📚 Fonti Bibliografiche e Canoniche

Il dataset e le descrizioni teorico-pratiche unificano le seguenti opere:
- *Codex Arithmantiae* — Zeno & Glaphira Hawstein
- *Manuale di Difesa Contro le Arti Oscure* — Gellert Mortem, Kaido Flarehelm
- *Exorcismis Occultis* e *Maledictio* — Yashiro Isana Mortem
- *Manuale Completo di Trasfigurazione* — Yashiro Isana Mortem
- Dispensa metodologica *Incantesimi* e Regolamento di Duello Ministeriale

---

## 📄 Licenza

Distribuito sotto licenza **MIT**. Consulta il file [`LICENSE`](LICENSE) per ulteriori dettagli.
