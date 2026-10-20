# -*- coding: utf-8 -*-
with open('docs/compendio_incantesimi.md', 'r', encoding='utf-8') as f:
    text = f.read()

target = '### Regole Fondamentali:\n1. **Calcolo della Valenza**:'
replacement = '''### Struttura in Sette Libri del Codex Arithmantiae (*Zeno & Glaphira Hawstein*):
Il trattato fondamentale si articola in 7 Libri e appendici operative, integrati nel corso di studi:
- **Liber I — I Fondamenti dell\'Arte**: introduzione teorica, livelli d\'azione (T.L.A.), valenza magica pitagorica, numeri speciali e Bridget Wenlock (il sacro numero 7).
- **Liber II — Numero e Anima**: numerologia, aritmomanzia e onomanzia, archetipi, numero del carattere, destino, cuore e ruota di Pitagora.
- **Liber III — Incantesimi**: incanti ripetibili e irripetibili, controincanti aritmantici, formule elementali (*Coerceo*, *Finge*, *Adultero*, *Plasma*), difese statiche di zona (*Protego Totalum*, *Muffliato*), piante elementali e incantesimo *Proteus*.
- **Liber IV — Geometria Magica**: figure geometriche e incantesimo segnante *Signo*, quadrati magici di Agrippa e Sator, sezione aurea e varchi proporzionali (*Phi Porta*, *Phi Revelio*).
- **Liber V — La Cabala**: sephirot, vie di saggezza ed evoluzione esoterica caldea.
- **Liber VI — Spazio e Traslazione (Sesto Anno / VI Anno)**: pozzi comunicanti (*Emineo*, *Emineo Puteus*), smaterializzazione, passaporta (*Portus*), triangolo traslatore (*Transatio Objecto*), giratempo e memoria delle bacchette (*Prior Incantatem*).
- **Liber VII — Rituali, Sigilli e Trappole (Settimo Anno / VII Anno)**: rituali di passaggio e iniziazione, ricordi silenti (*Capio Memoriam*), sigilli aritmantici (*Deminatio Gravitas*, *Magnes Lathos Addicis*, *Protegis Hoc Incantementum*), rottura dei sigilli (*Nodum Solvo*), trappole geometriche (*Abscondas*, *Fermo*, *In Fine Laqueo*, *Quae Reversa*).

### Regole Fondamentali:
1. **Calcolo della Valenza**:'''

if target in text:
    text = text.replace(target, replacement)
    with open('docs/compendio_incantesimi.md', 'w', encoding='utf-8') as f:
        f.write(text)
    with open('/Users/andreamorachioli/.gemini/antigravity/brain/3a4f7fa7-8206-4f51-b303-aa9b9d9eaf5c/compendio_incantesimi.md', 'w', encoding='utf-8') as f:
        f.write(text)
    print('Successfully updated docs/compendio_incantesimi.md!')
else:
    print('Target not found in docs/compendio_incantesimi.md')
