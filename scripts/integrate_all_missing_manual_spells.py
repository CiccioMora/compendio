# -*- coding: utf-8 -*-
"""
scripts/integrate_all_missing_manual_spells.py
Integra tutti gli incantesimi mancanti dal manuale ufficiale Arcane GDR (112 pagine),
da Trasfigurazione e DCAO, senza aggiungere duplicati e riallineando gli anni accademici.
"""

import json
import re

BASE_DIR = '/Users/andreamorachioli/.gemini/antigravity/scratch/portale-incantesimi'

PYTHAGOREAN = {
    'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9,
    'J': 1, 'K': 2, 'L': 3, 'M': 4, 'N': 5, 'O': 6, 'P': 7, 'Q': 8, 'R': 9,
    'S': 1, 'T': 2, 'U': 3, 'V': 4, 'W': 5, 'X': 6, 'Y': 7, 'Z': 8
}

GEOMETRY_MAP = {
    1: "Circonferenza (Elemento Acqua)",
    2: "Angolo / Linea (Dualismo / Forza)",
    3: "Triangolo equilatero (Elemento Fuoco Caotico)",
    4: "Quadrato (Risoluzione / Immanenza)",
    5: "Pentagono regolare (Elemento Aria)",
    6: "Esagono regolare (Elemento Terra / Equilibrio)",
    7: "Ettagono regolare (Opposizione / Dono)",
    8: "Ottagono regolare (Elemento Fuoco)",
    9: "Ellisse (Elemento Aria / Tempesta)"
}

VALENCE_RUNES_MAP = {
    1: "ᚠ Fehu (Pos. 1ª)",
    2: "ᚢ Uruz (Pos. 2ª)",
    3: "ᚦ Thurisaz (Pos. 3ª)",
    4: "ᚨ Ansuz (Pos. 4ª)",
    5: "ᚱ Raido (Pos. 5ª)",
    6: "ᚲ Kenaz (Pos. 6ª)",
    7: "ᚷ Gebo (Pos. 7ª)",
    8: "ᚹ Wunjo (Pos. 8ª)",
    9: "ᚺ Hagalaz (Pos. 9ª)"
}

def arith(formula, forced_v=None):
    clean = [c for c in formula.upper() if c in PYTHAGOREAN]
    s = sum(PYTHAGOREAN[c] for c in clean)
    if forced_v:
        r = forced_v
    else:
        r = s
        while r > 9:
            r = sum(int(d) for d in str(r))
    opp = 10 - r
    geom = GEOMETRY_MAP.get(r, "Circonferenza")
    rune = VALENCE_RUNES_MAP.get(r, "ᚠ Fehu (Pos. 1ª)")
    return s, r, opp, geom, rune

# 1. Carica spellsData.js
with open(f'{BASE_DIR}/spellsData.js', 'r', encoding='utf-8') as f:
    text = f.read()
data = json.loads(text[text.find('['):text.rfind(']')+1])

# Costruisci set formule e nomi esistenti per prevenire duplicati
existing_formulas = {re.sub(r'[^a-z0-9]', '', s.get('formula','').lower()) for s in data}
existing_ids = {s.get('id','') for s in data}

# 2. Aggiorna anni accademici degli incantesimi già presenti per allinearli al manuale ufficiale 2026
YEAR_CORRECTIONS = {
    'arresto-momentum': (3, 'III Anno'),
    'immobilus': (3, 'III Anno'),
    'aguamenti': (3, 'III Anno'),
    'incendio': (3, 'III Anno'),
    'ventus': (3, 'III Anno'),
    'locomotor': (4, 'IV Anno'),
    'bagaglius': (4, 'IV Anno'),
    'mobiliarbus': (4, 'IV Anno'),
    'alohomora': (4, 'IV Anno'),
    'colloportus': (4, 'IV Anno'),
    'circumrota': (4, 'IV Anno'),
    'salvio-hexia': (5, 'V Anno'),
    'muffliato': (5, 'V Anno'),
    'alarte-ascenderai': (5, 'V Anno'),
    'rictusempra': (5, 'V Anno'),
    'titillando': (5, 'V Anno'),
    'carpe-retractum': (6, 'VI Anno'),
    'ferula': (2, 'II Anno')
}

for s in data:
    if s.get('id') in YEAR_CORRECTIONS:
        yr, lbl = YEAR_CORRECTIONS[s['id']]
        s['anno'] = yr
        s['annoLabel'] = lbl

# 3. Lista dei nuovi incantesimi verificati senza duplicati
RAW_NEW_SPELLS = [
    # --- TOMO I (I ANNO) ---
    {
        "id": "levioso",
        "anno": 1,
        "annoLabel": "I Anno",
        "nome": "Incantesimo di Librazione (Levioso)",
        "formula": "Levioso",
        "ripetibile": True,
        "tipologia": "Incanto di Levitazione Statica / Utilità",
        "inDuello": True,
        "duelloNote": "Utilizzabile per far levitare staticamente piccoli ostacoli o armi dell'avversario a mezz'aria.",
        "movimento": "Disegnare un 2 ruotato di lato in senso antiorario puntando l'oggetto.",
        "movimentoSvg": "M 40,80 C 40,40 80,40 80,60 C 80,90 40,110 90,110",
        "descrizione": "A differenza di Wingardium Leviosa, che solleva e muove gli oggetti verso l'alto o nello spazio, Levioso li fa levitare staticamente sul posto sfidando la gravità.",
        "etimologia": "Dal latino levis (leggero) e levo (sollevare in equilibrio).",
        "maxRipetizioni": 5
    },
    {
        "id": "ascendio",
        "anno": 1,
        "annoLabel": "I Anno",
        "nome": "Incantesimo di Ascensione (Ascendio)",
        "formula": "Ascendio",
        "ripetibile": False,
        "tipologia": "Auto-Levitazione / Mobilità Personale",
        "inDuello": True,
        "duelloNote": "Permette una rapida fuga verticale da creature furiose o attacchi a terra. Efficace anche sott'acqua.",
        "movimento": "Puntare la punta del catalizzatore mossa con decisione verso il punto più alto (soffitto o cielo).",
        "movimentoSvg": "M 75,120 L 75,30 M 50,55 L 75,30 L 100,55",
        "descrizione": "Sortilegio di auto-levitazione che proietta chi pronuncia la formula rapidamente verso l'alto. Richiede alta concentrazione per non precipitare. Utilizzabile anche per riemergere a razzo dall'acqua.",
        "etimologia": "Dal latino ascendo (innalzarsi, salire verso l'alto).",
        "maxRipetizioni": 2
    },
    {
        "id": "skurge",
        "anno": 1,
        "annoLabel": "I Anno",
        "nome": "Incantesimo Disincrostante Ectoplasmatico (Skurge)",
        "formula": "Skurge",
        "ripetibile": True,
        "tipologia": "Pulizia Avanzata / Anti-Ectoplasma",
        "inDuello": False,
        "duelloNote": "Non da duello classico. Efficace palliativo contro spiriti, spettri e poltergeist.",
        "movimento": "Frustata secca discendente a spirale verso la macchia ectoplasmatica.",
        "movimentoSvg": "M 50,30 C 90,40 90,80 50,90 C 20,95 40,120 80,120",
        "descrizione": "Sortilegio formulato specificamente per eliminare gli ectoplasmi appiccicosi lasciati dai fantasmi e scacciare presenze spettrali fastidiose. Consigliato in sostituzione del Solvente di Nonna Acetonella.",
        "etimologia": "Dall'inglese scourge (flagellare, tormentare, ripulire con forza).",
        "maxRipetizioni": 4
    },
    {
        "id": "tergeo",
        "anno": 1,
        "annoLabel": "I Anno",
        "nome": "Incantesimo Pulente (Tergeo)",
        "formula": "Tergeo",
        "ripetibile": True,
        "tipologia": "Incantesimo di Pulizia Generico / Domestico",
        "inDuello": False,
        "duelloNote": "Non da duello. Utilizzato anche per detergere ferite aperte da corpi estranei lievi.",
        "movimento": "Tocco leggero con sfioramento ad aspirazione della sporcizia.",
        "movimentoSvg": "M 45,75 C 45,50 105,50 105,75 C 105,100 45,100 45,75",
        "descrizione": "Incantesimo generico di pulizia che aspira e rimuove macchie lievi, polvere, liquidi o sangue secco da abiti, superfici o corpi viventi.",
        "etimologia": "Dal verbo latino tergeo (asciugare, nettare, pulire).",
        "maxRipetizioni": 6
    },
    {
        "id": "impervius",
        "anno": 1,
        "annoLabel": "I Anno",
        "nome": "Incantesimo Impermeabile (Impervius)",
        "formula": "Impervius",
        "ripetibile": False,
        "tipologia": "Difensivo Passivo / Idrorepellente",
        "inDuello": False,
        "duelloNote": "Protegge occhiali, vestiti e catalizzatori da pioggia battente, nebbia e schizzi.",
        "movimento": "Circonferenza transitoria seguita da una traccia parallela orizzontale.",
        "movimentoSvg": "M 60,75 A 25,25 0 1,1 60,74 M 35,110 L 115,110",
        "descrizione": "Rende una superficie o indumento completamente impermeabile all'acqua, respingendo gocce, liquidi e fango. Fondamentale nelle partite di Quidditch sotto il diluvio.",
        "etimologia": "Dal latino impervius (impenetrabile, che non lascia passare).",
        "maxRipetizioni": 1
    },
    {
        "id": "oculus-reparo",
        "anno": 1,
        "annoLabel": "I Anno",
        "nome": "Incantesimo Ripara-Occhiali (Oculus Reparo)",
        "formula": "Oculus Reparo",
        "ripetibile": False,
        "tipologia": "Riparazione di Precisione",
        "inDuello": False,
        "duelloNote": "Non da duello. Ripristina istantaneamente lenti scheggiate e montature spezzate.",
        "movimento": "Disegno di due piccoli cerchi concentrici congiunti da una linea a ponte.",
        "movimentoSvg": "M 45,75 A 15,15 0 1,1 45,74 M 60,75 L 90,75 M 105,75 A 15,15 0 1,1 105,74",
        "descrizione": "Declinazione specializzata dell'Incantesimo Riparatore per montature e lenti di occhiali rotti, risaldandone i frammenti senza lasciare opacità.",
        "etimologia": "Dal latino oculus (occhio) e reparo (aggiustare).",
        "maxRipetizioni": 1
    },
    {
        "id": "nox",
        "anno": 1,
        "annoLabel": "I Anno",
        "nome": "Incantesimo Spegni-Bacchetta (Nox)",
        "formula": "Nox",
        "ripetibile": False,
        "tipologia": "Contro-Incanto di Luce / Utilità",
        "inDuello": True,
        "duelloNote": "Spegne istantaneamente la luce della bacchetta per tornare nell'ombra del duello notturno.",
        "movimento": "Tocco secco o lieve scatto verso l'alto con arresto immediato.",
        "movimentoSvg": "M 75,85 L 75,45",
        "descrizione": "Controincantesimo fondamentale di Lumos: estingue istantaneamente la luce emessa dall'apice del catalizzatore riportando l'ambiente all'oscurità naturale.",
        "etimologia": "Dal latino nox (notte, buio).",
        "maxRipetizioni": 1
    },

    # --- TOMO II (II ANNO) ---
    {
        "id": "anapneo",
        "anno": 2,
        "annoLabel": "II Anno",
        "nome": "Incantesimo di Guarigione Respiratoria (Anapneo)",
        "formula": "Anapneo",
        "ripetibile": False,
        "tipologia": "Curativo Medimagico / Pronto Soccorso",
        "inDuello": False,
        "duelloNote": "Utilizzabile per soccorrere compagni soffocati da polveri, corpi estranei o incanti ostruttivi.",
        "movimento": "Puntamento verso il torace o la gola con lieve e rapido movimento ascendente.",
        "movimentoSvg": "M 75,105 L 75,45 M 60,65 L 75,45 L 90,65",
        "descrizione": "Incantesimo di guarigione delle vie aeree: libera istantaneamente la trachea da corpi estranei, saliva o cibi ingeriti provocando colpi di tosse liberatori.",
        "etimologia": "Dal greco an- (privativo) e apnea (senza respiro), 'riprendere fiato'.",
        "maxRipetizioni": 2
    },
    {
        "id": "epismendo",
        "anno": 2,
        "annoLabel": "II Anno",
        "nome": "Incantesimo Emostatico Ripara-Microfratture (Epismendo)",
        "formula": "Epismendo",
        "ripetibile": True,
        "tipologia": "Curativo Medimagico",
        "inDuello": True,
        "duelloNote": "Blocca all'istante emorragie nasali da impatto ed epistassi in combattimento.",
        "movimento": "Pressione direzionale con la punta della bacchetta sul punto lesionato.",
        "movimentoSvg": "M 50,75 L 100,75 M 75,50 L 75,100",
        "descrizione": "Arresta emorragie inarrestabili ed epistassi e risalda microfratture della cartilagine (come il setto nasale). Poco efficace contro maledizioni dissanguanti oscure.",
        "etimologia": "Dal greco antico episkeué (riparazione, restauro).",
        "maxRipetizioni": 3
    },
    {
        "id": "brachium-emendo",
        "anno": 2,
        "annoLabel": "II Anno",
        "nome": "Incantesimo Ripara-Fratture Ossa (Brachium Emendo)",
        "formula": "Brachium Emendo",
        "ripetibile": False,
        "tipologia": "Curativo Chirurgico",
        "inDuello": False,
        "duelloNote": "Richiede immensa precisione fonetica ed esecutiva: un errore elimina le ossa invece di risaldarle.",
        "movimento": "Tracciato rettilineo lungo l'asse dell'arto con bagliore bianco finale.",
        "movimentoSvg": "M 40,50 L 110,50 L 110,100 L 40,100",
        "descrizione": "Emette un bagliore bianco che risalda istantaneamente fratture ossee medie o gravi. Se pronunciato male, 'emendo' elimina l'osso trasformandolo in gomma (rimediabile solo con Ossofast).",
        "etimologia": "Dal latino brachium (braccio) ed emendo (sanare, correggere o rimuovere).",
        "maxRipetizioni": 1
    },
    {
        "id": "aparecium",
        "anno": 2,
        "annoLabel": "II Anno",
        "nome": "Incantesimo Rivelatore di Inchiostri Invisibili (Aparecium)",
        "formula": "Aparecium",
        "ripetibile": False,
        "tipologia": "Incantesimo di Rivelazione Grafica",
        "inDuello": False,
        "duelloNote": "Svela scritture celate da inchiostri simpatici o formule di occultamento cartaceo.",
        "movimento": "Tocco delicato e scorrimento a zig-zag piatto sulla superficie della pergamena.",
        "movimentoSvg": "M 40,50 L 110,50 L 50,85 L 110,85",
        "descrizione": "Fa affiorare istantaneamente testi scritti con inchiostro invisibile, formule segrete e appunti celati su pergamene o libri.",
        "etimologia": "Dal latino appareo (apparire, mostrarsi alla vista).",
        "maxRipetizioni": 2
    },
    {
        "id": "molliare",
        "anno": 2,
        "annoLabel": "II Anno",
        "nome": "Incantesimo Imbottito (Molliare)",
        "formula": "Molliare",
        "ripetibile": False,
        "tipologia": "Incantesimo di Modificazione Materica",
        "inDuello": False,
        "duelloNote": "Utilizzato per creare un cuscino invisibile protettivo sul manico delle scope da corsa.",
        "movimento": "Movimento ondulatorio morbido dall'alto in basso.",
        "movimentoSvg": "M 40,60 Q 75,90 110,60 Q 75,110 40,60",
        "descrizione": "Rende soffice e imbottita una superficie rigida creando una morbidezza invisibile e duratura. Inventato da Elliot Smethwyck nel 1820 per i manici di scopa.",
        "etimologia": "Dal latino mollio (rendere tenero, ammorbidire).",
        "maxRipetizioni": 2
    },

    # --- TOMO III (III ANNO) ---
    {
        "id": "impedimenta",
        "anno": 3,
        "annoLabel": "III Anno",
        "nome": "Incantesimo di Ostacolo (Impedimenta)",
        "formula": "Impedimenta",
        "ripetibile": True,
        "tipologia": "Difensivo / Controllo Cinetico",
        "inDuello": True,
        "duelloNote": "Uno dei pilastri del duello: blocca o rallenta la corsa dell'avversario per diversi secondi.",
        "movimento": "Stoccata orizzontale diretta e decisa da sinistra a destra.",
        "movimentoSvg": "M 40,75 L 110,75 M 95,60 L 110,75 L 95,90",
        "descrizione": "Rallenta o congela sul posto il movimento di persone o oggetti in avvicinamento. Inefficace contro creature dalla pelle magica coriacea (come Graphorn o Tebo) se non colpite sul ventre.",
        "etimologia": "Dal latino impedimentum (ostacolo, intralcio al cammino).",
        "maxRipetizioni": 4
    },
    {
        "id": "fulgari",
        "anno": 3,
        "annoLabel": "III Anno",
        "nome": "Incantesimo di Legamento Luminoso (Fulgari)",
        "formula": "Fulgari",
        "ripetibile": False,
        "tipologia": "Incantesimo di Confinamento / Arresto",
        "inDuello": True,
        "duelloNote": "Lega strettamente le braccia del bersaglio al busto con corde di pura energia luminosa.",
        "movimento": "Movimento rotatorio stretto dei polsi seguito da un fendente centrale.",
        "movimentoSvg": "M 75,30 A 30,30 0 1,1 74,30 M 75,60 L 75,120",
        "descrizione": "Sortilegio che scaturisce corde fulgide e luminose dalla bacchetta, serrando all'istante le braccia dell'avversario e impedendogli di muovere il catalizzatore.",
        "etimologia": "Dal latino fulgur (fulmine, bagliore accecante).",
        "maxRipetizioni": 2
    },
    {
        "id": "emancipare",
        "anno": 3,
        "annoLabel": "III Anno",
        "nome": "Incantesimo di Liberazione dai Vincoli (Emancipare)",
        "formula": "Emancipare",
        "ripetibile": False,
        "tipologia": "Contro-Incanto di Liberazione",
        "inDuello": True,
        "duelloNote": "Scioglie corde, ceppi fisici, bende o legacci luminosi (come quelli di Fulgari o Incarceramus).",
        "movimento": "Doppio taglio a croce diagonale verso i vincoli da recidere.",
        "movimentoSvg": "M 45,45 L 105,105 M 105,45 L 45,105",
        "descrizione": "Controincantesimo specifico che discioglie o spezza istantaneamente vincoli materiali o fasce magiche che imprigionano un mago o un bersaglio.",
        "etimologia": "Dal latino emancipo (liberare dalla patria potestà, affrancare dal vincolo).",
        "maxRipetizioni": 2
    },
    {
        "id": "aqua-eructo",
        "anno": 3,
        "annoLabel": "III Anno",
        "nome": "Incantesimo Idrante a Getto Distruttivo (Aqua Eructo)",
        "formula": "Aqua Eructo",
        "ripetibile": True,
        "tipologia": "Elementale Acqua / Spegnimento Fuoco",
        "inDuello": True,
        "duelloNote": "Scatena un torrente d'acqua ad altissima pressione in grado di respingere nemici e domare fiamme.",
        "movimento": "Movimento sinusoidale continuo culminante in una stoccata orizzontale a pompa.",
        "movimentoSvg": "M 40,85 Q 60,60 80,85 T 120,85",
        "descrizione": "A differenza di Aguamenti, che evoca acqua potabile per sgorgo, Aqua Eructo sprigiona un getto d'acqua continuo e distruttivo ideale per spegnere focolai e travolgere creature di fuoco.",
        "etimologia": "Dal latino aqua (acqua) ed eructo (eruttare, scaturire con veemenza).",
        "maxRipetizioni": 3
    },
    {
        "id": "incantesimo-incendiario",
        "anno": 3,
        "annoLabel": "III Anno",
        "nome": "Incantesimo Incendiario / Muro di Fiamme",
        "formula": "Incendia Flamma",
        "ripetibile": False,
        "tipologia": "Elementale Fuoco Avanzato",
        "inDuello": True,
        "duelloNote": "Erompe una barriera muraria di fiamme ardenti che impedisce il passaggio fisico.",
        "movimento": "Ampio arco orizzontale da sinistra a destra con affondo finale a terra.",
        "movimentoSvg": "M 35,90 Q 75,40 115,90 L 115,120 L 35,120 Z",
        "descrizione": "Sortilegio dalla formula arcaica che innalza una vera e propria cortina di fiamme continue. Ritenuto imparentato con il Fuoco Gubraithiano in quanto non estinguibile con semplice acqua ordinaria.",
        "etimologia": "Dal latino incendia (roghi) e flamma (fiamma viva).",
        "maxRipetizioni": 1
    },
    {
        "id": "testabolla",
        "anno": 3,
        "annoLabel": "III Anno",
        "nome": "Incantesimo Testabolla (Testabolla)",
        "formula": "Testabolla",
        "ripetibile": False,
        "tipologia": "Incantesimo di Respirazione e Protezione Ambientale",
        "inDuello": False,
        "duelloNote": "Consente la respirazione subacquea o in ambienti saturi di fumo, gas asfissianti o polveri velenose.",
        "movimento": "Tracciare una cupola emisferica attorno al proprio capo.",
        "movimentoSvg": "M 45,95 C 45,45 105,45 105,95",
        "descrizione": "Crea una bolla d'aria magica protettiva e perennemente purificata attorno alla testa dell'incantatore, consentendo di respirare sott'acqua o resistere a miasmi pestilenziali.",
        "etimologia": "Dal latino testa (capo) e bolla (sfera d'aria gassosa).",
        "maxRipetizioni": 1
    },
    {
        "id": "furgus",
        "anno": 3,
        "annoLabel": "III Anno",
        "nome": "Incantesimo Fulminante (Furgus)",
        "formula": "Furgus",
        "ripetibile": True,
        "tipologia": "Elementale Elettrico / Offensivo",
        "inDuello": True,
        "duelloNote": "Scatena una saetta elettrica dalla bacchetta provocando una violenta scossa e paralisi temporanea.",
        "movimento": "Movimento angolare a zig-zag evocativo di una saetta verso l'obiettivo.",
        "movimentoSvg": "M 75,25 L 55,70 L 85,70 L 65,125",
        "descrizione": "Sprigiona un fulmine scoppiettante dall'apice della bacchetta. La letalità della scarica è inversamente proporzionale al tono di voce: pronunciato a voce bassa o sussurrata risulta devastante.",
        "etimologia": "Dal latino fulgur / furgus (folgore, fulmine, scarica elettrica).",
        "maxRipetizioni": 3
    },
    {
        "id": "defodio",
        "anno": 3,
        "annoLabel": "III Anno",
        "nome": "Incantesimo di Scavo (Defodio)",
        "formula": "Defodio",
        "ripetibile": True,
        "tipologia": "Modificazione Materica / Scavo",
        "inDuello": False,
        "duelloNote": "Utilizzato dagli Spezzaincantesimi per sbancare roccia, terra friabile e aprire gallerie.",
        "movimento": "Tracciato continuo di una lettera 'e' in corsivo puntata verso il terreno.",
        "movimentoSvg": "M 60,85 C 45,85 45,55 75,55 C 95,55 95,85 60,85 C 60,110 85,110 100,100",
        "descrizione": "Trasforma l'energia della bacchetta in una scavatrice magica, intagliando o sbancando porzioni di terra e roccia senza richiedere alcuno sforzo manuale.",
        "etimologia": "Dal latino defodio (scavare, sventrare la terra, estrarre).",
        "maxRipetizioni": 4
    },
    {
        "id": "dominusterra",
        "anno": 3,
        "annoLabel": "III Anno",
        "nome": "Incantesimo Anti-Levitazione e Tellurico (Dominusterra)",
        "formula": "Dominusterra",
        "ripetibile": False,
        "tipologia": "Gravitazionale / Tellurico",
        "inDuello": True,
        "duelloNote": "Forza al suolo oggetti o nemici sollevati e provoca una vibrazione sismica nel terreno sotto i piedi del nemico.",
        "movimento": "Stoccata perpendicolare diretta verso il basso contro il suolo.",
        "movimentoSvg": "M 75,35 L 75,115 M 50,115 L 100,115",
        "descrizione": "Riporta violentemente verso la superficie bersagli sospesi a mezz'aria. Puntato direttamente verso la terra produce un impulso sismico ondulatorio che sbilancia gli avversari.",
        "etimologia": "Dal latino dominus (padrone) e terra (suolo, terraferma).",
        "maxRipetizioni": 2
    },
    {
        "id": "reducio",
        "anno": 3,
        "annoLabel": "III Anno",
        "nome": "Incantesimo Riducente (Reducio)",
        "formula": "Reducio",
        "ripetibile": True,
        "tipologia": "Modificazione Dimensionale / Contro-Engorgio",
        "inDuello": True,
        "duelloNote": "Controincantesimo immediato di Engorgio, riduce la massa molecolare degli oggetti a dimensioni minime.",
        "movimento": "Disegnare con la bacchetta una 'V' netta con vertice rivolto verso il basso.",
        "movimentoSvg": "M 45,45 L 75,115 L 105,45",
        "descrizione": "Comprime la distanza intermolecolare di un corpo inanimato o animale, rimpicciolendolo sensibilmente o ripristinando le sue dimensioni naturali dopo un ingrandimento.",
        "etimologia": "Dal latino reduco (ricondurre indietro, ridurre di volume).",
        "maxRipetizioni": 3
    },

    # --- TOMO IV (IV ANNO) ---
    {
        "id": "waddiwasi",
        "anno": 4,
        "annoLabel": "IV Anno",
        "nome": "Incantesimo Proiettile (Waddiwasi)",
        "formula": "Waddiwasi",
        "ripetibile": True,
        "tipologia": "Cinetico Balistico / Offensivo",
        "inDuello": True,
        "duelloNote": "Stappa piccoli oggetti incastrati (es. gomma da masticare o pietre) scagliandoli come proiettili nel naso del bersaglio.",
        "movimento": "Gesto fulmineo della mano che richiama il lancio e la punta di un proiettile.",
        "movimentoSvg": "M 55,115 C 55,65 95,65 95,115",
        "descrizione": "Libera piccoli corpi inanimati incastrati in fessure o serrature e li accelera ad altissima velocità verso un obiettivo specifico, colpendolo a sorpresa.",
        "etimologia": "Dallo svedese vadd (ovatta) e dal francese vas-y (vai lì).",
        "maxRipetizioni": 3
    },
    {
        "id": "cistem-aperio",
        "anno": 4,
        "annoLabel": "IV Anno",
        "nome": "Incantesimo di Esplosione a Scatola (Cistem Aperio)",
        "formula": "Cistem Aperio",
        "ripetibile": False,
        "tipologia": "Apertura Meccanica Esplosiva",
        "inDuello": False,
        "duelloNote": "Apre violentemente forzieri, bauli e scatole sigillate facendo saltare il coperchio.",
        "movimento": "Stoccata centrale sul lucchetto seguita da una rapida apertura a ventaglio.",
        "movimentoSvg": "M 75,90 L 75,45 M 50,60 L 75,45 L 100,60",
        "descrizione": "Fa saltare il coperchio di bauli, casseforti ordinarie e scatole mediante un'improvvisa detonazione controllata diretta sul meccanismo di chiusura.",
        "etimologia": "Dal latino cista (baule, cassa) ed aperio (aprire, spalancare).",
        "maxRipetizioni": 2
    },
    {
        "id": "accio",
        "anno": 4,
        "annoLabel": "IV Anno",
        "nome": "Incantesimo di Appello (Accio)",
        "formula": "Accio",
        "ripetibile": True,
        "tipologia": "Cinetico di Richiamo / Fondamentale",
        "inDuello": True,
        "duelloNote": "Richiama a grande velocità verso la mano del mago un oggetto distante o disarmato.",
        "movimento": "Ampia arcata del polso verso il basso senza emissione di luce visibile.",
        "movimentoSvg": "M 45,55 C 45,95 105,95 105,55",
        "descrizione": "Uno dei più antichi e celebri incantesimi del mondo magico. Attira oggetti inanimati o piccoli animali verso l'utilizzatore attraverso il legame mentale e la concentrazione sulla posizione.",
        "etimologia": "Dal latino accio (chiamare a sé, convocare, invitare).",
        "maxRipetizioni": 5
    },
    {
        "id": "depulso",
        "anno": 4,
        "annoLabel": "IV Anno",
        "nome": "Incantesimo di Esilio / Respingimento (Depulso)",
        "formula": "Depulso",
        "ripetibile": True,
        "tipologia": "Cinetico di Allontanamento / Opposto ad Accio",
        "inDuello": True,
        "duelloNote": "Allontana violentemente oggetti o armi scagliandoli lontano dalla portata dell'avversario.",
        "movimento": "Gesto scattante in avanti dal petto verso l'esterno con rilascio del polso.",
        "movimentoSvg": "M 50,90 L 95,45 L 115,70",
        "descrizione": "Controparte speculare dell'incantesimo di appello: scaglia e allontana con forza un oggetto verso un punto distante prefissato dal mago.",
        "etimologia": "Dal verbo latino depello / depulsum (scacciare, respingere con veemenza).",
        "maxRipetizioni": 4
    },

    # --- TOMO V (V ANNO) ---
    {
        "id": "disillusione",
        "anno": 5,
        "annoLabel": "V Anno",
        "nome": "Incantesimo di Disillusione / Mimetismo Camaleontico",
        "formula": "Disillusio",
        "ripetibile": False,
        "tipologia": "Occultamento Ottico / Camuffamento",
        "inDuello": True,
        "duelloNote": "Rende il mago o un oggetto quasi invisibile, facendogli assumere texture e colore dell'ambiente.",
        "movimento": "Roteare la bacchetta su se stessi come avvolgendosi in una fune invisibile o toccare il bersaglio.",
        "movimentoSvg": "M 75,35 A 40,40 0 1,1 74,35 M 75,55 A 20,20 0 1,1 74,55",
        "descrizione": "Fa assumere al bersaglio le esatte sfumature e la trama dello sfondo su cui si trova, conferendo una sensazione come di uovo freddo spaccato sulla testa. I maestri possono rendersi invisibili.",
        "etimologia": "Dal latino dis- (separazione) e illusio (inganno visivo).",
        "maxRipetizioni": 1
    },
    {
        "id": "sonorus",
        "anno": 5,
        "annoLabel": "V Anno",
        "nome": "Incantesimo Amplificatore della Voce (Sonorus)",
        "formula": "Sonorus",
        "ripetibile": False,
        "tipologia": "Modulazione Acustica / Utilità",
        "inDuello": False,
        "duelloNote": "Amplifica la voce del mago per farsi udire attraverso stadi interi senza sforzo.",
        "movimento": "Puntare la punta della bacchetta direttamente a contatto con la gola.",
        "movimentoSvg": "M 45,75 L 105,75 M 105,55 L 105,95",
        "descrizione": "Amplifica enormemente il volume della voce dell'incantatore trasformandola come in un megafono magico naturale, udibile a chilometri di distanza.",
        "etimologia": "Dall'aggettivo latino sonorus (risonante, fragoroso).",
        "maxRipetizioni": 1
    },
    {
        "id": "quietus",
        "anno": 5,
        "annoLabel": "V Anno",
        "nome": "Incantesimo di Calma / Riduzione Sonora (Quietus)",
        "formula": "Quietus",
        "ripetibile": False,
        "tipologia": "Contro-Incanto Acustico",
        "inDuello": False,
        "duelloNote": "Ripristina il volume vocale ordinario o abbassa la voce a livello di sussurro.",
        "movimento": "Movimento discendente armonioso e leggiadro con punta verso la gola.",
        "movimentoSvg": "M 45,45 Q 75,75 105,45",
        "descrizione": "Controincantesimo di Sonorus: attenua i rumori e ristabilisce il normale livello sonoro delle corde vocali.",
        "etimologia": "Dal latino quietus (calmo, silenzioso, pacifico).",
        "maxRipetizioni": 1
    },

    # --- TOMO VI (VI ANNO) ---
    {
        "id": "divversio",
        "anno": 6,
        "annoLabel": "VI Anno",
        "nome": "Incantesimo Rallegrante / Euforia (Divversio)",
        "formula": "Divversio",
        "ripetibile": False,
        "tipologia": "Incantesimo Mentale / Emozionale",
        "inDuello": False,
        "duelloNote": "Lenisce tristezza e paure stimolando risate e serotonina; palliativo contro l'angoscia dei Dissennatori.",
        "movimento": "Disegno di una lettera 'D' coricata a pancia in giù, evocativa di un largo sorriso.",
        "movimentoSvg": "M 45,85 L 105,85 C 105,50 45,50 45,85",
        "descrizione": "Ideato dal giullare Felix Summerbee nel XV secolo: dissipa le sensazioni oscure e infonde uno stato di euforia e allegria. Un uso eccessivo può sfociare in riso isterico.",
        "etimologia": "Dal latino diversio (svago, distrazione, sollievo dell'animo).",
        "maxRipetizioni": 2
    },
    {
        "id": "obliterans",
        "anno": 6,
        "annoLabel": "VI Anno",
        "nome": "Incantesimo Obliterante / Tracce Fisiche (Obliterans)",
        "formula": "Obliterans",
        "ripetibile": True,
        "tipologia": "Occultamento Fisico / Bonifica Tracce",
        "inDuello": False,
        "duelloNote": "Cancella orme, impronte e tracce fisiche lasciate nella neve, fango o sabbia.",
        "movimento": "Movimento rettangolare continuo attorno alla traccia da dissolvere.",
        "movimentoSvg": "M 45,50 L 105,50 L 105,100 L 45,100 Z",
        "descrizione": "A differenza di Deletrius (che cancella tracce e simboli magici), l'Incantesimo Obliterante rimuove le tracce fisiche tangibili lasciate dal passaggio umano, impedendo inseguimenti babbani o magici.",
        "etimologia": "Dal latino oblitero (cancellare, cancellare dalla memoria, disperdere orme).",
        "maxRipetizioni": 3
    },

    # --- TOMO VII (VII ANNO) ---
    {
        "id": "capacius-extremis",
        "anno": 7,
        "annoLabel": "VII Anno",
        "nome": "Incantesimo Estensivo Irriconoscibile (Capacius Extremis)",
        "formula": "Capacius Extremis",
        "ripetibile": False,
        "tipologia": "Spazio e Traslazione Avanzata / M.A.G.O.",
        "inDuello": False,
        "duelloNote": "Espande enormemente il volume interno di bauli e borse mantenendo invariate le dimensioni esterne.",
        "movimento": "Tracciato tridimensionale a cubo espanso dal centro verso l'esterno.",
        "movimentoSvg": "M 50,50 L 90,50 L 110,80 L 70,80 Z M 50,50 L 50,90 L 70,120 L 70,80",
        "descrizione": "Noto anche come Adduco Maxima: dilata i confini spaziali interni di un contenitore rendendo al tempo stesso il carico leggero come una piuma. Rigidissimamente controllato dal Ministero.",
        "etimologia": "Dal latino capax (capiente, ampio) ed extremus (all'estremo grado).",
        "maxRipetizioni": 1
    },
    {
        "id": "fidelio",
        "anno": 7,
        "annoLabel": "VII Anno",
        "nome": "Incantesimo Fidelius (Fidelio)",
        "formula": "Fidelio",
        "ripetibile": False,
        "tipologia": "Magia Antica Atonale / Occultamento Assoluto",
        "inDuello": False,
        "duelloNote": "Nasconde un segreto o luogo all'interno dell'anima di un singolo individuo (Custode del Segreto).",
        "movimento": "Magia atonale antica priva di movimento rigido di polso.",
        "movimentoSvg": "M 75,40 C 50,40 50,90 75,110 C 100,90 100,40 75,40 Z",
        "descrizione": "Una delle più antiche e complesse forme di magia. Rende un luogo invisibile, intangibile, insonorizzato e inaccessibile a chiunque, a meno che il Custode del Segreto non riveli volontariamente l'informazione.",
        "etimologia": "Dal latino fidelis (fedele, fidato).",
        "maxRipetizioni": 1
    },

    # --- CHICCHE DI MAGIA (PAGINA 104) ---
    {
        "id": "colovaria",
        "anno": 0,
        "annoLabel": "Altri",
        "nome": "Incantesimo Muta-Colore (Colovaria)",
        "formula": "Colovaria",
        "ripetibile": True,
        "tipologia": "Chicche di Magia / Alterazione Cromatica",
        "inDuello": False,
        "duelloNote": "Cambia il colore di vestiti, capelli o pareti a piacimento dell'incantatore.",
        "movimento": "Spennellata curva della bacchetta sul bersaglio.",
        "movimentoSvg": "M 45,90 C 60,40 90,40 105,90",
        "descrizione": "Permette di alterare istantaneamente la colorazione del bersaglio selezionato secondo la gamma cromatica visualizzata nella mente.",
        "etimologia": "Dal latino color (colore) e vario (variare, mutare).",
        "maxRipetizioni": 4
    },
    {
        "id": "erecto",
        "anno": 0,
        "annoLabel": "Altri",
        "nome": "Incantesimo di Montaggio e Costruzione (Erecto)",
        "formula": "Erecto",
        "ripetibile": False,
        "tipologia": "Chicche di Magia / Cinetica Architettonica",
        "inDuello": False,
        "duelloNote": "Erige e monta autonomamente tende da campo, impalcature e ripari magici.",
        "movimento": "Gesto verso l'alto con apertura bilaterale delle braccia.",
        "movimentoSvg": "M 75,115 L 75,45 M 45,75 L 105,75",
        "descrizione": "Incantesimo utilitario che assembla, tende e picchetta strutture prefabbricate o tende in pochissimi istanti.",
        "etimologia": "Dal latino erigo / erectum (innalzare, drizzare, costruire).",
        "maxRipetizioni": 2
    },
    {
        "id": "fianto-duri",
        "anno": 0,
        "annoLabel": "Altri",
        "nome": "Incantesimo di Fortificazione Barriere (Fianto Duri)",
        "formula": "Fianto Duri",
        "ripetibile": False,
        "tipologia": "Chicche di Magia / Difensivo Avanzato M.A.G.O.",
        "inDuello": True,
        "duelloNote": "Amplifica scudi d'area disintegrando chi tenta di attraversarli con la forza.",
        "movimento": "Puntamento solido a due mani verso l'alto della cupola protettiva.",
        "movimentoSvg": "M 40,95 A 35,35 0 0,1 110,95 L 110,110 L 40,110 Z",
        "descrizione": "Incantesimo di consolidamento magico che, unito a Protego Maxima e Repello Inimicum, rende le barriere impenetrabili anche all'attacco congiunto di centinaia di maghi.",
        "etimologia": "Dal latino fio (diventare) e durus (duro, infrangibile).",
        "maxRipetizioni": 1
    },
    {
        "id": "finestra",
        "anno": 0,
        "annoLabel": "Altri",
        "nome": "Incantesimo Frantuma-Vetri Senza Schegge (Finestra)",
        "formula": "Finestra",
        "ripetibile": False,
        "tipologia": "Chicche di Magia / Infiltrazione M.A.G.O.",
        "inDuello": False,
        "duelloNote": "Polverizza vetrate e finestre riducendole a pulviscolo senza emettere rumore o schegge pericolose.",
        "movimento": "Picchiettio secco al centro del vetro seguito da un cerchio rapido.",
        "movimentoSvg": "M 75,75 M 50,75 A 25,25 0 1,1 50,74",
        "descrizione": "Sortilegio di precisione che dissolve istantaneamente lastre di vetro trasformandole in una polvere finissima, evitando scheggiature o ferite.",
        "etimologia": "Dall'italiano finestra.",
        "maxRipetizioni": 2
    },
    {
        "id": "illegibilus",
        "anno": 0,
        "annoLabel": "Altri",
        "nome": "Incantesimo Rendi-Illegibile (Illegibilus)",
        "formula": "Illegibilus",
        "ripetibile": False,
        "tipologia": "Chicche di Magia / Riservatezza Documentale",
        "inDuello": False,
        "duelloNote": "Trasforma le scritte su pergamena in un groviglio di segni indecifrabili.",
        "movimento": "Ondulazione orizzontale a linea continua sopra il testo.",
        "movimentoSvg": "M 40,65 Q 60,85 80,65 T 120,65",
        "descrizione": "Offusca i caratteri grafici su documenti sensibili rendendoli visivamente incomprensibili a chi non possiede la chiave di rimozione.",
        "etimologia": "Dall'inglese illegible / latino illegibilis (non leggibile).",
        "maxRipetizioni": 2
    },
    {
        "id": "imperturbabile",
        "anno": 0,
        "annoLabel": "Altri",
        "nome": "Incantesimo Imperturbabile (Imperturbabile)",
        "formula": "Imperturbabile",
        "ripetibile": False,
        "tipologia": "Chicche di Magia / Barriera Oggetti e Suoni M.A.G.O.",
        "inDuello": False,
        "duelloNote": "Crea una barriera invisibile che blocca fisicamente l'accesso a porte e intercetta ogni suono o orecchio allungabile.",
        "movimento": "Tracciato solido attorno al telaio dell'ingresso o superficie.",
        "movimentoSvg": "M 45,115 L 45,45 L 105,45 L 105,115",
        "descrizione": "Sigilla porte o varchi contro intrusioni fisiche o sonore; qualsiasi oggetto rimbalza all'indietro e nessun suono può filtrare.",
        "etimologia": "Dal latino imperturbabilis (che non può essere turbato o penetrato).",
        "maxRipetizioni": 1
    },
    {
        "id": "lavapiatti",
        "anno": 0,
        "annoLabel": "Altri",
        "nome": "Incantesimo Domestico Lavapiatti",
        "formula": "Lavapiatti",
        "ripetibile": True,
        "tipologia": "Chicche di Magia / Magia Domestica",
        "inDuello": False,
        "duelloNote": "Anima spugne e sapone per far lavare e asciugare le stoviglie in autonomia.",
        "movimento": "Doppio cerchio rapido rivolto verso il lavello.",
        "movimentoSvg": "M 55,75 A 15,15 0 1,1 55,74 M 95,75 A 15,15 0 1,1 95,74",
        "descrizione": "Comando domestico che conferisce autonomia alle stoviglie sporche affinché si insaponino e si sciacquino da sole.",
        "etimologia": "Composto italiano lava e piatti.",
        "maxRipetizioni": 3
    },
    {
        "id": "pluma-levis",
        "anno": 0,
        "annoLabel": "Altri",
        "nome": "Incanto Leggero come una Piuma",
        "formula": "Pluma Levis",
        "ripetibile": False,
        "tipologia": "Chicche di Magia / Riduzione Peso M.A.G.O.",
        "inDuello": False,
        "duelloNote": "Annulla il peso corporeo percepito di carichi massicci rendendoli maneggevoli come piume.",
        "movimento": "Disegno di una curva ascendente sinuosa come una piuma che fluttua.",
        "movimentoSvg": "M 50,110 C 60,70 90,70 100,30",
        "descrizione": "Incantesimo di riduzione della densità ponderale di un oggetto, consentendo a un singolo mago di trasportare massi o mobili pesantissimi senza fatica.",
        "etimologia": "Dal latino pluma (piuma) e levis (leggero).",
        "maxRipetizioni": 2
    },
    {
        "id": "aetas-limen",
        "anno": 0,
        "annoLabel": "Altri",
        "nome": "Incantesimo Linea dell'Età",
        "formula": "Aetas Limen",
        "ripetibile": False,
        "tipologia": "Chicche di Magia / Barriera d'Accesso M.A.G.O.",
        "inDuello": False,
        "duelloNote": "Traccia una linea dorata sul pavimento insuperabile per chi non ha raggiunto una determinata età anagrafica.",
        "movimento": "Incisione lineare sul pavimento con rotazione completa a cerchio aureo.",
        "movimentoSvg": "M 35,75 L 115,75 M 75,55 A 20,20 0 1,1 75,95",
        "descrizione": "Sortilegio di confinamento impenetrabile a chiunque sia al di sotto dell'età richiesta. Immune a tentativi di inganno tramite Pozioni Invecchianti o Polisucco.",
        "etimologia": "Dal latino aetas (età) e limen (soglia, confine).",
        "maxRipetizioni": 1
    },

    # --- CAPITOLI SPECIALI DEL MANUALE ---
    {
        "id": "appare-vestigium",
        "anno": 0,
        "annoLabel": "Altri",
        "nome": "Incantesimo Rivelatore di Tracce Recenti (Appare Vestigium)",
        "formula": "Appare Vestigium",
        "ripetibile": False,
        "tipologia": "Investigativo / Scanner Magico",
        "inDuello": False,
        "duelloNote": "Genera un vortice aureo che rivela orme, smaterializzazioni e incantesimi lanciati nei giorni precedenti.",
        "movimento": "Vortice continuo evocato dalla punta del catalizzatore di colore oro.",
        "movimentoSvg": "M 75,75 m -35,0 a 35,35 0 1,0 70,0 a 35,35 0 1,0 -70,0",
        "descrizione": "Sortilegio investigativo di altissimo livello: scansiona un'intera area mostrando come in una registrazione tridimensionale dorata tutte le magie, passaggi di creature e azioni avvenute nei giorni precedenti.",
        "etimologia": "Dal latino appare (mostrati) e vestigium (orma, traccia).",
        "maxRipetizioni": 1
    },
    {
        "id": "maleficium-revelio",
        "anno": 0,
        "annoLabel": "Altri",
        "nome": "Incantesimo Rivelatore di Magia Oscura (Maleficium Revelio)",
        "formula": "Maleficium Revelio",
        "ripetibile": False,
        "tipologia": "Rivelazione Forense / Anti-Magia Oscura",
        "inDuello": False,
        "duelloNote": "Ispeziona oggetti per scoprire fatture, veleni o maledizioni attive in corso di esecuzione.",
        "movimento": "Cerchio cauto attorno all'oggetto con stoccata d'avvicinamento.",
        "movimentoSvg": "M 55,75 A 20,20 0 1,1 55,74 L 85,75",
        "descrizione": "Permette di identificare se un oggetto sia stato corrotto o imbevuto di magia oscura, fatture o malefici dormienti pronti a scattare.",
        "etimologia": "Dal latino maleficium (fattura, delitto oscuro) e revelo (svelare).",
        "maxRipetizioni": 2
    },
    {
        "id": "hommenum-revelio",
        "anno": 0,
        "annoLabel": "Altri",
        "nome": "Incantesimo Rivelatore di Presenze Umane (Hommenum Revelio)",
        "formula": "Hommenum Revelio",
        "ripetibile": False,
        "tipologia": "Rilevazione di Presenza",
        "inDuello": True,
        "duelloNote": "Percepisce istantaneamente la presenza di qualsiasi essere umano nell'edificio, anche se sotto Mantello dell'Invisibilità.",
        "movimento": "Arco aperto verso l'alto con percezione delle vibrazioni.",
        "movimentoSvg": "M 45,90 Q 75,35 105,90",
        "descrizione": "Rivela la presenza e il battito vitale di esseri umani nell'ambiente circostante, penetrando disillusioni ordinarie e mantelli invisibili.",
        "etimologia": "Dal latino homo / hominem (essere umano) e revelo (rivelare).",
        "maxRipetizioni": 2
    },
    {
        "id": "vinculum-revelio",
        "anno": 0,
        "annoLabel": "Altri",
        "nome": "Incantesimo Rivelatore di Legami Runici (Vinculum Revelio)",
        "formula": "Vinculum Revelio",
        "ripetibile": False,
        "tipologia": "Magia Runica Investigativa / Aritmanzia",
        "inDuello": False,
        "duelloNote": "Ripercorre incisioni runiche mostrando con una linea di luce i legami attivi tra di esse.",
        "movimento": "Ripercorrere la forma dei simboli per poi tracciare una linea che li unisce.",
        "movimentoSvg": "M 40,75 L 75,45 L 110,75 M 40,75 L 110,75",
        "descrizione": "Evidenzia i fili invisibili d'energia che collegano tra loro rune incise su un supporto materiale, confermando l'attivazione di Triadi o cerchi di confinamento.",
        "etimologia": "Dal latino vinculum (legame, vincolo) e revelo (scoprire).",
        "maxRipetizioni": 2
    },
    {
        "id": "revelio-minimum",
        "anno": 0,
        "annoLabel": "Altri",
        "nome": "Incantesimo Rivelatore di Pozioni di Scarpin (Revelio Minimum)",
        "formula": "Revelio Minimum",
        "ripetibile": False,
        "tipologia": "Rivelazione Analitica di Pozioni",
        "inDuello": False,
        "duelloNote": "Analizza un preparato o veleno restituendo l'elenco esatto degli ingredienti e delle dosi.",
        "movimento": "Movimento circolare lento sopra il calderone o la fiala con goccia terminale.",
        "movimentoSvg": "M 75,45 A 25,25 0 1,1 74,45 M 75,70 L 75,105",
        "descrizione": "Ideato dal pozionista Scarpin: analizza la struttura molecolare di una miscela svelandone ogni singolo elemento chimico-magico e le proporzioni necessarie per formulare l'antidoto (Leggi di Golpalott).",
        "etimologia": "Dal latino revelo (svelare) e minimum (ai minimi dettagli atomici).",
        "maxRipetizioni": 1
    },
    {
        "id": "avenseguim",
        "anno": 0,
        "annoLabel": "Altri",
        "nome": "Incantesimo di Tracciamento a Ritroso (Avenseguim)",
        "formula": "Avenseguim",
        "ripetibile": False,
        "tipologia": "Localizzazione e Tracciamento Forense",
        "inDuello": False,
        "duelloNote": "Anima un oggetto facendolo librare a ritroso sui luoghi in cui è stato e verso il proprietario.",
        "movimento": "Puntamento sull'oggetto seguito da un arco a mezzaluna.",
        "movimentoSvg": "M 50,50 Q 85,75 50,100",
        "descrizione": "Consente a un reperto (es. un'arma o un pugnale) di ripercorrere all'indietro i propri spostamenti per condurre gli investigatori alla sua origine o al possessore originale.",
        "etimologia": "Dal latino ad-venio (giungere) e sequor (seguire a ritroso).",
        "maxRipetizioni": 1
    },
    {
        "id": "bombarda-maxima",
        "anno": 6,
        "annoLabel": "VI Anno",
        "nome": "Sortilegio Esplosivo Massimizzato (Bombarda Maxima)",
        "formula": "Bombarda Maxima",
        "ripetibile": False,
        "tipologia": "Sortilegio Esplosivo Massimizzato / Distruzione Ostacoli",
        "inDuello": True,
        "duelloNote": "Genera una deflagrazione devastante capace di far crollare intere mura e cancellate di ferro.",
        "movimento": "Stoccata esplosiva a due mani con caricamento del polso e scatto violento in avanti.",
        "movimentoSvg": "M 45,75 L 105,75 M 105,45 L 105,105 M 65,55 L 85,95",
        "descrizione": "Versione massimizzata dell'incantesimo Bombarda. Produce un'onda d'urto e un'esplosione distruttiva amplificata, in grado di polverizzare barriere spesse e porte blindate.",
        "etimologia": "Dall'italiano bombarda e latino maxima (massima, suprema).",
        "maxRipetizioni": 1
    },
    {
        "id": "adesio-perpetua",
        "anno": 0,
        "annoLabel": "Altri",
        "nome": "Incantesimo di Adesione Permanente (Adesio Perpetua)",
        "formula": "Adesio Perpetua",
        "ripetibile": False,
        "tipologia": "Sigillo Materico / Incollamento Permanente",
        "inDuello": False,
        "duelloNote": "Incolla in modo indissolubile un oggetto a una superficie (come i ritratti dei Black).",
        "movimento": "Pressione prolungata con la punta della bacchetta seguita da un sigillo quadrato.",
        "movimentoSvg": "M 50,50 L 100,50 L 100,100 L 50,100 Z",
        "descrizione": "Fissa permanentemente un oggetto a una parete o pavimento. Rende l'oggetto inamovibile da qualsiasi forza fisica o comune controincantesimo.",
        "etimologia": "Dal latino adhaesio (aderenza) e perpetua (eterna).",
        "maxRipetizioni": 1
    },
    {
        "id": "protego-maxima",
        "anno": 6,
        "annoLabel": "VI Anno",
        "nome": "Barriera Protettiva Massimizzata (Protego Maxima)",
        "formula": "Protego Maxima",
        "ripetibile": False,
        "tipologia": "Difensivo Massimizzato / Protezione d'Area",
        "inDuello": True,
        "duelloNote": "Forma uno scudo ad alta resilienza in grado di reggere attacchi multipli e simultanei.",
        "movimento": "Ampia rotazione ascendente della bacchetta che racchiude l'intero perimetro dell'incantatore.",
        "movimentoSvg": "M 35,95 A 40,40 0 1,1 115,95",
        "descrizione": "Evoluzione avanzata del Sortilegio Scudo: erige una barriera protettiva spessa e semi-tangibile capace di deflettere sortilegi ad alta intensità lanciati da più avversari.",
        "etimologia": "Dal latino protego (proteggere) e maxima (massima).",
        "maxRipetizioni": 2
    },
    {
        "id": "protego-horribilis",
        "anno": 7,
        "annoLabel": "VII Anno",
        "nome": "Barriera Avanzata Anti-Maledizioni (Protego Horribilis)",
        "formula": "Protego Horribilis",
        "ripetibile": False,
        "tipologia": "D.C.A.O. Avanzata / Protezione Oscura",
        "inDuello": True,
        "duelloNote": "Specializzazione di vertice per arginare e deviare maledizioni oscure di immenso spessore magico.",
        "movimento": "Doppio scatto incrociato con rilascio di un bagliore azzurro-fumo denso.",
        "movimentoSvg": "M 40,40 L 110,110 M 110,40 L 40,110 M 75,30 L 75,120",
        "descrizione": "Scudo di livello M.A.G.O. specificamente concepito per intercettare forme di Magia Oscura e anatemi complessi, impedendo danni irreversibili a chi si trova dietro la linea difensiva.",
        "etimologia": "Dal latino protego (difendere) e horribilis (orribile, spaventoso).",
        "maxRipetizioni": 1
    },
    {
        "id": "protego-diabolica",
        "anno": 7,
        "annoLabel": "VII Anno",
        "nome": "Incantesimo Protettivo del Fuoco Nero (Protego Diabolica)",
        "formula": "Protego Diabolica",
        "ripetibile": False,
        "tipologia": "Magia Difensiva e Distruttiva Suprema",
        "inDuello": True,
        "duelloNote": "Evoca un anello fiammeggiante nero che distrugge all'istante i nemici lasciando illesi gli alleati.",
        "movimento": "Cerchio completo tracciato a terra con fendente infuocato verso l'alto.",
        "movimentoSvg": "M 75,75 m -45,0 a 45,45 0 1,0 90,0 a 45,45 0 1,0 -90,0 M 75,30 L 75,75",
        "descrizione": "Genera una colonna circolare di fiamme nere e bluastre attorno all'incantatore. Chiunque sia ostile o traditore viene incenerito al tocco, mentre gli alleati possono varcare la soglia senza subire alcun danno.",
        "etimologia": "Dal latino protego (proteggo) e diabolica (infernale, diabolica).",
        "maxRipetizioni": 1
    },
    {
        "id": "repello-babbanum",
        "anno": 0,
        "annoLabel": "Altri",
        "nome": "Incantesimo Scaccia-Babbani (Repello Babbanum)",
        "formula": "Repello Babbanum",
        "ripetibile": False,
        "tipologia": "Occultamento Territoriale / Statuto di Segretezza",
        "inDuello": False,
        "duelloNote": "Fa ricordare ai Babbani impegni improvvisi costringendoli ad allontanarsi dall'area magica.",
        "movimento": "Gesto di spinta circolare verso i confini del terreno.",
        "movimentoSvg": "M 40,75 C 60,45 90,45 110,75 C 90,105 60,105 40,75",
        "descrizione": "Incantesimo fondamentale dello Statuto di Segretezza: induce nei Babbani che si avvicinano un'improvvisa amnesia o la sensazione di dover sbrigare una commissione urgente altrove.",
        "etimologia": "Dal latino repello (respingere) e babbanum (babbano).",
        "maxRipetizioni": 1
    },
    {
        "id": "aberto",
        "anno": 0,
        "annoLabel": "Altri",
        "nome": "Antico Incantesimo di Apertura (Aberto)",
        "formula": "Aberto",
        "ripetibile": True,
        "tipologia": "Incantesimo di Sblocco Tradizionale",
        "inDuello": False,
        "duelloNote": "Antica formula per dischiudere porte e passaggi non sigillati da magia oscura.",
        "movimento": "Movimento del polso a mezza luna verso l'esterno.",
        "movimentoSvg": "M 55,45 C 85,45 85,105 55,105",
        "descrizione": "Una delle formule più antiche del repertorio magico per aprire porte chiuse a chiave senza forzarne i cardini.",
        "etimologia": "Dallo spagnolo / portoghese aberto (aperto) o latino aperio.",
        "maxRipetizioni": 3
    },
    {
        "id": "portaberto",
        "anno": 0,
        "annoLabel": "Altri",
        "nome": "Incantesimo Rudimentale di Sblocco Porta (Portaberto)",
        "formula": "Portaberto",
        "ripetibile": False,
        "tipologia": "Incantesimo di Sblocco Arcaico",
        "inDuello": False,
        "duelloNote": "Fa saltare la toppa della porta lasciando talvolta un buco fumante.",
        "movimento": "Stoccata brusca diretta alla toppa della serratura.",
        "movimentoSvg": "M 50,75 L 90,75 M 90,65 L 105,75 L 90,85",
        "descrizione": "Precursore rudimentale di Alohomora impiegato prima del XVII secolo. Apriva le porte provocando spesso danni da fumo e scheggiature al legno della serratura.",
        "etimologia": "Composto latino porta e aperto.",
        "maxRipetizioni": 2
    },
    {
        "id": "liberate",
        "anno": 0,
        "annoLabel": "Altri",
        "nome": "Incantesimo di Apertura Varchi (Liberate)",
        "formula": "Liberate",
        "ripetibile": False,
        "tipologia": "Incantesimo di Apertura Porte e Varchi",
        "inDuello": False,
        "duelloNote": "Dischiude cancellate e grate metalliche allentandone i catenacci.",
        "movimento": "Gesto a fendente orizzontale seguito da apertura verso destra.",
        "movimentoSvg": "M 45,75 L 85,75 L 105,50",
        "descrizione": "Variante dell'incanto di apertura adatta a sbloccare grate, catenacci multipli e varchi vincolati.",
        "etimologia": "Dal latino liberare (rendere libero, sgombrare).",
        "maxRipetizioni": 2
    },
    {
        "id": "dunamis",
        "anno": 0,
        "annoLabel": "Altri",
        "nome": "Incantesimo di Apertura a Forza Bruta (Dunamis)",
        "formula": "Dunamis",
        "ripetibile": False,
        "tipologia": "Sblocco Cinetico Esplosivo",
        "inDuello": True,
        "duelloNote": "Sfondamento a forza d'urto di porte pesanti, simile a un piccolo Bombarda.",
        "movimento": "Affondo potente con scatto in avanti dell'avambraccio.",
        "movimentoSvg": "M 45,75 L 105,75 M 85,55 L 105,75 L 85,95",
        "descrizione": "Spalanca porte e portoni blindati applicando una violenta pressione cinetica, abbattendo catenacci e scardinando cardini arrugginiti.",
        "etimologia": "Dal greco antico dynamis (potenza, forza, energia vitale).",
        "maxRipetizioni": 2
    },

    # --- DAL MANUALE DI TRASFIGURAZIONE ED EVOCAZIONE ---
    {
        "id": "ebublio",
        "anno": 4,
        "annoLabel": "IV Anno",
        "nome": "Fattura / Evocazione delle Bolle d'Aria (Ebublio)",
        "formula": "Ebublio",
        "ripetibile": True,
        "tipologia": "Trasfigurazione Animata / Evocazione Elementale",
        "inDuello": True,
        "duelloNote": "Intrappola l'avversario o oggetti all'interno di una gigantesca bolla d'aria indistruttibile.",
        "movimento": "Disegno a spirale circolare ascendente dall'apice della bacchetta.",
        "movimentoSvg": "M 75,105 A 30,30 0 1,1 75,45 A 30,30 0 1,1 75,105",
        "descrizione": "Sortilegio catalogato tra le evocazioni tecniche: imprigiona il bersaglio in una sfera d'aria trasparente elastica che lo sospende a mezz'aria, annullandone le mosse.",
        "etimologia": "Dal latino ebullio (gorgogliare, erompere in bolle).",
        "maxRipetizioni": 3
    },
    {
        "id": "obscuro",
        "anno": 4,
        "annoLabel": "IV Anno",
        "nome": "Incantesimo di Bendatura Oculare Improvvisa (Obscuro)",
        "formula": "Obscuro",
        "ripetibile": False,
        "tipologia": "Evocazione / Accecamento Tattico",
        "inDuello": True,
        "duelloNote": "Materializza all'istante una benda di stoffa scura ben annodata sugli occhi del bersaglio.",
        "movimento": "Doppia stoccata orizzontale all'altezza degli occhi con scatto indietro.",
        "movimentoSvg": "M 40,70 L 110,70 M 40,80 L 110,80",
        "descrizione": "Sortilegio evocativo che genera istantaneamente una benda coprente attorno agli occhi del nemico, privandolo della vista e della linea di tiro per i suoi incanti.",
        "etimologia": "Dal verbo latino obscuro (oscurare, rendere cieco alla vista).",
        "maxRipetizioni": 2
    },
    {
        "id": "serpensortia",
        "anno": 2,
        "annoLabel": "II Anno",
        "nome": "Incantesimo di Evocazione Serpente (Serpensortia)",
        "formula": "Serpensortia",
        "ripetibile": False,
        "tipologia": "Evocazione Zoo-Trasfigurativa",
        "inDuello": True,
        "duelloNote": "Evoca un serpente vivo dalla bacchetta pronto a fronteggiare l'avversario.",
        "movimento": "Colpo di frusta sinuoso a forma di serpente che termina verso il terreno.",
        "movimentoSvg": "M 45,45 Q 75,65 50,85 T 105,105",
        "descrizione": "Emette dall'apice della bacchetta un serpente vivo che si scaglia verso il bersaglio. Annullabile con l'incantesimo di evanescenza o Vipera Evanesca.",
        "etimologia": "Dal latino serpens (serpente) e ortus / sortiri (scaturire, nascere).",
        "maxRipetizioni": 2
    },
    {
        "id": "pulveris",
        "anno": 3,
        "annoLabel": "III Anno",
        "nome": "Incantesimo di Evocazione Polvere e Cenere (Pulveris)",
        "formula": "Pulveris",
        "ripetibile": True,
        "tipologia": "Evocazione Materica / Disturbante",
        "inDuello": True,
        "duelloNote": "Solleva una densa nube di cenere e polvere che acceca e fa tossire gli avversari.",
        "movimento": "Sventagliata orizzontale rapida all'altezza del petto.",
        "movimentoSvg": "M 40,75 Q 75,95 110,75",
        "descrizione": "Evoca dal nulla una nube densa e soffocante di polvere e residui cenerini, ideale per coprire una ritirata strategica o disorientare i nemici.",
        "etimologia": "Dal latino pulveris (della polvere, pulviscolo).",
        "maxRipetizioni": 3
    },
    {
        "id": "slugulus-eructo",
        "anno": 2,
        "annoLabel": "II Anno",
        "nome": "Fattura Mangialumache (Slugulus Eructo)",
        "formula": "Slugulus Eructo",
        "ripetibile": False,
        "tipologia": "Fattura Disgustante / Evocazione Interna",
        "inDuello": True,
        "duelloNote": "Costringe la vittima a vomitare viscide lumache senza sosta per diverse ore.",
        "movimento": "Gesto circolare stretto terminante con un affondo verso la bocca del nemico.",
        "movimentoSvg": "M 75,45 C 50,45 50,85 75,85 C 95,85 95,115 65,115",
        "descrizione": "Celebre fattura che provoca conati irrefrenabili di lumache viscide. Non neutralizzabile con comune evanescenza, richiede tempo o una specifica contro-fattura.",
        "etimologia": "Dall'inglese slug (lumaca) e dal latino eructo (eruttare, vomitare).",
        "maxRipetizioni": 1
    },

    # --- DAL MANUALE DI D.C.A.O. ---
    {
        "id": "imposium",
        "anno": 4,
        "annoLabel": "IV Anno",
        "nome": "Incantesimo di Imbrigliamento Kelpie (Imposium)",
        "formula": "Imposium",
        "ripetibile": False,
        "tipologia": "D.C.A.O. Specialistica / Soggiogamento Creature",
        "inDuello": False,
        "duelloNote": "Infonde una testiera e briglie magiche sulla testa di un Kelpie rendendolo docile e cavalcabile.",
        "movimento": "Lancio a cappio energetico attorno al collo della creatura.",
        "movimentoSvg": "M 75,35 C 50,35 50,85 75,85 C 100,85 100,35 75,35 M 75,85 L 75,120",
        "descrizione": "Sortilegio fondamentale di Difesa contro Creature Oscure: applica una briglia magica (detta Imposium) al Kelpie, bloccandone l'istinto predatorio e rendendolo completamente sottomesso.",
        "etimologia": "Dal latino impositum (imporre, applicare sopra un freno).",
        "maxRipetizioni": 1
    }
]

added_count = 0
for raw in RAW_NEW_SPELLS:
    clean_f = re.sub(r'[^a-z0-9]', '', raw['formula'].lower())
    if clean_f in existing_formulas or raw['id'] in existing_ids:
        print(f"Skipping already existing: {raw['formula']}")
        continue

    # Calcolo aritmantico
    s_let, val, opp, geom, rune = arith(raw['formula'])

    note_aritm = f"Valenza Magica {val} (somma pitagorica {s_let} ridotta a {val}). Valenza opposta di simmetria: {opp}. Figura geometrica operativa: {geom}. Limite di reiterazione efficace: {raw.get('maxRipetizioni', 1)} volte."

    spell_obj = {
        "id": raw['id'],
        "anno": raw['anno'],
        "annoLabel": raw['annoLabel'],
        "nome": raw['nome'],
        "formula": raw['formula'],
        "ripetibile": raw['ripetibile'],
        "tipologia": raw['tipologia'],
        "inDuello": raw['inDuello'],
        "duelloNote": raw['duelloNote'],
        "movimento": raw['movimento'],
        "movimentoSvg": raw['movimentoSvg'],
        "descrizione": raw['descrizione'],
        "etimologia": raw['etimologia'],
        "valenza": val,
        "sommaLettere": s_let,
        "valenzaOpposta": opp,
        "maxRipetizioni": raw.get('maxRipetizioni', 1),
        "figuraGeometrica": geom,
        "noteAritmantiche": note_aritm,
        "runeAssociate": rune
    }

    data.append(spell_obj)
    existing_formulas.add(clean_f)
    existing_ids.add(raw['id'])
    added_count += 1

print(f"Aggiunti {added_count} nuovi incantesimi canonici.")

# Ordina l'archivio: incantesimi prima (per anno da 1 a 7, poi 0), poi le 25 rune (anno 8)
def sort_key(s):
    if s.get('isRune'):
        return (8, s.get('posizioneNum', 99), s.get('nome',''))
    yr = s.get('anno', 0)
    yr_order = 99 if yr == 0 else yr
    return (yr_order, s.get('nome',''))

data.sort(key=sort_key)

# Riscrivi spellsData.js
new_spells_data_content = f"""// spellsData.js - Archivio Completo dei {len(data)} Incantesimi e Rune dell'Antico Futhark
// Sincronizzato con il Programma Ufficiale di Studio di Arcane GDR, Trattati Didattici, Astronomia, Erbologia e Codex Arithmantiae

const SPELLS_DATA = {json.dumps(data, ensure_ascii=False, indent=2)};
"""

with open(f'{BASE_DIR}/spellsData.js', 'w', encoding='utf-8') as f:
    f.write(new_spells_data_content)

print(f"spellsData.js completato con successo. Totale record nel database: {len(data)}")
