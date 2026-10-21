# -*- coding: utf-8 -*-
"""
Completamento delle pozioni dal V al VII Anno per il compendio didattico.
"""
import json

pozioni_v_vi_vii = [
    # V ANNO
    {
        "id": "pot-risata",
        "nome": "Pozione della Risata",
        "nomeAlternativo": "Laughing Potion (Zygmunt Budge)",
        "anno": 5,
        "annoLabel": "V Anno",
        "tipologia": "Alteratrice di Stato / Goliardica",
        "coloreFinale": "Giallo sole",
        "tempoPreparazione": "45 minuti",
        "difficolta": "Avanzato",
        "metodoAssunzione": "Ingestione",
        "ingredienti": [
            "Acqua di Sorgente (1/2 litro)",
            "Aculei di Knarl (3)",
            "Ali di Billywig (17)",
            "Alioto (10 foglie)",
            "Peluria di Puffola Pigmea (1)",
            "Rafano in polvere (1 pizzico)"
        ],
        "preparazione": [
            "1. Aggiungere mezzo litro d'acqua di sorgente e foglie di Alioto tritate, mescolando lentamente per 5 volte in senso orario.",
            "2. Posizionare il volto al centro del calderone ed emettere una risata sonora per 3 secondi.",
            "3. Polverizzare 17 ali di Billywig in mortaio, aggiungerle e mescolare 3 volte in senso antiorario.",
            "4. Aggiungere 3 aculei di Knarl a distanza di 3 secondi l'uno dall'altro, portare a bollore.",
            "5. Mescolare 7 volte in senso orario e 7 volte in senso antiorario, ridere per 3 secondi sul vapore.",
            "6. Rasare una Puffola Pigmea e spargerne i peli sulla superficie, mescolare per 5 volte in senso antiorario a fuoco vivo.",
            "7. Ridere per 10 secondi sul composto, aggiungere il rafano, mescolare 8 volte in senso orario e imbottigliare."
        ],
        "avvertenze": "Indossare protezioni respiratorie contro i pollini di Alioto. Utile per stordire Banshee e mettere in fuga Mollicci col riso.",
        "inventoreOrigine": "Creata da Zygmunt Budge in gioventù su indicazione della nonna.",
        "descrizione": "Induce un'allegria contagiosa e risate irrefrenabili. Se preparata male oscilla tra isteria e malinconia."
    },
    {
        "id": "pot-restringente",
        "nome": "Soluzione Restringente",
        "nomeAlternativo": "Shrinking Solution (Formula Reducio)",
        "anno": 5,
        "annoLabel": "V Anno",
        "tipologia": "Trasformante / Riduzione",
        "coloreFinale": "Verde acido brillante",
        "tempoPreparazione": "1 ora e 20 minuti",
        "difficolta": "Avanzato",
        "metodoAssunzione": "Ingestione a gocce o contatto",
        "ingredienti": [
            "Bruchi schiacciati (5)",
            "Essenza di Cicuta Virosa (3 gocce)",
            "Grinzafico sbucciato (2)",
            "Infuso di Assenzio (3 cucchiai)",
            "Margherita (4 gambi tritati)",
            "Milza di ratto (1)",
            "Sanguisughe pestate (4)"
        ],
        "preparazione": [
            "1. Sbucciare i Grinzafichi pestandone buccia e polpa; tritare i gambi di margherita e schiacciare 5 bruchi.",
            "2. Inserire 5 misurini di Grinzafico e mezzo litro d'acqua. [Opzionale: 6 giri in senso orario per regressione d'età].",
            "3. Scaldare per 25 secondi, unire margherite e pasta di bruchi lasciando in infusione per 30 minuti.",
            "4. Spegnere, unire 3 cucchiai d'Assenzio, mescolare 10 volte in senso orario, aggiungere 3 misurini di succo di sanguisughe mescolando 6 volte in senso antiorario.",
            "5. Aggiungere 2 misurini di milza di ratto, nebulizzare 3 gocce di Cicuta Virosa, mescolare 5 volte in senso antiorario.",
            "6. Cuocere a fiamma alta per 10 secondi, infondere per 30 minuti e lanciare la formula 'Reducio' direttamente sul liquido prima di imbottigliare."
        ],
        "avvertenze": "Lanciare 'Reducio' sul liquido e non sul calderone. L'eccesso fa scomparire il soggetto.",
        "inventoreOrigine": "Zygmunt Budge, 1500.",
        "descrizione": "Rimpicciolisce oggetti, carichi o esseri viventi. Con procedimento alterato induce regressione d'età (da rana a girino)."
    },
    {
        "id": "pot-tartagliante",
        "nome": "Pozione Tartagliante",
        "nomeAlternativo": "Pozione Balbettante (Babbling Beverage)",
        "anno": 5,
        "annoLabel": "V Anno",
        "tipologia": "Alteratrice del Linguaggio / Goliardica",
        "coloreFinale": "Rosso corallo",
        "tempoPreparazione": "25 minuti",
        "difficolta": "Intermedio",
        "metodoAssunzione": "Ingestione",
        "ingredienti": [
            "Aconito (3 foglie)",
            "Dittamo (4 foglie)",
            "Rametto di Valeriana (1)"
        ],
        "preparazione": [
            "1. Pestare 3 foglie di aconito con 4 foglie di dittamo fino a pasta viola brillante.",
            "2. Dividere il composto in 3 parti; scaldare mezzo litro d'acqua con la valeriana portando a bollore.",
            "3. Dopo 3 minuti aggiungere la prima parte e mescolare 6 volte in senso orario.",
            "4. Ripetere per le restanti due parti, spegnere, filtrare e imbottigliare."
        ],
        "avvertenze": "Maneggiare l'aconito con guanti di drago per neutralizzare la tossicità col dittamo.",
        "inventoreOrigine": "Pozione goliardica di corte.",
        "descrizione": "Costringe il bevitore a pronunciare solo frasi sconnesse, farfugliamenti e balbettii incomprensibili."
    },
    {
        "id": "pot-invecchiante",
        "nome": "Pozione Invecchiante",
        "nomeAlternativo": "Aging Potion (Admir Gibilgeo)",
        "anno": 5,
        "annoLabel": "V Anno",
        "tipologia": "Trasformante / Aspetto",
        "coloreFinale": "Verde foglia",
        "tempoPreparazione": "40 minuti",
        "difficolta": "Avanzato",
        "metodoAssunzione": "Ingestione dosata a sorsi",
        "ingredienti": [
            "Banane mature (3)",
            "Foglia di Alchemilla (1)",
            "Milza di tritone sfilacciata (1)",
            "Pelle di Serpe del Grano essiccata e triturata (3 misurini)"
        ],
        "preparazione": [
            "1. Essiccare la pelle di serpente per 2 volte con l'Incantesimo Essiccante e tritarla finemente.",
            "2. Schiacciare le banane con 1 misurino di pelle in mortaio.",
            "3. Scaldare 1 litro d'acqua a fuoco basso, aggiungere il composto e girare lentamente per 10 volte in senso orario.",
            "4. Lasciare in infusione per 20 minuti, aggiungere la foglia di alchemilla e girare 10 volte in senso antiorario.",
            "5. Aggiungere a poco a poco la milza sfilacciata e i restanti 2 misurini di pelle di serpente, spegnere e imbottigliare."
        ],
        "avvertenze": "Modifica solo l'aspetto somatico esteriore per 48 ore; inefficace contro le linee d'età magiche come quella del Calice di Fuoco.",
        "inventoreOrigine": "Creata per errore nel 1545 da Admir Gibilgeo nel tentativo di creare l'elisir di giovinezza.",
        "descrizione": "Invecchia esteriormente l'aspetto: un sorso invecchia di mesi, mezza fiala di 2 anni interi."
    },
    {
        "id": "pot-invisibilita",
        "nome": "Pozione dell'Invisibilità",
        "nomeAlternativo": "Invisibility Potion",
        "anno": 5,
        "annoLabel": "V Anno",
        "tipologia": "Trasformante / Mimesi Ottica",
        "coloreFinale": "Argenteo scintillante (sapore frizzantino)",
        "tempoPreparazione": "13 ore (12 ore di infusione)",
        "difficolta": "Avanzato",
        "metodoAssunzione": "Ingestione (massimo 1 fiala ogni 4 mesi)",
        "ingredienti": [
            "Ciliegia sgusciata (1)",
            "Gambi di Elleboro tagliuzzati (4)",
            "Petali di Stella Alpina (10)",
            "Ragni interi (4)",
            "Unghie di Tebo polverizzate (3)"
        ],
        "preparazione": [
            "1. Bollire 1 litro d'acqua per 10 minuti, spegnere e unire la ciliegia e i 10 petali di stella alpina lasciando in infusione per 12 ore.",
            "2. Filtrare ottenendo l'infuso base; polverizzare le unghie di Tebo e tagliuzzare l'elleboro.",
            "3. Rimettere l'infuso sul fuoco unendo unghie e gambi di elleboro, mescolare 4 volte in senso antiorario.",
            "4. Aggiungere 3 ragni, mescolare 4 volte in senso orario, unire l'ultimo ragno e spegnere il fuoco."
        ],
        "avvertenze": "Non assumere più di una fiala ogni 4 mesi per evitare la perdita permanente della consistenza corporea.",
        "inventoreOrigine": "Alternativa alchemica ai mantelli dell'invisibilità.",
        "descrizione": "Rende completamente invisibile il corpo e le vesti di chi la assume per un lasso di tempo prestabilito."
    },
    {
        "id": "pot-esplosiva",
        "nome": "Pozione Esplosiva",
        "nomeAlternativo": "Exploding Potion",
        "anno": 5,
        "annoLabel": "V Anno",
        "tipologia": "Offensiva / Tattica",
        "coloreFinale": "Arancione incandescente",
        "tempoPreparazione": "Procedura classificata",
        "difficolta": "Avanzato / Pericoloso",
        "metodoAssunzione": "Lancio a contatto d'impatto",
        "ingredienti": [
            "Corno di Erumpent in polvere",
            "Coda di Erumpent",
            "Fluido Esplosivo di Erumpent"
        ],
        "preparazione": [
            "Procedura non divulgata integralmente per ragioni di sicurezza ministeriale. Richiede assunzione preventiva di Pozione del Ghiaccio e camera blindata."
        ],
        "avvertenze": "ESTREMAMENTE INSTABILE. I suoi componenti sono Materiali Commerciabili di Classe B a severo controllo.",
        "inventoreOrigine": "Artiglieria magica difensiva.",
        "descrizione": "Detona con immane potenza al minimo urto o contatto contro superfici rigide o bersagli."
    },
    {
        "id": "pot-cambiapersonalita",
        "nome": "Pozione Cambiapersonalità",
        "nomeAlternativo": "Gender-Switching Draught",
        "anno": 5,
        "annoLabel": "V Anno",
        "tipologia": "Trasformante / Strutturale",
        "coloreFinale": "Rossastro",
        "tempoPreparazione": "45 minuti",
        "difficolta": "Avanzato",
        "metodoAssunzione": "Ingestione immediata calda",
        "ingredienti": [
            "Artigli di Ippogrifo in polvere (4)",
            "Capello del bevitore (1)",
            "Crine di Unicorno (1)",
            "Occhio di Serpente (1)",
            "Polvere di Cristallo tritata (1 misurino)",
            "Scorza di radice di Salice Piangente (1)",
            "Sangue di Folletto (5 gocce)",
            "Zampa di rana (1)"
        ],
        "preparazione": [
            "1. Portare a bollore l'acqua; ricavare e polverizzare la scorza di salice piangente essiccata assieme agli artigli d'Ippogrifo e alla polvere di cristallo.",
            "2. Mescolare le polveri per 10 minuti, versare nel calderone con 5 gocce di sangue di folletto e riposare per 10 minuti.",
            "3. Spegnere, unire zampa di rana, crine di unicorno e il capello della persona; girare in senso antiorario per 36 volte.",
            "4. Imbottigliare; inserire l'occhio di serpente nel bicchiere un attimo prima di bere (deve sciogliersi a contatto)."
        ],
        "avvertenze": "Va bevuta bollente entro 10 minuti. L'antidoto è una seconda dose della pozione stessa.",
        "inventoreOrigine": "Alchimia anatomica seicentesca.",
        "descrizione": "Muta l'organismo esteriore e il timbro vocale del bevitore nella versione di sé stesso del sesso opposto per 24 ore senza alterare l'anima."
    },
    {
        "id": "pot-intruglio-confondente",
        "nome": "Intruglio Confondente",
        "nomeAlternativo": "Confusing Concoction",
        "anno": 5,
        "annoLabel": "V Anno",
        "tipologia": "Alteratrice di Stato / Illusoria",
        "coloreFinale": "Trasparente (consistenza pastosa)",
        "tempoPreparazione": "4 ore",
        "difficolta": "Intermedio / Avanzato",
        "metodoAssunzione": "Ingestione",
        "ingredienti": [
            "Coclearia (18 foglie)",
            "Levistico (15 foglie)",
            "Lumache Cornute (2)",
            "Starnutaria (18 foglie)"
        ],
        "preparazione": [
            "1. Creare un infuso con 10 foglie di Levistico, 10 di Coclearia e 10 di Starnutaria portando a bollore e lasciando in infusione per 3 ore e 40 minuti.",
            "2. Mescolare 6 volte in senso orario e filtrare.",
            "3. Pestare in mortaio 5 foglie di Levistico, 1 lumaca cornuta, 8 foglie di Coclearia e 8 di Starnutaria fino a pasta.",
            "4. Versare la pasta nell'infuso su fiamma bassa nell'arco di 10 minuti, mescolare 8 volte in senso antiorario.",
            "5. Aggiungere la seconda lumaca cornuta, mescolare lentamente 3 volte in senso orario con moto ondulatorio alto-basso e 7 volte in senso antiorario prima di imbottigliare."
        ],
        "avvertenze": "Svanisce autonomamente dopo 6 ore. Antidoto: Pozione Aguzzaingegno.",
        "inventoreOrigine": "Composto classico d'esame al quinto anno.",
        "descrizione": "Offusca il discernimento inducendo allucinazioni vivide, imprudenza e percezione distorta dell'ambiente."
    },
    {
        "id": "pot-aguzzaingegno",
        "nome": "Pozione Aguzzaingegno",
        "nomeAlternativo": "Pozione Genialotta (Wit-Sharpening Potion)",
        "anno": 5,
        "annoLabel": "V Anno",
        "tipologia": "Cognitiva / Antidoto Confusione",
        "coloreFinale": "Viola acceso",
        "tempoPreparazione": "35 minuti",
        "difficolta": "Intermedio",
        "metodoAssunzione": "Ingestione bollente",
        "ingredienti": [
            "Bile di Armadillo (5 gocce)",
            "Milza di Tritone (1)",
            "Radice di Zenzero (1)",
            "Scarabei essiccati e tritati (10)"
        ],
        "preparazione": [
            "1. Tagliare la radice di zenzero a metà per la lunghezza; essiccare 10 scarabei per 2 volte e tritarli in mortaio.",
            "2. Mettere mezza radice in acqua, accendere il fuoco, portare a bollore per 10 minuti.",
            "3. Unire 2 gocce di bile di armadillo (vira al blu), aggiungere la polvere di scarabei e altre 3 gocce di bile.",
            "4. Mescolare per 9 volte in senso antiorario; aggiungere il resto dello zenzero in 4 pezzi nell'arco di 7 minuti.",
            "5. Mescolare in senso orario per 9 volte, unire la milza di tritone sfilacciata, mescolare 18 volte in senso orario, filtrare 2 volte e imbottigliare."
        ],
        "avvertenze": "Maneggiare la bile di armadillo con cautela (veleno da contatto). Bandita rigorosamente durante gli esami ufficiali G.U.F.O. e M.A.G.O.",
        "inventoreOrigine": "Antidoto ufficiale all'Intruglio Confondente.",
        "descrizione": "Dona fulminea chiarezza di pensiero, massima concentrazione e capacità di calcolo mentale complesso."
    },
    {
        "id": "pot-exstimulo",
        "nome": "Pozione Exstimulo (Base, Forte, Potente)",
        "nomeAlternativo": "Spell-Power Enhancer",
        "anno": 5,
        "annoLabel": "V Anno",
        "tipologia": "Potenziamento Magico",
        "coloreFinale": "Azzurro etereo",
        "tempoPreparazione": "26 ore (sobbollitura di 25 ore)",
        "difficolta": "Avanzato",
        "metodoAssunzione": "Ingestione prima del lancio",
        "ingredienti": [
            "Acqua Distillata (1 litro)",
            "Bucaneve (6 fiori)",
            "Crini di Granio (3 per Base, 9 per Forte, 21 per Potente)",
            "Radice amara (1)",
            "Sangue di Re’em (4 gocce per Base, 5 per Forte, 6 per Potente)"
        ],
        "preparazione": [
            "1. Intrecciare i crini di Granio in treccia salda; unire sangue di Re'em, treccia e acqua distillata a fiamma bassissima per 25 ore.",
            "2. Spegnere, mescolare 3 volte in senso orario e trasferire in calderone pulito.",
            "3. Tagliare la radice amara in 7 parti, pestarla estraendone i succhi e unire la fibra disidratata al calderone bollendo per 27 minuti.",
            "4. Mescolare 7 volte in senso antiorario, unire i fiori di bucaneve uno a uno, mescolare per 12 minuti, imbottigliare e aggiungere 4 cc del succo della radice amara."
        ],
        "avvertenze": "Ingredienti di Classe B. Nella variante suprema i crini di Granio possono essere sostituiti con crini di Abraxan.",
        "inventoreOrigine": "Alchimia di duello avanzata.",
        "descrizione": "Amplifica la portata e la potenza degli incantesimi lanciati: da 1 incanto (Base), fino a 4 incantesimi (Forte) o per 24 ore continue senza limiti (Potente)."
    },
    {
        "id": "pot-mopsus",
        "nome": "Pozione Mopsus",
        "nomeAlternativo": "Draught of Mopsus the Seer",
        "anno": 5,
        "annoLabel": "V Anno",
        "tipologia": "Divinatoria / Telecinetica",
        "coloreFinale": "Lilla con fumi color pesca",
        "tempoPreparazione": "7 ore",
        "difficolta": "Avanzato",
        "metodoAssunzione": "Ingestione (veggenza) o Inalazione dei fumi (telecinesi)",
        "ingredienti": [
            "Achillea (6 foglie)",
            "Alloro (3 rametti da bruciare)",
            "Gusci d'uovo di Runespoor in polvere (1 misurino)",
            "Pungiglioni di Billywig (1)",
            "Salvia (6 foglie)"
        ],
        "preparazione": [
            "1. Infuso con 6 foglie di achillea e 6 di salvia per 3 ore, filtrare e riposare per 3 ore.",
            "2. Mettere nel calderone, bruciare il primo rametto di alloro sulla bocca facendo cadere la cenere; mescolare 3 volte in senso orario a fuoco basso.",
            "3. Unire i gusci d'uovo di Runespoor, bruciare il secondo rametto d'alloro, mescolare 3 volte in senso antiorario.",
            "4. Inserire il pungiglione di Billywig, bruciare il terzo rametto d'alloro, mescolare per 6 volte alternando orario e antiorario.",
            "5. Cuocere per 45 secondi a fiamma viva e filtrare due volte."
        ],
        "avvertenze": "Non assumere per due volte consecutive per non incorrere in emicranie croniche e distacco dalla realtà.",
        "inventoreOrigine": "Intitolata all'antico indovino greco Mopso.",
        "descrizione": "Ingerita conferisce doti di chiaroveggenza divinatoria; inalata dona il potere di manipolare gli oggetti con la telecinesi senza usare la bacchetta."
    },
    {
        "id": "pot-distillato-alioto",
        "nome": "Distillato di Alioto",
        "nomeAlternativo": "Alihotsy Draught / Distillato di Ilarità",
        "anno": 5,
        "annoLabel": "V Anno",
        "tipologia": "Distillato / Psico-reattivo",
        "coloreFinale": "Blu con densi fumi dello stesso colore",
        "tempoPreparazione": "2 ore di distillazione in alambicco",
        "difficolta": "Avanzato",
        "metodoAssunzione": "Ingestione o inalazione",
        "ingredienti": [
            "Acqua Distillata (1 litro totale)",
            "Foglie di Alioto essiccate (1 kg)"
        ],
        "preparazione": [
            "1. Essiccare le foglie di Alioto e caricarle nel serbatoio dell'alambicco con mezzo litro d'acqua senza ostruire la serpentina.",
            "2. Portare a bollore a chiusura ermetica; dopo 30 minuti inizia la distillazione nel condensatore.",
            "3. Raccogliere per 60 minuti, filtrare con cotone puro, diluire con mezzo litro d'acqua distillata e mescolare dolcemente per 5 minuti."
        ],
        "avvertenze": "Gli effetti possono perdurare per giorni. L'unico antidoto noto è la melassa di Glumbumble.",
        "inventoreOrigine": "Distillazione d'Erbologia applicata.",
        "descrizione": "Scatena attacchi incontenibili di risa convulse e isteria prolungata."
    },
    {
        "id": "pot-sputafuoco",
        "nome": "Pozione Sputafuoco",
        "nomeAlternativo": "Fire-Breathing Potion",
        "anno": 5,
        "annoLabel": "V Anno",
        "tipologia": "Offensiva / Fuoco Reale",
        "coloreFinale": "Arancione scuro",
        "tempoPreparazione": "1 ora e 30 minuti",
        "difficolta": "Avanzato",
        "metodoAssunzione": "Sorso in bocca da espellere a getto (NON DEGLUTIRE)",
        "ingredienti": [
            "Corno polverizzato di drago Lungocorno Rumeno (1 misurino)",
            "Foglie di Lavanda (4)",
            "Foglie di Menta (4)",
            "Rametti di valeriana (2)",
            "Semi di Fuoco (2)"
        ],
        "preparazione": [
            "1. Tostare a fuoco per 45 minuti in mortaio di granito il corno polverizzato di Lungocorno Rumeno.",
            "2. Portare a bollore 1 litro d'acqua con la valeriana per 20 minuti; pestare intanto menta e lavanda in pasta.",
            "3. Aggiungere 2 Semi di Fuoco al calderone, mescolare 3 volte in senso orario e 9 in senso antiorario.",
            "4. Aggiungere la polvere di drago tostata e la pasta di menta e lavanda.",
            "5. Mescolare in senso orario per 15 minuti costanti, far raffreddare e imbottigliare."
        ],
        "avvertenze": "NON DEGLUTIRE: trattenere in bocca e sputare verso il bersaglio; a contatto con la saliva e l'aria si trasforma in vere fiamme ardenti. Menta e lavanda proteggono la bocca da ustioni.",
        "inventoreOrigine": "Piro-alchimia d'avanguardia.",
        "descrizione": "Consente di sputare raffiche di vero fuoco ad altissima temperatura capaci di incendiare oggetti e nemici."
    },
    # Oggetti V Anno
    {
        "id": "pot-everklena",
        "nome": "Everklena",
        "nomeAlternativo": "Falso Detergente Trasparente",
        "anno": 5,
        "annoLabel": "V Anno",
        "tipologia": "Per Oggetti / Burla",
        "coloreFinale": "Trasparente spumoso",
        "tempoPreparazione": "20 minuti",
        "difficolta": "Base",
        "metodoAssunzione": "Applicazione su superfici",
        "ingredienti": ["Liscivia magica", "Muffa di palude", "Essenza di fungo"],
        "preparazione": ["Miscelazione a freddo."],
        "avvertenze": "Genera sporcizia indelebile e muffa invece di pulire.",
        "inventoreOrigine": "Frode commerciale per vendere altri detergenti.",
        "descrizione": "Venduta come detersivo miracoloso, riveste gli oggetti colpiti di uno strato tenace di grasso e muffa."
    },
    {
        "id": "pot-laccatura-antimalocchio",
        "nome": "Laccatura Antimalocchio",
        "nomeAlternativo": "Anti-Jinx Broom Varnish",
        "anno": 5,
        "annoLabel": "V Anno",
        "tipologia": "Per Oggetti / Difensiva",
        "coloreFinale": "Resina dorata trasparente",
        "tempoPreparazione": "1 ora",
        "difficolta": "Intermedio",
        "metodoAssunzione": "Spennellatura su legni e manici di scopa",
        "ingredienti": ["Resina di frassino", "Polvere d'argento", "Corteccia di salice"],
        "preparazione": ["Fonderia a caldo e stesura a pennello."],
        "avvertenze": "Rinnovare ogni sei mesi per garantire la protezione di volo.",
        "inventoreOrigine": "Manutenzione scope da corsa.",
        "descrizione": "Respinge fatture, malocchi e sortilegi di disarcionamento scagliati contro il manico di scopa in volo."
    },
    {
        "id": "pot-fumogena",
        "nome": "Pozione Fumogena",
        "nomeAlternativo": "Smoke-Screen Potion",
        "anno": 5,
        "annoLabel": "V Anno",
        "tipologia": "Per Oggetti / Fuga",
        "coloreFinale": "Arancione pressurizzata (fumo colorato denso)",
        "tempoPreparazione": "30 minuti",
        "difficolta": "Base",
        "metodoAssunzione": "Stappatura dell'ampolla a pressione",
        "ingredienti": ["Polvere d'argento", "Pigmenti colorati", "Polvere pirica magica"],
        "preparazione": ["Imbottigliamento sotto pressione controllata."],
        "avvertenze": "Può causare tosse se inalata a causa dell'argento.",
        "inventoreOrigine": "Tattiche di occultamento.",
        "descrizione": "Appena stappata genera un'impenetrabile cortina di fumo denso colorato ideale per coprire la fuga."
    },
    {
        "id": "pot-animare-foto",
        "nome": "Pozione per Animare le Foto",
        "nomeAlternativo": "Developing Potion for Moving Photographs",
        "anno": 5,
        "annoLabel": "V Anno",
        "tipologia": "Per Oggetti / Fotografica",
        "coloreFinale": "Soluzione trasparente incolore",
        "tempoPreparazione": "25 minuti",
        "difficolta": "Base",
        "metodoAssunzione": "Bagno di sviluppo su lastre e stampe",
        "ingredienti": ["Nitrato d'argento magico", "Essenza di crisopa", "Acqua distillata"],
        "preparazione": ["Diluzione chimica in camera oscura."],
        "avvertenze": "Agisce anche su fotografie babbane ma con minore definizione.",
        "inventoreOrigine": "Fotografia magica ottocentesca.",
        "descrizione": "Dona il movimento fluido e la ripetizione dei gesti ai soggetti ritratti sulle fotografie."
    },
    {
        "id": "pot-smacchiatore-scower",
        "nome": "Smacchiatore Magico di Mrs Scower",
        "nomeAlternativo": "Mrs Scower's All-Purpose Magical Mess Remover",
        "anno": 5,
        "annoLabel": "V Anno",
        "tipologia": "Per Oggetti / Detersione Estrema",
        "coloreFinale": "Bianco schiumoso",
        "tempoPreparazione": "45 minuti",
        "difficolta": "Intermedio",
        "metodoAssunzione": "Frizione su tessuti e pavimenti",
        "ingredienti": ["Secrezione di Bundimun purificata", "Soda magica", "Succo di limone fatato"],
        "preparazione": ["Miscela concentrata ad azione solvente."],
        "avvertenze": "Elimina anche residui di ectoplasma rilasciati da fantasmi e Poltergeist.",
        "inventoreOrigine": "Inventato nel 1492 da Mrs Scower.",
        "descrizione": "Il detergente universale più famoso al mondo, capace di dissolvere qualsiasi macchia ostinata."
    },
    {
        "id": "pot-lucidante-glossy",
        "nome": "Soluzione per Pulire l’Argento di Madame Glossy",
        "nomeAlternativo": "Madame Glossy's Silver Polish",
        "anno": 5,
        "annoLabel": "V Anno",
        "tipologia": "Per Oggetti / Lucidante",
        "coloreFinale": "Crema argentea",
        "tempoPreparazione": "20 minuti",
        "difficolta": "Base",
        "metodoAssunzione": "Stesura a panno su calderoni e manufatti in argento",
        "ingredienti": ["Polvere di pietra pomice magica", "Olio di lino", "Cera protettiva"],
        "preparazione": ["Emulsione lucidante a freddo."],
        "avvertenze": "Non intacca la finitura magica degli alambicchi.",
        "inventoreOrigine": "Manutenzione argenteria magica.",
        "descrizione": "Lucidante eccezionale che rimuove ogni ossidazione donando splendore perenne a calderoni e calici d'argento."
    },

    # ==========================================
    # VI ANNO
    # ==========================================
    {
        "id": "pot-morte-vivente",
        "nome": "Distillato della Morte Vivente",
        "nomeAlternativo": "Draught of Living Death (Leticia Somnolens)",
        "anno": 6,
        "annoLabel": "VI Anno",
        "tipologia": "Sonnifero Estremo / Coma Magico",
        "coloreFinale": "Rosa pallido chiarissimo (dopo il passaggio nero-ribes)",
        "tempoPreparazione": "Circa 90 minuti (più notte di ammollo)",
        "difficolta": "M.A.G.O. / Massimo Livello",
        "metodoAssunzione": "Ingestione o contaminazione di cibo",
        "ingredienti": [
            "Acqua di luna (50 cl)",
            "Acqua Distillata (3 litri)",
            "Capolino - infiorescenza con 3 fiori lilla (2)",
            "Cervello di Bradipo (1)",
            "Fagiolo Sopoforoso schiacciato (1)",
            "Infuso di Assenzio (20 gocce)",
            "Infuso di Rugiada Lunare (4 gocce)",
            "Radice di Asfodelo in polvere (4 misurini)",
            "Radice di Valeriana a tocchetti (3)",
            "Sale marino africano (5 misurini)"
        ],
        "preparazione": [
            "1. Tenere a mollo le radici di valeriana tagliate a quadretti in acqua di luna per una notte.",
            "2. Unire sale marino africano a 3 litri d'acqua distillata e far riposare per 70 minuti, poi versare nel calderone.",
            "3. Versare 10 gocce d'Assenzio tenendo il calderone inclinato a destra, accendere a fiamma bassa, unire altre 10 gocce inclinato a sinistra (vira a color ribes scuro).",
            "4. Aggiungere 4 gocce di Rugiada Lunare, 1 Capolino e il succo del Fagiolo Sopoforoso schiacciato con lama piatta d'argento.",
            "5. Aggiungere 20 gocce dell'acqua d'ammollo di valeriana; mescolare 10 volte in senso orario (sfumatura lilla).",
            "6. Mescolare in senso antiorario finché non diventa chiaro e limpido come acqua pura.",
            "7. Inserire 7 pezzi di valeriana, mescolare 10 volte in senso antiorario, unire 4 misurini d'Asfodelo in polvere e il secondo Capolino.",
            "8. Inclinare a destra mescolando delicatamente 10 volte in senso orario e 8 in senso antiorario; riposare per 2 minuti e mezzo.",
            "9. Unire un ultimo pezzetto di valeriana e il cervello di bradipo; spegnere e imbottigliare."
        ],
        "avvertenze": "Indossare guanti di drago per calderone incandescente. Chi lo assume cade in coma profondo in cui i parametri vitali sembrano azzerati. Antidoto: Pozione Rigeneratrice.",
        "inventoreOrigine": "Inventato dalla strega Leticia Somnolens (ispirò la fiaba della Bella Addormentata). Capolavoro del manuale di Libatius Borage.",
        "descrizione": "Il più potente sonnifero conosciuto: fa cadere in un sonno indistinguibile dalla morte. Addormenta anche creature titaniche di livello XXXXX."
    },
    {
        "id": "pot-rigeneratrice",
        "nome": "Pozione Rigeneratrice",
        "nomeAlternativo": "Wiggenweld Supreme Restorative",
        "anno": 6,
        "annoLabel": "VI Anno",
        "tipologia": "Curativa Suprema / Antidoto Risvegliante",
        "coloreFinale": "Verde chiaro brillante",
        "tempoPreparazione": "Oltre 30 ore",
        "difficolta": "M.A.G.O. / Maestro",
        "metodoAssunzione": "Applicazione Topica su ferite o ingestione a gocce",
        "ingredienti": [
            "Aconito (2 foglie)",
            "Acqua di Miele (1/3 di litro)",
            "Cervello di bradipo (1)",
            "Corno di Unicorno (1)",
            "Corteccia di Sorbo Magico (40 cm divisa in due)",
            "Dittamo (2 foglie)",
            "Infuso di Rugiada Lunare (4 gocce)",
            "Mandragola in umido (1)",
            "Melma da pungiglione fresco di Billywig (1 goccia)",
            "Moly (2 foglie)",
            "Muco di Vermicolo (4 gocce)",
            "Rametto di Menta (1)",
            "Sangue di Tritone (6 gocce)",
            "Spine di Pesce Leone (5)",
            "Succo di Boom Barry (4 bacche)",
            "Succo di Horklump (13 gocce)",
            "Zanne di Chizpurfle (2)"
        ],
        "preparazione": [
            "1. Mettere mezza corteccia di Sorbo in calderone con acqua tradizionale e miele (2:1), unire menta, mandragola e corno d'unicorno a fuoco basso per 24 ore.",
            "2. Preparare intanto una pasta con cervello di bradipo e 4 gocce di muco di vermicolo; tritare in polvere spine di pesce leone, zanne di Chizpurfle e la restante corteccia.",
            "3. Dopo 24 ore spegnere, filtrare il decotto e far riposare in luogo fresco per 4 ore.",
            "4. In nuovo calderone versare 4 litri d'acqua a fiamma alta, unire 4 gocce di Rugiada Lunare e versare il decotto lungo il bordo.",
            "5. Mescolare 13 volte in senso orario, unire 6 gocce di Sangue di Tritone e 2 foglie di Aconito, mescolando 2 volte molto lentamente per un minuto.",
            "6. Aggiungere la polvere di spine e zanne, mescolare 8 volte in senso orario, abbassare la fiamma, unire 13 gocce di succo di Horklump e 4 Boom Barry schiacciate, sobbollendo per 47 minuti.",
            "7. Mescolare 9 volte in senso orario, spegnere, far cadere 1 goccia di melma fresca di Billywig, attendere 27 minuti.",
            "8. Riaccendere a bollore, unire 4 misurini della pasta di bradipo e vermicolo, mescolare 7 volte in senso antiorario, inserire 2 foglie di Moly e 2 di Dittamo, attendere 40 minuti, spegnere e imbottigliare."
        ],
        "avvertenze": "Maneggiare l'aconito con guanti di drago. È l'UNICA pozione al mondo in grado di ridestare chi è caduto vittima del Distillato della Morte Vivente.",
        "inventoreOrigine": "L'apice assoluto della Medimagia pozionistica.",
        "descrizione": "Rigenera tessuti devastati da magia oscura e ridesta istantaneamente da qualsiasi coma o letargia magica."
    },
    {
        "id": "pot-polisucco",
        "nome": "Pozione Polisucco",
        "nomeAlternativo": "Polyjuice Potion",
        "anno": 6,
        "annoLabel": "VI Anno",
        "tipologia": "Trasformante Suprema",
        "coloreFinale": "Fangoso e ribollente; colore e sapore finale variano a seconda dell'animo della persona da copiare",
        "tempoPreparazione": "1 mese (richiede 21 giorni di stufatura e plenilunio)",
        "difficolta": "M.A.G.O. Avanzato",
        "metodoAssunzione": "Ingestione immediata dopo l'aggiunta della parte corporea",
        "ingredienti": [
            "Centinodia (2 steli)",
            "Corno di Bicorno polverizzato (1)",
            "Erba fondente raccolta con la luna piena (3 misurini)",
            "Mosche Crisopa stufate per 21 giorni (2 misurini)",
            "Parte del corpo della persona da copiare (capello, forfora, unghia)",
            "Pelle tritata di Boomslang (10 cm)",
            "Sanguisughe (4)"
        ],
        "preparazione": [
            "Prima parte: Essiccare l'Erba Fondente per 3 volte con l'Incantesimo Essiccante e tritarla (3 misurini nel calderone). Tagliare gli steli di Centinodia in 10 parti e aggiungerli con acqua a fiamma bassa. Mescolare 4 volte in senso orario e lasciar fermentare per 80 minuti. Spegnere, unire 4 sanguisughe schiacciate ritmicamente. Pestare le Mosche Crisopa in pasta (rapporto 3:1), aggiungere la parte maggiore, scaldare per 30 secondi e riposare per 48 ore.",
            "Seconda parte: Tritare 3 misurini di pelle di Boomslang e 1 di corno di Bicorno polverizzato, scaldare ad alta temperatura per 20 secondi, abbassare e fermentare per 24 ore. Unire l'ultima parte di crisope e mescolare 3 volte in senso antiorario. La pozione bolle fangosa. Unire il capello un attimo prima di bere."
        ],
        "avvertenze": "Valida solo per trasformazioni tra umani: totalmente inefficace o mostruosamente deformante se usata con peli di animali o creature magiche. Durata da 10 minuti a 12 ore.",
        "inventoreOrigine": "Formula M.A.G.O. del Reparto Proibito. Variante minore: Sciroppo di Erba Fondente.",
        "descrizione": "Consente al bevitore di assumere fedelmente e integralmente le sembianze fisiche, la voce e i tratti somatici di un'altra persona."
    },
    {
        "id": "pot-traccia",
        "nome": "Pozione della Traccia",
        "nomeAlternativo": "Trace-Reading Draught for Curse-Breakers",
        "anno": 6,
        "annoLabel": "VI Anno",
        "tipologia": "Percettiva / Spezzaincantesimi",
        "coloreFinale": "Color caramello dal profumo dolce e invitante",
        "tempoPreparazione": "22 ore e mezza",
        "difficolta": "Avanzato",
        "metodoAssunzione": "Ingestione (massimo una al mese)",
        "ingredienti": [
            "Acetosa di Bosco (11 foglie)",
            "Caramello fuso (10 cl)",
            "Fagiolo Sopoforoso spremuto (2)",
            "Guscio di Granchio in polvere (3)",
            "Infuso di Achillea (50 cl, infuso per 18 ore)",
            "Radice di Cespuglio Farfallino a rondelle (2)",
            "Radice di Valeriana a rondelle (2)"
        ],
        "preparazione": [
            "1. Infuso d'Achillea per 18 ore; portare a bollore unendo 10 cl di caramello fuso da calderone da tavolo mescolando 7 volte in senso antiorario.",
            "2. Aggiungere 2 litri d'acqua, al bollore unire le 11 foglie di Acetosa una al minuto, spegnere e riposare per 4 ore.",
            "3. Polverizzare i gusci di granchio, unirvi il succo di 2 Fagioli Sopoforosi e versare nel calderone dopo le 4 ore.",
            "4. Mescolare 10 volte in senso orario, accendere per 30 secondi inserendo velocemente le rondelle di Valeriana e Cespuglio Farfallino, spegnere e filtrare."
        ],
        "avvertenze": "Non assumere più di una volta al mese per non provocare lesioni cerebrali. Permette di percepire la magia ma non insegna a decifrarla.",
        "inventoreOrigine": "Apprezzatissima dagli Spezzaincantesimi della Gringott. Variante superiore: Tonico di Rilevamento Tracce.",
        "descrizione": "Potenzia per 3 ore la sensibilità percettiva permettendo di visualizzare e seguire le tracce eteriche residue lasciate da incantesimi antichi anche di millenni."
    },
    {
        "id": "pot-antilupo",
        "nome": "Pozione Antilupo",
        "nomeAlternativo": "Wolfsbane Potion (Damocles Belby)",
        "anno": 6,
        "annoLabel": "VI Anno",
        "tipologia": "Curativa Complessa / Licantropia",
        "coloreFinale": "Blu profondo con caratteristico fumo bluastro sottile",
        "tempoPreparazione": "Molto complessa, da somministrare quotidianamente",
        "difficolta": "M.A.G.O. / Estrema Precisione",
        "metodoAssunzione": "Un calice ogni giorno per la settimana precedente la luna piena",
        "ingredienti": [
            "Aconito - Luparia (17 foglie)",
            "Acqua di Luna pura",
            "Argento finissimo in polvere",
            "Bacche di Semi di Luna",
            "Corno di Unicorno in polvere",
            "Dittamo",
            "Piuma di Augurey",
            "Sciroppo di Elleboro (2 gocce)",
            "Succo di due foglie di Mandragola",
            "Succo di sette Fagioli Soporosi",
            "Sangue di Drago (3 gocce)",
            "Tentacoli di Purvincolo (3)",
            "Uovo di Occamy delicatamente schiacciato (1)"
        ],
        "preparazione": [
            "1. Aggiungere diciassette foglie di aconito e il succo di due foglie di mandragola con tre gocce di sangue di drago.",
            "2. Regolare con assoluta precisione la temperatura, unire la pietra di luna in polvere e mescolare 3 volte in senso orario.",
            "3. Aggiungere 2 gocce di sciroppo d'elleboro e 3 tentacoli di Purvincolo mantenendo temperatura media.",
            "4. Incorporare il succo di sette fagioli soporosi uno alla volta, abbassare al minimo, schiacciare l'uovo d'Occamy nel calderone.",
            "5. Agitare la bacchetta, mescolare 6 volte in senso antiorario e completare con un secondo gesto della bacchetta."
        ],
        "avvertenze": "Sapore estremamente disgustoso: è assolutamente vietato zuccherarla o dolcificarla, pena l'annullamento chimico degli effetti. Saltare anche una sola dose rende vana l'intera terapia. Non impedisce la mutazione fisica ma preserva la mente umana.",
        "inventoreOrigine": "Ideata da Damocles Belby negli anni '70 e perfezionata dal professor Severus Piton per Remus Lupin.",
        "descrizione": "Consente al Licantropo di mantenere intatte le facoltà mentali, la memoria e la coscienza umana durante la trasformazione in luna piena, rendendolo un lupo docile e assonnato."
    },
    {
        "id": "pot-bile-armadillo",
        "nome": "Miscela di Bile di Armadillo",
        "nomeAlternativo": "Corrosive Acid Paste",
        "anno": 6,
        "annoLabel": "VI Anno",
        "tipologia": "Corrosiva / Caustica Estrema",
        "coloreFinale": "Crema densa pastosa",
        "tempoPreparazione": "4 ore",
        "difficolta": "Avanzato / Pericoloso",
        "metodoAssunzione": "Applicazione a distanza su superfici",
        "ingredienti": [
            "Aconito (5,3 dg)",
            "Ali di Pipistrello sminuzzate (1,4 dg)",
            "Amortentia (4 dl)",
            "Assenzio (6,2 dg)",
            "Bile di Armadillo (10,3 dg)",
            "Veleno di Acromantula (1,3 dg)"
        ],
        "preparazione": [
            "1. Inserire una foglia d'Assenzio nel veleno d'Acromantula per 3 ore (guanti di drago obbligatori).",
            "2. Tagliuzzare le ali di pipistrello eliminando tutta la cartilagine; far bollire 2 litri d'acqua a fuoco basso.",
            "3. Creare una pasta con l'assenzio imbevuto e l'aconito, versare nel calderone e mescolare 6 volte in senso orario, spegnere dopo 10 secondi.",
            "4. Aggiungere l'Amortentia e riaccendere a fiamma media finché i vapori non diventano completamente neri, poi spegnere.",
            "5. Unire le ali di pipistrello, mescolare 10 volte in senso antiorario, far cadere goccia a goccia la bile d'armadillo.",
            "6. Mescolare magicamente con il solo movimento della bacchetta per non liquefare il mestolo finché non diventa pastosa."
        ],
        "avvertenze": "In caso di contatto accidentale con la cute lenire all'istante con Crini di Unicorno per scongiurare necrosi profonda.",
        "inventoreOrigine": "Alchimia militare di breccia.",
        "descrizione": "Pasta iper-corrosiva capace di sciogliere in pochi minuti qualsiasi metallo, pietra o serratura incantata."
    },
    {
        "id": "pot-dorata",
        "nome": "Pozione Dorata",
        "nomeAlternativo": "Solar Orb Draught",
        "anno": 6,
        "annoLabel": "VI Anno",
        "tipologia": "Ottica / Illuminazione Magica",
        "coloreFinale": "Flusso di luce dorata pura",
        "tempoPreparazione": "50 minuti",
        "difficolta": "Intermedio",
        "metodoAssunzione": "Stappatura in ambiente chiuso",
        "ingredienti": [
            "Argento in polvere",
            "Infuso di Achillea",
            "Pietra di Luna in polvere"
        ],
        "preparazione": [
            "Sospendere le polveri metalliche nell'infuso alchemico focalizzando la luce con la bacchetta."
        ],
        "avvertenze": "Se stappata all'aperto la luce si disperde rendendo vano il preparato.",
        "inventoreOrigine": "Illuminazione monumentale d'interni.",
        "descrizione": "Emana un fascio di luce dorata che raccoglie tutte le luci della stanza formando una sfera radiosa simile a un piccolo sole sul soffitto, orientabile con la bacchetta."
    },
    {
        "id": "pot-memoria",
        "nome": "Pozione della Memoria",
        "nomeAlternativo": "Memory Potion",
        "anno": 6,
        "annoLabel": "VI Anno",
        "tipologia": "Cognitiva / Richiamo Mnestico",
        "coloreFinale": "Lilla brillante con scintille viola",
        "tempoPreparazione": "5 ore e mezza",
        "difficolta": "Avanzato",
        "metodoAssunzione": "Ingestione",
        "ingredienti": [
            "Alioto (1 radice sminuzzata)",
            "Bucaneve (4 fiori)",
            "Menta Piperita (5 foglie)",
            "Occhi di Anguilla (5)",
            "Piume di Jobberknoll (1)",
            "Radici di Mandragola in umido (1)",
            "Salvia in polvere (10 foglie essiccate)"
        ],
        "preparazione": [
            "1. Sminuzzare mandragola e radice d'alioto; pestare in crema 1 foglia di menta con 5 occhi d'anguilla.",
            "2. Essiccare la salvia per 3 volte e polverizzarla in mortaio.",
            "3. Bollire 3 litri d'acqua; dopo 10 minuti unire 4 foglie di menta e mescolare velocemente 3 volte.",
            "4. Unire i fiori di bucaneve e sobbollire per 4 ore a fiamma bassa; spegnere e filtrare 2 volte.",
            "5. In altro calderone unire 2 misurini di salvia, mescolare 6 volte in senso orario a fuoco medio, unire la pasta d'occhi d'anguilla.",
            "6. Aggiungere 8 pezzi d'alioto, mescolare 2 volte in senso orario, unire 9 pezzi di mandragola, mescolare 3 volte in senso antiorario, attendere 25 minuti.",
            "7. Inserire la piuma di Jobberknoll partendo dalla punta: a contatto con la soluzione svanisce lasciando scintille viola."
        ],
        "avvertenze": "Severamente vietata durante gli esami ufficiali. Attenua gli effetti della Pozione Obliviosa.",
        "inventoreOrigine": "Varianti minori: Elisir Scervellante di Baruffio e Soluzione Scintillante.",
        "descrizione": "Potenzia la cognizione mentale per 12 ore riportando a galla ricordi remoti, confusi o annebbiati."
    },
    {
        "id": "pot-amortentia",
        "nome": "Amortentia",
        "nomeAlternativo": "Il Filtro d'Amore Supremo",
        "anno": 6,
        "annoLabel": "VI Anno",
        "tipologia": "Filtro d'Amore / Coercizione Affettiva",
        "coloreFinale": "Madreperlaceo brillante con vapori che si innalzano a spirale",
        "tempoPreparazione": "Procedura segreta ministeriale",
        "difficolta": "M.A.G.O. / Estrema Maestria",
        "metodoAssunzione": "Ingestione nascosta in cibi o bevande",
        "ingredienti": [
            "Acqua di Luna pura",
            "Peperoncino in polvere",
            "Petali di Rosa freschissima",
            "Polvere di Perle orientali",
            "Uova di Ashwinder congelate"
        ],
        "preparazione": [
            "Procedura strettamente protetta dal Ministero della Magia per la sua eccezionale pericolosità sociale."
        ],
        "avvertenze": "Non genera vero amore (impossibile da creare artificialmente), ma una morbosa ossessione fanatica e pericolosa per chi la offre. L'odore varia per ogni individuo richiamando ciò che intimamente lo attrae.",
        "inventoreOrigine": "Creata nel XIX secolo dalla strega Corvonero Laverne de Montmorency (1823-1893).",
        "descrizione": "Il filtro d'amore più potente e temuto al mondo, paragonabile per livello di coercizione mentale alla Maledizione Imperius."
    },
    {
        "id": "pot-amicizia",
        "nome": "Pozione dell’Amicizia",
        "nomeAlternativo": "Untuoso Unguento di Gregory (Gregory’s Unctuous Unction)",
        "anno": 6,
        "annoLabel": "VI Anno",
        "tipologia": "Coercizione Mentale / Illegale",
        "coloreFinale": "Untuoso e opaco",
        "tempoPreparazione": "1 ora",
        "difficolta": "Avanzato",
        "metodoAssunzione": "Ingestione o contatto untuoso",
        "ingredienti": [
            "Foglie di Rosa",
            "Foglie di Alioto",
            "Salice Bianco"
        ],
        "preparazione": ["Procedura vietata dalle leggi magiche."],
        "avvertenze": "Considerata dal Ministero al pari della Maledizione Imperius; i suoi effetti svaniscono spontaneamente dopo 24 ore.",
        "inventoreOrigine": "Ideata da Gregory il Viscido.",
        "descrizione": "Inganna l'assuntore convincendolo che chi gli ha offerto la pozione sia il suo più caro e intimo migliore amico."
    },
    {
        "id": "pot-odio",
        "nome": "Pozione dell’Odio",
        "nomeAlternativo": "Hate Potion / Antidoto all'Infatuazione",
        "anno": 6,
        "annoLabel": "VI Anno",
        "tipologia": "Antidoto Emotivo / Rivelatrice",
        "coloreFinale": "Rosa con striature nere",
        "tempoPreparazione": "25 ore",
        "difficolta": "Avanzato",
        "metodoAssunzione": "Ingestione",
        "ingredienti": [
            "Capello della persona bersaglio (1)",
            "Essenza di Violetta (7 gocce)",
            "Occhi di ratto (3)",
            "Piume di Corvo (2)",
            "Spine di Rosa (7)"
        ],
        "preparazione": [
            "1. Portare a bollore l'acqua con 7 gocce d'Essenza di Violetta, mescolare 7 volte in senso orario, cuocere a fuoco lento per 10 minuti.",
            "2. Mescolare 2 volte in senso antiorario ogni 2 minuti per 30 minuti, unire la piuma di corvo e bollire per 7 minuti mescolando costantemente.",
            "3. Aggiungere il capello cuocendo fino al rosa, unire 3 occhi di ratto, togliere dal calderone e mescolare fino a striature nere.",
            "4. Riposare per 24 ore; scaldare poi con l'incantesimo Riscalda-Acqua, mescolare 7 volte in senso antiorario e imbottigliare."
        ],
        "avvertenze": "Legale per curare cuori infranti o spezzare filtri d'amore; vietata nei tribunali per non influenzare i verdetti.",
        "inventoreOrigine": "Alchimia comportamentale.",
        "descrizione": "Mostra impietosamente al bevitore i lati più sgradevoli, le cattive abitudini e i peggiori difetti di una persona per 24 ore."
    },
    # WonderWitch Weasley VI Anno
    {
        "id": "pot-bolle-seducenti",
        "nome": "Bolle Seducenti del Primo Amore",
        "nomeAlternativo": "First Love Beguiling Bubbles (WonderWitch)",
        "anno": 6,
        "annoLabel": "VI Anno",
        "tipologia": "Filtro d'Amore Minore / Scherzo",
        "coloreFinale": "Rosso rubino effervescente",
        "tempoPreparazione": "25 minuti",
        "difficolta": "Intermedio",
        "metodoAssunzione": "Ingestione furtiva",
        "ingredienti": ["Polvere di perle", "Essenza di fragola magica", "Rugiada mattutina"],
        "preparazione": ["Infuso effervescente con perle micro-polverizzate."],
        "avvertenze": "Effetto blando che si dissolve spontaneamente in 30 minuti esatti.",
        "inventoreOrigine": "Linea WonderWitch di Fred e George Weasley.",
        "descrizione": "Induce una tenera e passeggera infatuazione per la persona che offre la pozione."
    },
    {
        "id": "pot-cristalli-cupido",
        "nome": "Cristalli di Cupido",
        "nomeAlternativo": "Cupid Crystals (WonderWitch)",
        "anno": 6,
        "annoLabel": "VI Anno",
        "tipologia": "Filtro Emotivo / Euforizzante",
        "coloreFinale": "Rosa pastello con aroma di vaniglia e biscotto",
        "tempoPreparazione": "30 minuti",
        "difficolta": "Intermedio",
        "metodoAssunzione": "Inalazione dei vapori profumati",
        "ingredienti": ["Zucchero magico vanigliato", "Petali di rosa essiccati", "Essenza di cacao fatato"],
        "preparazione": ["Cristallizzazione a freddo da sciogliere in acqua calda."],
        "avvertenze": "Non crea amore verso una persona specifica, ma trasmette una generale sensazione di innamoramento verso il mondo.",
        "inventoreOrigine": "Fred e George Weasley.",
        "descrizione": "I suoi vapori profumati infondono spensieratezza, farfalle nello stomaco e voglia irresistibile di sorridere."
    },
    {
        "id": "pot-lacrime-crepacuore",
        "nome": "Lacrime di Crepacuore",
        "nomeAlternativo": "Heartbreak Teardrops (WonderWitch)",
        "anno": 6,
        "annoLabel": "VI Anno",
        "tipologia": "Filtro Sentimentale / Malinconia",
        "coloreFinale": "Azzurro goccia di cristallo",
        "tempoPreparazione": "35 minuti",
        "difficolta": "Intermedio",
        "metodoAssunzione": "Ingestione",
        "ingredienti": ["Melassa di Glumbumble", "Lacrime di coccodrillo", "Acqua distillata"],
        "preparazione": ["Decotto a fuoco lento."],
        "avvertenze": "Genera una struggente nostalgia per la persona lontana.",
        "inventoreOrigine": "Linea WonderWitch dei Tiri Vispi Weasley.",
        "descrizione": "Induce una passeggera ma vivida sensazione di malinconica mancanza per la persona amata."
    },
    {
        "id": "pot-miscuglio-baci",
        "nome": "Miscuglio di Baci",
        "nomeAlternativo": "Kissing Concoction (WonderWitch)",
        "anno": 6,
        "annoLabel": "VI Anno",
        "tipologia": "Cosmetica / Fascino Magnetico",
        "coloreFinale": "Rosa perla lucido",
        "tempoPreparazione": "40 minuti",
        "difficolta": "Intermedio",
        "metodoAssunzione": "Ingestione",
        "ingredienti": ["Polvere di perle", "Zucchero filato fatato", "Essenza di menta piperita"],
        "preparazione": ["Emulsione idroalcolica dolce."],
        "avvertenze": "Rende irresistibilmente desiderabili per 12 ore; priva di tossicità ma può indurre dipendenza psicologica.",
        "inventoreOrigine": "Il prodotto più venduto del negozio dei gemelli Weasley.",
        "descrizione": "Amplifica il magnetismo estetico del bevitore rendendolo straordinariamente attraente per chiunque lo guardi."
    },
    {
        "id": "pot-raggi-crepuscolari",
        "nome": "Raggi Crepuscolari di Luna",
        "nomeAlternativo": "Twilight Moonbeams (WonderWitch)",
        "anno": 6,
        "annoLabel": "VI Anno",
        "tipologia": "Profumo / Magnetismo Olfattivo",
        "coloreFinale": "Profumo spray trasparente iridescente",
        "tempoPreparazione": "30 minuti",
        "difficolta": "Intermedio",
        "metodoAssunzione": "Nebulizzazione su corpo o vesti",
        "ingredienti": ["Acqua di luna", "Essenza floreale di gelsomino notturno", "Alcol alchemico"],
        "preparazione": ["Distillazione cosmetica profumata."],
        "avvertenze": "Creata per superare i controlli ministeriali come comune profumo.",
        "inventoreOrigine": "Fred e George Weasley.",
        "descrizione": "Si fonde con la fragranza cutanea della persona generando un'aura di irresistibile fascino per un giorno intero."
    },

    # ==========================================
    # VII ANNO
    # ==========================================
    {
        "id": "pot-instabilita",
        "nome": "Essenza dell’Instabilità",
        "nomeAlternativo": "Essence of Instability (L'Antitesi della Felix Felicis)",
        "anno": 7,
        "annoLabel": "VII Anno",
        "tipologia": "Allucinogena / Destabilizzante",
        "coloreFinale": "Verde smeraldo",
        "tempoPreparazione": "15 ore (10 ore di distillazione in alambicco)",
        "difficolta": "M.A.G.O. Avanzato",
        "metodoAssunzione": "Ingestione o inalazione",
        "ingredienti": [
            "Cervello di Rana (1)",
            "Distillato di Alioto (5 gocce)",
            "Formicaleone (4 foglie)",
            "Gambi di Orchidea (7)",
            "Levistico (1 mazzetto essiccato e polverizzato)",
            "Lumache Cornute pestate (3)",
            "Mosche Crisopa (3)",
            "Occhi di Scarabeo (10)"
        ],
        "preparazione": [
            "Prima fase: Roteare 5 gocce di distillato di Alioto nel calderone a fuoco basso, cuocere un cervello di rana per un minuto a lato e toglierlo dopo 5 minuti. Aggiungere 2 litri d'acqua, 5 misurini di levistico e 7 gambi d'orchidea portando a bollore.",
            "Unire occhi di scarabeo e crisope pestati, mescolare 7 volte in senso antiorario, unire il cervello di rana tagliato in 3 parti e spegnere. Unire 4 foglie di formicaleone in infusione per 8 ore. Aggiungere 3 lumache cornute pestate, mescolare 2 volte in senso orario e filtrare 4 volte.",
            "Seconda fase: Trasferire nella caldaia dell'alambicco e distillare per 10 ore a fuoco regolare. Il condensato è la pozione finita."
        ],
        "avvertenze": "Estremamente pericolosa e sotto stretta sorveglianza ministeriale: spinge a scelte suicide e totale distacco dalla realtà.",
        "inventoreOrigine": "Studi di alchimia comportamentale del Ministero.",
        "descrizione": "Considerata l'opposto speculare della Felix Felicis: crea allucinazioni terrorizzanti, angoscia incontrollabile e conduce a decisioni irrazionali e deleterie."
    },
    {
        "id": "pot-nenia",
        "nome": "Pozione della Nenia",
        "nomeAlternativo": "Dirge Draught / Pozione Acustica della Morte",
        "anno": 7,
        "annoLabel": "VII Anno",
        "tipologia": "Acustica / Eterea",
        "coloreFinale": "Viola scuro tendente al nero (viscosa, emette costanti bolle sonore)",
        "tempoPreparazione": "Oltre 21 giorni",
        "difficolta": "M.A.G.O. Avanzato",
        "metodoAssunzione": "Scoperchiatura acustica entro 50 metri",
        "ingredienti": [
            "Acqua Distillata (2 litri)",
            "Capelli di Banshee (20)",
            "Piuma di Augurey (1)",
            "Sale Marino (3 g)",
            "Sangue di Thestral (30 cl)",
            "Scarabei Neri (4)",
            "Scilla Marittima (54 petali)",
            "Spine di Shrake (14)"
        ],
        "preparazione": [
            "1. Immergere 20 capelli di Banshee in 30 cl di sangue di Thestral per 20 giorni consecutivi (al fresco di giorno, ai raggi lunari di notte), mescolando 7 volte in senso antiorario a mezzanotte.",
            "2. Trasferire in calderone d'argento a fiamma bassa con 2 litri d'acqua distillata, unire 14 spine di Shrake e mescolare 36 volte velocissimo finché si ode un lamento.",
            "3. Portare a bollore, spegnere, unire 54 petali di Scilla Marittima per 35 minuti.",
            "4. Aggiungere la piuma d'Augurey, bollire per 25 minuti, aggiungere 3g sale marino, alzare la fiamma, unire 4 scarabei neri, spegnere, filtrare 2 volte e sigillare ermeticamente per 24 ore."
        ],
        "avvertenze": "L'ascolto per più di 10 minuti genera profondo sconforto e traumi emotivi duraturi.",
        "inventoreOrigine": "Uno dei rarissimi esempi di pozione che agisce per via acustica.",
        "descrizione": "Grazie alla continua formazione di bolle gassose produce onde sonore che echeggiano fino a cinquanta metri riproducendo strazianti lamenti di persone scomparse."
    },
    {
        "id": "pot-veritaserum",
        "nome": "Veritaserum",
        "nomeAlternativo": "Il Siero della Verità Supremo",
        "anno": 7,
        "annoLabel": "VII Anno",
        "tipologia": "Siero della Verità / Coercizione Cognitiva",
        "coloreFinale": "Completamente limpido e trasparente come l'acqua più pura",
        "tempoPreparazione": "Un ciclo lunare intero (28 giorni di fermentazione)",
        "difficolta": "M.A.G.O. Supremo / Maestria",
        "metodoAssunzione": "3 sole gocce in bevanda o cibo",
        "ingredienti": [
            "Piume di Jobberknoll",
            "Acqua pura di sorgente",
            "Principi attivi purificati a fermentazione lunare (ricetta segreta di Stato)"
        ],
        "preparazione": [
            "Preparazione magistrale custodita e strettamente regolamentata dal Ministero della Magia britannico."
        ],
        "avvertenze": "Severamente vietata la somministrazione ai minorenni. Nei processi del Wizengamot è considerata inaffidabile perché non rivela la verità oggettiva ma solo ciò che il soggetto crede vero, e può essere contrastata con l'Occlumanzia.",
        "inventoreOrigine": "Codificato dall'Ufficio Applicazione della Legge di Magia.",
        "descrizione": "Il più potente siero della verità esistente: bastano 3 gocce per costringere chi lo assume a confessare ogni segreto più intimo con tono piatto e sguardo rilassato per un'ora intera."
    },
    {
        "id": "pot-antidoto-veritaserum",
        "nome": "Antidoto al Veritaserum",
        "nomeAlternativo": "Truth Serum Antidote",
        "anno": 7,
        "annoLabel": "VII Anno",
        "tipologia": "Antidoto Specifico Cognitivo",
        "coloreFinale": "Arancione pesca luminoso",
        "tempoPreparazione": "9 ore",
        "difficolta": "M.A.G.O. Avanzato",
        "metodoAssunzione": "Ingestione preventiva o tempestiva",
        "ingredienti": [
            "Acetosa di Bosco (20 foglie)",
            "Coclearia (2 rametti - separare la polpa dalle fibre)",
            "Corno di Bicorno in polvere (4 misurini)",
            "Mosche Crisopa (10)",
            "Pungiglione di Billywig in polvere (1)",
            "Scarabei Stercorari (4)",
            "Semi di Fuoco (4)"
        ],
        "preparazione": [
            "1. Pestare foglie di Acetosa e Semi di Fuoco in mortaio; riscaldare a bianco il calderone d'argento.",
            "2. Unire a distanza di 4 secondi: 5 mosche crisopa, 4 scarabei stercorari, le restanti 5 mosche crisopa.",
            "3. Aggiungere 20 cl d'acqua, mescolare 10 volte in senso antiorario, unire la pasta di acetosa e semi di fuoco, portare a 2 litri d'acqua.",
            "4. Mescolare per 16 volte in senso antiorario e lasciare in infusione per 8 ore.",
            "5. Polverizzare bicorno e pungiglione di Billywig, mescolare per 8 volte in senso orario col retro del mestolo.",
            "6. Tagliare la coclearia estraendo la sola polpa; dopo le 8 ore spegnere il fuoco, unire la polpa e il composto di polveri, mescolare 8 volte in senso antiorario e imbottigliare."
        ],
        "avvertenze": "Garantisce protezione totale per due ore consecutive all'eventuale ingestione di Veritaserum.",
        "inventoreOrigine": "Sviluppato per agenti segreti e cospiratori magici.",
        "descrizione": "Schera la mente impedendo al Veritaserum di abbattere i freni inibitori e la capacità di dissimulazione."
    },
    {
        "id": "pot-felix-felicis",
        "nome": "Felix Felicis",
        "nomeAlternativo": "Fortuna Liquida (Formula Felixempra)",
        "anno": 7,
        "annoLabel": "VII Anno",
        "tipologia": "Fortuna Liquida / Prodigio Alchemico",
        "coloreFinale": "Oro colato brillante (bolle che guizzano sulla superficie come pesci rossi)",
        "tempoPreparazione": "6 mesi di maturazione alchemica",
        "difficolta": "M.A.G.O. Supremo / Capolavoro",
        "metodoAssunzione": "Ingestione (pochi sorsi)",
        "ingredienti": [
            "Gusci d'uovo di Occamy in polvere",
            "Infuso di Timo concentrato",
            "Ruta in polvere finissima",
            "Scilla Marittima (bulbi e fiori)",
            "Tentacoli di Purvincolo filtrati",
            "Uovo di Ashwinder congelato"
        ],
        "preparazione": [
            "1. Preparazione alchemica della durata di sei mesi esatti con dosaggi millimetrici.",
            "2. Richiede il lancio dell'incanto catalizzatore 'Felixempra' tracciando una figura a forma di otto (infinito) sopra la bocca del calderone."
        ],
        "avvertenze": "L'abuso provoca vertigini, incoscienza e pericolosissima superbia. Rigorosamente bandita da tutte le competizioni sportive ufficiali (Quidditch) e dagli esami.",
        "inventoreOrigine": "Il capolavoro assoluto ideato da Zygmunt Budge nel XVI secolo: 'Una dose di buona fortuna in bottiglia'.",
        "descrizione": "Dona straordinaria fortuna e infallibile successo in ogni impresa per un tempo commisurato alla dose, ispirando l'assuntore a scegliere la via più brillante e propizia."
    },
    {
        "id": "pot-elisir-euforia",
        "nome": "Elisir dell’Euforia",
        "nomeAlternativo": "Elixir to Induce Euphoria",
        "anno": 7,
        "annoLabel": "VII Anno",
        "tipologia": "Elisir Idroalcolico / Felicità",
        "coloreFinale": "Violaceo con la viscosità del miele (inizialmente giallo sole al limone)",
        "tempoPreparazione": "3 ore e mezza",
        "difficolta": "Avanzato",
        "metodoAssunzione": "Ingestione (massimo due dosi)",
        "ingredienti": [
            "Acqua distillata (5 litri)",
            "Aculei di Porcospino (7)",
            "Essenza di Assenzio (25 gocce nell'ampolla)",
            "Fagiolo Sopoforoso spremuto (1)",
            "Grinzafichi (2)",
            "Menta fresca (1 gambo e 12 foglie)",
            "Semi di Ricino affettati (20)"
        ],
        "preparazione": [
            "1. Portare a bollore 5 litri d'acqua in calderone d'argento con menta sminuzzata (vira a turchese); spegnere dopo 20 minuti e filtrare 3 volte.",
            "2. Tagliare a metà un Grinzafico e unirlo (vira al blu scuro); aggiungere 7 aculei di porcospino a fuoco spento.",
            "3. Sobbollire per 2 ore a fiamma media; affettare 20 semi di ricino in acqua fredda per 15 minuti finché tremano, scolarli e unirli al calderone.",
            "4. Schiacciare il Fagiolo Sopoforoso facendone cadere il succo nel calderone; unire l'altro Grinzafico intero finché diventa blu chiaro.",
            "5. Versare 25 gocce di Essenza d'Assenzio nell'ampolla finale; far raffreddare la pozione, filtrarla e versarla nell'ampolla agitando con moto rotatorio fino a violaceo denso come miele."
        ],
        "avvertenze": "Dura 12 ore; l'eccesso provoca ilarità smodata, voglia improvvisa di cantare e prurito al naso (arginato dal rametto di menta).",
        "inventoreOrigine": "Elisir classico di benessere e antidoto ai singhiozzi incoercibili.",
        "descrizione": "Infonde un irrazionale e radioso buon umore, scacciando qualsiasi ombra di tristezza."
    },
    # Raccolta Elisir VII Anno
    {
        "id": "pot-elisir-mandragola",
        "nome": "Elisir di Mandragola",
        "nomeAlternativo": "Elixir of Mandrake",
        "anno": 7,
        "annoLabel": "VII Anno",
        "tipologia": "Elisir / Antidoto Trasfigurativo",
        "coloreFinale": "Limpido dal sentore acidulo",
        "tempoPreparazione": "Lenta macerazione lunare",
        "difficolta": "Avanzato",
        "metodoAssunzione": "Ingestione",
        "ingredienti": ["Lavorazione integrale di ogni singola parte di Mandragole mature", "Alcol purissimo"],
        "preparazione": ["Fermentazione alcolica calibrata su precise fasi astronomiche."],
        "avvertenze": "Antidoto aspecifico a spettro più ampio rispetto al Ricostituente.",
        "inventoreOrigine": "Raccolta di Elisir (pag. 123).",
        "descrizione": "Riporta alla forma originale qualsiasi corpo alterato da pozioni complesse o incantesimi trasfigurativi."
    },
    {
        "id": "pot-elisir-7",
        "nome": "Elisir 7",
        "nomeAlternativo": "Elixir Seven / Uniformante Tricologico",
        "anno": 7,
        "annoLabel": "VII Anno",
        "tipologia": "Elisir Cosmetico Alcolico",
        "coloreFinale": "Tonalità color cioccolato dal forte profumo speziato",
        "tempoPreparazione": "40 minuti",
        "difficolta": "Intermedio",
        "metodoAssunzione": "Applicazione Topica sul cuoio capelluto (5 sole gocce)",
        "ingredienti": ["Base alcolica al 25%", "Essenze vegetali speziate", "Polvere d'ambra"],
        "preparazione": ["Infusione idroalcolica profumata."],
        "avvertenze": "Non superare 5 gocce: dosi eccessive causano repentina caduta dei capelli.",
        "inventoreOrigine": "Cosmesi magica d'alta moda.",
        "descrizione": "Uniforma perfettamente la tonalità e il colore della chioma mascherando capelli bianchi o discromie."
    },
    {
        "id": "pot-elisir-peperoncino",
        "nome": "Elisir al Peperoncino",
        "nomeAlternativo": "Chilli Elixir",
        "anno": 7,
        "annoLabel": "VII Anno",
        "tipologia": "Elisir Termico Idroalcolico",
        "coloreFinale": "Rosso fuoco vivace",
        "tempoPreparazione": "30 minuti",
        "difficolta": "Intermedio",
        "metodoAssunzione": "Massimo 7 gocce (sul petto per tosse o nel calderone)",
        "ingredienti": ["Base alcolica al 46%", "Peperoncini magici concentrati", "Semi di fuoco"],
        "preparazione": ["Distillazione alcolica ad alta gradazione."],
        "avvertenze": "Usare per non più di 7 gocce.",
        "inventoreOrigine": "Alchimia termica.",
        "descrizione": "Additivo catalizzatore per pozioni ignee ed esplosive; gocciolato sul petto debella febbri e raffreddori al pari della Pepata."
    },
    {
        "id": "pot-elisir-lunga-vita",
        "nome": "Elisir di Lunga Vita",
        "nomeAlternativo": "Elixir of Life (Nicolas Flamel)",
        "anno": 7,
        "annoLabel": "VII Anno",
        "tipologia": "Alchemico Supremo / Immortalità",
        "coloreFinale": "Rubino brillante trasparente",
        "tempoPreparazione": "Legata alla Pietra Filosofale",
        "difficolta": "Leggendario / Inaccessibile",
        "metodoAssunzione": "Ingestione regolare e periodica",
        "ingredienti": [
            "Pietra Filosofale (catalizzatore unico)",
            "Oro alchemico puro disciolto",
            "Acqua purissima"
        ],
        "preparazione": [
            "Prodigio dell'Alchimia suprema perfezionato da Nicolas Flamel; la ricetta è andata perduta con la distruzione della Pietra Filosofale nel 1992."
        ],
        "avvertenze": "Crea dipendenza fisiologica assoluta: interrompere l'assunzione conduce ineluttabilmente alla morte. Non impedisce al corpo di invecchiare.",
        "inventoreOrigine": "Creato nel XIV secolo dal celebre alchimista francese Nicolas Flamel (vissuto oltre 665 anni).",
        "descrizione": "Rende immortale chiunque lo assuma regolarmente e possiede la facoltà di restituire un corpo fisico a un'anima disincarnata."
    },
    # Preparati Illegali VII Anno
    {
        "id": "pot-bevanda-disperazione",
        "nome": "Bevanda della Disperazione",
        "nomeAlternativo": "Pozione Smeraldo (Emerald Potion)",
        "anno": 7,
        "annoLabel": "VII Anno",
        "tipologia": "Magia Oscura / Elisir Eterno Illegale",
        "coloreFinale": "Verde fosforescente brillante",
        "tempoPreparazione": "Procedura oscura bandita",
        "difficolta": "Magia Oscura Suprema",
        "metodoAssunzione": "Ingestione forzata fino all'ultima goccia",
        "ingredienti": [
            "Composti occulti di Magia Oscura",
            "Acqua di Lete concentrata",
            "Resine eterne inestinguibili"
        ],
        "preparazione": ["Rituale di Magia Oscura pura protetto da Azkaban."],
        "avvertenze": "Non può essere travasata, aspirata, evaporata, trasfigurata o annullata con la magia: può solo essere interamente bevuta.",
        "inventoreOrigine": "Creata da Lord Voldemort per proteggere il medaglione-Horcrux nella grotta marina.",
        "descrizione": "Elisir eterno che scatena incubi atroci, visioni terrorizzanti, panico straziante e una sete devastante lasciando la vittima inerme."
    },
    {
        "id": "pot-pozione-morte",
        "nome": "Pozione della Morte",
        "nomeAlternativo": "American MACUSA Execution Draught",
        "anno": 7,
        "annoLabel": "VII Anno",
        "tipologia": "Magia Oscura / Esecutiva",
        "coloreFinale": "Nero corvino della consistenza dell'olio minerale denso",
        "tempoPreparazione": "Segreto di Stato degli Indicibili",
        "difficolta": "Avanzato / Letale",
        "metodoAssunzione": "Immersione totale del condannato",
        "ingredienti": [
            "Ricordi felici estratti dal condannato (Pensatoio)",
            "Composti caustici neri e corrosivi"
        ],
        "preparazione": ["Custodita dagli Indicibili del Dipartimento dei Misteri americano."],
        "avvertenze": "Utilizzata fino al secolo scorso in America per le condanne capitali magiche.",
        "inventoreOrigine": "MACUSA (Dipartimento dei Misteri).",
        "descrizione": "Mostra alla vittima i suoi ricordi più cari ammaliandola come un Pensatoio, per poi avvolgerla e dissolverla senza sofferenza violenta."
    },
    {
        "id": "pot-rigenerazione-oscura",
        "nome": "Pozione della Rigenerazione Oscura",
        "nomeAlternativo": "Riddle Rebirth Potion",
        "anno": 7,
        "annoLabel": "VII Anno",
        "tipologia": "Magia Oscura Suprema / Rituale",
        "coloreFinale": "Scintille accecanti e vapore denso biancastro",
        "tempoPreparazione": "Rituale della notte al cimitero",
        "difficolta": "Magia Oscura Suprema",
        "metodoAssunzione": "Immersione dell'omuncolo rudimentale nel calderone gigante",
        "ingredienti": [
            "Osso del padre (preso all'insaputa)",
            "Carne del servo (donata volontariamente)",
            "Sangue del nemico (strappato con la forza)",
            "Veleno di Nagini",
            "Sangue di unicorno"
        ],
        "preparazione": [
            "Calderone gigante colmo di liquido ribollente su fuoco mistico in cimitero profanato."
        ],
        "avvertenze": "Magia Oscura antica e proibita. Detenzione a vita ad Azkaban per chiunque ne possieda gli scritti.",
        "inventoreOrigine": "Arcana formula utilizzata da Lord Voldemort la notte del 24 giugno 1995 a Little Hangleton.",
        "descrizione": "Rigenera un corpo fisico integro e adulto per un mago mutilato, disincarnato o ridotto a larva spirituale."
    }
]

# Append to data_pozioni.py
with open('/Users/andreamorachioli/.gemini/antigravity/scratch/portale-incantesimi/scripts/data_pozioni.py', 'r', encoding='utf-8') as f:
    current_content = f.read()

# remove old test prints
clean_content = '\n'.join([line for line in current_content.split('\n') if not line.startswith('print(')])

with open('/Users/andreamorachioli/.gemini/antigravity/scratch/portale-incantesimi/scripts/data_pozioni.py', 'w', encoding='utf-8') as f:
    f.write(clean_content)
    f.write('\n# POZIONI ANNI V, VI, VII AGGIUNTE:\n')
    f.write('pozioni_data.extend(' + json.dumps(pozioni_v_vi_vii, ensure_ascii=False, indent=4) + ')\n')
    f.write('print(f"Totale Pozioni caricate nel compendio finale: {len(pozioni_data)}")\n')

print("Fase V-VI-VII Pozioni completata con successo!")
