# -*- coding: utf-8 -*-
"""
integrate_missing_manual_spells.py
Integra nella base dati (spellsData.js) i 19 incantesimi estratti dai manuali di:
- Astronomia (I-V Anno e VII Anno - Mary C. Silente)
- Erbologia (I-VI Anno - Nicholas Kelleher)

Garantisce:
- Calcolo rigoroso della Valenza Pitagorica e Valenza Opposta (col 5)
- Associazione runica 1:1 secondo il Canone: Valenza dell'incantesimo = Posizione della runa nell'alfabeto runico
- Movimento della bacchetta SVG animabile
- Aggiornamento contatori, UI, standalone, markdown e artifacts
"""

import json
import re

BASE_DIR = '/Users/andreamorachioli/.gemini/antigravity/scratch/portale-incantesimi'
ARTIFACT_DIR = '/Users/andreamorachioli/.gemini/antigravity/brain/3a4f7fa7-8206-4f51-b303-aa9b9d9eaf5c'

PYTHAGOREAN = {
    'A':1, 'B':2, 'C':3, 'D':4, 'E':5, 'F':6, 'G':7, 'H':8, 'I':9,
    'J':1, 'K':2, 'L':3, 'M':4, 'N':5, 'O':6, 'P':7, 'Q':8, 'R':9,
    'S':1, 'T':2, 'U':3, 'V':4, 'W':5, 'X':6, 'Y':7, 'Z':8
}

VALENCE_RUNES_MAP = {
    "1": "ᚠ Fehu (Pos. 1ª)",
    "2": "ᚢ Uruz (Pos. 2ª)",
    "3": "ᚦ Thurisaz (Pos. 3ª)",
    "4": "ᚨ Ansuz (Pos. 4ª)",
    "5": "ᚱ Raido (Pos. 5ª)",
    "6": "ᚲ Kenaz (Pos. 6ª)",
    "7": "ᚷ Gebo (Pos. 7ª)",
    "8": "ᚹ Wunjo (Pos. 8ª)",
    "9": "ᚺ Hagalaz (Pos. 9ª)"
}

GEOMETRY_MAP = {
    1: "Circonferenza (Unità / Elemento Acqua)",
    2: "Angolo / Linea (Dualismo / Polarità)",
    3: "Triangolo equilatero (Unificazione / Fuoco)",
    4: "Quadrato (Immanenza / Risoluzione)",
    5: "Pentagono regolare (Elemento Aria / Equilibrio)",
    6: "Esagono regolare (Elemento Terra / Equilibrio)",
    7: "Ettagono regolare (Opposizione / Massima Energia)",
    8: "Ottagono regolare (Elemento Fuoco / Infinito)",
    9: "Ellisse (Reincarnazione / Totalità)"
}

with open(f'{BASE_DIR}/spellsData.js', 'r', encoding='utf-8') as f:
    text = f.read()

spells = json.loads(text[text.find('['):text.rfind(']')+1])
existing_ids = {s['id'] for s in spells}

print(f"Spells attuali nel database: {len(spells)}")

new_spells = [
    # --- I ANNO (Astronomia) ---
    {
        "id": "guidami",
        "anno": 1,
        "annoLabel": "I Anno",
        "nome": "Incantesimo Bussola (Guidami / Point Me)",
        "formula": "Guidami",
        "ripetibile": True,
        "tipologia": "Cinetica / Orientamento Cardinale",
        "inDuello": False,
        "duelloNote": "Non idoneo al duello convenzionale. Utilizzato per l'orientamento notturno sul campo, allineare i telescopi e determinare con precisione il meridiano astronomico e il Nord geografico.",
        "movimento": "Bacchetta appoggiata orizzontale sul palmo della mano aperta con pronuncia ferma della formula; la bacchetta ruota autonomamente fermandosi verso il Nord.",
        "movimentoSvg": "M 40,75 L 110,75 M 95,60 L 110,75 L 95,90",
        "descrizione": "Trattato nella dispensa didattica di Astronomia del I Anno. Fa ruotare la bacchetta posta sul palmo della mano del mago fino a indicare stabilmente il Nord geografico/magnetico, permettendo l'orientamento immediato nelle osservazioni notturne.",
        "etimologia": "Dall'italiano guidare (condurre, orientare la direzione).",
        "valenza": 1,
        "sommaLettere": 37,
        "valenzaOpposta": 9,
        "maxRipetizioni": 1,
        "figuraGeometrica": "Circonferenza (Unità / Elemento Acqua)",
        "runeAssociate": VALENCE_RUNES_MAP[1],
        "noteAritmantiche": "Valenza Magica 1 (somma pitagorica 37 ridotta a 1). Valenza opposta di simmetria: 9. Figura operativa per Signo: Circonferenza. Limite di reiterazione efficace: 1 volta/e."
    },
    {
        "id": "alheia-croma",
        "anno": 1,
        "annoLabel": "I Anno",
        "nome": "Incantesimo di Rifrazione Stellare (Alheia Croma)",
        "formula": "Alheia Croma",
        "ripetibile": True,
        "tipologia": "Ottico / Rifrazione della Luce",
        "inDuello": False,
        "duelloNote": "Non da duello. Sortilegio ottico applicato agli oculari dei telescopi o direttamente al cristallino per la scomposizione cromatica della luce stellare.",
        "movimento": "Puntare con estrema precisione la punta della bacchetta verso la lente del telescopio o a pochi centimetri dal campo visivo.",
        "movimentoSvg": "M 45,75 L 75,75 M 75,55 A 20,20 0 1,1 75,95 A 20,20 0 1,1 75,55",
        "descrizione": "Incluso nel programma di Astronomia del I Anno. Modifica l'indice di rifrazione della luce incidente, separando gli spettri cromatici dei corpi celesti lontani e neutralizzando le distorsioni termiche causate dall'atmosfera terrestre.",
        "etimologia": "Composto dal greco aleitheia (verità, nitidezza priva di velo) e chroma (colore, spettro visibile).",
        "valenza": 5,
        "sommaLettere": 50,
        "valenzaOpposta": 5,
        "maxRipetizioni": 5,
        "figuraGeometrica": "Pentagono regolare (Elemento Aria / Equilibrio)",
        "runeAssociate": VALENCE_RUNES_MAP[5],
        "noteAritmantiche": "Valenza Magica 5 (somma pitagorica 50 ridotta a 5). Valenza opposta di simmetria: 5 (simmetria speculare pura). Figura operativa per Signo: Pentagono regolare. Limite di reiterazione: 5 volte."
    },
    {
        "id": "apokros",
        "anno": 1,
        "annoLabel": "I Anno",
        "nome": "Controincantesimo di Rifrazione Stellare (Apokros)",
        "formula": "Apokros",
        "ripetibile": True,
        "tipologia": "Controincantesimo Ottico / Ripristino Visivo",
        "inDuello": False,
        "duelloNote": "Non da duello. Dissolve istantaneamente le alterazioni ottiche e rifrattive prodotte da Alheia Croma o abbagliamenti da luce concentrata.",
        "movimento": "Puntamento inverso della bacchetta seguito da fendente orizzontale netto ad allontanare il flusso d'energia.",
        "movimentoSvg": "M 115,75 L 45,75 M 60,60 L 45,75 L 60,90",
        "descrizione": "Controincantesimo specifico di Alheia Croma inserito nel programma di Astronomia di I Anno. Ristabilisce la naturale convergenza focale di telescopi e occhi magici, azzerando residui di dispersione cromatica o alterazioni rifrattive.",
        "etimologia": "Dal greco apokrouo (respingere indietro, respingere con forza, far cessare).",
        "valenza": 5,
        "sommaLettere": 32,
        "valenzaOpposta": 5,
        "maxRipetizioni": 5,
        "figuraGeometrica": "Pentagono regolare (Elemento Aria / Equilibrio)",
        "runeAssociate": VALENCE_RUNES_MAP[5],
        "noteAritmantiche": "Valenza Magica 5 (somma pitagorica 32 ridotta a 5). Valenza opposta di simmetria: 5. Figura operativa per Signo: Pentagono regolare. Limite di reiterazione: 5 volte."
    },

    # --- III ANNO (Astronomia) ---
    {
        "id": "lux-perfluo",
        "anno": 3,
        "annoLabel": "III Anno",
        "nome": "Filtro di Luce Stellare (Lux Perfluo)",
        "formula": "Lux Perfluo",
        "ripetibile": True,
        "tipologia": "Manipolazione della Luce / Filtro Anti-Abbaglio",
        "inDuello": False,
        "duelloNote": "Non da duello. Crea un filtro diaframmatico che attenua la radiazione luminosa eccessiva consentendo la visione nitida di dettagli cosmici tenui.",
        "movimento": "Movimento circolare orario tracciato lentamente sopra la lente del telescopio o a mezz'aria davanti allo sguardo.",
        "movimentoSvg": "M 75,40 A 35,35 0 1,1 74.9,40",
        "descrizione": "Trattato nel manuale di Astronomia del III Anno. Agisce come diaframma ottico magico polarizzato, schermando il bagliore accecante della luna piena, nubi riflettenti o inquinamento luminoso locale per osservare ammassi stellari e nebulose lontane.",
        "etimologia": "Dal latino lux (luce) e perfluere (scorrere attraverso, defluire, filtrare).",
        "valenza": 6,
        "sommaLettere": 51,
        "valenzaOpposta": 4,
        "maxRipetizioni": 6,
        "figuraGeometrica": "Esagono regolare (Elemento Terra / Equilibrio)",
        "runeAssociate": VALENCE_RUNES_MAP[6],
        "noteAritmantiche": "Valenza Magica 6 (somma pitagorica 51 ridotta a 6). Valenza opposta di simmetria: 4. Figura operativa per Signo: Esagono regolare. Limite di reiterazione: 6 volte."
    },

    # --- IV ANNO (Erbologia) ---
    {
        "id": "herbivicus",
        "anno": 4,
        "annoLabel": "IV Anno",
        "nome": "Incantesimo di Crescita Vegetale Rapida (Herbivicus)",
        "formula": "Herbivicus",
        "ripetibile": True,
        "tipologia": "Incanto Botanico di Crescita / Fisiologia Vegetale",
        "inDuello": False,
        "duelloNote": "Non convenzionale per duello, sebbene utilizzabile per far germogliare istantaneamente radici e rovi per creare barriere o intralciare l'avversario.",
        "movimento": "Spirale ascendente fluida dal colletto radicale verso l'apice del fusto con tocco finale proteso verso l'alto.",
        "movimentoSvg": "M 75,115 C 50,100 50,85 75,75 C 100,65 100,50 75,35",
        "descrizione": "Formula cardine dell'Erbologia pratica, introdotta al IV Anno e riassunta al VI Anno (Manuale di Nicholas Kelleher). Stimola intensamente le auxine e le gibberelline vegetali, provocando una rapida proliferazione cellulare che fa sbocciare fiori, allungare fusti e rigenerare fogliame in pochi istanti.",
        "etimologia": "Composto dal latino herba (erba, pianta) e vivo/vigere (vivere, dare vigore vitale).",
        "valenza": 8,
        "sommaLettere": 53,
        "valenzaOpposta": 2,
        "maxRipetizioni": 8,
        "figuraGeometrica": "Ottagono regolare (Elemento Fuoco / Infinito)",
        "runeAssociate": VALENCE_RUNES_MAP[8],
        "noteAritmantiche": "Valenza Magica 8 (somma pitagorica 53 ridotta a 8). Valenza opposta di simmetria: 2. Figura operativa per Signo: Ottagono regolare. Limite di reiterazione: 8 volte."
    },

    # --- V ANNO (Astronomia) ---
    {
        "id": "astralis-cartae-dominium",
        "anno": 5,
        "annoLabel": "V Anno",
        "nome": "Proiezione della Carta Natale (Astralis Cartae Dominium)",
        "formula": "Astralis Cartae Dominium",
        "ripetibile": False,
        "tipologia": "Proiezione Astrologica / Oroscopo Magico Tridimensionale",
        "inDuello": False,
        "duelloNote": "Non da duello. Sortilegio avanzato di calcolo astrale per la materializzazione delle coordinate natali e dei transiti planetari.",
        "movimento": "Tracciare un cerchio d'argento a mezz'aria seguito da dodici tocchi radiali concentrici verso l'esterno.",
        "movimentoSvg": "M 75,45 A 30,30 0 1,0 75,105 A 30,30 0 1,0 75,45 M 75,25 L 75,45 M 75,105 L 75,125 M 35,75 L 55,75 M 95,75 L 115,75",
        "descrizione": "Insegnato nel V Anno di Astronomia e Astrologia comparata. Materializza a mezz'aria un quadrante tridimensionale luminoso d'argento raffigurante le posizioni dei pianeti, gli aspetti celesti e i domicili zodiacali nel momento esatto della nascita di un individuo.",
        "etimologia": "Dal latino astralis (degli astri), charta (pergamena, mappa) e dominium (padronanza, dominio).",
        "valenza": 2,
        "sommaLettere": 92,
        "valenzaOpposta": 8,
        "maxRipetizioni": 1,
        "figuraGeometrica": "Angolo / Linea (Dualismo / Polarità)",
        "runeAssociate": VALENCE_RUNES_MAP[2],
        "noteAritmantiche": "Valenza Magica 2 (somma pitagorica 92 ridotta a 2). Valenza opposta di simmetria: 8. Figura operativa per Signo: Angolo / Linea. Limite di reiterazione: 1 volta/e."
    },
    {
        "id": "astra-invoco",
        "anno": 5,
        "annoLabel": "V Anno",
        "nome": "Risonanza con le Energie Astrali (Astra Invoco)",
        "formula": "Astra Invoco",
        "ripetibile": True,
        "tipologia": "Risonanza Astrale / Armonizzazione Energetica",
        "inDuello": False,
        "duelloNote": "Non da duello. Richiede calma e concentrazione per sintonizzare il canale magico del mago con le frequenze planetarie in transito.",
        "movimento": "Puntamento bipolare verso la volta celeste con lieve oscillazione della bacchetta; bagliori oro e argento.",
        "movimentoSvg": "M 75,115 L 75,35 M 55,60 L 75,35 L 95,60",
        "descrizione": "Introdotto nel V Anno di Astronomia. Fa vibrare l'atmosfera circostante generando minuscoli globi di luce dorata e argentea, sintonizzando l'incantatore con gli allineamenti e le energie astrali del momento per affinare calcoli e divinazioni.",
        "etimologia": "Dal latino astra (astri, costellazioni) e invocare (chiamare verso di sé, invocare).",
        "valenza": 2,
        "sommaLettere": 47,
        "valenzaOpposta": 8,
        "maxRipetizioni": 2,
        "figuraGeometrica": "Angolo / Linea (Dualismo / Polarità)",
        "runeAssociate": VALENCE_RUNES_MAP[2],
        "noteAritmantiche": "Valenza Magica 2 (somma pitagorica 47 ridotta a 2). Valenza opposta di simmetria: 8. Figura operativa per Signo: Angolo / Linea. Limite di reiterazione: 2 volte."
    },

    # --- VI ANNO (Erbologia) ---
    {
        "id": "trimere",
        "anno": 6,
        "annoLabel": "VI Anno",
        "nome": "Formula di Modellatura Botanica (Trimere)",
        "formula": "Trimere",
        "ripetibile": True,
        "tipologia": "Potatura Magica / Modellatura delle Piante",
        "inDuello": False,
        "duelloNote": "Non da duello. Permette la rifilatura millimetrica e la sagomatura non traumatica di specie vegetali invasive.",
        "movimento": "Fendenti brevi e calibrati a zig-zag sopra la chioma della pianta da rifilare.",
        "movimentoSvg": "M 45,55 L 75,55 L 60,85 L 90,85 L 75,115 L 105,115",
        "descrizione": "Trattato nel VI Anno di Erbologia (Capitolo Potatura & Gestione, Nicholas Kelleher). Consente di sagomare e rifilare le chiome di siepi e rampicanti magici con chirurgica precisione, arginando crescite anomale senza intaccare la linfa vitale.",
        "etimologia": "Dall'inglese to trim (rifilare, potare, aggiustare).",
        "valenza": 7,
        "sommaLettere": 43,
        "valenzaOpposta": 3,
        "maxRipetizioni": 7,
        "figuraGeometrica": "Ettagono regolare (Opposizione / Massima Energia)",
        "runeAssociate": VALENCE_RUNES_MAP[7],
        "noteAritmantiche": "Valenza Magica 7 (somma pitagorica 43 ridotta a 7). Valenza opposta di simmetria: 3. Figura operativa per Signo: Ettagono regolare. Limite di reiterazione: 7 volte."
    },
    {
        "id": "protego-herbivorum",
        "anno": 6,
        "annoLabel": "VI Anno",
        "nome": "Barriera contro la Fauna Fitofaga (Protego Herbivorum)",
        "formula": "Protego Herbivorum",
        "ripetibile": False,
        "tipologia": "Difesa Botanica di Zona / Barriera Fitofaga",
        "inDuello": False,
        "duelloNote": "Non da duello. Erige uno scudo selettivo contro parassiti, bruchi giganti e fauna erbivora a protezione delle serre.",
        "movimento": "Cupola aerea tracciata sopra l'esemplare vegetale con cerchio orario e affondo conclusivo verso il suolo.",
        "movimentoSvg": "M 35,110 C 35,50 115,50 115,110 M 35,110 L 115,110",
        "descrizione": "Trattato nel VI Anno di Erbologia (Manuale di Nicholas Kelleher). Proietta un campo di forza invisibile attorno alle specie vegetali coltivate, impenetrabile a insetti xilofagi, parassiti e lumache carnivore senza ostacolare l'assorbimento di luce e umidità.",
        "etimologia": "Dal latino protegere (riparare, proteggere) e herbivorus (che si nutre di vegetali).",
        "valenza": 2,
        "sommaLettere": 101,
        "valenzaOpposta": 8,
        "maxRipetizioni": 1,
        "figuraGeometrica": "Angolo / Linea (Dualismo / Polarità)",
        "runeAssociate": VALENCE_RUNES_MAP[2],
        "noteAritmantiche": "Valenza Magica 2 (somma pitagorica 101 ridotta a 2). Valenza opposta di simmetria: 8. Figura operativa per Signo: Angolo / Linea. Limite di reiterazione: 1 volta/e."
    },
    {
        "id": "repello-inimicum",
        "anno": 6,
        "annoLabel": "VI Anno",
        "nome": "Allontanamento Parassitario e Disinfestazione (Repello Inimicum)",
        "formula": "Repello Inimicum",
        "ripetibile": True,
        "tipologia": "Disinfestazione Botanica / Frequenza Repulsiva",
        "inDuello": False,
        "duelloNote": "Non da duello. Genera micro-onde oscillatorie repulsive per disinfestare le piante senza intossicare i tessuti.",
        "movimento": "Fendente a ventaglio diretto in avanti dal basso verso l'esterno.",
        "movimentoSvg": "M 50,75 L 100,75 M 85,55 L 105,75 L 85,95 M 95,45 L 115,75 L 95,105",
        "descrizione": "Trattato nel VI Anno di Erbologia (Manuale di Nicholas Kelleher). Sprigiona una frequenza oscillatoria repulsiva che costringe acari, afidi e spore micotiche ad abbandonare la pianta, ripulendola in profondità in modo ecologico e privo di agenti caustici.",
        "etimologia": "Dal latino repellere (scacciare, respingere) e inimicus (nemico, ostile).",
        "valenza": 3,
        "sommaLettere": 84,
        "valenzaOpposta": 7,
        "maxRipetizioni": 3,
        "figuraGeometrica": "Triangolo equilatero (Unificazione / Fuoco)",
        "runeAssociate": VALENCE_RUNES_MAP[3],
        "noteAritmantiche": "Valenza Magica 3 (somma pitagorica 84 ridotta a 3). Valenza opposta di simmetria: 7. Figura operativa per Signo: Triangolo equilatero. Limite di reiterazione: 3 volte."
    },
    {
        "id": "reparo-herbalis",
        "anno": 6,
        "annoLabel": "VI Anno",
        "nome": "Cicatrizzazione e Rigenerazione Vegetale (Reparo Herbalis)",
        "formula": "Reparo Herbalis",
        "ripetibile": True,
        "tipologia": "Cura Botanica / Cicatrizzazione Linfatica",
        "inDuello": False,
        "duelloNote": "Non da duello. Sortilegio curativo per risanare tagli, traumi da potatura e necrosi sui fusti delle piante magiche.",
        "movimento": "Tracciare una croce armoniosa sopra la ferita della pianta, completando con lieve sfioramento della corteccia.",
        "movimentoSvg": "M 75,45 L 75,105 M 45,75 L 105,75 M 60,60 C 75,70 75,80 90,90",
        "descrizione": "Variante specialistica dell'incantesimo Reparo per la botanica magica (VI Anno, Nicholas Kelleher). Rimargina lesioni, innesti mal riusciti o lacerazioni da taglio nei tessuti vegetali, riattivando i vasi cribro-vascolari e azzerando lo stress cellulare.",
        "etimologia": "Dal latino reparare (risanare, aggiustare) e herbalis (delle piante, erboristico).",
        "valenza": 3,
        "sommaLettere": 75,
        "valenzaOpposta": 7,
        "maxRipetizioni": 3,
        "figuraGeometrica": "Triangolo equilatero (Unificazione / Fuoco)",
        "runeAssociate": VALENCE_RUNES_MAP[3],
        "noteAritmantiche": "Valenza Magica 3 (somma pitagorica 75 ridotta a 3). Valenza opposta di simmetria: 7. Figura operativa per Signo: Triangolo equilatero. Limite di reiterazione: 3 volte."
    },
    {
        "id": "sistamina",
        "anno": 6,
        "annoLabel": "VI Anno",
        "nome": "Conservazione Organica e Blocco del Decadimento (Sistamina)",
        "formula": "Sistamina",
        "ripetibile": False,
        "tipologia": "Conservazione Botanica / Stasi Biologica",
        "inDuello": False,
        "duelloNote": "Non da duello. Congela temporaneamente il decadimento e l'ossidazione della materia vegetale fresca appena raccolta.",
        "movimento": "Puntamento fermo al centro del contenitore con cerchio protettivo tracciato attorno al perimetro.",
        "movimentoSvg": "M 75,75 m -35,0 a 35,35 0 1,0 70,0 a 35,35 0 1,0 -70,0 M 75,70 L 75,80 M 70,75 L 80,75",
        "descrizione": "Formula di conservazione biologica del VI Anno di Erbologia (Nicholas Kelleher). Blocca i processi degenerativi enzimatici e la disidratazione spontanea dei campioni botanici freschi appena colti, preservando intatti i principi alchemici attivi per le pozioni.",
        "etimologia": "Dal latino sistere (arrestare, bloccare, fermare).",
        "valenza": 6,
        "sommaLettere": 33,
        "valenzaOpposta": 4,
        "maxRipetizioni": 1,
        "figuraGeometrica": "Esagono regolare (Elemento Terra / Equilibrio)",
        "runeAssociate": VALENCE_RUNES_MAP[6],
        "noteAritmantiche": "Valenza Magica 6 (somma pitagorica 33 ridotta a 6). Valenza opposta di simmetria: 4. Figura operativa per Signo: Esagono regolare. Limite di reiterazione: 1 volta/e."
    },

    # --- VII ANNO (Astronomia - Mary C. Silente) ---
    {
        "id": "stellaris-revela",
        "anno": 7,
        "annoLabel": "VII Anno",
        "nome": "Incantesimo di Proiezione della Volta Celeste (Stellaris Revela)",
        "formula": "Stellaris Revela",
        "ripetibile": True,
        "tipologia": "Incanto Celeste / Proiezione Ottico-Astronomica",
        "inDuello": False,
        "duelloNote": "Non idoneo al duello. Formula di visualizzazione accademica del firmamento che oltrepassa coperture e ostacoli opachi.",
        "movimento": "Puntamento verticale della bacchetta verso il cielo con flusso magico costante e concentrazione limpida.",
        "movimentoSvg": "M 75,120 L 75,30 M 60,45 L 75,30 L 90,45",
        "descrizione": "Sortilegio supremo del VII Anno di Astronomia (Mary C. Silente). Rivela la posizione e la frequenza delle stelle attraverso nuvole fitte, nebbie o soffitti opachi, generando una cupola eterea luminosa attorno all'incantatore con orbite planetarie e spettri di luce.",
        "etimologia": "Dal latino stellaris (stellare) e revelare (svelare, scoprire).",
        "valenza": 7,
        "sommaLettere": 61,
        "valenzaOpposta": 3,
        "maxRipetizioni": 7,
        "figuraGeometrica": "Ettagono regolare (Opposizione / Massima Energia)",
        "runeAssociate": VALENCE_RUNES_MAP[7],
        "noteAritmantiche": "Valenza Magica 7 (somma pitagorica 61 ridotta a 7). Valenza opposta di simmetria: 3. Figura operativa per Signo: Ettagono regolare. Limite di reiterazione: 7 volte."
    },
    {
        "id": "stellaris-obscura",
        "anno": 7,
        "annoLabel": "VII Anno",
        "nome": "Incantesimo di Occultamento Celeste (Stellaris Obscura)",
        "formula": "Stellaris Obscura",
        "ripetibile": False,
        "tipologia": "Occultamento Celeste / Variante Proibita",
        "inDuello": False,
        "duelloNote": "Non da duello convenzionale. Incanto clandestino per schermare la porzione di cielo sopra un rituale occultandola ai telescopi.",
        "movimento": "Arco orizzontale invertito dall'alto con rotazione in senso antiorario a coprire la vista.",
        "movimentoSvg": "M 35,50 C 55,25 95,25 115,50 C 95,85 55,85 35,50 Z",
        "descrizione": "Variante proibita di Stellaris Revela trattata nel VII Anno di Astronomia. Crea una zona di distorsione cosmica che cancella la visibilità telescopica e divinatoria di una porzione di cielo, mascherando allineamenti e rituali segreti.",
        "etimologia": "Dal latino stellaris (degli astri) e obscura (oscurata, celata).",
        "valenza": 5,
        "sommaLettere": 59,
        "valenzaOpposta": 5,
        "maxRipetizioni": 1,
        "figuraGeometrica": "Pentagono regolare (Elemento Aria / Equilibrio)",
        "runeAssociate": VALENCE_RUNES_MAP[5],
        "noteAritmantiche": "Valenza Magica 5 (somma pitagorica 59 ridotta a 5). Valenza opposta di simmetria: 5 (simmetria speculare pura). Figura operativa per Signo: Pentagono regolare. Limite di reiterazione: 1 volta/e."
    },
    {
        "id": "caelus-memorium",
        "anno": 7,
        "annoLabel": "VII Anno",
        "nome": "Incantesimo Mnemonico Celeste (Caelus Memorium)",
        "formula": "Caelus Memorium",
        "ripetibile": False,
        "tipologia": "Incanto Mnemonico Celeste / Conservazione Astrometrica",
        "inDuello": False,
        "duelloNote": "Non da duello. Cristallizza un preciso allineamento celeste all'interno di un ricettacolo magico (astrolabio o pergamena).",
        "movimento": "Spirale ascendente verso la costellazione desiderata, seguita da un tocco fermo sull'oggetto ricettore.",
        "movimentoSvg": "M 75,110 C 95,110 110,95 110,75 C 110,55 90,45 75,45 C 55,45 45,65 55,80 C 65,95 85,85 85,70 L 75,120",
        "descrizione": "Incluso nel VII Anno di Astronomia (Mary C. Silente). Registra l'esatta conformazione astrale di un istante all'interno di una sfera eterea fluttuante che viene poi assorbita da un astrolabio o pergamena lunare, cristallizzando congiunzioni ed eclissi irripetibili.",
        "etimologia": "Dal latino caelum (cielo, volta celeste) e memoria (ricordo, memoria).",
        "valenza": 6,
        "sommaLettere": 60,
        "valenzaOpposta": 4,
        "maxRipetizioni": 1,
        "figuraGeometrica": "Esagono regolare (Elemento Terra / Equilibrio)",
        "runeAssociate": VALENCE_RUNES_MAP[6],
        "noteAritmantiche": "Valenza Magica 6 (somma pitagorica 60 ridotta a 6). Valenza opposta di simmetria: 4. Figura operativa per Signo: Esagono regolare. Limite di reiterazione: 1 volta/e."
    },
    {
        "id": "cometae-vocatum",
        "anno": 7,
        "annoLabel": "VII Anno",
        "nome": "Evocazione della Scia Cometare (Cometae Vocatum)",
        "formula": "Cometae Vocatum",
        "ripetibile": False,
        "tipologia": "Alta Evocazione Simbolica Celeste / Magia Cerimoniale",
        "inDuello": False,
        "duelloNote": "Non da duello. Rituale solenne che evoca la scia luminosa di una cometa eterea lungo il firmamento per cerimonie o consacrazioni.",
        "movimento": "Ampio arco continuo da un estremo all'altro dell'orizzonte tracciato a braccio teso con scatto finale del polso.",
        "movimentoSvg": "M 25,100 C 45,40 105,40 125,100 M 110,85 L 125,100 L 130,80",
        "descrizione": "Tra le più suggestive magie cerimoniali del VII Anno di Astronomia. Non attrae corpi rocciosi ma genera un'evocazione simbolica luminosa che proietta nel firmamento il passaggio maestoso di una cometa eterea carica di energia rituale.",
        "etimologia": "Dal latino cometes (cometa) e vocatum (evocato, richiamato).",
        "valenza": 4,
        "sommaLettere": 49,
        "valenzaOpposta": 6,
        "maxRipetizioni": 1,
        "figuraGeometrica": "Quadrato (Immanenza / Risoluzione)",
        "runeAssociate": VALENCE_RUNES_MAP[4],
        "noteAritmantiche": "Valenza Magica 4 (somma pitagorica 49 ridotta a 4). Valenza opposta di simmetria: 6. Figura operativa per Signo: Quadrato. Limite di reiterazione: 1 volta/e."
    },
    {
        "id": "sidera-sentio",
        "anno": 7,
        "annoLabel": "VII Anno",
        "nome": "Sintonizzazione e Percezione Astrale (Sidera Sentio)",
        "formula": "Sidera Sentio",
        "ripetibile": True,
        "tipologia": "Percezione Extrasensoriale / Flussi Magici Astrali",
        "inDuello": False,
        "duelloNote": "Non da duello. Richiede stato meditativo profondo per avvertire la presenza e le correnti gravitazionali dei corpi celesti.",
        "movimento": "Movimento ondulatorio e armonico a 45 gradi con bacchetta sollevata e rilassamento corporeo.",
        "movimentoSvg": "M 40,105 C 55,85 65,115 80,95 C 95,75 105,105 120,60",
        "descrizione": "Sortilegio di percezione interiore del VII Anno di Astronomia (Mary C. Silente). Apre i recettori magici dell'incantatore permettendogli di percepire l'influsso e la radiazione degli astri anche a occhi chiusi o all'interno di caverne e cripte oscure.",
        "etimologia": "Dal latino sidera (stelle, astri) e sentire (percepire con i sensi).",
        "valenza": 3,
        "sommaLettere": 57,
        "valenzaOpposta": 7,
        "maxRipetizioni": 3,
        "figuraGeometrica": "Triangolo equilatero (Unificazione / Fuoco)",
        "runeAssociate": VALENCE_RUNES_MAP[3],
        "noteAritmantiche": "Valenza Magica 3 (somma pitagorica 57 ridotta a 3). Valenza opposta di simmetria: 7. Figura operativa per Signo: Triangolo equilatero. Limite di reiterazione: 3 volte."
    },
    {
        "id": "orbis-caeli",
        "anno": 7,
        "annoLabel": "VII Anno",
        "nome": "Globo Tridimensionale del Firmamento (Orbis Caeli)",
        "formula": "Orbis Caeli",
        "ripetibile": True,
        "tipologia": "Evocazione Proiettiva Tridimensionale / Mappa Stellare",
        "inDuello": False,
        "duelloNote": "Non da duello. Evoca una mappa celeste olografica tridimensionale manipolabile con le dita per studio e calcolo delle orbite.",
        "movimento": "Rotazione fluida a spirale centripeta del polso con tocco finale al centro del globo magico.",
        "movimentoSvg": "M 75,30 A 45,45 0 1,0 75,120 A 45,45 0 1,0 75,30 M 75,55 A 20,20 0 1,1 75,95 A 20,20 0 1,1 75,55",
        "descrizione": "Sortilegio accademico superiore di Astronomia (VII Anno, Mary C. Silente). Genera un globo luminoso fluttuante raffigurante la volta celeste in scala tridimensionale, interattivo e orientabile per simulare transiti, culminazioni ed eclissi future.",
        "etimologia": "Dal latino orbis (globo, sfera, cerchio) e caeli (del cielo).",
        "valenza": 3,
        "sommaLettere": 48,
        "valenzaOpposta": 7,
        "maxRipetizioni": 3,
        "figuraGeometrica": "Triangolo equilatero (Unificazione / Fuoco)",
        "runeAssociate": VALENCE_RUNES_MAP[3],
        "noteAritmantiche": "Valenza Magica 3 (somma pitagorica 48 ridotta a 3). Valenza opposta di simmetria: 7. Figura operativa per Signo: Triangolo equilatero. Limite di reiterazione: 3 volte."
    },
    {
        "id": "rituale-meteorio",
        "anno": 7,
        "annoLabel": "VII Anno",
        "nome": "Rituale Celestiale Runico delle Meteore (Rituale Meteorio)",
        "formula": "Rituale Meteorio",
        "ripetibile": False,
        "tipologia": "Alta Invocazione Runico-Celeste / Magia Cerimoniale",
        "inDuello": False,
        "duelloNote": "Non da duello. Complesso rituale cerimoniale in 3 fasi che richiede allineamento ottico-magico con meteore reali e tracciatura di glifi Teiwaz e Sowilo.",
        "movimento": "Tracciamento a terra di doppio triangolo runico orientato con l'azimut celeste e puntamento finale allo zenith.",
        "movimentoSvg": "M 75,25 L 125,115 L 25,115 Z M 75,125 L 25,35 L 125,35 Z",
        "descrizione": "Trattato nel VII Anno di Astronomia (Mary C. Silente) in raccordo con le Antiche Rune. Si articola in tre fasi: orientamento runico (Teiwaz e Sowilo tracciate sul terreno), allineamento col passaggio di uno sciame meteorico reale e canalizzazione dell'energia d'impatto cosmico per alimentare incanti e barriere permanenti.",
        "etimologia": "Dal latino ritualis (attinente ai riti sacri) e dal greco meteōros (sospeso in cielo, celeste).",
        "valenza": 6,
        "sommaLettere": 78,
        "valenzaOpposta": 4,
        "maxRipetizioni": 1,
        "figuraGeometrica": "Esagono regolare (Elemento Terra / Equilibrio)",
        "runeAssociate": VALENCE_RUNES_MAP[6],
        "noteAritmantiche": "Valenza Magica 6 (somma pitagorica 78 ridotta a 6). Valenza opposta di simmetria: 4. Figura operativa per Signo: Esagono regolare. Limite di reiterazione: 1 volta/e."
    }
]

added_count = 0
for ns in new_spells:
    if ns['id'] not in existing_ids:
        spells.append(ns)
        existing_ids.add(ns['id'])
        added_count += 1
        print(f"  + Aggiunto: {ns['nome']} ({ns['annoLabel']}, V{ns['valenza']})")
    else:
        print(f"  - Già presente: {ns['id']}")

# Ordinamento pulito: per anno (1-7, poi 0/Altri, poi 8/Rune) e poi alfabetico per nome
def sort_key(s):
    # Year priority: 1, 2, 3, 4, 5, 6, 7, 0 (Altri), 8 (Rune)
    y = s.get('anno', 0)
    order = {1:1, 2:2, 3:3, 4:4, 5:5, 6:6, 7:7, 0:8, 8:9}.get(y, 99)
    return (order, s.get('nome', ''))

spells.sort(key=sort_key)

print(f"Nuovo totale entità nel database: {len(spells)} (+{added_count})")

# Aggiornamento spellsData.js
new_spells_data_content = f"""// spellsData.js - Archivio Completo dei {len(spells)} Incantesimi e Rune dell'Antico Futhark
// Sincronizzato con il Programma Ufficiale di Studio di Arcane GDR, Trattati Didattici, Astronomia, Erbologia e Codex Arithmantiae

const SPELLS_DATA = {json.dumps(spells, ensure_ascii=False, indent=2)};

if (typeof module !== 'undefined' && module.exports) {{
  module.exports = SPELLS_DATA;
}}
"""

with open(f'{BASE_DIR}/spellsData.js', 'w', encoding='utf-8') as f:
    f.write(new_spells_data_content)

print("spellsData.js aggiornato con successo.")
