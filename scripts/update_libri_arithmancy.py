# -*- coding: utf-8 -*-
import json
import re
import os

BASE_DIR = '/Users/andreamorachioli/.gemini/antigravity/scratch/portale-incantesimi'

pythagorean = {
    'A':1, 'B':2, 'C':3, 'D':4, 'E':5, 'F':6, 'G':7, 'H':8, 'I':9,
    'J':1, 'K':2, 'L':3, 'M':4, 'N':5, 'O':6, 'P':7, 'Q':8, 'R':9,
    'S':1, 'T':2, 'U':3, 'V':4, 'W':5, 'X':6, 'Y':7, 'Z':8
}

geometry_map = {
    1: 'Circonferenza (Elemento Acqua)',
    2: 'Angolo / Linea (Dualismo)',
    3: 'Triangolo equilatero (Unificazione)',
    4: 'Quadrato (Immanenza / Risoluzione)',
    5: 'Pentagono regolare (Elemento Aria / Etere)',
    6: 'Esagono regolare (Elemento Terra / Equilibrio)',
    7: 'Ettagono regolare (Opposizione / Massima Energia)',
    8: 'Ottagono regolare (Elemento Fuoco / Infinito)',
    9: 'Ellisse (Reincarnazione / Dinamismo estremo)'
}

def calc_v(formula):
    clean = [c.upper() for c in formula if c.upper() in pythagorean]
    total = sum(pythagorean[c] for c in clean)
    s = total
    while total > 9:
        total = sum(int(d) for d in str(total))
    return total, s, 5 - total + 5

# Load current spells
with open(f'{BASE_DIR}/spellsData.js', 'r', encoding='utf-8') as f:
    content = f.read()

start = content.find('[')
end = content.rfind(']') + 1
spells = json.loads(content[start:end])

# 1. Update existing spells that belong to Liber Sextus or Septimus
for s in spells:
    if s['id'] == 'prior-incantatem':
        s['anno'] = 6
        s['annoLabel'] = 'VI Anno (Liber Sextus)'
        s['tipologia'] = 'Aritmantico / Indagine / Memoria Bacchette'
        s['noteAritmantiche'] = 'Trattato in Codex Arithmantiae, Liber Sextus (Cap. VII: Le bacchette e l\'aritmologia). Valenza 5 (somma 77 ridotta a 5). Valenza opposta: 5. Figura per Signo: Pentagono regolare.'
    elif s['id'] == 'nodum-solvo':
        s['anno'] = 7
        s['annoLabel'] = 'VII Anno (Liber Septimus)'
        s['tipologia'] = 'Contro-Sigillo Aritmantico'
        s['noteAritmantiche'] = 'Trattato in Codex Arithmantiae, Liber Septimus (Cap. VII: La rottura di un sigillo). Valenza 6 (somma 42 ridotta a 6). Valenza opposta: 4. Figura per Signo: Esagono regolare.'

# Check which IDs already exist
existing_ids = {s['id'] for s in spells}

# New spells from Liber Sextus (Sesto Anno - Spazio e Traslazione)
liber_sextus_spells = [
    {
        'id': 'emineo',
        'anno': 6,
        'annoLabel': 'VI Anno (Liber Sextus)',
        'nome': 'Formula dei Pozzi Comunicanti (Emineo)',
        'formula': 'Emineo',
        'ripetibile': False,
        'tipologia': 'Aritmantico / Traslazione / Pozzi Comunicanti',
        'inDuello': False,
        'duelloNote': 'Non utilizzabile in duello diretto. Formula di attivazione statica del primo pozzo comunicante per la traslazione di oggetti o messaggi.',
        'movimento': 'Rotazione orizzontale in senso orario sul bordo del pozzo seguita da tocco al centro del livello dell\'acqua.',
        'movimentoSvg': 'M 75,30 A 45,45 0 1,1 74,30 Z M 75,55 L 75,95 M 55,75 L 95,75',
        'descrizione': 'Attiva la prima estremità di un sistema di pozzi comunicanti aritmantici. Crea una connessione risonante con la terra e l\'acqua sotterranea per consentire il transito istantaneo.',
        'etimologia': 'Dal latino eminere (innalzarsi, emergere, spiccare all\'esterno).'
    },
    {
        'id': 'emineo-puteus',
        'anno': 6,
        'annoLabel': 'VI Anno (Liber Sextus)',
        'nome': 'Formula di Collegamento Pozzi (Emineo Puteus)',
        'formula': 'Emineo Puteus',
        'ripetibile': False,
        'tipologia': 'Aritmantico / Traslazione / Pozzi Comunicanti',
        'inDuello': False,
        'duelloNote': 'Non utilizzabile in duello. Formula di chiusura e aggancio che collega il secondo pozzo al primo già attivato.',
        'movimento': 'Discesa verticale della bacchetta all\'interno della cavità seguita da una mezzaluna verso l\'alto.',
        'movimentoSvg': 'M 75,25 L 75,95 Q 75,120 105,100',
        'descrizione': 'Stabilisce il ponte magico tra il secondo pozzo comunicante e il primo. Una volta completato il collegamento, qualsiasi oggetto immerso nel primo pozzo emerge simultaneamente nel secondo.',
        'etimologia': 'Dal latino eminere e puteus (pozzo, cavità d\'acqua).'
    },
    {
        'id': 'portus',
        'anno': 6,
        'annoLabel': 'VI Anno (Liber Sextus)',
        'nome': 'Incantesimo Passaporta (Portus)',
        'formula': 'Portus',
        'ripetibile': False,
        'tipologia': 'Aritmantico / Traslazione ad Area',
        'inDuello': False,
        'duelloNote': 'Non da duello d\'attacco rapido; utilizzabile per ritirate tattiche d\'emergenza predisposte o per evacuare alleati su un oggetto prefissato.',
        'movimento': 'Puntamento fermo e prolungato sull\'oggetto con tocco vibrante al termine della formula; rilascia un bagliore azzurro.',
        'movimentoSvg': 'M 40,75 L 110,75 M 90,55 L 110,75 L 90,95 M 75,40 A 35,35 0 0,1 75,110',
        'descrizione': 'Trattato nel Liber Sextus (Cap. IV). Trasforma qualsiasi oggetto comune in una Passaporta abilitata a trasportare chiunque la tocchi a una destinazione e ora prestabilite.',
        'etimologia': 'Dal latino porta (passaggio, varco d\'accesso).'
    },
    {
        'id': 'transatio-objecto',
        'anno': 6,
        'annoLabel': 'VI Anno (Liber Sextus)',
        'nome': 'Triangolo Traslatore (Transatio Objecto)',
        'formula': 'Transatio Objecto',
        'ripetibile': False,
        'tipologia': 'Aritmantico / Traslazione Geometrica',
        'inDuello': True,
        'duelloNote': 'Utilizzabile in duello strategico avanzato: trasferisce all\'istante armi, scudi o trappole tra due aree segnate da triangoli perfetti.',
        'movimento': 'Tracciare due triangoli equilateri concentrici nell\'aria ruotati di 180 gradi con stoccata al vertice superiore.',
        'movimentoSvg': 'M 75,30 L 115,105 L 35,105 Z M 75,115 L 35,40 L 115,40 Z',
        'descrizione': 'Trattato nel Liber Sextus (Cap. V). Crea un condotto di traslazione geometrica istantanea fra due triangoli equilateri tracciati con Signo, smaterializzando e rimaterializzando l\'oggetto bersaglio.',
        'etimologia': 'Dal latino translatio (trasferimento) e objectum (oggetto posto innanzi).'
    }
]

# New spells from Liber Septimus (Settimo Anno - Rituali, Sigilli e Trappole)
liber_septimus_spells = [
    {
        'id': 'abscondas',
        'anno': 7,
        'annoLabel': 'VII Anno (Liber Septimus)',
        'nome': 'Formula Celante di Trappola (Abscondas)',
        'formula': 'Abscondas',
        'ripetibile': True,
        'tipologia': 'Aritmantico / Occultamento di Trappola',
        'inDuello': True,
        'duelloNote': 'Molto efficace in duello tattico e imboscata: cela completamente la runa, il campo d\'attivazione e la presenza della trappola magica preparata sul terreno.',
        'movimento': 'Tre cerchi concentrici discendenti tracciati sopra la trappola con dissolvenza finale verso l\'esterno.',
        'movimentoSvg': 'M 75,35 A 40,40 0 1,1 74,35 Z M 75,50 A 25,25 0 1,1 74,50 Z M 75,65 A 10,10 0 1,1 74,65 Z',
        'descrizione': 'Trattata nel Liber Septimus (Cap. IX & Glossario). Formula celante delle trappole aritmantiche di valenza sei. Occulta la trama energetica del campo e le cariche legate, rendendola impercettibile alla vista.',
        'etimologia': 'Dal latino abscondere (nascondere, sottrarre alla vista).'
    },
    {
        'id': 'fermo',
        'anno': 7,
        'annoLabel': 'VII Anno (Liber Septimus)',
        'nome': 'Formula di Vincolo e Trappola d\'Incanto (Fermo)',
        'formula': 'Fermo',
        'ripetibile': True,
        'tipologia': 'Aritmantico / Trappola d\'Incanto / Vincolo',
        'inDuello': True,
        'duelloNote': 'Utilizzabile in duello: impone un comando coattivo di blocco su un oggetto animato o genera una trappola d\'incanto al suolo. Richiede 7 ripetizioni rituali.',
        'movimento': 'Puntamento fermo e perentorio verso il suolo o l\'oggetto animato con colpo secco discendente.',
        'movimentoSvg': 'M 75,30 L 75,115 M 50,115 L 100,115 M 55,75 L 95,75',
        'descrizione': 'Trattata nel Liber Septimus (Cap. XII). Impone un\'azione vincolante a un oggetto animato o genera un\'area d\'incanto pronta a scattare sul primo bersaglio. Va ripetuta esattamente sette volte.',
        'etimologia': 'Dal latino firmare / fermare (rendere saldo, stabilire un vincolo immutabile).'
    },
    {
        'id': 'in-fine-laqueo',
        'anno': 7,
        'annoLabel': 'VII Anno (Liber Septimus)',
        'nome': 'Interruzione di Trappola Aritmantica (In Fine Laqueo)',
        'formula': 'In Fine Laqueo',
        'ripetibile': False,
        'tipologia': 'Contro-Trappola Aritmantica',
        'inDuello': True,
        'duelloNote': 'Fondamentale in duello tattico: disinnesca all\'istante una propria trappola attiva per permettere il transito sicuro di compagni o per evitare contraccolpi.',
        'movimento': 'Fendente a forbice dall\'esterno verso l\'interno che taglia il vincolo del laccio magico.',
        'movimentoSvg': 'M 35,40 L 115,110 M 115,40 L 35,110',
        'descrizione': 'Trattata nel Liber Septimus (Cap. IX). Formula specifica di disinnesco e interruzione delle trappole aritmantiche. Solo chi ha originariamente creato la trappola può pronunciarla con pieno effetto.',
        'etimologia': 'Dal latino in fine (al termine, alla conclusione) e laqueus (laccio, trappola, cappio).'
    },
    {
        'id': 'quae-reversa',
        'anno': 7,
        'annoLabel': 'VII Anno (Liber Septimus)',
        'nome': 'Formula di Serrata per Trappole (Quae Reversa)',
        'formula': 'Quae Reversa',
        'ripetibile': True,
        'tipologia': 'Aritmantico / Sigillo di Trappola',
        'inDuello': True,
        'duelloNote': 'Utilizzabile in duello: serra e arma i vertici della trappola geometrica. Richiede di essere ripetuta su ciascun vertice del poligono d\'innesco.',
        'movimento': 'Movimento a uncino che si chiude su se stesso toccando ciascun vertice della figura geometrica tracciata.',
        'movimentoSvg': 'M 40,75 Q 75,35 110,75 Q 90,115 55,100 L 75,75',
        'descrizione': 'Trattata nel Liber Septimus (Cap. IX & Glossario). Formula di serrata delle trappole geometriche di valenza 6. Da ripetere su ciascun vertice del perimetro per rendere la chiusura irreversibile per gli intrusi.',
        'etimologia': 'Dal latino quae reversa (ciò che è stato rivoltato o serrato indietro).'
    },
    {
        'id': 'deminatio-gravitas',
        'anno': 7,
        'annoLabel': 'VII Anno (Liber Septimus)',
        'nome': 'Sigillo Antigravitazionale (Deminatio Gravitas)',
        'formula': 'Deminatio Gravitas',
        'ripetibile': False,
        'tipologia': 'Aritmantico / Sigillo Statico di Gravità',
        'inDuello': False,
        'duelloNote': 'Non da duello rapido. Chiude il Sigillo Antigravitazionale in una stanza o deposito, riducendo la forza gravitazionale da 9.8N a 1.6N.',
        'movimento': 'Tracciare un ettagono regolare al suolo con Signo e imprimere la chiusura con puntamento ascendente.',
        'movimentoSvg': 'M 75,25 L 110,45 L 125,85 L 95,115 L 55,115 L 25,85 L 40,45 Z',
        'descrizione': 'Trattata nel Liber Septimus (Cap. VIII). Formula di serrata del Sigillo Antigravitazionale. Altera la fisica magica dell\'area abbattendo la costante di gravità a valori lunari.',
        'etimologia': 'Dal latino deminutio (diminuzione, alleggerimento) e gravitas (peso, gravità terrestre).'
    },
    {
        'id': 'magnes-lathos-addicis',
        'anno': 7,
        'annoLabel': 'VII Anno (Liber Septimus)',
        'nome': 'Sigillo Elettromagnetizzante (Magnes Lathos Addicis)',
        'formula': 'Magnes Lathos Addicis',
        'ripetibile': True,
        'tipologia': 'Aritmantico / Sigillo Magnetico',
        'inDuello': False,
        'duelloNote': 'Non da duello ravvicinato. Sigillo di mezzaluna da ripetere due volte alle estremità per polarizzare metalli e respingere cariche.',
        'movimento': 'Arco a mezzaluna tracciato nell\'aria con tocco vibrante alle due cuspidi estreme.',
        'movimentoSvg': 'M 40,40 A 50,50 0 0,0 40,110 A 35,35 0 0,1 40,40 Z',
        'descrizione': 'Trattato nel Liber Septimus (Cap. VIII). Genera un campo magnetico permanente su oggetti o armature metalliche. Blocca l\'avvicinamento di lame ferrose e devia dardi polarizzati.',
        'etimologia': 'Dal greco magnes (magnete, calamita) e latino addicere (vincolare a forza).'
    },
    {
        'id': 'protegis-hoc-incantementum',
        'anno': 7,
        'annoLabel': 'VII Anno (Liber Septimus)',
        'nome': 'Sigillo di Protezione Caldeo (Protègis Hòc Incanteméntum)',
        'formula': 'Protegis Hoc Incantementum',
        'ripetibile': False,
        'tipologia': 'Aritmantico / Sigillo Protettivo Superiore',
        'inDuello': False,
        'duelloNote': 'Non da duello. Sigillo protettivo caldeo di massima complessità per schermare incantesimi statici di lunga durata o Horcrux.',
        'movimento': 'Ottagono tracciato nello spazio con la bacchetta puntata al centro della sfera di protezione.',
        'movimentoSvg': 'M 50,30 L 100,30 L 125,55 L 125,95 L 100,120 L 50,120 L 25,95 L 25,55 Z',
        'descrizione': 'Trattato nel Liber Septimus (Cap. VIII). Il più impenetrabile dei sigilli difensivi noti nel Codex Arithmantiae: protegge un incanto permanente moltiplicandone le difese contro ogni tentativo di scasso.',
        'etimologia': 'Dalla formula arcaica caldea di protezione incantata e vincolo.'
    },
    {
        'id': 'rotas-sator',
        'anno': 7,
        'annoLabel': 'VII Anno (Liber Septimus)',
        'nome': 'Attivazione del Quadrato di Sator (Rotas Sator)',
        'formula': 'Rotas Opera Tenet Arepo Sator',
        'ripetibile': True,
        'tipologia': 'Aritmantico / Quadrato Palindromo Magico',
        'inDuello': False,
        'duelloNote': 'Non da duello rapido. Richiede cinque ripetizioni consecutive nei quattro sensi del quadrato palindromo.',
        'movimento': 'Disegnare un quadrato perfetto suddiviso in cinque fasce con tocco centrale sulla parola TENET.',
        'movimentoSvg': 'M 35,35 L 115,35 L 115,115 L 35,115 Z M 75,35 L 75,115 M 35,75 L 115,75',
        'descrizione': 'Trattata nel Liber IV e Liber VII del Codex Arithmantiae. Attiva il leggendario Quadrato Palindromo magico di Sator creando una barriera di simmetria perfetta che respinge qualsiasi incantesimo dispari.',
        'etimologia': 'Celebre quadrato magico palindromo latino di epoca romana imperiale.'
    },
    {
        'id': 'capio-memoriam',
        'anno': 7,
        'annoLabel': 'VII Anno (Liber Septimus)',
        'nome': 'Duplicazione dei Ricordi (Capio Memoriam)',
        'formula': 'Capio Memoriam',
        'ripetibile': False,
        'tipologia': 'Aritmantico / Medimagia / Rituale Mentale',
        'inDuello': False,
        'duelloNote': 'Non utilizzabile in duello. Formula del Rituale dei Ricordi Silenti per duplicare ed estrarre memorie senza alterare la mente originale.',
        'movimento': 'Punta della bacchetta a contatto con la tempia, estrazione lenta e continua del filamento argenteo.',
        'movimentoSvg': 'M 40,75 C 60,45 80,105 110,75 L 100,65 M 110,75 L 100,85',
        'descrizione': 'Trattata nel Liber Septimus (Rituale dei Ricordi Silenti & Glossario). Estrae e duplica un ricordo integro dal cervello dell\'incantatore per conservarlo in un pensatoio o in una fiala sigillata.',
        'etimologia': 'Dal latino capere (cogliere, accogliere, catturare) e memoria.'
    }
]

# Enrich and append new spells
for new_s in liber_sextus_spells + liber_septimus_spells:
    if new_s['id'] in existing_ids:
        # Update existing
        for idx, cur in enumerate(spells):
            if cur['id'] == new_s['id']:
                spells[idx].update(new_s)
                v, s_num, opp = calc_v(new_s['formula'])
                spells[idx]['valenza'] = v
                spells[idx]['sommaLettere'] = s_num
                spells[idx]['valenzaOpposta'] = opp
                spells[idx]['maxRipetizioni'] = v if new_s['ripetibile'] else 1
                spells[idx]['figuraGeometrica'] = geometry_map[v]
                spells[idx]['noteAritmantiche'] = f"Valenza Magica {v} (somma pitagorica {s_num} ridotta a {v}). Valenza opposta di simmetria: {opp}. Figura operativa per Signo: {geometry_map[v]}. Limite di reiterazione efficace: {v if new_s['ripetibile'] else 1} volta/e."
                break
    else:
        v, s_num, opp = calc_v(new_s['formula'])
        new_s['valenza'] = v
        new_s['sommaLettere'] = s_num
        new_s['valenzaOpposta'] = opp
        new_s['maxRipetizioni'] = v if new_s['ripetibile'] else 1
        new_s['figuraGeometrica'] = geometry_map[v]
        new_s['noteAritmantiche'] = f"Valenza Magica {v} (somma pitagorica {s_num} ridotta a {v}). Valenza opposta di simmetria: {opp}. Figura operativa per Signo: {geometry_map[v]}. Limite di reiterazione efficace: {v if new_s['ripetibile'] else 1} volta/e."
        spells.append(new_s)

# Save updated spellsData.js
js_output = '''// spellsData.js - Archivio Completo degli Incantesimi suddiviso per Anni
// Fonti: Codex Arithmantiae (Z. & G. Hawstein), Manuale di D.C.A.O. (G. Mortem), Exorcismis Occultis & Maledictio (Y. I. Mortem), Manuale di Trasfigurazione, Dispensa Incantesimi

const SPELLS_DATA = ''' + json.dumps(spells, ensure_ascii=False, indent=2) + ''';

if (typeof module !== "undefined" && module.exports) {
  module.exports = SPELLS_DATA;
}
'''

with open(f'{BASE_DIR}/spellsData.js', 'w', encoding='utf-8') as f:
    f.write(js_output)

print(f"Updated spellsData.js with total {len(spells)} spells!")

# Print stats by year
from collections import Counter
counts = Counter(s['anno'] for s in spells)
for y in sorted(counts.keys()):
    print(f"Anno {y}: {counts[y]} incantesimi")
