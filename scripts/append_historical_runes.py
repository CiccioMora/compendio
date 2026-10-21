import re

BASE_DIR = "/Users/andreamorachioli/.gemini/antigravity/scratch/portale-incantesimi"
ARTIFACT_DIR = "/Users/andreamorachioli/.gemini/antigravity/brain/3a4f7fa7-8206-4f51-b303-aa9b9d9eaf5c"

with open(f"{BASE_DIR}/docs/compendio_antiche_rune.md", "r", encoding="utf-8") as f:
    content = f.read()

section_6 = """

---

## 6. Le Varianti Runiche Storiche e la Dottrina delle Rune Capovolte

Dal trattato accademico di Yashiro Isana Mortem (*Antiche Rune*, Capitolo I, Pagine 11–15 e Capitolo IV, Pagine 42–43):

### 6.1 Il Fuþark Recente (Vichingo / Nordico a 16 Rune)
A partire dall'VIII secolo, il Fuþark Antico a 24 glifi subì un processo di essenzializzazione in Scandinavia, contraendosi in sole **16 rune**. Tale transizione rifletteva una distillazione del potere magico in simboli più densi:
- **Rami Lunghi (Danesi)**: forme standard per iscrizioni monumentali su pietra.
- **Rami Corti (Svedesi-Norvegesi)**: forme corsive semplificate su legno, in cui 9 rune riducono i propri tratti conservando inalterate le restanti 7.

| Fonema | Nome / Archetipo | Glifo Rami Lunghi | Glifo Rami Corti | Dominio Principale |
|:---:|---|:---:|:---:|---|
| **f** | Fé (Fehu) | **ᚠ** | **ᚠ** | Ricchezza mobile, spirito primigenio *(conservata)* |
| **u** | Úr (Uruz) | **ᚢ** | **ᚢ** | Pioggia, scoria di ferro, uro *(conservata)* |
| **þ** | Þurs (Thurisaz) | **ᚦ** | **ᚦ** | Gigante, spina, tormento *(conservata)* |
| **ą / o** | Óss (As / Ansuz) | **ᚬ** | **ᚭ** | Divinità ancestrale, estuario, verbo *(semplificata)* |
| **r** | Reið (Raido) | **ᚱ** | **ᚱ** | Cavalcata, viaggio, carro celeste *(conservata)* |
| **k** | Kaun (Kenaz) | **ᚴ** | **ᚴ** | Piaga, ulcera, fiaccola purificatrice *(semplificata)* |
| **h** | Hagall (Hagalaz) | **ᚼ** | **ᚽ** | Grandine, rottura, mutamento *(semplificata)* |
| **n** | Nauðr (Nauthiz) | **ᚾ** | **ᚿ** | Necessità, costrizione, travaglio *(semplificata)* |
| **i** | Íss (Isa) | **ᛁ** | **ᛁ** | Ghiaccio, stasi, riflesso immobile *(conservata)* |
| **a** | Ár (Jera) | **ᛅ** | **ᛆ** | Annata abbondante, raccolto, tempo *(semplificata)* |
| **s** | Sól (Sowilo) | **ᛋ** | **ᛌ** | Sole, guida radiosa, calore vitale *(semplificata)* |
| **t** | Týr (Teiwaz) | **ᛏ** | **ᛐ** | Dio Tyr, giustizia celeste *(semplificata)* |
| **b** | Bjarkan (Berkana) | **ᛒ** | **ᛓ** | Betulla, rinascita primaverile *(semplificata)* |
| **m** | Maðr (Mannaz) | **ᛘ** | **ᛙ** | Uomo, incremento umano, stirpe *(semplificata)* |
| **l** | Lögr (Laguz) | **ᛚ** | **ᛚ** | Acqua torrenziale, cascata *(conservata)* |
| **ʀ** | Ýr (Algiz/Eihwaz) | **ᛦ** | **ᛧ** | Tasso, arco da guerra, protezione *(semplificata)* |

### 6.2 Il Fuþork Anglosassone (33 Rune)
Sviluppatosi nelle Isole Britanniche per adattare il sistema runico alle mutate esigenze fonetiche dell'antico inglese. L'alfabeto si estese prima a 28, poi a **33 segni**, introducendo glifi specifici quali:
- **ᚪ Ác** (quercia), **ᚫ Æsc** (frassino), **ᚣ Ýr** (arco di tasso), **ᛠ Éar** (polvere sepolcrale / terra tombale).
- Nella magia cerimoniale di Hogwarts, il Fuþork Anglosassone è impiegato per la formula del Rituale Meteorico (`Ic-onciplie-jecundelicas-gaestas`).

### 6.3 Le Rune Medievali (Fuþork Medievale) & Glifi Avanzati
1. **Rune Puntate**: introdotte per rappresentare l'esatta corrispondenza con l'alfabeto latino cristiano, aggiungendo un punto centrale che inverte la sonorità della consonante (es. dalla sorda *t* ᛏ alla sonora *d* ᛑ; dalla velare *k* ᚴ alla sonora *g* ᚵ; dalla bilabiale *b* ᛒ alla sorda *p* ᛔ).
2. **Rune Legate (Bindrunes)**: fusione grafica di due o più glifi su un'unica asta comune (o collegati da un arco sottile), creando un amalgama inseparabile d'intenti magici. Costituiscono l'archetipo storico del *Trivio (`Compòsitum`)*.
3. **Ascendenza Umbro-Etrusca**: Yashiro Isana Mortem evidenzia come i glifi runici condividano radici antichissime con le **Tavole Eugubine** rinvenute in Umbria e con l'antico alfabeto etrusco, confermando l'universalità della magia sigillare nelle civiltà arcaiche.

### 6.4 La Dottrina della Runa Capovolta (Pagine 42–43)
Nell'Antica Ars Magica, la rotazione di una runa non è mai accidentale:
- **Orientamento Rituale**: una runa ruotata di **90° in senso destrorso (orario)** diviene *Capovolta*, fungendo da chiave d'accesso ai domini speculari o contrari rispetto alla sua ortodossia canonica.
- **Attivazione Volitiva vs Perturbata**: se impressa consapevolmente dal mago, devia l'energia verso il polo opposto (es. ᛏ Teiwaz capovolta dissolve la motivazione avversaria o altera il dominio della difficoltà); se causata da errore di tracciamento, genera squilibri caotici pericolosi.
- **Principio dell'Immutabilità dell'Intaglio**: l'inversione fisica o ottica successiva di un amuleto **non muta** la natura della runa. È l'atto dell'incisione originaria e l'intento infuso con *Exsèquor* a determinare irrevocabilmente se il glifo operi dritto o capovolto.
"""

if "## 6. Le Varianti Runiche Storiche" not in content:
    content += section_6
    with open(f"{BASE_DIR}/docs/compendio_antiche_rune.md", "w", encoding="utf-8") as f:
        f.write(content)
    with open(f"{ARTIFACT_DIR}/compendio_antiche_rune.md", "w", encoding="utf-8") as f:
        f.write(content)
    print("Section 6 successfully added to compendio_antiche_rune.md!")
else:
    print("Section 6 already present.")
