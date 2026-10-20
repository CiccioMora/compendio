# 🪄 Compendium Magicum — Portale della Conoscenza degli Incantesimi

[![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)](https://developer.mozilla.org/it/docs/Web/HTML)
[![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)](https://developer.mozilla.org/it/docs/Web/JavaScript)
[![Tailwind CSS](https://img.shields.io/badge/Tailwind_CSS-38B2AC?style=for-the-badge&logo=tailwind-css&logoColor=white)](https://tailwindcss.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-amber.svg?style=for-the-badge)](LICENSE)
[![Incantesimi](https://img.shields.io/badge/Incantesimi_Catalogati-129-blueviolet?style=for-the-badge)](#)

> **Portale Web interattivo e compendio accademico completo che suddivide e cataloga la conoscenza degli incantesimi per anni di studio (I-VII Anno, M.A.G.O. e Grimorio Aritmantico Hawstein).**
>
> Ogni scheda include: **Nome**, **Formula**, **Valenza Magica Pitagorica (1-9)**, **Valenza Opposta di Simmetria**, **Movimento della Bacchetta (con animazione vettoriale SVG)**, **Tipologia Magica**, **Idoneità ed Utilizzo in Duello** (con tattiche dedicate) ed **Etimologia**.

---

## 🌟 Caratteristiche Principali

- **📅 Suddivisione Accademica per Anni di Corso**:
  - **I Anno** (16 incantesimi): *Fondamenti di Difesa, Cinetica e Incantesimi Generali (Flipendo, Expelliarmus, Wingardium Leviosa, Lumos, Diffindo...)*
  - **II Anno** (14 incantesimi): *Fatture, Trasfigurazione Inanimata e Creature (Rictusempra, Tarantallegra, Engorgio, Reducio, Arania Exumai...)*
  - **III Anno** (16 incantesimi): *Elementi di Gelo, Impatto e Locomozione (Glacius, Carpe Retractum, Riddikulus, Ascendio, Immobulus...)*
  - **IV Anno** (20 incantesimi): *Tattiche di Difesa, Distruzione e Medimagia (Bombarda, Stupeficium Avanzato, Aguamenti, Episkey, Avis, Oppugno...)*
  - **V Anno** (24 incantesimi): *Preparazione ai G.U.F.O., Esplosivi e Maledizioni (Confringo, Expecto Patronum, Sectumsempra, Muffliato, Silencio...)*
  - **M.A.G.O. & Arti Oscure** (16 incantesimi): *Formule di livello avanzato e proibite (Fiendfyre, Maledizioni Senza Perdono: Imperius, Crucio, Avada Kedavra, Partis Temporus, Morsmordre...)*
  - **Grimorio Aritmantico Operativo** (23 formule): *Trattati operativi di Zeno & Glaphira Hawstein (Signo e le 9 Figure Geometriche, Coerceo, Plasma, Finge, Adultero, Sigilli di Controvalenza)*.

- **⚔️ Filtro e Valutazione Tattica per il Duello Magico**:
  - **86 Incantesimi Abilitati al Duello**: catalogati con finestra di lancio rapido, tempo di caricamento verbale/non verbale e contromisure.
  - **43 Incantesimi Non da Duello**: formule di utilità domestica, riparazione, scasso (*Alohomora*), sigilli lenti (*Colloportus*) o trasfigurazioni complesse d'aula.
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
├── spellsData.js           # Database completo dei 129 incantesimi strutturato in JSON/JS
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
git remote add origin https://github.com/<TUO-USERNAME>/portale-incantesimi.git

# Effettua il push
git push -u origin main
```

### 3. Attivare GitHub Pages (Sito Web Online Gratis)

1. Nel tuo repository su GitHub, vai su **Settings** > **Pages** (nel menu laterale sinistro).
2. Sotto **Build and deployment** > **Branch**:
   - Seleziona il branch: `main`
   - Seleziona la cartella: `/ (root)`
3. Clicca su **Save**.
4. Dopo circa 1-2 minuti, il tuo portale sarà accessibile pubblicamente all'indirizzo:
   `https://<TUO-USERNAME>.github.io/portale-incantesimi/`

---

## 💻 Utilizzo in Locale

Non è richiesto alcun ambiente Node o build step:
1. Clona il repository:
   ```bash
   git clone https://github.com/<TUO-USERNAME>/portale-incantesimi.git
   cd portale-incantesimi
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
