# -*- coding: utf-8 -*-
import json

pythagorean = {
    'A':1, 'B':2, 'C':3, 'D':4, 'E':5, 'F':6, 'G':7, 'H':8, 'I':9,
    'J':1, 'K':2, 'L':3, 'M':4, 'N':5, 'O':6, 'P':7, 'Q':8, 'R':9,
    'S':1, 'T':2, 'U':3, 'V':4, 'W':5, 'X':6, 'Y':7, 'Z':8
}

def calc_v(formula):
    clean = [c.upper() for c in formula if c.upper() in pythagorean]
    total = sum(pythagorean[c] for c in clean)
    s = total
    while total > 9:
        total = sum(int(d) for d in str(total))
    return total, s

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

raw_spells = [
  # --- I ANNO ---
  {
    'id': 'flipendo', 'anno': 1, 'annoLabel': 'I Anno', 'nome': 'Maleficio di Respinta (Flipendo)',
    'formula': 'Flipendo', 'ripetibile': True, 'tipologia': 'Offensivo / Respinta', 'inDuello': True,
    'duelloNote': 'Utilizzabile in duello. Efficace per sbilanciare l'avversario, farlo indietreggiare bruscamente o interrompere la concentrazione e il puntamento.',
    'movimento': 'Movimento deciso del polso dal basso verso l'alto con una frustata diagonale secca verso il bersaglio.',
    'movimentoSvg': 'M 30,120 Q 50,40 120,30 L 110,45',
    'descrizione': 'Sortilegio che scaglia all'indietro il bersaglio o lo fa cadere al suolo. All'impatto produce un rumore secco e genera la sensazione di un pugno diretto al torace o di una padellata alla testa. Ampiamente impiegato dalla Task Force dello Statuto di Segretezza per respingere creature come Gnomi e Pixie.',
    'etimologia': 'Dall'inglese 'to flip' (rovesciare, scagliare con un colpo secco).'
  },
  {
    'id': 'expelliarmus', 'anno': 1, 'annoLabel': 'I Anno', 'nome': 'Incantesimo di Disarmo (Expelliarmus)',
    'formula': 'Expelliarmus', 'ripetibile': False, 'tipologia': 'Difensivo / Disarmo', 'inDuello': True,
    'duelloNote': 'Fondamentale in duello. L'incantesimo per eccellenza per privare l'avversario della bacchetta o di qualunque arma impugnata, chiudendo lo scontro senza spargimento di sangue.',
    'movimento': 'Spirale rapida e fluida in senso orario che termina con una stoccata orizzontale diretta alla mano armata del bersaglio.',
    'movimentoSvg': 'M 75,75 m -35,0 a 35,35 0 1,1 70,0 a 20,20 0 1,1 -40,0 L 130,75',
    'descrizione': 'Emette un accecante fascio di luce scarlatta che stacca con forza la bacchetta o qualsiasi arma dalla mano dell'avversario, proiettandola verso l'alto o verso l'incantatore. Alcuni storici ne attribuiscono l'invenzione a Merlino, altri al Madagascar dell'XI secolo; divenne celebre nel 1379 quando Elizabeth Smudgling lo usò nel torneo di Dartmoor.',
    'etimologia': 'Dal latino 'expellere' (scacciare, espellere) e 'armus' (arma, braccio).'
  },
  {
    'id': 'innerva', 'anno': 1, 'annoLabel': 'I Anno', 'nome': 'Incantesimo Energizzante (Innerva)',
    'formula': 'Innerva', 'ripetibile': False, 'tipologia': 'Curativo / Rianimazione', 'inDuello': True,
    'duelloNote': 'Utilizzabile in duello a squadre o coppie. Indispensabile per risvegliare e rimettere in piedi un alleato colpito da uno Schiantesimo (Stupeficium).',
    'movimento': 'Puntamento calmo e tocco vibrante con la punta della bacchetta all'altezza del plesso solare o della fronte del soggetto privo di sensi; luce dorata.',
    'movimentoSvg': 'M 75,20 L 75,100 M 55,100 L 95,100 M 75,100 L 75,120',
    'descrizione': 'Sortilegio di risveglio concepito specificamente per neutralizzare gli effetti degli schiantesimi. Non va assolutamente confuso con Reinnerva: Innerva agisce sul trauma magico da svenimento indotto da sortilegi come Stupeficium.',
    'etimologia': 'Dal prefisso intensivo 'in-' e dal latino 'nervus' (vigore, fibra, nervo).'
  },
  {
    'id': 'reinnerva', 'anno': 1, 'annoLabel': 'I Anno', 'nome': 'Incantesimo Rigenerante (Reinnerva)',
    'formula': 'Reinnerva', 'ripetibile': False, 'tipologia': 'Curativo / Medimagia', 'inDuello': False,
    'duelloNote': 'Non utilizzabile in duello. Efficace esclusivamente per far riprendere conoscenza a chi è svenuto per cause biologiche o naturali (affaticamento, spavento, calo di pressione), inefficace contro schiantesimi.',
    'movimento': 'Ampio cerchio orizzontale in senso orario sopra il busto seguito da movimento lungo il corpo; luce dorata.',
    'movimentoSvg': 'M 75,35 A 40,40 0 1,1 74,35 M 75,75 L 75,125 L 85,115',
    'descrizione': 'Incantesimo di ripristino delle funzioni vitali e della lucidità in soggetti che hanno perso conoscenza per cause non magiche. Utilizzato in infermeria e nei primi soccorsi.',
    'etimologia': 'Dal latino 're-' (di nuovo) e 'innervare' (donare nuova fibra e vigore).'
  },
  {
    'id': 'protego', 'anno': 1, 'annoLabel': 'I Anno', 'nome': 'Sortilegio Scudo (Protego)',
    'formula': 'Protego', 'ripetibile': True, 'tipologia': 'Difensivo', 'inDuello': True,
    'duelloNote': 'Il cardine assoluto della difesa in duello. Evoca uno scudo magico invisibile capace di deflettere fatture, schiantesimi e proiettili fisici. Inefficace solo contro l'Avada Kedavra.',
    'movimento': 'Movimento rapido a mezzaluna ascendente dal fianco fino a proteggere l'intero busto, con la bacchetta tenuta inclinata a 45 gradi.',
    'movimentoSvg': 'M 30,110 C 40,40 110,40 120,110',
    'descrizione': 'Genera una barriera translucida invisibile che riflette verso l'esterno gli incantesimi scagliati contro l'incantatore e blocca gli attacchi fisici. Reso celebre nel 1484 dal duello tra Hannah Cockleford e il tiranno Earl di Paunchley a Poppleton.',
    'etimologia': 'Dal verbo latino 'protegere' (riparare, difendere, fare da scudo).'
  },
  {
    'id': 'levicorpus', 'anno': 1, 'annoLabel': 'I Anno', 'nome': 'Incantesimo di Sospensione (Levicorpus)',
    'formula': 'Levicorpus', 'ripetibile': False, 'tipologia': 'Offensivo / Non-Verbale / Disabilitazione', 'inDuello': True,
    'duelloNote': 'Formidabile in duello: concepito per essere scagliato in modo non-verbale. Solleva l'avversario a mezz'aria per la caviglia, disorientandolo e impedendogli di mirare.',
    'movimento': 'Scatto rapido e verticale del polso dal basso verso l'alto come ad agganciare un laccio invisibile.',
    'movimentoSvg': 'M 75,125 L 75,35 M 60,50 L 75,35 L 90,50',
    'descrizione': 'Incantesimo ideato da Severus Piton ai tempi della scuola. Afferra la vittima per una caviglia invisibile e la proietta a testa in giù a mezz'aria. Se pronunciato verbalmente perde gran parte della sua efficacia e immediatezza.',
    'etimologia': 'Dal latino 'levare' (sollevare in alto) e 'corpus' (il corpo).'
  },
  {
    'id': 'liberacorpus', 'anno': 1, 'annoLabel': 'I Anno', 'nome': 'Contro-incanto di Sospensione (Liberacorpus)',
    'formula': 'Liberacorpus', 'ripetibile': False, 'tipologia': 'Contro-incantesimo / Difensivo', 'inDuello': True,
    'duelloNote': 'Utilizzabile in duello per liberare sé stessi (se capaci di lancio non-verbale) o un compagno sospeso dall'incantesimo Levicorpus.',
    'movimento': 'Fendente netto del polso dall'alto verso il basso a tagliare il vincolo di sospensione.',
    'movimentoSvg': 'M 75,25 L 75,115 M 60,100 L 75,115 L 90,100',
    'descrizione': 'Il naturale contro-incanto ideato da Severus Piton per annullare istantaneamente l'effetto di Levicorpus, rilasciando la vittima a terra.',
    'etimologia': 'Dal latino 'liberare' (sciogliere dai ceppi) e 'corpus' (corpo).'
  },
  {
    'id': 'stupeficium', 'anno': 1, 'annoLabel': 'I Anno', 'nome': 'Schiantesimo (Stupeficium)',
    'formula': 'Stupeficium', 'ripetibile': True, 'tipologia': 'Offensivo / Schiantesimo', 'inDuello': True,
    'duelloNote': 'L'arma offensiva principale e più diffusa del duello magico. Mette fuori combattimento l'avversario provocando uno svenimento immediato.',
    'movimento': 'Due cerchi concentrici tracciati nell'aria seguiti da un rapido e violento movimento dall'alto verso il basso, come una sferzata.',
    'movimentoSvg': 'M 75,30 A 45,45 0 1,1 74,30 M 75,45 A 30,30 0 1,1 74,45 M 75,45 L 75,125',
    'descrizione': 'Emette un dardo di energia rosso brillante che fa volare all'indietro e priva di sensi la persona colpita per un tempo considerevole. Efficace contro umani, Berretti Rossi e Pogrebin; inefficace contro pelli coriacee (Draghi, Giganti).',
    'etimologia': 'Dal latino 'stupefactus' (stordito, reso privo di sensi) e 'facere' (rendere).'
  },
  {
    'id': 'verdimillious', 'anno': 1, 'annoLabel': 'I Anno', 'nome': 'Sortilegio di Scintille Verdi (Verdimillious)',
    'formula': 'Verdimillious', 'ripetibile': True, 'tipologia': 'Offensivo / Tattico / Segnalazione', 'inDuello': True,
    'duelloNote': 'Utilizzabile in duello per accecare temporaneamente il rivale, rompere la concentrazione o illuminare oggetti nascosti. Non ha effetto letale.',
    'movimento': 'Movimento rotatorio circolare a spirale che si apre in avanti rilasciando uno scoppiettio di scintille smeraldine.',
    'movimentoSvg': 'M 40,110 C 30,50 110,30 110,80 C 110,110 60,110 60,80 C 60,60 90,60 90,75 L 125,75',
    'descrizione': 'Genera una raffica sibilante di faville e luce verde smeraldo dalla punta della bacchetta. Usato sia per segnalare la propria posizione in pericolo sia per accecare il nemico nei duelli ravvicinati. Non ha alcun effetto contro i Gytrash.',
    'etimologia': 'Dal francese/latino 'vert' (verde) e 'mille' (migliaia di scintille).'
  },
  {
    'id': 'wingardium-leviosa', 'anno': 1, 'annoLabel': 'I Anno', 'nome': 'Incantesimo di Levitazione Inanimata (Wingardium Leviosa)',
    'formula': 'Wingardium Leviosa', 'ripetibile': True, 'tipologia': 'Utilità / Cinetica / Levitazione', 'inDuello': True,
    'duelloNote': 'Utilizzabile in duello: permette di sollevare e scagliare pesanti oggetti, massi o mobili contro l'avversario, oppure manipolare i suoi indumenti per sbilanciarlo.',
    'movimento': 'Disegnare un numero 2 ruotato di lato in senso antiorario puntando con decisione l'oggetto alla fine.',
    'movimentoSvg': 'M 40,55 C 40,35 70,30 90,50 C 95,65 70,95 45,110 L 115,110',
    'descrizione': 'Celebre incantesimo che annulla la forza di gravità su oggetti inanimati o indumenti, permettendo di sollevarli e guidarli nell'aria con estrema precisione. Non agisce direttamente sulla carne umana. Contro-incanto: Finite Incantatem, Depulso o Relascio.',
    'etimologia': 'Composto dall'inglese 'wing' (ala), latino 'arduus' (alto) e 'levis' (leggero).'
  },
  {
    'id': 'lumos', 'anno': 1, 'annoLabel': 'I Anno', 'nome': 'Incantesimo Accendi-Bacchetta (Lumos)',
    'formula': 'Lumos', 'ripetibile': True, 'tipologia': 'Utilità / Luce Pura', 'inDuello': True,
    'duelloNote': 'Utilizzabile in duello per accecare la vista dell'avversario a distanza ravvicinata, illuminare aree buie o scacciare creature spettrali come i Marciotti (costringendoli alla forma solida).',
    'movimento': 'Tenere la bacchetta verticalmente e tracciare un cerchietto all'apice.',
    'movimentoSvg': 'M 75,120 L 75,55 M 75,35 A 15,15 0 1,1 74,35 Z',
    'descrizione': 'Ideato nel 1772 da Levina Monkstanley presso il Ministero della Magia per ritrovare una penna caduta. Genera una viva sorgente di luce bianca all'apice della bacchetta. La punta si riscalda e richiede attenzione con materiali infiammabili.',
    'etimologia': 'Dal latino 'lumen' (luce, splendore).'
  },
  {
    'id': 'alohomora', 'anno': 1, 'annoLabel': 'I Anno', 'nome': 'Incantesimo di Apertura Porte (Alohomora)',
    'formula': 'Alohomora', 'ripetibile': False, 'tipologia': 'Utilità / Scasso Magico', 'inDuello': False,
    'duelloNote': 'Non utilizzabile in duello. Serve per aprire porte, bauli e serrature chiuse magicamente o meccanicamente.',
    'movimento': 'Tracciare un cerchio in senso antiorario e, appena completato, una retta discendente perpendicolare.',
    'movimentoSvg': 'M 75,35 A 35,35 0 1,0 74,35 M 75,70 L 75,125',
    'descrizione': 'Introdotto a Londra nel Seicento dall'esploratore magico Eldon Elsrickle (che lo apprese in Africa occidentale, con il significato di 'amico dei ladri'). Scatta e apre serrature ordinarie e sigilli non rinforzati con rune antiche.',
    'etimologia': 'Da dialetto dell'Africa occidentale ('favorevole ai ladri').'
  },
  {
    'id': 'colloportus', 'anno': 1, 'annoLabel': 'I Anno', 'nome': 'Incantesimo di Chiusura Porte (Colloportus)',
    'formula': 'Colloportus', 'ripetibile': False, 'tipologia': 'Difensivo / Sigillo Meccanico', 'inDuello': False,
    'duelloNote': 'Utilizzabile in ritirata tattica: sigilla ermeticamente una porta alle proprie spalle impedendo l'inseguimento nemico.',
    'movimento': 'Movimento squadrato netto a disegnare un rettangolo intorno alla serratura da sigillare.',
    'movimentoSvg': 'M 45,45 L 105,45 L 105,105 L 45,105 Z',
    'descrizione': 'Ideato da Blagdon Blay per contrastare i furti sistematici compiuti da Eldon Elsrickle. Sigilla con un rumore di risucchio porte e battenti.',
    'etimologia': 'Dal latino 'colligere' (legare insieme) e 'portus' (porta, passaggio).'
  },
  {
    'id': 'reparo', 'anno': 1, 'annoLabel': 'I Anno', 'nome': 'Incantesimo Riparatore (Reparo)',
    'formula': 'Reparo', 'ripetibile': True, 'tipologia': 'Utilità / Ricostruzione', 'inDuello': False,
    'duelloNote': 'Non utilizzabile in duello. Risana oggetti rotti, vetri in frantumi e meccanismi spezzati.',
    'movimento': 'Disegnare tante curve continue e morbide con la bacchetta mentre si pronuncia la formula puntando l'oggetto.',
    'movimentoSvg': 'M 35,75 Q 55,45 75,75 Q 95,105 115,75',
    'descrizione': 'Incantesimo pre-medievale fondamentale nella quotidianità magica. Ricompone le parti spezzate e le risalda all'istante. Su edifici e intere stanze distrutte viene applicato da squadre di obliviatori del Dipartimento Catastrofi.',
    'etimologia': 'Dal latino 'reparare' (aggiustare, rimettere in pristino).'
  },
  {
    'id': 'diffindo', 'anno': 1, 'annoLabel': 'I Anno', 'nome': 'Incantesimo di Taglio (Diffindo)',
    'formula': 'Diffindo', 'ripetibile': True, 'tipologia': 'Offensivo / Utilità / Taglio', 'inDuello': True,
    'duelloNote': 'Molto efficace in duello. Può recidere cinghie, corde, vesti o infliggere tagli netti e dolorosi a distanza.',
    'movimento': 'Fendente diagonale netto della bacchetta visualizzando mentalmente la profondità e la direzione del taglio.',
    'movimentoSvg': 'M 35,35 L 115,115 M 100,115 L 115,115 L 115,100',
    'descrizione': 'Ideato nel XV secolo dalla sarta magica Delfina Crimp. Trancia materiali di ogni consistenza (stoffa, legno, cuoio, carne). Se visualizzato con violenza può infliggere ferite lacero-contuse profonde. Parabile con Protego.',
    'etimologia': 'Dal latino 'diffindere' (fendere, spaccare in due).'
  },
  {
    'id': 'incendio', 'anno': 1, 'annoLabel': 'I Anno', 'nome': 'Incantesimo del Fuoco (Incendio)',
    'formula': 'Incendio', 'ripetibile': True, 'tipologia': 'Offensivo / Elementale Fuoco', 'inDuello': True,
    'duelloNote': 'Utilizzabile in duello: genera fiammate e barriere di fuoco, o un'esplosione fiammeggiante con rincorsa. Ottimo per liberarsi da piante aggressive come il Tranello del Diavolo.',
    'movimento': 'Gesto curvo ascendente che richiama la sagoma sinuosa di una fiamma viva.',
    'movimentoSvg': 'M 75,120 C 50,100 45,70 65,55 C 65,40 75,25 75,25 C 75,25 85,40 85,55 C 105,70 100,100 75,120 Z',
    'descrizione': 'Emette una fiammata o proietta lingue di fuoco ardente dalla bacchetta. Impiegato sia nella vita quotidiana sia nel duello difensivo ed offensivo. Contromisure: Aguamenti, Protego, Finite Incantatem.',
    'etimologia': 'Dal latino 'incendere' (appiccare fuoco, infiammare).'
  },

  # --- II ANNO ---
  {
    'id': 'fumos', 'anno': 2, 'annoLabel': 'II Anno', 'nome': 'Incantesimo Fumogeno (Fumos)',
    'formula': 'Fumos', 'ripetibile': True, 'tipologia': 'Difensivo / Occultamento / Tattico', 'inDuello': True,
    'duelloNote': 'Utilissimo in duello per spezzare la linea visiva avversaria, occultare il proprio posizionamento o favorire un disimpegno tattico.',
    'movimento': 'Movimento circolare continuo e morbido della bacchetta a disegnare una spirale d'aria davanti a sé.',
    'movimentoSvg': 'M 75,75 m -40,0 a 40,40 0 1,0 80,0 a 40,40 0 1,0 -80,0',
    'descrizione': 'Genera una nube densa e persistente di fumo grigio-nerastro che esce dal catalizzatore e avvolge rapidamente l'area, impedendo all'avversario di prendere la mira.',
    'etimologia': 'Dal latino 'fumus' (fumo, vapore denso).'
  },
  {
    'id': 'homorphus', 'anno': 2, 'annoLabel': 'II Anno', 'nome': 'Incanto Homorphus',
    'formula': 'Homorphus', 'ripetibile': False, 'tipologia': 'Modificazione / Anti-Licantropo', 'inDuello': False,
    'duelloNote': 'Non impiegabile nei duelli tradizionali tra maghi. È un incanto specialistico concepito per forzare la regressione umana di un lupo mannaro.',
    'movimento': 'Puntamento fermo e risoluto a distanza verso la gola o il plesso del licantropo, rigorosamente non-verbale.',
    'movimentoSvg': 'M 35,75 L 115,75 M 100,60 L 115,75 L 100,90',
    'descrizione': 'Complesso sortilegio non-verbale ideato da uno stregone armeno per costringere un licantropo mutato a riassumere provvisoriamente la forma umana per il tempo necessario alla cattura. Non costituisce una cura permanente.',
    'etimologia': 'Dal greco 'homo' (uomo) e 'morphe' (forma).'
  },
  {
    'id': 'peskipiksi-pesternomi', 'anno': 2, 'annoLabel': 'II Anno', 'nome': 'Incanto anti-Pixie (Peskipiksi Pesternomi)',
    'formula': 'Peskipiksi Pesternomi', 'ripetibile': False, 'tipologia': 'Controllo Creature', 'inDuello': False,
    'duelloNote': 'Non utilizzabile in duello tra maghi. Sortilegio mirato esclusivamente a placare o neutralizzare i Pixie della Cornovaglia.',
    'movimento': 'Movimento rapido e a zig-zag nell'aria verso lo stormo di creature.',
    'movimentoSvg': 'M 30,40 L 70,70 L 40,95 L 110,120',
    'descrizione': 'Sortilegio volto a paralizzare o catturare i pestiferi Pixie blu. Data l'estrema velocità di queste creature, si raccomanda di combinarlo con un incantesimo congelante (Glacius).',
    'etimologia': 'Storpiatura di 'pesky pixie pester no more'.'
  },
  {
    'id': 'petrificus-totalus', 'anno': 2, 'annoLabel': 'II Anno', 'nome': 'Pastoia Totale / Pietrificante (Petrificus Totalus)',
    'formula': 'Petrificus Totalus', 'ripetibile': False, 'tipologia': 'Fattura / Paralisi Totale', 'inDuello': True,
    'duelloNote': 'Altamente efficace in duello: serra all'istante le braccia e le gambe dell'avversario facendolo cadere rigido come una tavola, neutralizzando ogni minaccia fisica e verbale.',
    'movimento': 'Disegnare una chiocciola a mezz'aria con la punta del catalizzatore e stoccata finale.',
    'movimentoSvg': 'M 75,75 m -35,0 a 35,35 0 1,1 70,0 a 20,20 0 1,1 -40,0 L 125,75',
    'descrizione': 'Sortilegio della Famiglia delle Pastoie che irrigidisce completamente il sistema muscolare e scheletrico del bersaglio con un lampo di luce azzurra. Gli occhi continuano a muoversi. L'effetto dura tra le 3 e le 4 ore salvo rilascio con Finite Incantem.',
    'etimologia': 'Dal greco 'petros' (pietra), latino 'facere' (rendere) e 'totalus' (completamente).'
  },
  {
    'id': 'acutus', 'anno': 2, 'annoLabel': 'II Anno', 'nome': 'Trasfigurazione in Ago (Acutus)',
    'formula': 'Acutus', 'ripetibile': False, 'tipologia': 'Trasfigurazione Inanimata', 'inDuello': True,
    'duelloNote': 'Utilizzabile in duello trasfigurativo: trasforma all'istante sassi o frammenti in aghi metallici acuminati d'acciaio da scagliare.',
    'movimento': 'Puntamento rapido verso l'oggetto con tocco discendente secco e affilato.',
    'movimentoSvg': 'M 75,25 L 75,125 M 65,40 L 75,25 L 85,40',
    'descrizione': 'Trasfigura un oggetto inanimato di partenza in un ago d'acciaio appuntito e maneggevole. Modifica Spazio e Struttura riducendo il volume originario.',
    'etimologia': 'Dal latino 'acutus' (aguzzo, affilato, appuntito).'
  },
  {
    'id': 'malum', 'anno': 2, 'annoLabel': 'II Anno', 'nome': 'Trasfigurazione in Mela (Malum)',
    'formula': 'Malum', 'ripetibile': False, 'tipologia': 'Trasfigurazione Inanimata', 'inDuello': False,
    'duelloNote': 'Non da duello. Esercizio classico di secondo anno di Trasfigurazione Inanimata.',
    'movimento': 'Arco tondeggiante con leggera battuta piatta alla base.',
    'movimentoSvg': 'M 75,35 C 45,35 35,70 50,110 C 65,120 85,120 100,110 C 115,70 105,35 75,35 Z M 75,35 L 75,20',
    'descrizione': 'Converte un oggetto inanimato in una mela non commestibile (nel pieno rispetto del Divieto di Gamp sul cibo).',
    'etimologia': 'Dal latino 'malum' (mela, frutto).'
  },
  {
    'id': 'gommosus', 'anno': 2, 'annoLabel': 'II Anno', 'nome': 'Incantesimo di Ammorbidimento (Gommosus)',
    'formula': 'Gommosus', 'ripetibile': False, 'tipologia': 'Trasfigurazione Inanimata / Elasticità', 'inDuello': True,
    'duelloNote': 'Utilizzabile in duello per rendere elastica una parete o il suolo quando un alleato sta per essere scaraventato contro di essi, prevenendo lesioni da urto.',
    'movimento': 'Disegnare una lettera S sinuosa che termina direttamente sull'oggetto bersaglio.',
    'movimentoSvg': 'M 95,35 C 55,35 55,75 75,75 C 95,75 95,115 55,115',
    'descrizione': 'Altera temporaneamente le proprietà meccaniche e la consistenza di una superficie solida o pavimento, rendendoli morbidi, flessibili ed elastici come gomma naturale.',
    'etimologia': 'Dal latino 'gummis' (gomma, resina elastica).'
  },
  {
    'id': 'vermiculus', 'anno': 2, 'annoLabel': 'II Anno', 'nome': 'Trasfigurazione in Lombrico (Vermiculus)',
    'formula': 'Vermiculus', 'ripetibile': False, 'tipologia': 'Trasfigurazione Inanimato-Animato / Fattura', 'inDuello': True,
    'duelloNote': 'Utilizzabile in duello: trasfigura piccoli oggetti o proiettili avversari in vermi innocui striscianti, neutralizzando l'attacco.',
    'movimento': 'Movimento ondulato orizzontale a fisarmonica con stoccata finale.',
    'movimentoSvg': 'M 35,75 Q 50,55 65,75 Q 80,95 95,75 Q 110,55 125,75',
    'descrizione': 'Trasforma un piccolo oggetto inanimato in un vermicolo illusorio privo di vita autonoma (Divieto di Gamp sulla Vita), destinato a dissolversi.',
    'etimologia': 'Dal latino 'vermis' (piccolo verme, lombrico).'
  },
  {
    'id': 'snufflifors', 'anno': 2, 'annoLabel': 'II Anno', 'nome': 'Trasfigurazione in Topo (Snufflifors)',
    'formula': 'Snufflifors', 'ripetibile': False, 'tipologia': 'Trasfigurazione Inanimato-Animato', 'inDuello': True,
    'duelloNote': 'Utilizzabile in duello per trasfigurare libri, pietre o piccoli oggetti scagliati dall'avversario in un topolino che scappa.',
    'movimento': 'Cerchio stretto seguito da due scatti rapidi a zig-zag a simulare i baffi e la coda.',
    'movimentoSvg': 'M 60,65 A 15,15 0 1,1 90,65 M 75,80 L 75,115 C 85,120 95,110 95,95',
    'descrizione': 'Incantesimo didattico del secondo anno: trasforma oggetti inanimati di piccola taglia (come tomi o sassi) in un simulacro temporaneo di topo.',
    'etimologia': 'Dall'inglese dialettale 'snuffle' (fiutare) e il suffisso trasfigurativo '-fors'.'
  },
  {
    'id': 'incarcifors', 'anno': 2, 'annoLabel': 'II Anno', 'nome': 'Trasfigurazione in Gabbia (Incarcifors)',
    'formula': 'Incarcifors', 'ripetibile': False, 'tipologia': 'Trasfigurazione / Confinamento', 'inDuello': True,
    'duelloNote': 'Utilizzabile in duello: trasforma un oggetto del campo di battaglia in una gabbia che imprigiona istantaneamente il nemico o la sua creatura.',
    'movimento': 'Tracciare le sbarre verticali con movimenti paralleli veloci e serrare con una cupola superiore.',
    'movimentoSvg': 'M 40,40 L 40,110 M 60,40 L 60,110 M 80,40 L 80,110 M 100,40 L 100,110 M 35,40 L 105,40 M 35,110 L 105,110',
    'descrizione': 'Riconfigura la materia di un oggetto inanimato trasformandolo in una gabbia resistente dimensionata per contenere la creatura o bersaglio designato.',
    'etimologia': 'Dal latino 'incarcerare' (rinchiudere) e '-fors'.'
  },
  {
    'id': 'arresto-momentum', 'anno': 2, 'annoLabel': 'II Anno', 'nome': 'Incantesimo di Arresto Cinetico (Arresto Momentum)',
    'formula': 'Arresto Momentum', 'ripetibile': False, 'tipologia': 'Cinetica / Difensivo', 'inDuello': True,
    'duelloNote': 'Utilizzabile in duello per frenare all'istante macigni scagliati con forza o arrestare la caduta libera di un compagno sbalzato in aria.',
    'movimento': 'Intercettare l'oggetto in caduta con la punta della bacchetta e accompagnarlo con un movimento morbido dall'alto verso il basso.',
    'movimentoSvg': 'M 75,25 L 75,115 M 50,90 L 75,115 L 100,90',
    'descrizione': 'Ideato nel 1711 dalla strega Daisy Pennifold per rallentare le pluffe nel Quidditch. Riduce progressivamente l'accelerazione fino a fermare un corpo a pochi centimetri dal suolo.',
    'etimologia': 'Dall'italiano/latino 'arrestare' e 'momentum' (quantità di moto).',
  },
  {
    'id': 'immobilus', 'anno': 2, 'annoLabel': 'II Anno', 'nome': 'Incantesimo Congelatore del Moto (Immobilus)',
    'formula': 'Immobilus', 'ripetibile': False, 'tipologia': 'Cinetica / Difensivo / Disabilitazione', 'inDuello': True,
    'duelloNote': 'Ottimo in duello: blocca e congela ogni movimento cinetico del bersaglio. Singolo bersaglio: linea a zig-zag e affondo; multi-bersaglio: cerchio.',
    'movimento': 'Linea a zig-zag orizzontale seguita da un affondo netto verso il bersaglio.',
    'movimentoSvg': 'M 35,75 L 60,50 L 85,95 L 110,75 L 130,75',
    'descrizione': 'Arresta i moti dei corpi nello spazio, siano essi esseri viventi o oggetti scagliati. Efficace per placare branchi di creature o bloccare frecce in volo.',
    'etimologia': 'Dal latino 'immobilis' (fermo, immobile).'
  },
  {
    'id': 'chartanimus', 'anno': 2, 'annoLabel': 'II Anno', 'nome': 'Animazione di Carta (Chartanimus)',
    'formula': 'Chartanimus', 'ripetibile': False, 'tipologia': 'Trasfigurazione Animata Elementare', 'inDuello': False,
    'duelloNote': 'Non da duello. Primo esercizio didattico per apprendere la trasfigurazione da bidimensionale a tridimensionale.',
    'movimento': 'Tocco leggero agli angoli del foglio di carta e sollevamento spiraleggiante.',
    'movimentoSvg': 'M 40,110 L 75,40 L 110,110 Z M 75,40 L 75,110',
    'descrizione': 'Trasforma un foglio di carta o pergamena in un origami tridimensionale magicamente animato che si muove secondo i comandi del mago.',
    'etimologia': 'Dal latino 'charta' (carta) e 'animus' (soffio vitale, animazione).'
  },
  {
    'id': 'deletrius', 'anno': 2, 'annoLabel': 'II Anno', 'nome': 'Incantesimo di Cancellazione (Deletrius)',
    'formula': 'Deletrius', 'ripetibile': False, 'tipologia': 'Contro-incanto / Rimozione Marchi', 'inDuello': False,
    'duelloNote': 'Non da duello. Rimuove scritte magiche, marchi trasfigurativi (Significo, Plansigno, Fersigno) o l'eco di proiezioni spettrali.',
    'movimento': 'Sinuoso movimento che disegna un rettangolo continuo intorno alla traccia da cancellare.',
    'movimentoSvg': 'M 40,50 L 110,50 L 110,100 L 40,100 Z',
    'descrizione': 'Dissolve tracce magiche, marchi impressi su oggetti o viventi e scritte invisibili. Usato per pulire le superfici incise.',
    'etimologia': 'Dal verbo latino 'delere' (cancellare, distruggere la traccia).'
  },

  # --- III ANNO ---
  {
    'id': 'riddikulus', 'anno': 3, 'annoLabel': 'III Anno', 'nome': 'Incantesimo Anti-Molliccio (Riddikulus)',
    'formula': 'Riddikulus', 'ripetibile': False, 'tipologia': 'Difensivo / Anti-Non-Esseri', 'inDuello': False,
    'duelloNote': 'Non utilizzabile in un duello tra maghi. Agisce unicamente sui Mollicci (Boggart), mutando la forma di terrore in una caricatura comica.',
    'movimento': 'Colpo di frusta ascendente con la bacchetta, focalizzando intensamente un'immagine ridicola.',
    'movimentoSvg': 'M 40,110 Q 75,90 75,60 Q 75,30 110,40',
    'descrizione': 'Incantesimo che costringe il Molliccio a mutare nella rappresentazione comica immaginata dall'incantatore. La risata che ne scaturisce distrugge o mette in fuga l'entità amortale.',
    'etimologia': 'Dal latino 'ridiculus' (degno di riso, comico).'
  },
  {
    'id': 'carpe-retractum', 'anno': 3, 'annoLabel': 'III Anno', 'nome': 'Incantesimo Tirante (Carpe Retractum)',
    'formula': 'Carpe Retractum', 'ripetibile': True, 'tipologia': 'Utilità / Mobilità / Attrazione', 'inDuello': True,
    'duelloNote': 'Utilizzabile in duello in modo strategico: aggancia oggetti, ripari o persino la veste dell'avversario tirandolo verso di sé per disorientarlo o strappargli armi.',
    'movimento': 'Movimento che evoca avere una corda o una frusta tra le mani, stoccata in avanti e strattone indietro.',
    'movimentoSvg': 'M 30,75 L 110,75 M 95,60 L 110,75 L 95,90 M 110,75 L 45,75',
    'descrizione': 'Emette dalla punta della bacchetta una corda di pura energia dorata e arancione. Se l'oggetto colpito è mobile, viene attirato verso il mago; se è inamovibile, l'incantatore viene proiettato verso il punto d'ancoraggio.',
    'etimologia': 'Dal latino 'carpere' (afferrare) e 'retractum' (tratto indietro).'
  },
  {
    'id': 'glacius', 'anno': 3, 'annoLabel': 'III Anno', 'nome': 'Incantesimo Congelante (Glacius)',
    'formula': 'Glacius', 'ripetibile': True, 'tipologia': 'Offensivo / Elementale Freddo', 'inDuello': True,
    'duelloNote': 'Molto efficace in duello. Congela il terreno sotto i piedi del rivale rendendolo scivoloso o ne imprigiona gli arti in blocchi di ghiaccio solido.',
    'movimento': 'Movimento diretto e conciso in un punto lungo la direzione del sortilegio.',
    'movimentoSvg': 'M 40,40 L 110,40 L 50,110 L 120,110',
    'descrizione': 'Scaglia un getto di aria gelata che trasforma l'acqua in ghiaccio e congela bersagli viventi o inanimati. Se combinato con Aguamenti crea lastre di ghiaccio istantanee. Trasforma il respiro circostante in nebbia densa.',
    'etimologia': 'Dal latino 'glacies' (ghiaccio).'
  },
  {
    'id': 'everte-statim', 'anno': 3, 'annoLabel': 'III Anno', 'nome': 'Incantesimo di Dispersione (Everte Statim)',
    'formula': 'Everte Statim', 'ripetibile': True, 'tipologia': 'Offensivo / Schiantesimo Impattante', 'inDuello': True,
    'duelloNote': 'Formidabile in duello. Scaraventa l'avversario in una traiettoria rotante all'indietro provocando dolore da impatto e stordimento.',
    'movimento': 'Pezzo a mezzaluna con scatto secco verso l'esterno, come per disperdere una massa.',
    'movimentoSvg': 'M 40,100 C 40,50 90,40 120,70 L 105,75',
    'descrizione': 'Sortilegio impattante di grande potenza cinetica. Scaraventa via con violenza inaudita l'avversario, facendolo girare su sé stesso in aria. Utile anche per disperdere i Marciotti quando resi corporei da Lumos.',
    'etimologia': 'Dal latino 'evertere' (rovesciare, scacciare) e 'statim' (sul posto, all'istante).'
  },
  {
    'id': 'orbis', 'anno': 3, 'annoLabel': 'III Anno', 'nome': 'Incantesimo del Vortice Terrestre (Orbis)',
    'formula': 'Orbis', 'ripetibile': True, 'tipologia': 'Offensivo / Elementale Terra', 'inDuello': True,
    'duelloNote': 'Ottimo in duello per privare l'avversario dell'equilibrio, sollevare zolle accecanti di terriccio e trascinarlo a terra.',
    'movimento': 'Spirale discendente disegnata verso il suolo sotto i piedi del bersaglio.',
    'movimentoSvg': 'M 75,30 A 40,25 0 1,1 74,30 M 75,55 A 30,18 0 1,1 74,55 M 75,80 A 18,10 0 1,1 74,80 L 75,120',
    'descrizione': 'Incantesimo legato all'elemento Terra. Crea un vortice di luce azzurra che risucchia il nemico verso il terreno, scagliando frammenti di terra e provocando abrasioni e accecamento.',
    'etimologia': 'Dal latino 'orbis' (cerchio, sfera, disco).'
  },
  {
    'id': 'feraverto', 'anno': 3, 'annoLabel': 'III Anno', 'nome': 'Trasfigurazione Animale in Calice (Feraverto)',
    'formula': 'Feraverto', 'ripetibile': False, 'tipologia': 'Trasfigurazione Animata-Inanimata', 'inDuello': False,
    'duelloNote': 'Non da duello. Pratica fondamentale del terzo anno di Trasfigurazione Animata.',
    'movimento': 'Tre tocchi leggeri con la punta della bacchetta sull'animale seguiti dalla pronuncia della formula.',
    'movimentoSvg': 'M 45,75 L 45,75 M 75,75 L 75,75 M 105,75 L 105,75 M 75,40 L 75,110',
    'descrizione': 'Converte un piccolo animale (come un topo o uccellino) in un calice di cristallo o vetro infrangibile contenente acqua illusoria.',
    'etimologia': 'Dal latino 'fera' (animale selvatico) e 'vertere' (trasformare).'
  },
  {
    'id': 'inferacus', 'anno': 3, 'annoLabel': 'III Anno', 'nome': 'Trasfigurazione Riccio in Portaspilli (Inferacus)',
    'formula': 'Inferacus', 'ripetibile': False, 'tipologia': 'Trasfigurazione Animata-Inanimata', 'inDuello': False,
    'duelloNote': 'Non da duello. Trasfigurazione didattica avanzata da vivente ad inanimato.',
    'movimento': 'Puntamento fermo e rotazione semicircolare sopra gli aculei.',
    'movimentoSvg': 'M 40,90 C 40,50 110,50 110,90 M 75,50 L 75,25',
    'descrizione': 'Converte un porcospino o riccio in un cuscinetto portaspilli, mutando il corpo in cotone/sughero e gli aculei in aghi metallici appuntiti.',
    'etimologia': 'Dal latino 'infero' (portare) e 'acus' (ago).'
  },
  {
    'id': 'lapifors', 'anno': 3, 'annoLabel': 'III Anno', 'nome': 'Trasfigurazione in Coniglio (Lapifors)',
    'formula': 'Lapifors', 'ripetibile': False, 'tipologia': 'Trasfigurazione Bivalente', 'inDuello': True,
    'duelloNote': 'Utilizzabile in duello per neutralizzare proiettili o piccole creature avversarie trasformandole in conigli che fuggono.',
    'movimento': 'Movimento a balzi d'arco con doppio scatto in avanti per delineare le lunghe orecchie.',
    'movimentoSvg': 'M 40,110 Q 55,40 70,110 Q 85,40 100,110',
    'descrizione': 'Incantesimo bivalente capace di agire sia su oggetti che su animali, trasformando il bersaglio in un coniglio. Molto usato dal Ministero per esche.',
    'etimologia': 'Dal latino 'lepus' (lepre/coniglio) e '-fors'.'
  },
  {
    'id': 'avifors', 'anno': 3, 'annoLabel': 'III Anno', 'nome': 'Trasfigurazione in Volatile (Avifors)',
    'formula': 'Avifors', 'ripetibile': False, 'tipologia': 'Trasfigurazione Bivalente', 'inDuello': True,
    'duelloNote': 'Utilizzabile in duello: trasforma sassi, detriti o frecce scagliate contro l'incantatore in uno stormo di uccelli innocui.',
    'movimento': 'Arco d'ali ascendente fluido con battito finale della bacchetta.',
    'movimentoSvg': 'M 30,80 Q 55,40 75,70 Q 95,40 120,80',
    'descrizione': 'Perfezionato nel 1198 dalla strega inglese Ilyan Broser. Trasfigura oggetti inanimati o piccoli animali in uccelli (o pipistrelli in casi eccezionali).',
    'etimologia': 'Dal latino 'avis' (uccello) e '-fors'.'
  },
  {
    'id': 'descendo', 'anno': 3, 'annoLabel': 'III Anno', 'nome': 'Incantesimo di Caduta Cinetica (Descendo)',
    'formula': 'Descendo', 'ripetibile': True, 'tipologia': 'Cinetica / Offensivo', 'inDuello': True,
    'duelloNote': 'Molto potente in duello: imprime un'accelerazione gravitazionale verso il basso a oggetti a mezz'aria per schiantarli su un bersaglio o far crollare pareti.',
    'movimento': 'Colpo di frusta secco dall'alto verso il basso con luce blu.',
    'movimentoSvg': 'M 75,25 L 75,120 M 55,95 L 75,120 L 95,95',
    'descrizione': 'Forza un corpo o una struttura a precipitare verso il basso ad alta velocità, convertendo il moto in energia cinetica d'impatto devastante.',
    'etimologia': 'Dal latino 'descendere' (scendere, precipitare).'
  },
  {
    'id': 'locomotor', 'anno': 3, 'annoLabel': 'III Anno', 'nome': 'Incantesimo di Locomozione (Locomotor)',
    'formula': 'Locomotor', 'ripetibile': True, 'tipologia': 'Locomozione / Cinetica', 'inDuello': True,
    'duelloNote': 'Utilizzabile in duello per muovere barricate, scudi pesanti o colonne di pietra tra sé e l'avversario sul piano X-Y.',
    'movimento': 'Puntare l'oggetto e muovere la bacchetta dirigendo i movimenti come un direttore d'orchestra.',
    'movimentoSvg': 'M 40,75 C 60,35 90,35 110,75 C 90,115 60,115 40,75 Z',
    'descrizione': 'Permette di sollevare a pochi centimetri dal suolo e muovere nello spazio oggetti pesanti, facendoli scivolare secondo la volontà mentale del mago.',
    'etimologia': 'Dal latino 'locus' (luogo) e 'motus' (movimento).'
  },
  {
    'id': 'bagaglius', 'anno': 3, 'annoLabel': 'III Anno', 'nome': 'Incantesimo Riordina-Bagagli (Bagaglius)',
    'formula': 'Bagaglius', 'ripetibile': False, 'tipologia': 'Locomozione Domestica', 'inDuello': False,
    'duelloNote': 'Non da duello. Sortilegio di locomozione per riordinare e impacchettare indumenti in valigie.',
    'movimento': 'Tracciare un lungo ed ampio gesto rivolto al pavimento verso i bauli.',
    'movimentoSvg': 'M 30,50 Q 75,120 120,50',
    'descrizione': 'Sfrutta la locomozione e la levitazione aerea per piegare e riporre ordinatamente gli abiti nelle valigie in pochi secondi.',
    'etimologia': 'Dall'italiano 'bagaglio'.'
  },
  {
    'id': 'mobilicorpus', 'anno': 3, 'annoLabel': 'III Anno', 'nome': 'Incantesimo di Movimento Corpi (Mobilicorpus)',
    'formula': 'Mobilicorpus', 'ripetibile': True, 'tipologia': 'Locomozione / Levitazione Medica', 'inDuello': True,
    'duelloNote': 'Utilizzabile in duello a squadre per evacuare un alleato privo di sensi facendolo fluttuare in salvo.',
    'movimento': 'Puntamento al corpo e movimento fluido della bacchetta a guidare la traslazione.',
    'movimentoSvg': 'M 35,75 L 115,75 M 100,60 L 115,75 L 100,90',
    'descrizione': 'Fa levitare in posizione verticale o orizzontale un corpo umano (anche privo di sensi o addormentato), consentendo di spostarlo come una marionetta invisibile.',
    'etimologia': 'Dal latino 'mobilis' (mobile) e 'corpus' (corpo).'
  },
  {
    'id': 'mobiliarbus', 'anno': 3, 'annoLabel': 'III Anno', 'nome': 'Incantesimo Sposta-Alberi (Mobiliarbus)',
    'formula': 'Mobiliarbus', 'ripetibile': True, 'tipologia': 'Locomozione Pesi Massicci', 'inDuello': False,
    'duelloNote': 'Non da duello rapido. Sposta alberi secolari, ceppi pesanti o carichi imponenti.',
    'movimento': 'Movimento ascendente con impugnatura salda a due mani e traslazione orizzontale.',
    'movimentoSvg': 'M 75,120 L 75,40 M 45,70 L 75,40 L 105,70',
    'descrizione': 'Permette di dissodare temporaneamente le radici di un albero o arbusto pesante per farlo fluttuare e riposizionarlo altrove.',
    'etimologia': 'Dal latino 'mobilis' e 'arbor' (albero).'
  },
  {
    'id': 'circumrota', 'anno': 3, 'annoLabel': 'III Anno', 'nome': 'Incantesimo di Rotazione Vincolata (Circumrota)',
    'formula': 'Circumrota', 'ripetibile': True, 'tipologia': 'Locomozione a Moto Circolare', 'inDuello': False,
    'duelloNote': 'Non da duello. Aziona perni, ruote, ingranaggi o saracinesche a vite.',
    'movimento': 'Rotazione continua della bacchetta su un piano perpendicolare al perno.',
    'movimentoSvg': 'M 75,35 A 40,40 0 1,1 74,35',
    'descrizione': 'Imprime a un oggetto dotato di perno o asse una rotazione continua e controllata.',
    'etimologia': 'Dal latino 'circum' (intorno) e 'rotare' (girare a ruota).'
  },
  {
    'id': 'scourgify', 'anno': 3, 'annoLabel': 'III Anno', 'nome': 'Incantesimo di Detersione (Gratta e Netta / Scourgify)',
    'formula': 'Scourgify', 'ripetibile': True, 'tipologia': 'Utilità / Detersione / Anti-Bundium', 'inDuello': True,
    'duelloNote': 'Utilizzabile in duello in modo goliardico o strategico: riempie istantaneamente la bocca del rivale di schiuma e sapone per impedirgli di scandire formule.',
    'movimento': 'Tracciare una lettera S verticale con decisione.',
    'movimentoSvg': 'M 95,35 C 55,35 55,75 75,75 C 95,75 95,115 55,115',
    'descrizione': 'Pulisce, sgrassa e igienizza oggetti e stoviglie. Efficace rimedio contro le infestazioni di Bundium, creature amanti del marciume. In duello zittisce temporaneamente l'avversario con sapone.',
    'etimologia': 'Dall'inglese 'to scour' (strofinare, ripulire).'
  },

  # --- IV ANNO ---
  {
    'id': 'conjunctivitus', 'anno': 4, 'annoLabel': 'IV Anno', 'nome': 'Fattura della Congiuntivite (Conjunctivitus)',
    'formula': 'Conjunctivitus', 'ripetibile': False, 'tipologia': 'Offensivo / Fattura Accecante', 'inDuello': True,
    'duelloNote': 'Micidiale in duello. Chiude gli occhi della vittima tra bruciori e lacrimazione incontrollata, rendendo impossibile mirare.',
    'movimento': 'Doppio tocco aereo rapido seguito da un affondo orizzontale mirato agli occhi.',
    'movimentoSvg': 'M 45,75 A 15,15 0 1,1 75,75 A 15,15 0 1,1 105,75 L 125,75',
    'descrizione': 'Provoca un'istantanea e acuta infiammazione oculare con abbondante secrezione e spasmo palpebrale. Efficace anche contro giganti, draghi e creature oscure la cui pelle è altrimenti impenetrabile.',
    'etimologia': 'Dal termine medico latino 'conjunctivitis' (infiammazione della congiuntiva).'
  },
  {
    'id': 'flagramus', 'anno': 4, 'annoLabel': 'IV Anno', 'nome': 'Incantesimo della Marcatura Infuocata (Flagramus)',
    'formula': 'Flagramus', 'ripetibile': True, 'tipologia': 'Utilità / Tattico / Aritmantico', 'inDuello': True,
    'duelloNote': 'Utilizzabile in duello per rendere incandescenti armi o ripari nemici, impedendo di toccarli sotto pena di gravi ustioni.',
    'movimento': 'Tracciamento deciso di una croce di fuoco o del segno alfabetico desiderato nell'aria o sulla materia.',
    'movimentoSvg': 'M 75,30 L 75,120 M 35,75 L 115,75',
    'descrizione': 'Incide rune, simboli o croci di fiamma pura sopra oggetti, pareti o porte, rendendoli incandescenti al tatto. Utilizzato nell'Aritmanzia pratica per iscrivere lettere e numeri nei cerchi rituali dopo il tracciamento con Signo.',
    'etimologia': 'Dal latino 'flagrare' (ardere, bruciare di viva fiamma).'
  },
  {
    'id': 'relascio', 'anno': 4, 'annoLabel': 'IV Anno', 'nome': 'Incantesimo d'Esilio (Relascio)',
    'formula': 'Relascio', 'ripetibile': True, 'tipologia': 'Offensivo / Disarmo / Allontanamento', 'inDuello': True,
    'duelloNote': 'Eccellente in duello. Allontana e disperde oggetti contundenti scagliati contro il mago ed esilia armi o bacchette fuori dalla portata dell'avversario.',
    'movimento': 'Mano portata rapidamente al petto e poi braccio steso con forza in avanti verso il bersaglio; fa scintille.',
    'movimentoSvg': 'M 50,110 L 80,75 L 125,45',
    'descrizione': 'Genera un getto sfrigolante di scintille o acqua bollente (sott'acqua) che allontana persone, oggetti o creature moleste come i Doxy. Opera come l'opposto funzionale dell'incantesimo di appello Accio.',
    'etimologia': 'Dal latino 'relasciari' / 'relaxare' (allentare, rilasciare, respingere via).'
  },
  {
    'id': 'expecto-patronum', 'anno': 4, 'annoLabel': 'IV Anno', 'nome': 'Incanto Patronus (Expecto Patronum)',
    'formula': 'Expecto Patronum', 'ripetibile': False, 'tipologia': 'Difensivo Superiore / Luce Pura', 'inDuello': False,
    'duelloNote': 'Non utilizzato nei duelli regolamentari tra maghi. Può fungere da scudo se l'avversario evoca Dissennatori o per inviare messaggi cifrati vocali agli alleati.',
    'movimento': 'Ampio cerchio ascendente in senso orario seguito da un affondo in avanti, catalizzando un ricordo di pura e intensa felicità.',
    'movimentoSvg': 'M 75,30 C 115,30 125,75 125,75 C 125,115 75,120 75,120 C 35,120 25,75 25,75 C 25,35 75,30 75,30 Z M 75,75 L 130,55',
    'descrizione': 'Uno degli incantesimi difensivi più complessi e potenti della magia antica. Evoca una figura eterea argentea (corporea o incorporea) alimentata dalla felicità, che respinge Dissennatori e Lethifold e funge da messaggero parlante.',
    'etimologia': 'Dal latino 'expectare' (attendere, invocare) e 'patronus' (protettore, difensore).'
  },
  {
    'id': 'lacarnum-inflamare', 'anno': 4, 'annoLabel': 'IV Anno', 'nome': 'Incantesimo Infiammante (Lacarnum Inflamare)',
    'formula': 'Lacarnum Inflamare', 'ripetibile': True, 'tipologia': 'Offensivo / Elementale Fuoco', 'inDuello': True,
    'duelloNote': 'Utilizzabile in duello. Infiamma istantaneamente il mantello o l'abito del rivale, provocando panico immediato e spezzando il suo ritmo di lancio.',
    'movimento': 'Schiocco rapido del polso a becco verso il mantello o il vestito dell'avversario.',
    'movimentoSvg': 'M 35,60 Q 75,30 115,75 L 75,100 Z',
    'descrizione': 'Emette una scintilla o dardo ardente che accende qualsiasi tessuto o superficie non trattata con sortilegi ignifughi.',
    'etimologia': 'Dal latino 'lacerna' (cappa, mantello) e 'inflammare' (dare alle fiamme).'
  },
  {
    'id': 'salvio-hexia', 'anno': 4, 'annoLabel': 'IV Anno', 'nome': 'Incantesimo Difensivo di Zona (Salvio Hexia)',
    'formula': 'Salvio Hexia', 'ripetibile': True, 'tipologia': 'Difensivo Statico di Zona (I.D.S.)', 'inDuello': False,
    'duelloNote': 'Non impiegabile nel duello diretto: è un incantesimo statico di protezione per accampamenti e rifugi.',
    'movimento': 'Tenere in alto la bacchetta a 45 gradi e discendere verso il basso, con il palmo della mano opposta aperto rivolto all'esterno.',
    'movimentoSvg': 'M 45,30 L 105,120 M 115,60 L 115,90',
    'descrizione': 'Incantesimo difensivo statico (I.D.S.) che rende invisibile un locale, una tenda o una zona prescelta, occultando chiunque vi si trovi all'interno. Potenziato tracciando con Signo un ottagono e ripetendo la formula su ciascuno degli 8 vertici.',
    'etimologia': 'Dal latino 'salvus' (illeso, salvo) e radice da 'hex' / 'hexe' (fattura, incanto protettivo).'
  },
  {
    'id': 'alarte-ascenderai', 'anno': 4, 'annoLabel': 'IV Anno', 'nome': 'Sortilegio di Slancio Verticale (Alarte Ascenderai)',
    'formula': 'Alarte Ascenderai', 'ripetibile': True, 'tipologia': 'Offensivo / Cinetico / Non-Verbale', 'inDuello': True,
    'duelloNote': 'Molto efficace in duello per scagliare l'avversario a parecchi metri di altezza facendolo ricadere bruscamente e togliendogli il respiro.',
    'movimento': 'Stoccata diretta dal basso verso l'alto con un lampo di luce rossa (preferibilmente non verbale).',
    'movimentoSvg': 'M 75,125 L 75,30 M 50,55 L 75,30 L 100,55',
    'descrizione': 'Emette una luce scarlatta che proietta il corpo della vittima in aria a grande velocità per poi lasciarlo schiantare al suolo. Utilizzato spesso per disorientare e neutralizzare temporaneamente il nemico.',
    'etimologia': 'Dal latino 'alatus' (alato, fornito d'ali) e 'ascendere' (salire in quota).'
  },
  {
    'id': 'avis', 'anno': 4, 'annoLabel': 'IV Anno', 'nome': 'Evocazione di Stormo Uccelli (Avis)',
    'formula': 'Avis', 'ripetibile': True, 'tipologia': 'Evocazione / Distrazione / Offensivo', 'inDuello': True,
    'duelloNote': 'Utilizzabile in duello: evoca un piccolo stormo di volatili che si scagliano contro il volto dell'avversario beccando e distraendolo.',
    'movimento': 'Movimento a scudisciata circolare nell'aria terminante con una detonazione come di sparo.',
    'movimentoSvg': 'M 40,75 C 60,35 90,35 110,75 C 90,115 60,115 40,75 Z M 75,75 L 125,50',
    'descrizione': 'Evoca direttamente un piccolo stormo di uccellini dal non-essere. A differenza di Avifors (che trasfigura materia), Avis materializza entità temporanee attraverso la bacchetta.',
    'etimologia': 'Dal latino 'avis' (uccello, volatile).'
  },
  {
    'id': 'farfallus-explodit', 'anno': 4, 'annoLabel': 'IV Anno', 'nome': 'Evocazione Farfalle Luminose (Farfallus Explodit)',
    'formula': 'Farfallus Explodit', 'ripetibile': True, 'tipologia': 'Evocazione / Accecamento / Distrazione', 'inDuello': True,
    'duelloNote': 'Utilizzabile in duello: libera migliaia di farfalle abbaglianti che accecano e stordiscono la linea di mira del rivale.',
    'movimento': 'Ampio ventaglio orizzontale della bacchetta con rilascio a fiotto.',
    'movimentoSvg': 'M 35,90 Q 75,30 115,90 M 75,30 L 75,110',
    'descrizione': 'Evoca un turbinio di migliaia di farfalle fluorescenti che fluttuano attorno al bersaglio disorientandolo. Non raccomandato per operazioni stealth.',
    'etimologia': 'Dall'italiano 'farfalla' e latino 'explodere' (scoppiare, disperdersi).'
  },
  {
    'id': 'episkey', 'anno': 4, 'annoLabel': 'IV Anno', 'nome': 'Incantesimo Curativo Rapido (Episkey)',
    'formula': 'Episkey', 'ripetibile': False, 'tipologia': 'Curativo / Medimagia da Campo', 'inDuello': True,
    'duelloNote': 'Utilizzabile nei duelli prolungati: ripara all'istante nasi rotti, labbra spaccate e dita lussate, arrestando il sangue.',
    'movimento': 'Puntare la bacchetta sulla ferita e pronunciare la formula con tono deciso.',
    'movimentoSvg': 'M 75,35 L 75,115 M 55,75 L 95,75',
    'descrizione': 'Sortilegio medimagico per traumi lievi, abrasioni, contusioni e piccole fratture. Provoca una sensazione alternata di caldo e gelo durante la sutura ossea.',
    'etimologia': 'Dal greco 'episkeue' (riparazione, restauro).'
  },
  {
    'id': 'ferula', 'anno': 4, 'annoLabel': 'IV Anno', 'nome': 'Incantesimo Fasciante (Ferula)',
    'formula': 'Ferula', 'ripetibile': False, 'tipologia': 'Curativo / Medimagia da Campo', 'inDuello': True,
    'duelloNote': 'Utilizzabile in duello a squadre: immobilizza e fascia un arto spezzato di un compagno con stecche e bende sterili.',
    'movimento': 'Puntare la bacchetta sull'arto ferito e ruotare delicatamente come a voler fasciare.',
    'movimentoSvg': 'M 75,35 A 40,40 0 1,1 74,35 M 40,75 L 110,75',
    'descrizione': 'Evoca all'istante stecche di legno e bende elastiche che si avvolgono da sole intorno alla frattura, immobilizzandola per prevenire complicazioni.',
    'etimologia': 'Dal latino 'ferula' (stecca per fratture, bacchetta medica).'
  },
  {
    'id': 'cicatris', 'anno': 4, 'annoLabel': 'IV Anno', 'nome': 'Incantesimo Salda-Tagli (Cicatris)',
    'formula': 'Cicatris', 'ripetibile': False, 'tipologia': 'Curativo / Medimagia Minore', 'inDuello': False,
    'duelloNote': 'Non da duello. Chiude tagli e graffi superficiali lasciando una lieve cicatrice lucida color pesca.',
    'movimento': 'Disegnare un piccolo semicerchio verso il taglio con luce tenue color pesca.',
    'movimentoSvg': 'M 45,75 A 30,30 0 0,1 105,75',
    'descrizione': 'Sutura magicamente ferite superficiali da taglio o graffi domestici. Un uso eccessivo può indurire la cute.',
    'etimologia': 'Dal latino 'cicatrix' (cicatrice, segno di saldatura).'
  },
  {
    'id': 'glisseo', 'anno': 4, 'annoLabel': 'IV Anno', 'nome': 'Incantesimo Leviga-Scale (Glisseo)',
    'formula': 'Glisseo', 'ripetibile': False, 'tipologia': 'Trasfigurazione Ambientale', 'inDuello': True,
    'duelloNote': 'Formidabile in duello urbano o su scalinate: trasforma gli scalini sotto i piedi dell'avversario in un piano inclinato scivoloso facendolo rovinare a terra.',
    'movimento': 'Onda discendente che segue il profilo della gradinata.',
    'movimentoSvg': 'M 35,40 L 60,65 L 85,90 L 115,115',
    'descrizione': 'Concepito originariamente dai fondatori di Hogwarts per proteggere i dormitori femminili. Trasforma istantaneamente qualsiasi scalinata in un ripido e levigato scivolo.',
    'etimologia': 'Dal francese 'glisser' (scivolare, rendere sdrucciolevole).'
  },
  {
    'id': 'duro', 'anno': 4, 'annoLabel': 'IV Anno', 'nome': 'Incantesimo Pietrificante di Cose (Duro)',
    'formula': 'Duro', 'ripetibile': False, 'tipologia': 'Litotrasfigurazione Inanimata', 'inDuello': True,
    'duelloNote': 'Molto utile in duello: trasforma arazzi, tende o liquidi in solida roccia per erigere scudi istantanei contro incantesimi.',
    'movimento': 'Tocco secco perpendicolare verso il bersaglio con pugno serrato sulla bacchetta.',
    'movimentoSvg': 'M 40,40 L 110,40 L 110,110 L 40,110 Z',
    'descrizione': 'Converte la consistenza di un oggetto inanimato in dura pietra massiccia, lasciando inalterato lo spazio occupato.',
    'etimologia': 'Dal latino 'durare' / 'durus' (rendere solido e duro come roccia).'
  },
  {
    'id': 'orchideus', 'anno': 4, 'annoLabel': 'IV Anno', 'nome': 'Evocazione Floreale (Orchideus)',
    'formula': 'Orchideus', 'ripetibile': False, 'tipologia': 'Evocazione Floreale', 'inDuello': False,
    'duelloNote': 'Non da duello. Sortilegio di cortesia, intrattenimento o distrazione leggera.',
    'movimento': 'Gesto a calice della mano verso l'alto con schiocco finale.',
    'movimentoSvg': 'M 75,120 L 75,70 M 50,50 Q 75,70 100,50 Q 75,25 50,50 Z',
    'descrizione': 'Fa scaturire dall'apice della bacchetta un fresco mazzo di orchidee multicolori effimere.',
    'etimologia': 'Dal nome botanico 'Orchis' / 'Orchidea'.'
  },
  {
    'id': 'melofors', 'anno': 4, 'annoLabel': 'IV Anno', 'nome': 'Fattura della Zucca (Melofors)',
    'formula': 'Melofors', 'ripetibile': False, 'tipologia': 'Fattura Trasfigurativa Irripetibile', 'inDuello': True,
    'duelloNote': 'Molto efficace in duello: ingabbia la testa del rivale all'interno di una pesante zucca, togliendogli la vista e disorientandolo.',
    'movimento': 'Arco a cupola sopra la testa dell'avversario con scatto verso il basso.',
    'movimentoSvg': 'M 40,75 C 40,40 110,40 110,75 C 110,110 40,110 40,75 Z M 75,40 L 75,25',
    'descrizione': 'Incantesimo citato nel Codex come classico esempio di incanto irripetibile: manifesta una zucca arancione sulla testa della vittima. Rilanciarlo non produce alcun effetto aggiuntivo.',
    'etimologia': 'Dal greco 'melon' (zucca, melone) e '-fors'.'
  },
  {
    'id': 'incarceramus', 'anno': 4, 'annoLabel': 'IV Anno', 'nome': 'Fattura delle Corde Vincolanti (Incarceramus)',
    'formula': 'Incarceramus', 'ripetibile': True, 'tipologia': 'Fattura Offensiva / Confinamento', 'inDuello': True,
    'duelloNote': 'Ottimo in duello: scaglia funi robuste che legano istantaneamente il corpo e le braccia dell'avversario alla vita.',
    'movimento': 'Doppio giro a cappio della bacchetta seguito da un affondo in avanti.',
    'movimentoSvg': 'M 40,50 C 75,20 110,50 90,85 C 70,120 40,85 75,75 L 125,75',
    'descrizione': 'Proietta lunghe e spesse corde magiche intrecciate che si avvinghiano attorno al bersaglio legandolo strettamente.',
    'etimologia': 'Dal latino 'incarcerare' (rinchiudere, imprigionare).'
  },
  {
    'id': 'epoximise', 'anno': 4, 'annoLabel': 'IV Anno', 'nome': 'Incantesimo Adesivo (Epoximise)',
    'formula': 'Epoximise', 'ripetibile': False, 'tipologia': 'Trasfigurazione Adesiva / Tattico', 'inDuello': True,
    'duelloNote': 'Utilizzabile in duello: incolla istantaneamente le suole delle scarpe dell'avversario al pavimento impedendogli ogni fuga.',
    'movimento': 'Schiocco verso la linea di contatto tra le due superfici da unire.',
    'movimentoSvg': 'M 40,65 L 110,65 M 40,85 L 110,85 M 75,65 L 75,85',
    'descrizione': 'Genera tra due superfici materiali uno strato di potentissima resina collante sintetica inseparabile.',
    'etimologia': 'Dal greco 'epoxy' (resina epossidica adesiva).'
  },
  {
    'id': 'silencio', 'anno': 4, 'annoLabel': 'IV Anno', 'nome': 'Incantesimo Ammutolente (Silencio)',
    'formula': 'Silencio', 'ripetibile': False, 'tipologia': 'Fattura Silenziante / Duello', 'inDuello': True,
    'duelloNote': 'Arma superba in duello: priva la vittima della voce, impedendole di pronunciare qualsiasi incantesimo verbale.',
    'movimento': 'Curva sinuosa a forma di U con discesa netta verso il basso.',
    'movimentoSvg': 'M 45,40 L 45,85 C 45,110 105,110 105,85 L 105,40',
    'descrizione': 'Nato storicamente per zittire il canto folle dei Fwooper. In duello toglie completamente la parola. Se eseguito male può provocare un rigonfiamento con rumori assordanti.',
    'etimologia': 'Dal latino 'silentium' (silenzio assoluto).'
  },
  {
    'id': 'expulso', 'anno': 4, 'annoLabel': 'IV Anno', 'nome': 'Sortilegio Esplosivo da Impulso (Expulso)',
    'formula': 'Expulso', 'ripetibile': True, 'tipologia': 'Offensivo / Esplosione Cinetica', 'inDuello': True,
    'duelloNote': 'Micidiale in duello: genera un'onda d'urto a pressione che scaraventa violentemente la persona colpita contro le pareti.',
    'movimento': 'Puntamento fermo e stoccata frontale con rilascio di scintille bluastre.',
    'movimentoSvg': 'M 40,75 L 115,75 M 95,55 L 115,75 L 95,95',
    'descrizione': 'Sortilegio esplosivo da minatori: comprime le molecole dell'oggetto bersaglio provocando un'onda d'urto espulsiva violenta.',
    'etimologia': 'Dal latino 'expellere' / 'expulsum' (scagliare fuori con violenza).'
  },

  # --- V ANNO ---
  {
    'id': 'confringo', 'anno': 5, 'annoLabel': 'V Anno', 'nome': 'Maledizione Esplosiva (Confringo)',
    'formula': 'Confringo', 'ripetibile': True, 'tipologia': 'Offensivo / Distruzione ed Esplosione', 'inDuello': True,
    'duelloNote': 'Devastante in duello: demolisce ripari fisici, genera schegge letali e fiamme. Richiede cautela in spazi chiusi per evitare danni collaterali all'incantatore.',
    'movimento': 'Impugnare saldamente la bacchetta, scoccarla verso l'alto vicino al capo e sferzarla violentemente in avanti verso l'obiettivo.',
    'movimentoSvg': 'M 50,110 L 75,30 L 100,110 M 60,85 L 90,85',
    'descrizione': 'Crea una deflagrazione infuocata violentissima all'impatto con il bersaglio. Inventato nel Basso Medioevo (1005 d.C.) da Bilbo il balbettante per abbattere le mura nemiche nella battaglia di York. Efficace anche contro Erkling e Berretti Rossi.',
    'etimologia': 'Dal verbo latino 'confringere' (spezzare, frantumare in mille pezzi con violenza).'
  },
  {
    'id': 'deprimo', 'anno': 5, 'annoLabel': 'V Anno', 'nome': 'Incantesimo di Pressione Crollante (Deprimo)',
    'formula': 'Deprimo', 'ripetibile': True, 'tipologia': 'Offensivo / Distruzione / Pressione', 'inDuello': True,
    'duelloNote': 'Utilizzabile in duello tattico: fa sprofondare il pavimento sotto i piedi del duellante o fa collassare porzioni di soffitto e rocce sull'avversario.',
    'movimento': 'Puntamento perpendicolare dall'alto verso il basso con pressione muscolare dell'intero braccio.',
    'movimentoSvg': 'M 35,45 L 115,45 M 75,45 L 75,120 M 55,100 L 75,120 L 95,100',
    'descrizione': 'Esercita una spaventosa pressione verso il basso sulla materia selezionata, causandone il collasso o la polverizzazione. Capace di far crollare il pavimento di un'intera stanza in pochi istanti. Non va confuso con Defodio che serve a scavare.',
    'etimologia': 'Dal latino 'deprimere' (spingere verso il basso, far sprofondare).'
  },
  {
    'id': 'reducto', 'anno': 5, 'annoLabel': 'V Anno', 'nome': 'Incantesimo Polverizzante (Reducto)',
    'formula': 'Reducto', 'ripetibile': True, 'tipologia': 'Offensivo / Polverizzazione', 'inDuello': True,
    'duelloNote': 'Imprescindibile in duello per disintegrate ostacoli solidi scagliati dall'avversario o distruggere barricate nemiche istantaneamente.',
    'movimento': 'Movimento a V rovesciata seguito da una stoccata orizzontale in avanti.',
    'movimentoSvg': 'M 40,110 L 75,40 L 110,110 M 75,40 L 75,90',
    'descrizione': 'Riduce in frantumi o fa saltare in aria oggetti solidi pesanti come macigni, cancelli o tronchi d'albero. Permette di liberarsi dai blocchi o creare cortine di macerie e diversivi per fuggire.',
    'etimologia': 'Dal latino 'reducere' (ricondurre allo stato elementare, ridurre in frammenti).'
  },
  {
    'id': 'furunculus', 'anno': 5, 'annoLabel': 'V Anno', 'nome': 'Fattura dei Foruncoli (Furunculus)',
    'formula': 'Furunculus', 'ripetibile': True, 'tipologia': 'Fattura Offensiva / Debilitante', 'inDuello': True,
    'duelloNote': 'Utilizzabile in duello. Causa dolore acuto e gonfiore purulento immediato, costringendo l'avversario a coprirsi il viso e distogliendo la concentrazione.',
    'movimento': 'Doppio tocco aereo rapido a puntura d'ape seguito da affondo verso il bersaglio.',
    'movimentoSvg': 'M 40,75 L 60,55 L 75,75 L 90,55 L 110,75',
    'descrizione': 'Ricopre istantaneamente la pelle e il volto della vittima di enormi e dolorose bolle colme di pus. Le lesioni possono essere alleviate con impacchi di Essenza di Dittamo o incantesimi curativi come Epismendo.',
    'etimologia': 'Dal latino 'furunculus' (ladro meschino, e termine medico per foruncolo).'
  },
  {
    'id': 'languelingua', 'anno': 5, 'annoLabel': 'V Anno', 'nome': 'Fattura Incolla-Lingua (Languelingua)',
    'formula': 'Languelingua', 'ripetibile': False, 'tipologia': 'Fattura / Maledizione Silenziante', 'inDuello': True,
    'duelloNote': 'Micidiale in duello contro duellanti convenzionali: incolla la lingua al palato impedendo di scandire qualsiasi formula verbale.',
    'movimento': 'Giro stretto del polso a nodo orizzontale seguito da un affondo.',
    'movimentoSvg': 'M 45,75 C 45,45 105,45 105,75 C 105,105 45,105 45,75 Z M 105,75 L 130,75',
    'descrizione': 'Incolla saldamente la lingua al palato come se fosse ingrossata, rendendo impossibile articolare parole e formule. Un duellante esperto può contrastarla solo tramite contro-incanti non-verbali.',
    'etimologia': 'Composto dal latino 'languere' (essere inerte) e 'lingua'.'
  },
  {
    'id': 'rictusempra', 'anno': 5, 'annoLabel': 'V Anno', 'nome': 'Sortilegio Solleticante (Rictusempra)',
    'formula': 'Rictusempra', 'ripetibile': True, 'tipologia': 'Fattura / Disabilitazione Lieve', 'inDuello': True,
    'duelloNote': 'Utilizzabile in duello. Piega in due l'avversario con risate e convulsioni da solletico irrefrenabile, rendendogli impossibile lanciare incantesimi precisi.',
    'movimento': 'Semicirconferenza con stoccata finale verso l'avversario; fiotto di luce bianca con urto simile a schiantesimo.',
    'movimentoSvg': 'M 35,75 Q 55,45 75,75 Q 95,105 115,75',
    'descrizione': 'Sortilegio che investe il bersaglio con un dardo di luce argentata procurando un solletico feroce e incontrollabile che fa scoppiare in risate isteriche chiunque venga colpito.',
    'etimologia': 'Dal latino 'rictus' (bocca spalancata nel riso) e 'semper' (continuamente).'
  },
  {
    'id': 'tarantallegra', 'anno': 5, 'annoLabel': 'V Anno', 'nome': 'Fattura Gambalesta (Tarantallegra)',
    'formula': 'Tarantallegra', 'ripetibile': True, 'tipologia': 'Fattura Offensiva / Inibizione Motoria', 'inDuello': True,
    'duelloNote': 'Utilizzabile in duello. Costringe le gambe dell'avversario a una danza irrefrenabile, distruggendone l'assetto da combattimento e l'equilibrio.',
    'movimento': 'Rapido movimento ritmico e sincopato a zig-zag verso le gambe del bersaglio.',
    'movimentoSvg': 'M 45,35 L 75,65 L 50,95 L 85,125',
    'descrizione': 'Inventata dal mago italiano Zaccaria Innocenti nel 79 d.C. all'interno del Vesuvio. Costringe le gambe della vittima a muoversi senza sosta a ritmo parossistico. L'effetto svanisce dopo poche ore o con Finite Incantem.',
    'etimologia': 'Dalla danza tradizionale italiana 'tarantella' e 'allegro' (veloce e animato).'
  },
  {
    'id': 'dolohoferio', 'anno': 5, 'annoLabel': 'V Anno', 'nome': 'Maledizione di Dolohov (Dolohoferio)',
    'formula': 'Dolohoferio', 'ripetibile': False, 'tipologia': 'Maledizione Oscura / Offensiva Letale', 'inDuello': True,
    'duelloNote': 'Utilizzabile in scontro mortale / bellico (proibita nei duelli sportivi e accademici). Crea una frusta infuocata viola che infligge lesioni interne gravissime e letali.',
    'movimento': 'Ampio e caratteristico movimento a frusta del catalizzatore magico, scagliato in diagonale con forza inaudita.',
    'movimentoSvg': 'M 35,45 C 50,20 120,40 100,85 C 80,120 40,80 125,120',
    'descrizione': 'Maledizione oscura ideata dal mangiamorte Antonin Dolohov. Genera una lunga scudisciata viola fiammeggiante che attraversa il bersaglio provocando estese emorragie interne senza lasciare ferite esteriori visibili.',
    'etimologia': 'Fusione del cognome 'Dolohov' con il latino 'ferire' o 'dolor'.'
  },
  {
    'id': 'densaugeo', 'anno': 5, 'annoLabel': 'V Anno', 'nome': 'Fattura Cresci-Denti (Densaugeo)',
    'formula': 'Densaugeo', 'ripetibile': False, 'tipologia': 'Fattura Trasfigurativa / DCAO V Anno', 'inDuello': True,
    'duelloNote': 'Molto insidiosa in duello: fa crescere a dismisura gli incisivi (fino a 7 cm) rendendo impossibile chiudere la bocca e pronunciare formule vocali.',
    'movimento': 'Puntamento deciso alla bocca con un doppio tocco verticale.',
    'movimentoSvg': 'M 75,40 L 75,70 M 65,70 L 85,70 M 75,80 L 75,115',
    'descrizione': 'Inserito nel programma didattico di DCAO del V anno a partire dagli anni '80. Fa crescere gli incisivi a vista d'occhio provocando grave imbarazzo e totale blocco della fonazione magica. Contro-incanto di valenza 9.',
    'etimologia': 'Dal latino 'dens' (dente) e 'augere' (accrescere, ingrandire).'
  },
  {
    'id': 'paperante', 'anno': 5, 'annoLabel': 'V Anno', 'nome': 'Trasfigurazione in Papera (Paperate)',
    'formula': 'Paperante', 'ripetibile': False, 'tipologia': 'Trasfigurazione da Duello', 'inDuello': True,
    'duelloNote': 'Arma definitiva da duello trasfigurativo: trasforma all'istante l'avversario in un'oca o papera, privandolo di ogni capacità di attacco magico.',
    'movimento': 'Movimenti circolari continui in senso orario dalla sommità del capo fino ai piedi del rivale.',
    'movimentoSvg': 'M 75,25 C 105,25 115,65 75,85 C 45,100 45,125 75,125 C 105,125 115,100 75,85',
    'descrizione': 'Ideato intorno al VII secolo: priva completamente il duellante della possibilità di contrattaccare chiudendo rapidamente il duello a proprio favore. L'essenza resta intatta.',
    'etimologia': 'Dal termine volgare 'papera' con suffisso participiale '-ante'.'
  },
  {
    'id': 'pullus', 'anno': 5, 'annoLabel': 'V Anno', 'nome': 'Trasfigurazione in Pollo (Pullus)',
    'formula': 'Pullus', 'ripetibile': False, 'tipologia': 'Trasfigurazione Umana-Aviaria / Duello', 'inDuello': True,
    'duelloNote': 'Utilizzabile in duello: trasforma temporaneamente l'avversario in un pollo starnazzante e innocuo. Micidiale contro gli Erkling della Foresta Nera.',
    'movimento': 'Puntamento frontale e scatto a becco con battito d'ali.',
    'movimentoSvg': 'M 50,80 Q 75,40 100,80 M 75,40 L 75,110',
    'descrizione': 'Documentato nel 1754 a seguito dell'impiego da parte del corridore su scopa italiano Silvio Astolfi. Trasforma la persona in un pollo; reversibile con Finite Incantatem non-verbale.',
    'etimologia': 'Dal latino 'pullus' (pulcino, piccolo animale, pollo).'
  },
  {
    'id': 'piscofors', 'anno': 5, 'annoLabel': 'V Anno', 'nome': 'Trasfigurazione in Pesce (Piscofors)',
    'formula': 'Piscofors', 'ripetibile': False, 'tipologia': 'Trasfigurazione Animata-Animata', 'inDuello': True,
    'duelloNote': 'Utilizzabile in duelli acquatici o per rendere inerme un rivale sulla terraferma trasformandolo in un pesce boccheggiante.',
    'movimento': 'Sinuosa onda orizzontale a forma di pinna di pesce.',
    'movimentoSvg': 'M 35,75 C 60,45 90,45 115,75 C 90,105 60,105 35,75 Z M 115,75 L 130,60 M 115,75 L 130,90',
    'descrizione': 'Trasforma temporaneamente un essere animato in un pesce. Reso celebre dalle prove del Torneo Tremaghi per l'adattamento subacqueo.',
    'etimologia': 'Dal latino 'piscis' (pesce) e '-fors'.'
  },
  {
    'id': 'furitum', 'anno': 5, 'annoLabel': 'V Anno', 'nome': 'Trasfigurazione in Furetto (Furitum)',
    'formula': 'Furitum', 'ripetibile': False, 'tipologia': 'Trasfigurazione Umana-Animale / Duello', 'inDuello': True,
    'duelloNote': 'Utilizzabile in duello (anche in modo non-verbale a sorpresa): riduce l'avversario a un furetto incapace di impugnare la bacchetta e di parlare.',
    'movimento': 'Giro ellittico stretto con stoccata morbida verso il pavimento.',
    'movimentoSvg': 'M 40,85 C 40,55 110,55 110,85 C 110,115 40,115 40,85 Z M 110,85 L 130,70',
    'descrizione': 'Trasfigura il soggetto in un furetto agile ma totalmente innocuo e privo di parola. Il ritorno richiede un controincantesimo non-verbale.',
    'etimologia': 'Dal latino 'fur, furis' (ladro, alludendo alla natura furtiva del furetto).'
  },
  {
    'id': 'entomorphis', 'anno': 5, 'annoLabel': 'V Anno', 'nome': 'Trasfigurazione Entomologica (Entomorphis)',
    'formula': 'Entomorphis', 'ripetibile': False, 'tipologia': 'Trasfigurazione Umana / Debilitazione', 'inDuello': True,
    'duelloNote': 'Utilizzabile in duello: priva la vittima dell'uso della parola e la costringe a movimenti striscianti a terra con tratti da insetto.',
    'movimento': 'Movimento a scatti rapidi a tre segmenti (capo, torace, addome).',
    'movimentoSvg': 'M 75,35 L 75,65 M 75,65 L 75,95 M 50,65 L 100,65 M 45,95 L 105,95',
    'descrizione': 'Conferisce temporaneamente al soggetto colpito la morfologia e i tratti funzionali di un insetto (assenza di parola, arti a zampa, movimento strisciante).',
    'etimologia': 'Dal greco 'éntomon' (insetto) e 'morphé' (forma).'
  },
  {
    'id': 'inflatus', 'anno': 5, 'annoLabel': 'V Anno', 'nome': 'Incantesimo di Gonfiamento Corporeo (Inflatus)',
    'formula': 'Inflatus', 'ripetibile': False, 'tipologia': 'Fattura Trasfigurativa / Espansione', 'inDuello': True,
    'duelloNote': 'Molto efficace in duello: gonfia il corpo della vittima a dismisura come un pallone aerostatico, facendola rimbalzare goffamente a mezz'aria.',
    'movimento': 'Circonferenza che si espande verso l'esterno con soffio d'aria.',
    'movimentoSvg': 'M 75,75 m -40,0 a 40,40 0 1,0 80,0 a 40,40 0 1,0 -80,0 M 75,25 L 75,10 M 75,125 L 75,140',
    'descrizione': 'Provoca l'espansione esponenziale del volume corporeo del bersaglio, incrementandone lo spazio occupato e rendendolo incapace di camminare.',
    'etimologia': 'Dal latino 'inflare' (gonfiare, dilatare con aria).'
  },
  {
    'id': 'crinus-muto', 'anno': 5, 'annoLabel': 'V Anno', 'nome': 'Trasfigurazione della Capigliatura (Crinus Muto)',
    'formula': 'Crinus Muto', 'ripetibile': False, 'tipologia': 'Trasfigurazione Umana Estetica', 'inDuello': False,
    'duelloNote': 'Non da duello. Usato per mutare colore e stile di capelli e sopracciglia.',
    'movimento': 'Passaggio a pettine della bacchetta sopra il capo.',
    'movimentoSvg': 'M 40,40 C 40,70 110,70 110,40 M 55,60 L 55,100 M 75,65 L 75,110 M 95,60 L 95,100',
    'descrizione': 'Altera temporaneamente la pigmentazione, lunghezza e consistenza della chioma e delle sopracciglia umane.',
    'etimologia': 'Dal latino 'crinis' (capello, crine) e 'mutare'.'
  },
  {
    'id': 'bombarda', 'anno': 5, 'annoLabel': 'V Anno', 'nome': 'Sortilegio Esplosivo da Breccia (Bombarda)',
    'formula': 'Bombarda', 'ripetibile': True, 'tipologia': 'Offensivo / Esplosivo da Minatori', 'inDuello': True,
    'duelloNote': 'Utilizzabile in duello: genera una forte detonazione che fa saltare sbarre, porte e ostacoli medi; unico incantesimo noto per dissolvere lo Stalker.',
    'movimento': 'Puntamento rigido seguito da un colpo secco in avanti come un detonatore.',
    'movimentoSvg': 'M 45,45 L 105,105 M 105,45 L 45,105',
    'descrizione': 'Sortilegio esplosivo utilizzato anticamente dai minatori. Non richiede una connessione emotiva viscerale e crea una forte deflagrazione materiale esterna.',
    'etimologia': 'Dall'italiano/latino 'bombarda' (antica bocca da fuoco).'
  },
  {
    'id': 'draconifors', 'anno': 5, 'annoLabel': 'V Anno', 'nome': 'Animazione Draconica (Draconifors)',
    'formula': 'Draconifors', 'ripetibile': False, 'tipologia': 'Litotrasfigurazione / Animazione', 'inDuello': True,
    'duelloNote': 'Formidabile in duello tattico: trasforma una statua di drago in una creatura vivente capace di sputare fiamme e attaccare il nemico.',
    'movimento': 'Tracciare la sagoma delle ali del drago e terminare con una spinta fiammeggiante.',
    'movimentoSvg': 'M 40,80 Q 75,30 110,80 L 75,110 Z',
    'descrizione': 'Scoperto nella prima metà del Novecento da Harvey Ridgebit (fondatore della Congrega dei Dragologisti in Romania) per contenere draghi selvaggi animando statue.',
    'etimologia': 'Dal latino 'draco' (drago) e '-fors'.'
  },
  {
    'id': 'piertotum-locomotor', 'anno': 5, 'annoLabel': 'V Anno / M.A.G.O.', 'nome': 'Animazione di Statue e Armature (Piertotum Locomotor)',
    'formula': 'Piertotum Locomotor', 'ripetibile': True, 'tipologia': 'Trasfigurazione d'Animazione / Difesa Massiva', 'inDuello': True,
    'duelloNote': 'Utilizzabile in duello difensivo su larga scala: risveglia statue e armature di pietra o metallo guidandole a difesa dell'incantatore.',
    'movimento': 'Ampio gesto solenne a braccia aperte con affondo della bacchetta verso le schiere di statue.',
    'movimentoSvg': 'M 30,50 L 75,25 L 120,50 L 100,120 L 50,120 Z',
    'descrizione': 'Conferisce temporaneamente movimento coordinato, forza e obbedienza a manufatti inanimati pesanti come le armature e statue del castello di Hogwarts.',
    'etimologia': 'Dal latino 'pie' (piamente), 'totum' (tutto), 'locus' (luogo) e 'motus' (movimento).'
  },
  {
    'id': 'adduco-maxima', 'anno': 5, 'annoLabel': 'V Anno', 'nome': 'Incantesimo di Estensione Irriconoscibile (Adduco Maxima)',
    'formula': 'Adduco Maxima', 'ripetibile': False, 'tipologia': 'Trasfigurazione Spaziale Avanzata', 'inDuello': False,
    'duelloNote': 'Non utilizzabile in duello. Crea uno spazio interno dimensionalmente espanso all'interno di un contenitore (es. borse, tende, stanze).',
    'movimento': 'Insieme di più circonferenze concentriche che richiamano l'espansione molecolare interna.',
    'movimentoSvg': 'M 75,75 m -50,0 a 50,50 0 1,1 100,0 a 50,50 0 1,1 -100,0 M 75,75 m -25,0 a 25,25 0 1,1 50,0 a 25,25 0 1,1 -50,0',
    'descrizione': 'Sofisticata distorsione dello spazio-tempo: genera una piega dimensionale interna permanente lasciando intatto il perimetro visibile esterno (es. Stanza delle Necessità o borse senza fondo).',
    'etimologia': 'Dal latino 'adducere' (aggiungere, dilatare) e 'maxima'.'
  },
  {
    'id': 'lumos-solem', 'anno': 5, 'annoLabel': 'V Anno', 'nome': 'Incanto della Luce Solare (Lumos Solem)',
    'formula': 'Lumos Solem', 'ripetibile': True, 'tipologia': 'Luce Pura / Anti-Oscuro', 'inDuello': True,
    'duelloNote': 'Utilizzabile in duello per sprigionare un fascio accecante di luce solare pura, efficace per neutralizzare gli Inferi e sciogliere le tenebre magiche.',
    'movimento': 'Puntamento verticale verso l'alto con fendente solare in avanti.',
    'movimentoSvg': 'M 75,120 L 75,40 M 75,30 A 20,20 0 1,1 74,30',
    'descrizione': 'Variante ad altissima intensità di Lumos. Genera una luce e calore identici a quelli del sole estivo, scacciando creature oscure della notte e incenerendo vegetali tenebrosi.',
    'etimologia': 'Dal latino 'lumen' e 'sol, solis' (luce del sole).'
  },
  {
    'id': 'obliviate', 'anno': 5, 'annoLabel': 'V Anno', 'nome': 'Cancellazione della Memoria (Oblivion / Obliviate)',
    'formula': 'Obliviate', 'ripetibile': False, 'tipologia': 'Magia della Mente / Modifica Mnemonica', 'inDuello': False,
    'duelloNote': 'Non utilizzabile nei duelli sportivi (uso riservato agli Obliviatori ministeriali o a maghi oscuri).',
    'movimento': 'Torsione lenta del polso in senso antiorario a spirale risucchiante diretta alla fronte.',
    'movimentoSvg': 'M 75,75 m -35,0 a 35,35 0 1,0 70,0 a 25,25 0 1,0 -50,0 a 15,15 0 1,0 30,0',
    'descrizione': 'Ideato nel Seicento da Mnemosine Radford. Cancella ricordi specifici o interi fili conduttori della memoria babbana o magica. Se eseguito male può provocare danni neurologici permanenti (Area di Broca).',
    'etimologia': 'Dal latino 'oblivisci' (dimenticare, cancellare dalla mente).'
  },
  {
    'id': 'rallegrante', 'anno': 5, 'annoLabel': 'V Anno', 'nome': 'Incantesimo Rallegrante / di Euforia',
    'formula': 'Incantesimo Rallegrante', 'ripetibile': False, 'tipologia': 'Magia Emozionale / Non-Verbale', 'inDuello': True,
    'duelloNote': 'Utilizzabile in duello contro creature amortali: agisce sullo stato emozionale stimolando il rilascio di serotonina, temporanea difesa contro Dissennatori.',
    'movimento': 'Tracciare una lettera D capovolta verso il basso, come a mimare un sorriso.',
    'movimentoSvg': 'M 40,75 L 110,75 C 110,110 40,110 40,75 Z',
    'descrizione': 'Ideato nel tardo Medioevo dal giullare di corte Felic Summerbee. La sua formula verbale è andata perduta ma viene eseguito efficacemente in modo non verbale per indurre euforia.',
    'etimologia': 'Formula perduta di matrice folklorica.'
  },

  # --- M.A.G.O. & ARTI OSCURE ---
  {
    'id': 'titillando', 'anno': 6, 'annoLabel': 'M.A.G.O. / Arti Oscure', 'nome': 'Fattura Solleticante Eterea (Titillando)',
    'formula': 'Titillando', 'ripetibile': True, 'tipologia': 'Fattura Eterea / Deconcentrazione', 'inDuello': True,
    'duelloNote': 'Utilizzabile in duello. Evoca mani ectoplasmatiche palpabili che assalgono e distraggono l'avversario solleticandolo.',
    'movimento': 'Onda circolare fluttuante seguita da una rapida vibrazione delle dita.',
    'movimentoSvg': 'M 30,75 C 50,45 70,105 90,75 C 100,55 110,95 125,75',
    'descrizione': 'Descritta in Maledictio: materializza mani spettrali di pura energia che toccano e infastidiscono il corpo della vittima azzerandone la mira.',
    'etimologia': 'Dal latino 'titillare' (solleticare, provocare solletico).'
  },
  {
    'id': 'exulcero', 'anno': 6, 'annoLabel': 'M.A.G.O. / Arti Oscure', 'nome': 'Fattura Ustionante / Pungente (Exulcero)',
    'formula': 'Exulcero', 'ripetibile': True, 'tipologia': 'Fattura Offensiva / Lesiva', 'inDuello': True,
    'duelloNote': 'Molto efficace in duello: causa bruciori e vesciche istantanee sulla cute della vittima, mandandola al tappeto.',
    'movimento': 'Stoccata orizzontale a punta di lancia verso la pelle del rivale.',
    'movimentoSvg': 'M 35,75 L 115,75 M 95,55 L 115,75 L 95,95',
    'descrizione': 'Produce ferite simili a bruciature di sigaro o punture urticanti dolorose. Trattabile tempestivamente con essenza di Dittamo.',
    'etimologia': 'Dal latino 'exulcerare' (produrre ulcere, piaghe).'
  },
  {
    'id': 'monstrum', 'anno': 6, 'annoLabel': 'M.A.G.O. / Arti Oscure', 'nome': 'Fattura Orcovolante (Monstrum)',
    'formula': 'Monstrum', 'ripetibile': False, 'tipologia': 'Fattura Evocativa / Offensiva', 'inDuello': True,
    'duelloNote': 'Utilizzabile in duello. Evoca mostruose figure volanti tenebrose che assaltano il viso dell'avversario graffiando e impedendogli la vista.',
    'movimento': 'Arco ad ali d'uccello sopra il capo terminante con un fendente in avanti.',
    'movimentoSvg': 'M 35,85 Q 55,35 75,75 Q 95,35 115,85 L 75,115 Z',
    'descrizione': 'Evoca mostruose figure volanti tenebrose che si fiondano sulla faccia dell'avversario graffiando e impedendogli la vista. Richiede contatto visivo diretto.',
    'etimologia': 'Dal latino 'monstrum' (prodigio terrificante, creatura mostruosa).'
  },
  {
    'id': 'dismundo', 'anno': 6, 'annoLabel': 'M.A.G.O. / Arti Oscure', 'nome': 'Incantesimo delle Visioni Spaventose (Dismundo)',
    'formula': 'Dismundo', 'ripetibile': False, 'tipologia': 'Magia Psichica / Non-Verbale', 'inDuello': True,
    'duelloNote': 'Utilizzabile in duello avanzato (anche non verbalmente): proietta la mente della vittima in visioni apocalittiche, paralizzandola dal terrore.',
    'movimento': 'Spirale concava dall'esterno verso l'interno all'altezza della fronte.',
    'movimentoSvg': 'M 75,35 A 40,40 0 1,1 74,35 M 75,50 A 25,25 0 1,1 74,50',
    'descrizione': 'Genera nella mente del bersaglio vivide allucinazioni di mondi spaventosi e rovine, minandone irrimediabilmente la lucidità e la forza di volontà.',
    'etimologia': 'Dal latino 'dis-' (separazione) e 'mundus' (mondo, realtà).'
  },
  {
    'id': 'locomotor-mortis', 'anno': 6, 'annoLabel': 'M.A.G.O. / Arti Oscure', 'nome': 'Maledizione della Pastoia (Locomotor Mortis)',
    'formula': 'Locomotor Mortis', 'ripetibile': False, 'tipologia': 'Maledizione / Inibizione Motoria Traumatica', 'inDuello': True,
    'duelloNote': 'Utilizzabile in duello. Incrocia dolorosamente le gambe della vittima come lacci di scarpe serrati, provocando caduta rovinosa e distorsioni.',
    'movimento': 'Movimento caratteristico della mano a forma di gancio serrato.',
    'movimentoSvg': 'M 55,40 C 95,40 105,75 80,95 C 65,105 55,85 70,75 L 75,115',
    'descrizione': 'Capostipite della Famiglia delle Pastoie. Lega saldamente le estremità inferiori provocando dolori intensi e deformazioni articolari temporanee.',
    'etimologia': 'Dal latino 'locomotor' (che attiene al moto) e 'mortis' (della morte, rigido).'
  },
  {
    'id': 'locomotor-wibbly', 'anno': 6, 'annoLabel': 'M.A.G.O. / Arti Oscure', 'nome': 'Maledizione Gambe di Gelatina (Locomotor Wibbly)',
    'formula': 'Locomotor Wibbly', 'ripetibile': False, 'tipologia': 'Maledizione / Debilitazione Motoria', 'inDuello': True,
    'duelloNote': 'Utilizzabile in duello. Emette un'aura arancione che priva le gambe di rigidità ossea facendole collassare come budino.',
    'movimento': 'Onda sinuosa che simula il cavallo interno dei pantaloni (ferro di cavallo ondulato).',
    'movimentoSvg': 'M 45,40 Q 60,90 75,70 Q 90,90 105,40',
    'descrizione': 'Conosciuta anche come Maledizione Zampe di Medusa. Rende le gambe del soggetto prive di tono e consistenza, provocando l'immediata caduta.',
    'etimologia': 'Dal latino 'locomotor' e l'inglese 'wobbly' / 'wibbly' (traballante, gelatinoso).'
  },
  {
    'id': 'sectumsempra', 'anno': 6, 'annoLabel': 'M.A.G.O. / Arti Oscure', 'nome': 'Maledizione Dissanguante (Sectumsempra)',
    'formula': 'Sectumsempra', 'ripetibile': True, 'tipologia': 'Maledizione Oscura / Taglio Letale', 'inDuello': True,
    'duelloNote': 'Utilizzabile in duelli all'ultimo sangue. Trasforma la bacchetta in una spada invisibile che trancia carne e vasi sanguigni provocando rapido dissanguamento.',
    'movimento': 'Fendente netto e saettante nell'aria, diagonale o orizzontale, come un colpo di sciabola.',
    'movimentoSvg': 'M 30,30 L 120,120 M 115,90 L 120,120 L 90,115',
    'descrizione': 'Maledizione oscura ideata dal Principe Mezzosangue (Severus Piton). Non emette luci né suoni: fende l'aria lacerando profondamente il corpo del nemico. Se non curato all'istante con il contro-rituale Vulnera Sanentur conduce a morte.',
    'etimologia': 'Dal participio latino 'sectum' (tagliato, reciso) e 'semper' (per sempre).'
  },
  {
    'id': 'vulnera-sanentur', 'anno': 6, 'annoLabel': 'M.A.G.O. / Medimagia', 'nome': 'Canto Curativo Contro-Sectumsempra (Vulnera Sanentur)',
    'formula': 'Vulnera Sanentur', 'ripetibile': True, 'tipologia': 'Curativo Avanzato / Contro-Maledizione', 'inDuello': False,
    'duelloNote': 'Non utilizzabile nella concitazione del duello: richiede di essere intonato come una nenia melodica ripetuta per tre volte sulle ferite aperte.',
    'movimento': 'Tracciamento continuo di un'onda fluida sopra le piaghe senza toccare il corpo.',
    'movimentoSvg': 'M 35,75 Q 55,45 75,75 Q 95,105 115,75',
    'descrizione': 'Contro-maledizione specifica di Sectumsempra. Il primo passaggio arresta l'emorragia, il secondo pulisce le carni e fa rifluire il sangue, il terzo cicatrizza e risalda i tessuti.',
    'etimologia': 'Dal latino 'vulnera sanentur' (che le ferite siano guarite).'
  },
  {
    'id': 'stalker-convocatus', 'anno': 6, 'annoLabel': 'M.A.G.O. / Arti Oscure', 'nome': 'Evocazione Demone Stalker (Stalker Convocatus)',
    'formula': 'Stalker Convocatus', 'ripetibile': False, 'tipologia': 'Evocazione Demoniaca / Spionaggio', 'inDuello': False,
    'duelloNote': 'Non da duello. Evoca una sentinella demoniaca a 3 o più occhi per sorvegliare luoghi pubblici o seguire persone.',
    'movimento': 'Movimento continuo e ondulato della bacchetta concentrandosi su una figura geometrica con tanti lati quanti gli occhi desiderati (minimo triangolo a 3 lati).',
    'movimentoSvg': 'M 40,110 L 75,35 L 110,110 Z M 75,65 A 10,10 0 1,1 74,65',
    'descrizione': 'Evoca uno Stalker, demone-spia sferico e butterato su tre zampe d'uccello che comunica solo sussurrando al proprio padrone ciò che ha visto. Neutralizzabile solo con Bombarda.',
    'etimologia': 'Dall'inglese 'stalker' (pedinatore) e latino 'convocare'.'
  },
  {
    'id': 'animaleus-nobodyx', 'anno': 6, 'annoLabel': 'M.A.G.O. / Magia Correttiva', 'nome': 'Incantesimo di Ripristino Umano (Animaleus Nobodyx)',
    'formula': 'Animaleus Nobodyx', 'ripetibile': False, 'tipologia': 'Trasfigurazione Correttiva / Disvelamento', 'inDuello': True,
    'duelloNote': 'Utilizzabile in duello contro animagi o avversari trasfigurati per forzarne istantaneamente il ritorno alla forma umana originaria.',
    'movimento': 'Puntare con assoluta fermezza la bacchetta verso l'individuo trasfigurato pronunciando chiaramente la formula rituale.',
    'movimentoSvg': 'M 35,75 L 115,75 M 100,55 L 115,75 L 100,95',
    'descrizione': 'Formula strategica di disvelamento identitario ('nessuno è più animale'). Riattiva istantaneamente le funzioni neurofisiologiche umane, frequenza cardiaca ed encefalica.',
    'etimologia': 'Composto pseudo-latino 'animal-eus' e 'nobody' (nessuno è più animale).'
  },
  {
    'id': 'reverto', 'anno': 6, 'annoLabel': 'M.A.G.O. / Trasfigurazione', 'nome': 'Controincantesimo Trasfigurativo di I Livello (Reverto)',
    'formula': 'Reverto', 'ripetibile': False, 'tipologia': 'Contro-incantesimo Trasfigurativo', 'inDuello': True,
    'duelloNote': 'Utilizzabile in duello per annullare rapidamente trasfigurazioni semplici applicate su oggetti o creature sul campo.',
    'movimento': 'Movimento spiraleggiante retrogrado con stoccata al centro.',
    'movimentoSvg': 'M 110,75 A 35,35 0 1,0 40,75 M 40,75 L 75,75',
    'descrizione': 'Annulla le alterazioni molecolari semplici ripristinando il ceppo e la conformazione originaria del materiale o dell'organismo.',
    'etimologia': 'Dal latino 'revertere' (ritornare allo stato originario).'
  },
  {
    'id': 'reparifarge', 'anno': 6, 'annoLabel': 'M.A.G.O. / Trasfigurazione', 'nome': 'Incantesimo di Rettifica Trasfigurativa (Reparifarge)',
    'formula': 'Reparifarge', 'ripetibile': False, 'tipologia': 'Detrasfigurazione Correttiva', 'inDuello': False,
    'duelloNote': 'Non da duello. Risana trasfigurazioni mal riuscite o parziali (es. calici con piume o zampette residue).',
    'movimento': 'Movimento circolare ampio focalizzando esclusivamente la forma originaria del soggetto.',
    'movimentoSvg': 'M 75,35 A 40,40 0 1,1 74,35',
    'descrizione': 'Incantesimo principe della Detrasfigurazione accademica. Riconduce la materia mal trasfigurata ai suoi parametri corretti.',
    'etimologia': 'Dal latino 'reparare' e radice da 'effigies' / '-farge'.'
  },
  {
    'id': 'morsmordre', 'anno': 7, 'annoLabel': 'M.A.G.O. / Magia Oscura', 'nome': 'Evocazione del Marchio Nero (Morsmordre)',
    'formula': 'Morsmordre', 'ripetibile': False, 'tipologia': 'Magia Oscura / Marchio del Terrore', 'inDuello': False,
    'duelloNote': 'Non impiegabile come attacco in duello. Viene scagliato in alto verso il cielo per firmare un luogo di massacro.',
    'movimento': 'Puntare la bacchetta verso la volta celeste e imprimere una rotazione a spirale verso l'alto con un lampo verde veleno.',
    'movimentoSvg': 'M 75,120 Q 55,80 75,55 Q 95,30 75,25',
    'descrizione': 'Proietta nel cielo notturno un colossale teschio formato da fumo verde smeraldo da cui fuoriesce un serpente vivo dalla bocca. Simbolo di Lord Voldemort e dei Mangiamorte.',
    'etimologia': 'Dal latino 'mors' (morte) e il francese 'mordre' (mordere).'
  },
  {
    'id': 'avada-kedavra', 'anno': 7, 'annoLabel': 'M.A.G.O. / Imperdonabili', 'nome': 'Anatema che Uccide (Avada Kedavra)',
    'formula': 'Avada Kedavra', 'ripetibile': False, 'tipologia': 'Maledizione Senza Perdono / Omicida', 'inDuello': True,
    'duelloNote': 'Usata in scontro mortale dai maghi oscuri. Illegale secondo la legge magica del 1717 (pena l'ergastolo ad Azkaban). Non può essere bloccata da Protego; può essere solo schivata o intercettata da un solido barriera materiale.',
    'movimento': 'Movimento a saetta o fulmine secco con puntamento letale accompagnato da un'autentica e viscerale volontà di uccidere.',
    'movimentoSvg': 'M 40,30 L 95,30 L 55,75 L 110,75 L 45,125',
    'descrizione': 'La peggiore delle Arti Oscure. Sprigiona un bagliore accecante verde smeraldo accompagnato da un boato ruggente: recide istantaneamente il legame tra anima e corpo senza lasciare traccia fisica o anatomica di morte.',
    'etimologia': 'Dall'aramaico 'avada kedavra' ('che la cosa sia distrutta').'
  },
  {
    'id': 'crucio', 'anno': 7, 'annoLabel': 'M.A.G.O. / Imperdonabili', 'nome': 'Maledizione Torturante (Crucio)',
    'formula': 'Crucio', 'ripetibile': False, 'tipologia': 'Maledizione Senza Perdono / Tortura', 'inDuello': True,
    'duelloNote': 'Usata nei combattimenti oscuri. Infligge un'agonia fisica totale che paralizza la vittima al suolo. Illegale (ergastolo ad Azkaban).',
    'movimento': 'Puntamento fisso e penetrante traendo piacere dal tormento.',
    'movimentoSvg': 'M 75,30 L 75,120 M 45,60 L 105,60 M 45,90 L 105,90',
    'descrizione': 'Genera un dolore spasmodico lancinante paragonabile a mille lame incandescenti piantate nelle carni. Un'esposizione prolungata distrugge la mente e conduce alla pazzia irreversibile (es. i coniugi Paciock).',
    'etimologia': 'Dal verbo latino 'cruciare' (tormentare, mettere in croce).'
  },
  {
    'id': 'imperio', 'anno': 7, 'annoLabel': 'M.A.G.O. / Imperdonabili', 'nome': 'Maledizione del Dominio (Imperio)',
    'formula': 'Imperio', 'ripetibile': False, 'tipologia': 'Maledizione Senza Perdono / Controllo Mentale', 'inDuello': True,
    'duelloNote': 'Usata in duello per soggiogare l'avversario e fargli deporre le armi o volgerlo contro i suoi alleati. Contrastabile solo con una volontà di ferro o occlumanzia.',
    'movimento': 'Movimento morbido e serpeggiante della bacchetta come ad azionare i fili di una marionetta invisibile.',
    'movimentoSvg': 'M 45,45 Q 75,20 105,45 Q 75,75 45,105 Q 75,130 105,105',
    'descrizione': 'Anatema delle Marionette. Priva la vittima di ogni libero arbitrio e pensiero critico, inducendo una beatitudine ingannevole in cui esegue ciecamente ogni ordine dell'incantatore.',
    'etimologia': 'Dal latino 'imperare' (comandare, esercitare assoluto potere).'
  },

  # --- GRIMORIO ARITMANTICO & SCIENZE TRASFIGURATIVE ---
  {
    'id': 'signo', 'anno': 0, 'annoLabel': 'Aritmanzia', 'nome': 'Incantesimo Segnante / Tracciante (Signo)',
    'formula': 'Signo', 'ripetibile': False, 'tipologia': 'Aritmantico Fondamentale / Tracciamento', 'inDuello': False,
    'duelloNote': 'Non utilizzabile in duello. È l'incantesimo cardine con cui gli aritmanti tracciano figure geometriche perfette su pietre, pavimenti o tessuti.',
    'movimento': 'Posizionare la bacchetta perpendicolarmente alla superficie e muoverla per formare la figura geometrica desiderata.',
    'movimentoSvg': 'M 75,25 A 50,50 0 1,1 74,25 Z',
    'descrizione': 'Traccia sul terreno o su qualsiasi superficie figure geometriche luminose (dal cerchio all'ellisse, 1-9) che svaniscono lasciando il segno perfetto impresso nella materia.',
    'etimologia': 'Dal latino 'signare' (tracciare, incidere un sigillo).'
  },
  {
    'id': 'finite-incantatem', 'anno': 0, 'annoLabel': 'Controincantesimi', 'nome': 'Controincantesimo Generale (Finite Incantatem)',
    'formula': 'Finite Incantatem', 'ripetibile': False, 'tipologia': 'Contro-incantesimo Generale', 'inDuello': True,
    'duelloNote': 'Essenziale in ogni duello: annulla all'istante l'effetto di gran parte delle fatture e degli incantesimi in corso su di sé o sui compagni.',
    'movimento': 'Fendente orizzontale secco a tagliare la trama magica dell'incanto avversario.',
    'movimentoSvg': 'M 30,75 L 120,75 M 105,60 L 120,75 M 105,90 L 120,75',
    'descrizione': 'Il controincantesimo per eccellenza. La sua valenza calcolata è 1, ma la grande aritmante Bridget Wenlock dimostrò nel XIII secolo la sua naturale affinità con il numero 7, il più potente serbatoio di opposizione magica.',
    'etimologia': 'Dal latino 'finire' (porre fine) e 'incantamentum' (incantesimo).'
  },
  {
    'id': 'coerceo', 'anno': 0, 'annoLabel': 'Elementale', 'nome': 'Formula di Controllo dell'Acqua (Coerceo)',
    'formula': 'Coerceo', 'ripetibile': False, 'tipologia': 'Elementale Acqua / Controllo', 'inDuello': True,
    'duelloNote': 'Utilizzabile in duello. Plasma torrenti e muri d'acqua per deflettere fiamme, travolgere il rivale o spegnere attacchi incendiari.',
    'movimento': 'Se l'acqua è già presente: scatto secco del polso verso il basso. Se evocata: puntamento fermo appena fuoriesce dalla punta.',
    'movimentoSvg': 'M 75,30 L 75,115 M 55,95 L 75,115 L 95,95',
    'descrizione': 'Formula aritmantica che assoggetta l'elemento naturale dell'Acqua (associato al numero 1 nella T.L.A.). Chi lo padroneggia sente l'acqua come un prolungamento della bacchetta.',
    'etimologia': 'Dal latino 'coercere' (contenere, domare, tenere a freno).'
  },
  {
    'id': 'finge', 'anno': 0, 'annoLabel': 'Elementale', 'nome': 'Formula di Controllo dell'Aria (Finge)',
    'formula': 'Finge', 'ripetibile': False, 'tipologia': 'Elementale Aria / Controllo', 'inDuello': True,
    'duelloNote': 'Utilizzabile in duello. Genera potenti vortici e barriere eoliche che deviano dardi magici e proiettili solidi.',
    'movimento': 'Mulinello orizzontale del polso da sinistra a destra con scatto in avanti.',
    'movimentoSvg': 'M 35,75 Q 75,40 115,75 Q 75,110 35,75',
    'descrizione': 'Domina e modella i flussi dell'aria e del vento (associati al numero 5 e all'etere classico nel Codex).',
    'etimologia': 'Dal latino 'fingere' (modellare, dare forma).'
  },
  {
    'id': 'adultero', 'anno': 0, 'annoLabel': 'Elementale', 'nome': 'Formula di Controllo della Terra (Adultero)',
    'formula': 'Adultero', 'ripetibile': False, 'tipologia': 'Elementale Terra / Controllo', 'inDuello': True,
    'duelloNote': 'Utilizzabile in duello. Erige muraglie di pietra o fango per parare colpi nemici o dissesta il suolo sotto i piedi del rivale.',
    'movimento': 'Puntamento secco al terreno seguito da uno strappo verso l'alto con entrambe le mani sulla presa.',
    'movimentoSvg': 'M 40,115 L 75,35 L 110,115',
    'descrizione': 'Governa la stabilità della terra, zolle e pietre (associata al numero 6 nella T.L.A.). Impiegato anche nella creazione della base dei pozzi comunicanti.',
    'etimologia': 'Dal latino 'adulterare' (alterare la natura e lo stato originale della materia).'
  },
  {
    'id': 'plasma', 'anno': 0, 'annoLabel': 'Elementale', 'nome': 'Formula di Controllo del Fuoco (Plasma)',
    'formula': 'Plasma', 'ripetibile': False, 'tipologia': 'Elementale Fuoco / Controllo', 'inDuello': True,
    'duelloNote': 'Utilizzabile in duello. Plasma fiammate, serpenti di fuoco o scudi termici contro attacchi di gelo o creature della notte.',
    'movimento': 'Sferzata orizzontale arcuata della bacchetta dal basso verso l'alto rilasciando la fiamma.',
    'movimentoSvg': 'M 35,110 C 60,80 60,50 75,35 C 90,50 90,80 115,110 Z',
    'descrizione': 'Controlla le forze del fuoco naturale o magico (associato al numero 8 nella T.L.A.). Richiede notevole padronanza per evitare ritorni di fiamma.',
    'etimologia': 'Dal greco 'plásma' (ciò che viene forgiato o plasmato nel calore).'
  },
  {
    'id': 'phi-porta', 'anno': 0, 'annoLabel': 'Aritmanzia', 'nome': 'Incantesimo Proporzionale Aureo (Phi Porta)',
    'formula': 'Phi Porta', 'ripetibile': False, 'tipologia': 'Traslazione / Varchi Aritmantici', 'inDuello': False,
    'duelloNote': 'Non utilizzabile in duello. Richiede di disegnare con Signo un rettangolo aureo continuo su una parete prima di aprire il varco.',
    'movimento': 'Disegnare un rettangolo continuo con rapporto lati 1,618 con la bacchetta perpendicolare.',
    'movimentoSvg': 'M 40,35 L 110,35 L 110,115 L 40,115 Z',
    'descrizione': 'Sfrutta la proporzione divina (1,618) del numero d'oro per aprire un passaggio segreto su una parete solida. Il varco deve essere aperto entro due minuti con la parola o gesto stabiliti.',
    'etimologia': 'Dalla lettera greca 'Phi' (simbolo della sezione aurea di Fidia) e 'porta'.'
  },
  {
    'id': 'phi-revelio', 'anno': 0, 'annoLabel': 'Aritmanzia', 'nome': 'Incantesimo Celante Aureo (Phi Revelio)',
    'formula': 'Phi Revelio', 'ripetibile': False, 'tipologia': 'Occultamento / Crittografia Magica', 'inDuello': False,
    'duelloNote': 'Non utilizzabile in duello. Usato per occultare scritture su pergamena leggibili solo con chiave d'accesso.',
    'movimento': 'Tracciamento rettangolo aureo sulla pergamena con Signo e tocco al centro.',
    'movimentoSvg': 'M 45,45 L 105,45 L 105,105 L 45,105 Z M 75,75 L 75,75',
    'descrizione': 'Permette di nascondere un messaggio scritto su pergamena rendendolo invisibile dopo 5 minuti dal tracciamento, riattivabile solo tramite gesto o parola segreta.',
    'etimologia': 'Da 'Phi' e il latino 'revelare' (svelare, togliere il velo).'
  },
  {
    'id': 'nodum-solvo', 'anno': 0, 'annoLabel': 'Aritmanzia', 'nome': 'Scioglimento dei Sigilli (Nodum Solvo)',
    'formula': 'Nodum Solvo', 'ripetibile': False, 'tipologia': 'Contro-Sigillo Aritmantico', 'inDuello': False,
    'duelloNote': 'Non utilizzabile in duello. Procedimento minuzioso per spezzare un sigillo applicato a un oggetto disegnando un pentacolo materiale.',
    'movimento': 'Puntare al centro del pentacolo disegnato e visualizzare la figura geometrica originaria spezzandone un lato.',
    'movimentoSvg': 'M 75,25 L 90,70 L 135,70 L 100,100 L 112,145 L 75,115 L 38,145 L 50,100 L 15,70 L 60,70 Z',
    'descrizione': 'Permette al creatore di un sigillo (o a maghi eccezionalmente potenti) di dissolvere il vincolo magico racchiuso nell'oggetto.',
    'etimologia': 'Dal latino 'nodum solvere' (sciogliere il nodo gordiano o magico).'
  },
  {
    'id': 'prior-incantatem', 'anno': 0, 'annoLabel': 'Investigazione', 'nome': 'Rivelazione della Memoria della Bacchetta (Prior Incantatem)',
    'formula': 'Prior Incantatem', 'ripetibile': False, 'tipologia': 'Rivelazione / Indagine Magica', 'inDuello': False,
    'duelloNote': 'Utilizzabile solo in casi rari di connessione tra bacchette gemelle con lo stesso nucleo (Prior Incantatio). Normalmente usato in indagini forensi ministeriali.',
    'movimento': 'Giunzione punta a punta con la bacchetta da ispezionare.',
    'movimentoSvg': 'M 75,30 L 75,70 M 75,80 L 75,120',
    'descrizione': 'Costringe una bacchetta a rilasciare l'ombra e l'eco degli ultimi sortilegi castati in ordine temporale inverso.',
    'etimologia': 'Dal latino 'prior' (precedente) e 'incantamentum' (incantesimo).'
  },
  {
    'id': 'protego-totalum', 'anno': 0, 'annoLabel': 'Difesa di Zona', 'nome': 'Protezione Totale di Zona (Protego Totalum)',
    'formula': 'Protego Totalum', 'ripetibile': True, 'tipologia': 'Difensivo Statico di Zona (I.D.S.)', 'inDuello': False,
    'duelloNote': 'Non da duello rapido: sortilegio perimetrale di protezione per fortificare una dimora o un accampamento.',
    'movimento': 'Disegnare il simbolo dell'infinito (lemniscata) tenendo la bacchetta sopra la propria testa prima di pronunciare la formula.',
    'movimentoSvg': 'M 40,75 C 40,55 60,55 75,75 C 90,95 110,95 110,75 C 110,55 90,55 75,75 C 60,95 40,95 40,75 Z',
    'descrizione': 'Incantesimo difensivo statico (I.D.S.) che erige una cupola impenetrabile a gran parte degli incantesimi esterni. Potenziato inscrivendo un'ellisse e ripetendo fino a 9 volte ai vertici.',
    'etimologia': 'Dal latino 'protegere' e 'totalus' (difesa totale ad area).'
  },
  {
    'id': 'muffliato', 'anno': 0, 'annoLabel': 'Difesa di Zona', 'nome': 'Incantesimo Antiacustico di Zona (Muffliato)',
    'formula': 'Muffliato', 'ripetibile': True, 'tipologia': 'Difensivo Statico di Zona / Acustico', 'inDuello': False,
    'duelloNote': 'Non da duello. Crea un ronzio indistinto nelle orecchie di chi si trova all'esterno della zona protetta, nascondendo conversazioni.',
    'movimento': 'Tre onde con il polso dal basso verso l'alto, ridiscese nel verso opposto e braccio spostato da sinistra verso destra.',
    'movimentoSvg': 'M 35,90 Q 50,45 65,90 Q 80,45 95,90 L 125,90',
    'descrizione': 'Impedisce a curiosi o spie di origliare ciò che viene detto all'interno di una stanza o di un campo.',
    'etimologia': 'Dall'inglese 'to muffle' (ovattare, soffocare i suoni).'
  },
  {
    'id': 'detecto', 'anno': 0, 'annoLabel': 'Trasfigurazione', 'nome': 'Incanto Diagnostico di Rifrazione (Detecto)',
    'formula': 'Detecto', 'ripetibile': False, 'tipologia': 'Diagnostica Trasfigurativa', 'inDuello': False,
    'duelloNote': 'Non da duello. Rivela se un oggetto è naturale o frutto di trasfigurazione mediante rifrazione luminosa.',
    'movimento': 'Puntamento orizzontale a sfioramento della superficie dell'oggetto.',
    'movimentoSvg': 'M 35,75 L 115,75 M 75,40 L 75,110',
    'descrizione': 'Provoca un bagliore luminescente sulla superficie di oggetti, piante o esseri trasfigurati o marchiati, distinguendoli da quelli autenticamente naturali.',
    'etimologia': 'Dal latino 'detegere' / 'detectum' (scoprire, smascherare).'
  },
  {
    'id': 'significo', 'anno': 0, 'annoLabel': 'Trasfigurazione', 'nome': 'Marchiatura di Oggetti Inanimati (Significo)',
    'formula': 'Significo', 'ripetibile': False, 'tipologia': 'Marchiatura Inanimata', 'inDuello': False,
    'duelloNote': 'Non da duello. Appone un marchio semitrasparente d'autore su oggetti inanimati trasfigurati.',
    'movimento': 'Pressione perpendicolare della punta concependo mentalmente il simbolo o lettera del marchio.',
    'movimentoSvg': 'M 50,50 L 100,50 L 100,100 L 50,100 Z',
    'descrizione': 'Applica un sigillo d'autore su oggetti inanimati trasfigurati per certificarne l'origine. Non va mai usato su viventi.',
    'etimologia': 'Dal latino 'significare' (imprimere un segno distintivo).'
  },
  {
    'id': 'plansigno', 'anno': 0, 'annoLabel': 'Trasfigurazione', 'nome': 'Marchiatura di Elementi Vegetali (Plansigno)',
    'formula': 'Plansigno', 'ripetibile': False, 'tipologia': 'Marchiatura Vegetale', 'inDuello': False,
    'duelloNote': 'Non da duello. Appone un marchio magico su arbusti o piante trasfigurate.',
    'movimento': 'Tocco delicato sulla foglia o fusto principale con rotazione oraria.',
    'movimentoSvg': 'M 75,115 L 75,55 Q 50,35 75,25 Q 100,35 75,55',
    'descrizione': 'Formula specifica per imprimere il marchio di trasfigurazione su elementi botanici senza alterarne l'apparato linfatico.',
    'etimologia': 'Dal latino 'planta' e 'signum'.'
  },
  {
    'id': 'fersigno', 'anno': 0, 'annoLabel': 'Trasfigurazione', 'nome': 'Marchiatura di Creature ed Entità Viventi (Fersigno)',
    'formula': 'Fersigno', 'ripetibile': False, 'tipologia': 'Marchiatura Vivente', 'inDuello': False,
    'duelloNote': 'Non da duello. Marchiatura specifica per animali e viventi (l'uso di formule per inanimati su viventi è letale).',
    'movimento': 'Sfioramento a mezz'aria sopra il dorso della creatura senza contatto diretto.',
    'movimentoSvg': 'M 40,65 Q 75,30 110,65 Q 75,100 40,65 Z',
    'descrizione': 'Formula designata per apporre marchi di riconoscimento su animali trasfigurati rispettando i flussi ematici dell'essere vivente.',
    'etimologia': 'Dal latino 'fera' (animale) e 'signum'.'
  },
  {
    'id': 'transfiguro', 'anno': 0, 'annoLabel': 'Trasfigurazione', 'nome': 'Trasfigurazione Morfologica di Forma (Transfiguro)',
    'formula': 'Transfiguro', 'ripetibile': False, 'tipologia': 'Trasfigurazione Inanimata di I Livello', 'inDuello': False,
    'duelloNote': 'Non da duello. Interviene solo sulla forma esteriore senza mutare il materiale costitutivo.',
    'movimento': 'Delineare la nuova sagoma aerea con la bacchetta mantenendo costante il materiale originario.',
    'movimentoSvg': 'M 40,110 L 75,35 L 110,110',
    'descrizione': 'Forma più elementare di trasfigurazione inanimata: muta esclusivamente l'aspetto geometrico ed esteriore dell'oggetto lasciando intatta la materia interna.',
    'etimologia': 'Dal latino 'transfigurare' (mutare aspetto).'
  },
  {
    'id': 'muto', 'anno': 0, 'annoLabel': 'Trasfigurazione', 'nome': 'Trasfigurazione Materica di Sostanza (Muto)',
    'formula': 'Muto', 'ripetibile': False, 'tipologia': 'Trasfigurazione Inanimata di II Livello', 'inDuello': False,
    'duelloNote': 'Non da duello. Muta il materiale costitutivo lasciando inalterata la forma esteriore.',
    'movimento': 'Tocco fermo al centro della massa dell'oggetto con concentrazione sulla nuova densità molecolare.',
    'movimentoSvg': 'M 75,35 L 75,115 M 40,75 L 110,75',
    'descrizione': 'Modifica la sostanza fisica di un oggetto (es. legno in metallo) mantenendone intatta la sagoma originaria. Non può generare materiali preziosi per la Legge di Gamp.',
    'etimologia': 'Dal latino 'mutare' (cambiare sostanza).'
  },
  {
    'id': 'verto', 'anno': 0, 'annoLabel': 'Trasfigurazione', 'nome': 'Trasfigurazione Totale (Verto)',
    'formula': 'Verto', 'ripetibile': False, 'tipologia': 'Trasfigurazione Inanimata di III Livello', 'inDuello': False,
    'duelloNote': 'Non da duello rapido. Muta simultaneamente sia la forma che il materiale costitutivo dell'oggetto.',
    'movimento': 'Tracciamento a doppia elica nello spazio attorno all'oggetto.',
    'movimentoSvg': 'M 45,40 Q 75,75 105,40 Q 75,75 45,110 Q 75,75 105,110',
    'descrizione': 'Il livello più elevato della trasfigurazione applicata agli oggetti: altera congiuntamente conformazione e composizione materica.',
    'etimologia': 'Dal latino 'vertere' (volgere, capovolgere interamente).'
  },
  {
    'id': 'evanesco', 'anno': 0, 'annoLabel': 'Trasfigurazione', 'nome': 'Incantesimo di Evanescenza per Inanimati e Liquidi (Evanesco)',
    'formula': 'Evanesco', 'ripetibile': False, 'tipologia': 'Evanescenza nel Non-Essere', 'inDuello': True,
    'duelloNote': 'Utilizzabile in duello: dissolve all'istante pozioni lanciate, veleni, liquidi o entità evocate da incantesimi come Serpensortia o Avis.',
    'movimento': 'Movimento a spirale centrifuga che si allarga dal centro verso l'esterno svanendo nel nulla.',
    'movimentoSvg': 'M 75,75 m -10,0 a 10,10 0 1,1 20,0 a 25,25 0 1,1 -50,0 a 40,40 0 1,1 80,0',
    'descrizione': 'Trasferisce oggetti inanimati e liquidi nel Non-Essere (la dimensione liminale di energia caotica). Opera come opposto speculare dell'evocazione.',
    'etimologia': 'Dal latino 'evanescere' (svanire, dissolversi nel nulla).'
  },
  {
    'id': 'ivanesco', 'anno': 0, 'annoLabel': 'Trasfigurazione', 'nome': 'Incantesimo di Evanescenza per Viventi (Ivanesco)',
    'formula': 'Ivanesco', 'ripetibile': False, 'tipologia': 'Evanescenza di Viventi nel Non-Essere', 'inDuello': True,
    'duelloNote': 'Utilizzabile in duello esclusivamente per dissolvere animali o creature precedentemente evocate da formule magiche (es. serpenti di Serpensortia).',
    'movimento': 'Fendente netto a triangolo aperto sopra la creatura evocata.',
    'movimentoSvg': 'M 40,110 L 75,40 L 110,110',
    'descrizione': 'Formula canonica per far svanire nel Non-Essere piante ed esseri viventi precedentemente evocati. Non può essere applicato parzialmente su un essere vivente.',
    'etimologia': 'Variante arcaica di 'evanescere'.'
  },
  {
    'id': 'dominum', 'anno': 0, 'annoLabel': 'Trasfigurazione', 'nome': 'Incantesimo Anti-Furto per Contenitori (Dominum)',
    'formula': 'Dominum', 'ripetibile': False, 'tipologia': 'Difesa Statica di Contenitori', 'inDuello': False,
    'duelloNote': 'Non da duello. Impedisce atti di evocazione o evanescenza non autorizzati sugli oggetti racchiusi in uno scrigno o armadio.',
    'movimento': 'Appoggiare la bacchetta sul contenitore e farla vibrare con una serie di picchiettii lungo tutto il perimetro.',
    'movimentoSvg': 'M 40,40 L 110,40 L 110,110 L 40,110 Z M 75,40 L 75,110',
    'descrizione': 'Garantisce che soltanto il legittimo proprietario possa interagire magicamente con il contenuto protetto di un forziere o mobiletto.',
    'etimologia': 'Dal latino 'dominus' (padrone, signore del possesso).'
  },
  {
    'id': 'obstringo-circulum', 'anno': 0, 'annoLabel': 'Trasfigurazione', 'nome': 'Trasfigurazione Circolare Intermittente (Obstringo Circulum)',
    'formula': 'Obstringo Circulum', 'ripetibile': True, 'tipologia': 'Trasfigurazione Programmata a Cicli', 'inDuello': False,
    'duelloNote': 'Non da duello. Programma alternanze cicliche tra trasformazione e detrasfigurazione a orari prefissati.',
    'movimento': 'Tracciare cerchi il cui diametro corrisponde all'intervallo temporale desiderato (es. 5 cm per 5 secondi di ciclo).',
    'movimentoSvg': 'M 75,30 A 45,45 0 1,1 74,30 Z M 75,50 A 25,25 0 1,1 74,50 Z',
    'descrizione': 'Rinnova ciclicamente gli effetti di un incanto trasfigurativo annullandoli e riattivandoli a intervalli regolari, ricaricando l'effetto.',
    'etimologia': 'Dal latino 'obstringere' (vincolare a patto) e 'circulus' (ciclo temporale).'
  }
]

# Enrich every spell with arithmantic calculations
enriched_spells = []
for s in raw_spells:
    v, total_sum = calc_v(s['formula'])
    opp = 5 - v + 5
    geom = geometry_map.get(v, 'Figura Aritmantica')
    max_rep = v if s.get('ripetibile', False) else 1
    
    letters = [c.upper() for c in s['formula'] if c.upper() in pythagorean]
    bd = ' + '.join([f"{c}({pythagorean[c]})" for c in letters])
    note_arith = f"Valenza Magica {v} (somma pitagorica {total_sum} ridotta a {v}). Valenza opposta di simmetria: {opp}. Figura operativa: {geom}. Limite di ripetibilità strutturale: {max_rep} volte."

    enriched_spells.append({
        'id': s['id'],
        'anno': s['anno'],
        'annoLabel': s['annoLabel'],
        'nome': s['nome'],
        'formula': s['formula'],
        'valenza': v,
        'sommaLettere': total_sum,
        'valenzaOpposta': opp,
        'ripetibile': s.get('ripetibile', False),
        'maxRipetizioni': max_rep,
        'figuraGeometrica': geom,
        'tipologia': s['tipologia'],
        'inDuello': s['inDuello'],
        'duelloNote': s['duelloNote'],
        'movimento': s['movimento'],
        'movimentoSvg': s['movimentoSvg'],
        'descrizione': s['descrizione'],
        'etimologia': s.get('etimologia', ''),
        'noteAritmantiche': note_arith
    })

print(f'Total enriched spells: {len(enriched_spells)}')

js_content = '// spellsData.js - Archivio Completo degli Incantesimi suddiviso per Anni
'
js_content += '// Fonti: Codex Arithmantiae, Manuale di D.C.A.O., Exorcismis Occultis, Maledictio, Trasfigurazione, Dispensa Incantesimi

'
js_content += 'const SPELLS_DATA = ' + json.dumps(enriched_spells, indent=2, ensure_ascii=False) + ';

'
js_content += 'if (typeof module !== "undefined" && module.exports) {
  module.exports = SPELLS_DATA;
}
'

with open('/Users/andreamorachioli/.gemini/antigravity/scratch/portale-incantesimi/spellsData.js', 'w', encoding='utf-8') as f:
    f.write(js_content)

print('Successfully written updated spellsData.js')
