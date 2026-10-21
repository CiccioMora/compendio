import re

BASE_DIR = "/Users/andreamorachioli/.gemini/antigravity/scratch/portale-incantesimi"
ARTIFACT_DIR = "/Users/andreamorachioli/.gemini/antigravity/brain/3a4f7fa7-8206-4f51-b303-aa9b9d9eaf5c"

content = """# 🪄 Compendio Accademico di Trasfigurazione Magica
**Dalla cattedra di Trasfigurazione della Scuola di Magia e Stregoneria di Hogwarts**  
*Classificazione Didattica Canonica secondo il Manuale Ufficiale di Yashiro Isana Mortem (Edizione Ufficiale)*

---

> [!NOTE]
> Il presente compendio formalizza la suddivisione metodologica e curricolare della **Trasfigurazione**, sincronizzata con la scansione esatta per pagine e argomenti stabilita dal testo didattico di cattedra:
> - **Prima di PAGINA 29**: Fondamenti Molecolari, Marchiatura e Forme Base (**I Anno**)
> - **PAGINA 29**: Trasfigurazione Inanimata elementare e avanzata (**II Anno**)
> - **PAGINA 40 — DETRASFIGURAZIONE**: Detrasfigurazione, Difesa Non-Verbale e Bivalenza (**III Anno**)
> - **PAGINA 51 — LITOTRASFIGURAZIONE**: Litotrasfigurazione, Animazione e Dilatazione (**IV Anno**)
> - **PAGINA 59 — EVOCAZIONE**: Evocazione floreale/materica, Evanescenza e Duplicazione (**V Anno**)
> - **Dopo PAGINA 59**: Trasfigurazione Umana, Tassonomia avanzata e Animagia (**VI & VII Anno**)
>
> Tutte le formule includono la **Valenza Magica Pitagorica (1–9)**, la **figura geometrica operativa per Signo** e la rigorosa **corrispondenza 1:1 con l'Antico Futhark** (Valenza = Posizione della singola Runa).

---

## 📅 Quadro Sinottico del Programma Didattico (I - VII Anno)

```mermaid
flowchart TD
    subgraph I_Anno["I Anno: Fondamenti & Marchiatura (Prima di Pagina 29)"]
        T1["Teoria: Parametri Molecolari, Leggi di Gamp, Marchiatura (Pag. 25), Livelli di Trasfigurazione"]
        P1["Pratica: Chartanimus, Transfiguro, Muto, Verto, Reverto, Significo, Plansigno, Fersigno, Detecto"]
    end

    subgraph II_Anno["II Anno: Trasfigurazione Inanimata (Inizio Pagina 29)"]
        T2["Teoria: Caratteristiche della Trasfigurazione Inanimata, Persistenza e Saturazione"]
        P2["Pratica: Acutus, Malum, Gommosus, Vermiculus, Snufflifors, Incarcifors, Feraverto, Inferacus"]
    end

    subgraph III_Anno["III Anno: Detrasfigurazione & Bivalenza (Inizio Pagina 40)"]
        T3["Teoria: Detrasfigurazione Molecolare, Difesa Non-Verbale, Bivalenza negli Incanti"]
        P3["Pratica: Reparifarge, Lapifors, Avifors, Avis, Farfallus Explodit, Furunculus, Glisseo"]
    end

    subgraph IV_Anno["IV Anno: Litotrasfigurazione & Animazione (Inizio Pagina 51)"]
        T4["Teoria: Litotrasfigurazione, Trasfigurazione Animata, Paradosso della Trasfigurazione"]
        P4["Pratica: Draconifors, Duro, Piertotum Locomotor, Engorgio, Diminuendo"]
    end

    subgraph V_Anno["V Anno: Evocazione & Evanescenza (Inizio Pagina 59)"]
        T5["Teoria: Principi di Evocazione ed Evanescenza, Duplicazione, Incanto Anti-furto, Demone Stalker"]
        P5["Pratica: Orchideus, Melofors, Epoximise, Incarceramus, Evanesco, Ivanesco"]
    end

    subgraph VI_Anno["VI Anno: Trasfigurazione Umana & Pieghe Spazio-Temporali"]
        T6["Teoria: Estensione Irriconoscibile (Adduco Maxima), Tassonomia della Trasformazione, T. Umana"]
        P6["Pratica: Crinus Muto, Pullus, Densaugeo, Paperante, Piscofors, Entomorphis, Furitum, Geminio, Inflatus"]
    end

    subgraph VII_Anno["VII Anno: Animagia Suprema & Disvelamento"]
        T7["Teoria: Animagia, Animagus, Licantropia/Mannarismo, Maledictus, Metamorphomagus"]
        P7["Pratica: Animaleus Nobodyx, Pozione Homine Reverto, Alta Evanescenza"]
    end

    I_Anno --> II_Anno --> III_Anno --> IV_Anno --> V_Anno --> VI_Anno --> VII_Anno
```

---

## 🏛️ 1. I ANNO — FONDAMENTI MOLECOLARI, MARCHIATURA E TRASFORMAZIONE BASE
*(Manuale di Studio: Sezioni precedenti a PAGINA 29)*

### Modulo di Teoria
1. **La concentrazione**: orientamento mentale e focalizzazione dell'intento (Pag. 9).
2. **Parametri Fondamentali** (Pag. 10):
   - **Spazio**: volume, ingombro tridimensionale e collocazione del corpo.
   - **Struttura**: legami molecolari e densità della materia.
   - **Colore**: dispersione cromatica e pigmentazione superficiale.
   - **Tonalità**: timbro materico, risonanza e lucentezza.
   - **Essenza**: matrice ontologica, peso e inerzia magica.
3. **La Perfezione Molecolare & Diagnostica** (Pag. 16): verifica della compattezza atomica mediante *Detecto*.
4. **Controincantesimi Trasfigurativi di Primo Livello** (Pag. 17–18): natura del controincanto universale *Reverto*.
5. **Leggi e Divieti di Gamp** (Pag. 20):
   - *Cinque Eccezioni Principali alla Legge di Gamp sulla Trasfigurazione degli Elementi* (impossibilità di creare cibo dal nulla, denaro reale, vita senziente, amore autentico o resuscitare i morti).
6. **La Marchiatura Animata ed Inanimata** (Pag. 25): imposizione di sigilli identificativi semitrasparenti su inanimato (*Significo*), vegetali (*Plansigno*) e viventi (*Fersigno*).
7. **Le Tre Branche di Trasfigurazione Elementare** (Pag. 26–27):
   - *Morfologica (Forma)*: `Transfiguro`.
   - *Materica (Sostanza)*: `Muto`.
   - *Totale (Forma + Materia)*: `Verto`.

### Modulo di Pratica
* **`Chartanimus`** (Animazione di Carta) — *Pagina 17*
  * *Formula*: `Chartanimus` | *Valenza*: **1** (Opposto 9, Circonferenza) | *Runa*: **ᚠ Fehu (Pos. 1ª)**
  * *Effetto*: Primo esercizio didattico: trasforma fogli o pergamene in origami animati capaci di volare e muoversi.
* **`Reverto`** (Controincantesimo Trasfigurativo di I Livello) — *Pagina 17–19*
  * *Formula*: `Reverto` | *Valenza*: **7** (Opposto 3, Ettagono) | *Runa*: **ᚷ Gebo (Pos. 7ª)**
  * *Effetto*: Annulla le trasfigurazioni semplici applicate su oggetti inanimati, piante o creature, ripristinandone la forma originaria.
* **`Signìfico`** (Marchiatura Inanimata) — *Pagina 25*
  * *Formula*: `Significo` | *Valenza*: **8** (Opposto 2, Ottagono) | *Runa*: **ᚹ Wunjo (Pos. 8ª)**
  * *Effetto*: Imprime un marchio magico identificativo semitrasparente su oggetti inanimati.
* **`Plansìgno`** (Marchiatura Vegetale) — *Pagina 25*
  * *Formula*: `Plansigno` | *Valenza*: **2** (Opposto 8, Angolo/Linea) | *Runa*: **ᚢ Uruz (Pos. 2ª)**
  * *Effetto*: Marchia elementi botanici e vegetali preservandone la linfa vitale.
* **`Fersìgno`** (Marchiatura Vivente) — *Pagina 25*
  * *Formula*: `Fersigno` | *Valenza*: **9** (Opposto 1, Ellisse) | *Runa*: **ᚺ Hagalaz (Pos. 9ª)**
  * *Effetto*: Applica un sigillo non lesivo su entità biologiche animate e creature.
* **`Detecto`** (Diagnostica Molecolare e Marchi) — *Pagine 16 & 25*
  * *Formula*: `Detecto` | *Valenza*: **9** (Opposto 1, Ellisse) | *Runa*: **ᚺ Hagalaz (Pos. 9ª)**
  * *Effetto*: Rivela marchi occulti ed esamina la coerenza molecolare dell'oggetto trasfigurato.
* **`Transfìguro`** (Trasfigurazione Morfologica) — *Pagina 26*
  * *Formula*: `Transfiguro` | *Valenza*: **8** (Opposto 2, Ottagono) | *Runa*: **ᚹ Wunjo (Pos. 8ª)**
  * *Effetto*: Modifica esclusivamente la conformazione esteriore lasciando inalterato il materiale.
* **`Muto`** (Trasfigurazione Materica) — *Pagina 26–27*
  * *Formula*: `Muto` | *Valenza*: **6** (Opposto 4, Esagono) | *Runa*: **ᚲ Kenaz (Pos. 6ª)**
  * *Effetto*: Altera la composizione materica senza variare la forma.
* **`Verto`** (Trasfigurazione Totale) — *Pagina 27*
  * *Formula*: `Verto` | *Valenza*: **6** (Opposto 4, Esagono) | *Runa*: **ᚲ Kenaz (Pos. 6ª)**
  * *Effetto*: Modifica simultaneamente forma e sostanza dell'oggetto.

---

## 🏛️ 2. II ANNO — LA TRASFIGURAZIONE INANIMATA
*(Manuale di Studio: Inizio a PAGINA 29 fino a Pagina 39)*

### Modulo di Teoria
1. **La Trasfigurazione Inanimata** (Pag. 29): transizione tra corpi privi di vita; stabilità della massa, inerzia e densità.
2. **Le caratteristiche della Trasfigurazione** (Pag. 36): la Potenza, la Durata e l’Efficacia; decadimento e saturazione magica.

### Modulo di Pratica
* **`Acutus`** (Trasfigurazione in Ago) — *Pagina 30*
  * *Formula*: `Acutus` | *Valenza*: **2** (Opposto 8, Angolo/Linea) | *Runa*: **ᚢ Uruz (Pos. 2ª)**
  * *Effetto*: Trasforma un fiammifero o scheggia lignea in un affilato ago d'acciaio.
* **`Malum`** (Trasfigurazione in Mela) — *Pagina 31*
  * *Formula*: `Malum` | *Valenza*: **6** (Opposto 4, Esagono) | *Runa*: **ᚲ Kenaz (Pos. 6ª)**
  * *Effetto*: Trasforma oggetti inanimati in una mela compatta e lucida.
* **`Gommosus`** (Incantesimo di Elasticità) — *Pagina 32*
  * *Formula*: `Gommosus` | *Valenza*: **1** (Opposto 9, Circonferenza) | *Runa*: **ᚠ Fehu (Pos. 1ª)**
  * *Effetto*: Rende superfici solide gommose ed elastiche come trampolini, ammortizzando impatti.
* **`Vermiculus`** (Trasfigurazione in Lombrico) — *Pagina 33*
  * *Formula*: `Vermiculus` | *Valenza*: **2** (Opposto 8, Angolo/Linea) | *Runa*: **ᚢ Uruz (Pos. 2ª)**
  * *Effetto*: Trasfigura piccoli oggetti o parassiti in lombrichi inoffensivi.
* **`Snufflifors`** (Trasfigurazione in Topo) — *Pagina 34*
  * *Formula*: `Snufflifors` | *Valenza*: **9** (Opposto 1, Ellisse) | *Runa*: **ᚺ Hagalaz (Pos. 9ª)**
  * *Effetto*: Converte libri o oggetti inanimati in topolini grigi.
* **`Incarcifors`** (Trasfigurazione in Gabbia) — *Pagina 35*
  * *Formula*: `Incarcifors` | *Valenza*: **8** (Opposto 2, Ottagono) | *Runa*: **ᚹ Wunjo (Pos. 8ª)**
  * *Effetto*: Muta arredi circostanti in robuste gabbie per imprigionare intrusi o creature.
* **`Feraverto`** (Trasfigurazione Animale in Calice) — *Pagina 37*
  * *Formula*: `Feraverto` | *Valenza*: **5** (Opposto 5, Pentagono) | *Runa*: **ᚱ Raido (Pos. 5ª)**
  * *Effetto*: Tre tocchi precisi: trasfigura un animale di piccola taglia in un calice di cristallo colmo d'acqua pura.
* **`Inferacus`** (Trasfigurazione in Portaspilli) — *Pagina 38*
  * *Formula*: `Inferacus` | *Valenza*: **1** (Opposto 9, Circonferenza) | *Runa*: **ᚠ Fehu (Pos. 1ª)**
  * *Effetto*: Trasfigura un riccio o piccolo animale aculeato in un puntaspilli di velluto.

---

## 🏛️ 3. III ANNO — DETRASFIGURAZIONE, DIFESA E BIVALENZA
*(Manuale di Studio: Inizio a PAGINA 40 — DETRASFIGURAZIONE fino a Pagina 50)*

### Modulo di Teoria
1. **Detrasfigurazione** (Pag. 40): de-strutturazione delle alterazioni trasfigurative e scomposizione molecolare selettiva.
2. **Difesa Non-Verbale** (Pag. 42): canalizzazione silenziosa dell'intento trasfigurativo senza fuga acustica.
3. **Bivalenza negli Incanti** (Pag. 43): sortilegi applicabili con esito speculare su inanimato e animato.

### Modulo di Pratica
* **`Reparifarge`** (Detrasfigurazione Rettificatrice) — *Pagina 41*
  * *Formula*: `Reparifarge` | *Valenza*: **6** (Opposto 4, Esagono) | *Runa*: **ᚲ Kenaz (Pos. 6ª)**
  * *Effetto*: Il controincanto principe di III Anno: annulla trasfigurazioni parziali, incomplete o difettose.
* **`Lapifors`** (Trasfigurazione Bivalente in Coniglio) — *Pagina 44*
  * *Formula*: `Lapifors` | *Valenza*: **9** (Opposto 1, Ellisse) | *Runa*: **ᚺ Hagalaz (Pos. 9ª)**
  * *Effetto*: Trasforma bersagli inanimati o piccole entità in conigli viventi.
* **`Avifors`** (Trasfigurazione in Uccelli) — *Pagina 45*
  * *Formula*: `Avifors` | *Valenza*: **7** (Opposto 3, Ettagono) | *Runa*: **ᚷ Gebo (Pos. 7ª)**
  * *Effetto*: Converte oggetti o statue in uno stormo di piccoli volatili.
* **`Avis`** (Evocazione di Stormo d'Uccelli) — *Pagina 46*
  * *Formula*: `Avis` | *Valenza*: **5** (Opposto 5, Pentagono) | *Runa*: **ᚱ Raido (Pos. 5ª)**
  * *Effetto*: Evoca dal nulla una nube di uccelli canori con getto balistico.
* **`Farfallus Explodit`** (Evocazione Farfalle Accecanti) — *Pagina 47*
  * *Formula*: `Farfallus Explodit` | *Valenza*: **7** (Opposto 3, Ettagono) | *Runa*: **ᚷ Gebo (Pos. 7ª)**
  * *Effetto*: Evoca migliaia di farfalle iridescenti che disorientano e stordiscono il nemico.
* **`Furunculus`** (Fattura Trasfigurativa dei Brufoli) — *Pagina 48*
  * *Formula*: `Furunculus` | *Valenza*: **1** (Opposto 9, Circonferenza) | *Runa*: **ᚠ Fehu (Pos. 1ª)**
  * *Effetto*: Causa un'eruzione epidermica istantanea trasfigurando il tessuto cutaneo in dolorosi foruncoli.
* **`Glisseo`** (Levigazione Trasfigurativa) — *Pagina 49*
  * *Formula*: `Glisseo` | *Valenza*: **6** (Opposto 4, Esagono) | *Runa*: **ᚲ Kenaz (Pos. 6ª)**
  * *Effetto*: Appiana scalinate o pendenze convertendole in scivoli levigati come marmo ghiacciato.

---

## 🏛️ 4. IV ANNO — LITOTRASFIGURAZIONE E ANIMAZIONE
*(Manuale di Studio: Inizio a PAGINA 51 — LITOTRASFIGURAZIONE fino a Pagina 58)*

### Modulo di Teoria
1. **Litotrasfigurazione** (Pag. 51): manipolazione avanzata della materia rocciosa, scultorea e minerale (*lithos*).
2. **Trasfigurazione Animata** (Pag. 54): infusione di schemi biologici motori ed eterici in manufatti inanimati.
3. **Paradosso della Trasfigurazione** (Pag. 56): tensione metafisica e limiti di autonomia della materia animata.

### Modulo di Pratica
* **`Draconifors`** (Litotrasfigurazione e Animazione Draconica) — *Pagina 51*
  * *Formula*: `Draconifors` | *Valenza*: **1** (Opposto 9, Circonferenza) | *Runa*: **ᚠ Fehu (Pos. 1ª)**
  * *Effetto*: Anima statue di draghi conferendo loro volo autonomo, morsi e getti di fiammelle.
* **`Duro`** (Litotrasfigurazione Pietrificante) — *Pagina 53*
  * *Formula*: `Duro` | *Valenza*: **4** (Opposto 6, Quadrato) | *Runa*: **ᚨ Ansuz (Pos. 4ª)**
  * *Effetto*: Converte all'istante materiali morbidi o liquidi in solida pietra massiccia.
* **`Piertotum Locomotor`** (Grande Animazione Litica) — *Pagina 55*
  * *Formula*: `Piertotum Locomotor` | *Valenza*: **8** (Opposto 2, Ottagono) | *Runa*: **ᚹ Wunjo (Pos. 8ª)**
  * *Effetto*: Risveglia statue colossali e armature del castello ordinando loro di combattere a difesa dell'istituto.
* **`Engorgio` & `Diminuendo`** (Dilatazione e Compressione Volumetrica) — *Pagina 57*
  * *Formule*: `Engorgio` | `Diminuendo` | *Valenza*: **9** (Opposto 1, Ellisse) | *Runa*: **ᚺ Hagalaz (Pos. 9ª)**
  * *Effetto*: Incrementano o comprimono uniformemente la scala dimensionale dei bersagli senza alterarne la densità.

---

## 🏛️ 5. V ANNO — EVOCAZIONE, EVANESCENZA E DUPLICAZIONE
*(Manuale di Studio: Inizio a PAGINA 59 — EVOCAZIONE)*

### Modulo di Teoria
1. **Principi Generali di Evocazione** (Pag. 60): creazione e richiamo di materia dal Non-Essere (regolata dalla Legge di Gamp).
2. **La Duplicazione** (Pag. 73): moltiplicazione di oggetti con decadimento qualitativo.
3. **Principi Generali di Evanescenza** (Pag. 74–76): dissoluzione ontologica di corpi inanimati ed entità viventi.
4. **Incanto Anti-Furto** (Pag. 77) e **Demone Stalker** (Pag. 68–72): spionaggio ed entità evocate.

### Modulo di Pratica
* **`Orchideus`** (Evocazione Floreale) — *Pagina 79*
  * *Formula*: `Orchideus` | *Valenza*: **3** (Opposto 7, Triangolo) | *Runa*: **ᚦ Thurisaz (Pos. 3ª)**
* **`Melofors`** (Fattura Trasfigurativa della Zucca) — *Pagina 80*
  * *Formula*: `Melofors` | *Valenza*: **6** (Opposto 4, Esagono) | *Runa*: **ᚲ Kenaz (Pos. 6ª)**
* **`Epoximise`** (Trasfigurazione Adesiva) — *Pagina 78*
  * *Formula*: `Epoximise` | *Valenza*: **7** (Opposto 3, Ettagono) | *Runa*: **ᚷ Gebo (Pos. 7ª)**
* **`Incarceramus`** (Evocazione di Corde e Legacci) — *Pagina 81*
  * *Formula*: `Incarceramus` | *Valenza*: **9** (Opposto 1, Ellisse) | *Runa*: **ᚺ Hagalaz (Pos. 9ª)**

---

## 🏛️ 6. VI ANNO — TRASFIGURAZIONE UMANA & TRASFUSIONE SPAZIALE
*(Argomenti successivi a Pagina 88 già classificati)*

* **Tassonomia della Trasformazione & Trasfigurazione Circolare** (Pag. 88–94)
* **Trasfigurazione Umana** (Pag. 96):
  * `Crinus Muto` (Valenza 8 • ᚹ Wunjo) — Alterazione estetica capillare.
  * `Pullus` (Valenza 8 • ᚹ Wunjo) — Trasfigurazione in pollo da duello.
  * `Densaugeo` (Valenza 5 • ᚱ Raido) — Crescita mostruosa dei denti.
  * `Paperante` (Valenza 1 • ᚠ Fehu) — Trasfigurazione in papera.
  * `Piscofors` (Valenza 3 • ᚦ Thurisaz) — Trasfigurazione marina in pesce.
  * `Entomorphis` (Valenza 9 • ᚺ Hagalaz) — Trasfigurazione in insetto.
  * `Furitum` (Valenza 7 • ᚷ Gebo) — Trasfigurazione in furetto.
  * `Geminio` (Valenza 6 • ᚲ Kenaz) — Duplicazione virale.
  * `Inflatus` (Valenza 6 • ᚲ Kenaz) — Rigonfiamento corporeo a pallone.
  * `Capacius Extremis` / `Adduco Maxima` (Valenza 2 / 1) — Estensione spaziale indistinguibile.

---

## 🏛️ 7. VII ANNO — ALTA ANIMAGIA, MANNARISMO E RIVERSIONE SUPREMA
*(Argomenti di coronamento accademico M.A.G.O. già classificati)*

* **Animagia & Animagus** (Pag. 108–110): trasformazione conscia e reversibile in animale guida.
* **Licantropia, Mannarismo e Maledictus** (Pag. 112–123): maledizioni del sangue e degenerazione ontologica.
* **`Animaleus Nobodyx`** (Valenza 6 • ᚲ Kenaz) — Formula correttiva per disvelare Animaghi e smascherare sembianze animali.
* **Pozione Homine Reverto** (Pag. 122) — Formulazione alchemica per costringere l'Animagus al ripristino umano.
"""

with open(f"{BASE_DIR}/docs/compendio_trasfigurazione.md", "w", encoding="utf-8") as f:
    f.write(content)

with open(f"{ARTIFACT_DIR}/compendio_trasfigurazione.md", "w", encoding="utf-8") as f:
    f.write(content)

print("compendio_trasfigurazione.md successfully updated and synchronized!")
