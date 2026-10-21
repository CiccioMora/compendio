# -*- coding: utf-8 -*-
"""
Script per aggiungere le pozioni del IV, V, VI e VII Anno a data_pozioni.py.
"""
import json

pozioni_restanti = [
    # ==========================================
    # IV ANNO
    # ==========================================
    {
        "id": "pot-veleno-chizpurfle",
        "nome": "Veleno per Chizpurfle",
        "nomeAlternativo": "Chizpurfle Pest Spray",
        "anno": 4,
        "annoLabel": "IV Anno",
        "tipologia": "Veleno / Pesticida",
        "coloreFinale": "Arancione (nebulizzabile)",
        "tempoPreparazione": "2 ore e 15 minuti",
        "difficolta": "Intermedio",
        "metodoAssunzione": "Nebulizzazione a spruzzo da erogatore",
        "ingredienti": [
            "Foglie di Rabarbaro sminuzzate (3)",
            "Piuma di Augurey (1)"
        ],
        "preparazione": [
            "1. Portare a bollore mezzo litro d'acqua a fiamma alta.",
            "2. Sminuzzare in mortaio le foglie di rabarbaro girando solo in senso orario e versarle al bollore.",
            "3. Mescolare in senso antiorario per 6 volte, alzare la fiamma e aggiungere la Piuma di Augurey.",
            "4. Mescolare 5 volte in senso orario, spegnere e lasciare in infusione per 2 ore.",
            "5. Filtrare per 3 volte e imbottigliare in flacone nebulizzatore."
        ],
        "avvertenze": "Basta una sola spruzzata per tramortirli; l'eccesso li rende iper-resistenti alla magia richiedendo l'intervento del Ministero.",
        "inventoreOrigine": "Disinfestazione da parassiti dei calderoni.",
        "descrizione": "Abbatte e disinfesta le colonie di Chizpurfle annidate nei calderoni incrostati o sul vello di creature magiche."
    },
    {
        "id": "pot-doxycida",
        "nome": "Doxycida",
        "nomeAlternativo": "Doxycide (Zygmunt Budge)",
        "anno": 4,
        "annoLabel": "IV Anno",
        "tipologia": "Veleno / Pesticida",
        "coloreFinale": "Nero, oleoso e fortemente maleodorante",
        "tempoPreparazione": "1 ora e 45 minuti",
        "difficolta": "Avanzato",
        "metodoAssunzione": "Nebulizzazione spray",
        "ingredienti": [
            "Essenza di Cicuta (3 cucchiai)",
            "Essenza di Cicuta Virosa (5 cucchiai)",
            "Fegato di Drago (1)",
            "Gusci di Streeler (2)",
            "Bundimun (2)",
            "Tintura di Tormentilla (3 gocce)"
        ],
        "preparazione": [
            "1. Pestare 2 Bundimun fino a pasta e versarne 3 misurini nel calderone con 2 misurini di gusci di Streeler tritati finemente.",
            "2. Mescolare 5 volte in senso orario, scaldare a fuoco basso per 15 secondi.",
            "3. Tritare il fegato di drago e unirlo al calderone, mescolando vigorosamente 10 volte in senso antiorario.",
            "4. Aggiungere mezzo litro d'acqua e lasciare in infusione per 1 ora a fiamma bassissima.",
            "5. Spegnere, unire 3 cucchiai di Cicuta, mescolare 4 volte in senso orario, aggiungere 5 cucchiai di Cicuta Virosa e 3 gocce di Tintura di Tormentilla.",
            "6. Mescolare 9 volte in senso antiorario, riscaldare a fiamma altissima per 16 secondi, poi tenere a fuoco basso per 30 minuti prima di imbottigliare."
        ],
        "avvertenze": "Maneggiare i gusci di Streeler con cautela per via delle punte velenose.",
        "inventoreOrigine": "Ideato da Zygmunt Budge nel XVI secolo sull'isola di Hermetray.",
        "descrizione": "Stordisce e paralizza all'istante i Doxy infestanti consentendo la loro rimozione senza pericolo di subire morsi velenosi."
    },
    {
        "id": "pot-agliosa",
        "nome": "Pozione Agliosa",
        "nomeAlternativo": "Garlic Potion / Protezione Vampirica",
        "anno": 4,
        "annoLabel": "IV Anno",
        "tipologia": "Veleno Selettivo / Protezione",
        "coloreFinale": "Biancastro maleodorante",
        "tempoPreparazione": "26 ore",
        "difficolta": "Intermedio",
        "metodoAssunzione": "Ingestione fredda",
        "ingredienti": [
            "Aglio (1 corona intera)",
            "Legno di Frassino in pezzi lunghi un indice (1)"
        ],
        "preparazione": [
            "1. Versare l'acqua nel calderone e immergervi la bacchetta accendendo l'incanto 'Lumos' prima di accendere il fuoco, estraendola poi con concentrazione.",
            "2. Accendere il fuoco a fiamma bassa; tagliare il Frassino e farlo bollire per 2 ore.",
            "3. Spegnere, travasare e attendere 24 ore di decantazione.",
            "4. Pestare l'aglio in mortaio e aggiungerlo al liquido, riportando a bollore fino a colore biancastro."
        ],
        "avvertenze": "Va consumata fredda nonostante il gusto sgradevole. Non impedisce ai vampiri esperti di fiutare l'aglio prima dell'attacco.",
        "inventoreOrigine": "Formula classica contro creature non-morte ematofaghe.",
        "descrizione": "Rende il sangue di chi la beve imbevibile e altamente velenoso per i Vampiri per circa 24 ore."
    },
    {
        "id": "pot-gas-strangolante",
        "nome": "Gas Strangolante",
        "nomeAlternativo": "Strangling Gas",
        "anno": 4,
        "annoLabel": "IV Anno",
        "tipologia": "Veleno Gassoso / Tossico",
        "coloreFinale": "Verde petrolio che sprigiona vapore trasparente",
        "tempoPreparazione": "13 ore (12 ore di riposo)",
        "difficolta": "Avanzato",
        "metodoAssunzione": "Inalazione del vapore sprigionato",
        "ingredienti": [
            "Essenza di Belladonna (1 ml)",
            "Orchidea (1 fiore)",
            "Ortica (4 foglie sminuzzate)",
            "Ramo di Tasso bruciato (1)"
        ],
        "preparazione": [
            "1. Versare mezzo litro d'acqua nel calderone con 1 ml di Essenza di Belladonna e far bollire per 25 minuti.",
            "2. Unire l'orchidea e 4 foglie d'ortica sminuzzate, attendere 25 minuti e mescolare 10 volte in senso orario.",
            "3. Spegnere; ricavare cenere bruciando un ramo di tasso e versarne 1 misurino nel calderone.",
            "4. Versare in flacone con coperchio, mescolare 7 volte in senso antiorario, sigillare subito e attendere 12 ore prima dell'apertura."
        ],
        "avvertenze": "Indossare guanti di drago per l'ortica. Il gas cessa la produzione 20 minuti dopo l'apertura; per altre vie non ha effetto.",
        "inventoreOrigine": "Tossicologia militare magica.",
        "descrizione": "I suoi vapori provocano una soffocante sensazione tattile allucinatoria di mani che stringono il collo fino alla perdita dei sensi."
    },
    {
        "id": "pot-veleno-trasparente",
        "nome": "Veleno Trasparente",
        "nomeAlternativo": "Karlaus' Invisible Poison",
        "anno": 4,
        "annoLabel": "IV Anno",
        "tipologia": "Veleno Letale / Ingestione",
        "coloreFinale": "Rosso acceso ma a contatto con liquidi diviene totalmente trasparente",
        "tempoPreparazione": "45 minuti",
        "difficolta": "Avanzato",
        "metodoAssunzione": "Ingestione furtiva",
        "ingredienti": [
            "Boletus Satanas triturato finissimo (1)",
            "Succo di Oleandro (10 gocce totali)",
            "Vescica di Pesce Palla (1)"
        ],
        "preparazione": [
            "1. Triturare finissimo il Boletus Satanas e farlo cuocere per 4 minuti mescolando 3 volte in senso antiorario.",
            "2. Aggiungere mezzo litro d'acqua, mescolare 5 volte in senso orario e alzare la fiamma.",
            "3. Versare 5 gocce di succo di oleandro, mescolare 3 volte in senso antiorario e lasciar sobbollire per 15 minuti.",
            "4. Tritare la vescica di pesce palla, aggiungerla, mescolare 8 volte in senso orario e cuocere per 10 minuti.",
            "5. Fiamma massima, aggiungere 5 gocce di oleandro, spegnere e mescolare 8 volte in senso orario prima dell'imbottigliamento a freddo."
        ],
        "avvertenze": "CRITICO: Il Boletus Satanas è tra i funghi più letali al mondo.",
        "inventoreOrigine": "Creato nel 1885 dal mago svedese Karlaus (autore della celebre Scala Velenosa).",
        "descrizione": "A basse dosi provoca forti allucinazioni e febbri deliranti; ad alte dosi è letale. Si camuffa scomparendo alla vista in qualsiasi bevanda."
    },
    # Raccolta Veleni IV Anno
    {
        "id": "pot-distillato-angelo",
        "nome": "Distillato d’Angelo",
        "nomeAlternativo": "Angel's Trumpet Draught",
        "anno": 4,
        "annoLabel": "IV Anno",
        "tipologia": "Veleno Letale",
        "coloreFinale": "Bianco latte opalescente",
        "tempoPreparazione": "1 ora",
        "difficolta": "Avanzato",
        "metodoAssunzione": "Ingestione",
        "ingredienti": ["Pianta Tromba d'Angelo distillata", "Acqua distillata"],
        "preparazione": ["Distillazione alchemica a vapore."],
        "avvertenze": "Provoca grave intossicazione, allucinazioni feroci e morte per paralisi cardiorespiratoria.",
        "inventoreOrigine": "Raccolta di Veleni (pag. 59).",
        "descrizione": "Distillato estratto dalla tossica Tromba d'Angelo altamente distruttivo per il sistema nervoso."
    },
    {
        "id": "pot-dogbane",
        "nome": "Dogbane",
        "nomeAlternativo": "Veleno Canino d'Oriente",
        "anno": 4,
        "annoLabel": "IV Anno",
        "tipologia": "Veleno Selettivo Animale",
        "coloreFinale": "Verde scuro",
        "tempoPreparazione": "40 minuti",
        "difficolta": "Intermedio",
        "metodoAssunzione": "Ingestione",
        "ingredienti": ["Dogbane asiatica", "Solvente alcolico"],
        "preparazione": ["Macerazione a caldo."],
        "avvertenze": "Altamente letale per canidi e creature affini ai cani (Crup).",
        "inventoreOrigine": "Raccolta di Veleni (pag. 59).",
        "descrizione": "Pozione specifica ad altissima tossicità per animali e creature canine."
    },
    {
        "id": "pot-essenza-aconito",
        "nome": "Essenza di Aconito",
        "nomeAlternativo": "Pure Wolfsbane Essence",
        "anno": 4,
        "annoLabel": "IV Anno",
        "tipologia": "Veleno Letale",
        "coloreFinale": "Blu metallico",
        "tempoPreparazione": "2 ore",
        "difficolta": "Avanzato",
        "metodoAssunzione": "Ingestione o contatto epidermico",
        "ingredienti": ["Foglie e radici di Aconito selvatico"],
        "preparazione": ["Estrazione con alambicco a circuito chiuso."],
        "avvertenze": "Causa formicolio, brividi di gelo, vomito incoercibile e bradicardia mortale.",
        "inventoreOrigine": "Raccolta di Veleni (pag. 59).",
        "descrizione": "Forma purificata e concentrata della magitossina di Luparia."
    },
    {
        "id": "pot-actea",
        "nome": "Pozione Actea",
        "nomeAlternativo": "Baneberry Draught",
        "anno": 4,
        "annoLabel": "IV Anno",
        "tipologia": "Veleno Neurotossico",
        "coloreFinale": "Rosso sangue",
        "tempoPreparazione": "35 minuti",
        "difficolta": "Intermedio",
        "metodoAssunzione": "Ingestione",
        "ingredienti": ["Bacche di Actea", "Acqua purificata"],
        "preparazione": ["Decotto a fuoco rapido."],
        "avvertenze": "Provoca contrazioni muscolari violente simili a scosse elettriche e torpore prolungato.",
        "inventoreOrigine": "Raccolta di Veleni (pag. 59).",
        "descrizione": "Neurotossina vegetale che paralizza la conduzione nervosa con spasmi dolorosi."
    },
    {
        "id": "pot-debolezza",
        "nome": "Pozione della Debolezza",
        "nomeAlternativo": "Draught of Weakness",
        "anno": 4,
        "annoLabel": "IV Anno",
        "tipologia": "Veleno Inalatorio",
        "coloreFinale": "Fumi giallastri opachi",
        "tempoPreparazione": "30 minuti",
        "difficolta": "Base",
        "metodoAssunzione": "Inalazione",
        "ingredienti": ["Zolfo", "Radici di assenzio", "Foglie di starnutaria"],
        "preparazione": ["Sublimazione a calore."],
        "avvertenze": "Azzeramento immediato del tono muscolare e della concentrazione mentale.",
        "inventoreOrigine": "Raccolta di Veleni (pag. 59).",
        "descrizione": "I suoi vapori giallastri debilitano all'istante la forza corporea e la lucidità mentale."
    },
    {
        "id": "pot-n07",
        "nome": "Pozione n. 07",
        "nomeAlternativo": "Formula Sperimentale 7",
        "anno": 4,
        "annoLabel": "IV Anno",
        "tipologia": "Veleno Sperimentale",
        "coloreFinale": "Verde bottiglia",
        "tempoPreparazione": "40 minuti",
        "difficolta": "Intermedio",
        "metodoAssunzione": "Ingestione",
        "ingredienti": ["Tentacula Velenosa (semi)", "Spine di Pesce Leone"],
        "preparazione": ["Macerazione a freddo."],
        "avvertenze": "Scatena nausea lancinante e violente vertigini.",
        "inventoreOrigine": "Laboratori sperimentali del Dipartimento.",
        "descrizione": "Miscela tossica basata su alcaloidi carnivori e tossine ittiche."
    },
    {
        "id": "pot-n113",
        "nome": "Pozione n. 113",
        "nomeAlternativo": "Formula Sperimentale 113",
        "anno": 4,
        "annoLabel": "IV Anno",
        "tipologia": "Veleno Epatico",
        "coloreFinale": "Azzurro cupo",
        "tempoPreparazione": "50 minuti",
        "difficolta": "Avanzato",
        "metodoAssunzione": "Ingestione",
        "ingredienti": ["Sciroppo d'Arnica concentrato", "Piume di Jobberknoll tritate"],
        "preparazione": ["Infusione in soluzione satura."],
        "avvertenze": "Causa gravissime lesioni epatiche e ipotensione arteriosa fulminante.",
        "inventoreOrigine": "Raccolta di Veleni (pag. 59).",
        "descrizione": "Composto tossico ad azione depressiva sul sistema cardiocircolatorio ed epatico."
    },
    {
        "id": "pot-n86",
        "nome": "Pozione n. 86",
        "nomeAlternativo": "Formula Sperimentale 86",
        "anno": 4,
        "annoLabel": "IV Anno",
        "tipologia": "Veleno Letale / Neurotossico",
        "coloreFinale": "Grigio perlaceo",
        "tempoPreparazione": "45 minuti",
        "difficolta": "Avanzato",
        "metodoAssunzione": "Ingestione",
        "ingredienti": ["Sciroppo di Elleboro", "Pietra di Luna in polvere"],
        "preparazione": ["Sospensione colloidale a caldo."],
        "avvertenze": "A dosi elevate conduce all'arresto respiratorio e cardiaco.",
        "inventoreOrigine": "Raccolta di Veleni (pag. 59).",
        "descrizione": "Sfrutta l'azione tossica dell'elleboro potenziata dalla risonanza lunare."
    },
    {
        "id": "pot-repellente-lumache",
        "nome": "Repellente per Lumache Carnivore",
        "nomeAlternativo": "Flesh-Eating Slug Repellent",
        "anno": 4,
        "annoLabel": "IV Anno",
        "tipologia": "Pesticida Magico",
        "coloreFinale": "Verde acido",
        "tempoPreparazione": "25 minuti",
        "difficolta": "Base",
        "metodoAssunzione": "Aspersione sui confini delle aiuole",
        "ingredienti": ["Sale minerale africano", "Cenere di quercia", "Succo di Horklump"],
        "preparazione": ["Emulsione a freddo."],
        "avvertenze": "Corrosivo per le lumache carnivore; innocuo per le radici vegetali.",
        "inventoreOrigine": "Disinfestazione agricola magica.",
        "descrizione": "Pesticida protettivo indispensabile per difendere i cavoli carnivori e le erbe preziose."
    },
    {
        "id": "pot-veleno-sanguinaria",
        "nome": "Veleno di Sanguinaria",
        "nomeAlternativo": "Bloodroot Slow Poison",
        "anno": 4,
        "annoLabel": "IV Anno",
        "tipologia": "Veleno Letale Progressivo",
        "coloreFinale": "Rosso scuro denso",
        "tempoPreparazione": "2 ore",
        "difficolta": "Avanzato",
        "metodoAssunzione": "Ingestione nascosta",
        "ingredienti": ["Rizoma di Sanguinaria essiccato", "Alcol purissimo"],
        "preparazione": ["Estrazione idroalcolica lenta."],
        "avvertenze": "Morte asintomatica e graduale per lisi cellulare senza tracce evidenti.",
        "inventoreOrigine": "Tossicologia clandestina medievale.",
        "descrizione": "Provoca la progressiva e inarrestabile disgregazione cellulare dell'organismo della vittima."
    },
    {
        "id": "pot-veleno-semi-luna",
        "nome": "Veleno di Semi di Luna",
        "nomeAlternativo": "Moonseed Lethal Narcotic",
        "anno": 4,
        "annoLabel": "IV Anno",
        "tipologia": "Veleno Narcotico Letale",
        "coloreFinale": "Bianco opaco",
        "tempoPreparazione": "1 ora",
        "difficolta": "Avanzato",
        "metodoAssunzione": "Ingestione",
        "ingredienti": ["Bacche di Semi di Luna (Moonseed)"],
        "preparazione": ["Pestaggio a freddo in mortaio d'agata."],
        "avvertenze": "Potente narcotico che paralizza i centri della respirazione.",
        "inventoreOrigine": "Raccolta di Veleni (pag. 59).",
        "descrizione": "Induce un sonno comatoso irreversibile che conduce al decesso senza agonia."
    },
    {
        "id": "pot-veleno-noxious",
        "nome": "Veleno Noxious",
        "nomeAlternativo": "Noxious Fume Poison",
        "anno": 4,
        "annoLabel": "IV Anno",
        "tipologia": "Veleno Emorragico Inalatorio",
        "coloreFinale": "Fumi verdi e profumati",
        "tempoPreparazione": "40 minuti",
        "difficolta": "Avanzato",
        "metodoAssunzione": "Inalazione",
        "ingredienti": ["Fosforo magico", "Resine velenose", "Tasso"],
        "preparazione": ["Combustione controllata a vaso chiuso."],
        "avvertenze": "Provoca sanguinamenti epiteliali e nasali che si diffondono al resto del corpo.",
        "inventoreOrigine": "Raccolta di Veleni (pag. 59).",
        "descrizione": "Emette vapori verde smeraldo dall'aroma gradevole che lacerano i capillari interni."
    },
    {
        "id": "pot-veleno-rosa-sgargiante",
        "nome": "Veleno Rosa Sgargiante",
        "nomeAlternativo": "False Love Poison (10-Component Blend)",
        "anno": 4,
        "annoLabel": "IV Anno",
        "tipologia": "Veleno Disorientante / Finto Filtro",
        "coloreFinale": "Rosa brillante ingannevole",
        "tempoPreparazione": "1 ora e 20 minuti",
        "difficolta": "Avanzato",
        "metodoAssunzione": "Ingestione",
        "ingredienti": ["Miscela di dieci differenti tipologie di veleno a dosaggio sub-letale"],
        "preparazione": ["Composizione complessa bilanciata."],
        "avvertenze": "Facilmente scambiabile per un filtro d'amore; provoca emicrania atroce e confusione.",
        "inventoreOrigine": "Raccolta di Veleni (pag. 60).",
        "descrizione": "Preparato ingannevole che mima l'aspetto di una pozione amorosa scatenando invece un violento collasso cognitivo."
    },
    # Antidoti IV Anno
    {
        "id": "pot-antidoto-veleni-comuni",
        "nome": "Antidoto ai Veleni Comuni",
        "nomeAlternativo": "Antidoto Polivalente (Antidote to Common Poisons)",
        "anno": 4,
        "annoLabel": "IV Anno",
        "tipologia": "Antidoto Composto / Aspecifico",
        "coloreFinale": "Verde acqua limpido",
        "tempoPreparazione": "75 minuti",
        "difficolta": "Intermedio",
        "metodoAssunzione": "Ingestione",
        "ingredienti": [
            "Bacche di Vischio (2)",
            "Bezoar (1)",
            "Corno di Unicorno in polvere (1 misurino)",
            "Ingrediente Standard (2 misurini)"
        ],
        "preparazione": [
            "1. Essiccare il Bezoar e ridurlo in polvere finissima in mortaio, versandone 4 misurini nel calderone con 2 misurini di Ingrediente Standard.",
            "2. Accendere il fuoco; dopo 6 minuti aggiungere mezzo litro d'acqua e mescolare 6 volte in senso orario.",
            "3. Portare a bollore per 7 minuti, spegnere e lasciare in infusione per 40 minuti.",
            "4. Aggiungere un pizzico di Corno di Unicorno, mescolare 2 volte in senso orario, sobbollire a fuoco basso per 20 minuti.",
            "5. Spremere le 2 bacche di vischio sul tagliere, versarne il succo, mescolare 2 volte in senso antiorario, spegnere, filtrare e imbottigliare."
        ],
        "avvertenze": "Efficacissimo contro veleni di Classe X e morsi di creature comuni; inefficace contro veleni letali o composti complessi (XXX).",
        "inventoreOrigine": "Codificato dalle prime due Leggi di Golpalott.",
        "descrizione": "Antidoto aspecifico universale che neutralizza morsi, punture e intossicazioni da veleni semplici."
    },
    {
        "id": "pot-antidoto-veleni-rari",
        "nome": "Antidoto ai Veleni Rari",
        "nomeAlternativo": "Antidote to Rare Poisons",
        "anno": 4,
        "annoLabel": "IV Anno",
        "tipologia": "Antidoto Composto / Classe XX",
        "coloreFinale": "Verde bottiglia brillante",
        "tempoPreparazione": "6 ore e 15 minuti",
        "difficolta": "Avanzato",
        "metodoAssunzione": "Ingestione",
        "ingredienti": [
            "Cenere di foglie di Semi di Fuoco (4 misurini)",
            "Corno di Graphorn in polvere (1 misurino)",
            "Gusci di Chizpurfle (4)",
            "Pungiglione di Billywig (1)"
        ],
        "preparazione": [
            "1. Polverizzare il corno di Graphorn con coltellino d'argento e mortaio battendo con forza.",
            "2. Mettere nel calderone il pungiglione di Billywig e 4 gusci di Chizpurfle con acqua a fiamma media.",
            "3. Portare a bollore e sobbollire per 6 ore creando un decotto concentrato.",
            "4. Spegnere, filtrare e trasferire in calderone pulito.",
            "5. Aggiungere 1 misurino di corno di Graphorn e mescolare 5 volte in senso orario e 6 volte in senso antiorario.",
            "6. Aggiungere 4 misurini di cenere di Semi di Fuoco, scaldare a fuoco altissimo per 60 secondi, spegnere e imbottigliare."
        ],
        "avvertenze": "Inefficace contro veleni composti di classe XXX e veleni letali puri.",
        "inventoreOrigine": "Formulato per contrastare tossine di creature magiche di livello XX.",
        "descrizione": "Neutralizza veleni rari e complessi di creature pericolose, compresi morsi di Malaclaw e intossicazioni da funghi velenosi."
    },
    {
        "id": "pot-ricostituente-mandragola",
        "nome": "Ricostituente alla Mandragola",
        "nomeAlternativo": "Pozione Anti-Paralisi (Mandrake Restorative Draught)",
        "anno": 4,
        "annoLabel": "IV Anno",
        "tipologia": "Antidoto Specifico / Anti-Pietrificazione",
        "coloreFinale": "Marrone tendente al giallo",
        "tempoPreparazione": "48 ore di infusione continua",
        "difficolta": "Avanzato",
        "metodoAssunzione": "Gocce orali (somministrabile anche a soggetti addormentati)",
        "ingredienti": [
            "Acqua distillata (1 litro)",
            "Bezoar polverizzato (1)",
            "Mandragola adulta e matura intera (1)"
        ],
        "preparazione": [
            "1. Inserire una Mandragola matura nel calderone con le foglie alla base e la radice rivolta in alto.",
            "2. Coprire con acqua distillata e lasciare in infusione a fiamma bassissima per 24 ore continue.",
            "3. Polverizzare un Bezoar e aggiungerne 1 misurino al composto scadute le prime 24 ore.",
            "4. Mescolare lentamente per 4 volte in senso orario e 2 in senso antiorario senza smuovere la radice.",
            "5. Lasciare in infusione per ulteriori 24 ore consecutive.",
            "6. Spegnere, filtrare una sola volta e imbottigliare; va somministrata bollente."
        ],
        "avvertenze": "La mandragola deve aver raggiunto la piena maturità sessuale (acne, umore mutevole) per essere efficace.",
        "inventoreOrigine": "Impiegata da Madam Chips nel 1993 per curare gli studenti pietrificati dal Basilisco.",
        "descrizione": "Antidoto specifico supremo che risana e sblocca corpi pietrificati da maledizioni (*Petrificus Totalus*) o dallo sguardo riflesso del Basilisco."
    },
    {
        "id": "pot-volubilis",
        "nome": "Pozione Volubilis",
        "nomeAlternativo": "Volubilis Potion / Restauratore Vocale",
        "anno": 4,
        "annoLabel": "IV Anno",
        "tipologia": "Antidoto Specifico / Alteratrice Voce",
        "coloreFinale": "Giallo",
        "tempoPreparazione": "25 ore (24 ore vapore)",
        "difficolta": "Avanzato",
        "metodoAssunzione": "Ingestione",
        "ingredienti": [
            "Acqua di Miele (2 cucchiai)",
            "Crini di Ippogrifo e Unicorno (per rete)",
            "Mandragola cotta al vapore (1 radice)",
            "Rametti di Menta fresca (2)",
            "Sciroppo di Elleboro (3 cucchiai)"
        ],
        "preparazione": [
            "1. Portare a bollore 3 litri d'acqua; creare una rete a telaio con crini d'ippogrifo e d'unicorno sulla bocca del calderone.",
            "2. Cuocere a vapore la radice di mandragola per 24 ore girandola ogni 6 ore, poi far raffreddare e tagliuzzare a striscioline.",
            "3. In altro calderone con 1 litro d'acqua aggiungere 2 cucchiai di Acqua di Miele (vira al rosso) e mescolare 8 volte in senso orario.",
            "4. Spegnere, unire 1 rametto di menta, riportare a bollore, aggiungere la mandragola e il secondo rametto di menta mescolando 17 volte in senso antiorario.",
            "5. Aggiungere 3 cucchiai di Sciroppo di Elleboro, spegnere, mescolare 2 volte in senso antiorario e 8 in senso orario, filtrare 2 volte."
        ],
        "avvertenze": "Altera la timbrica vocale e annulla gli incantesimi Silencio, Sonorus e il Distillato Smorzante.",
        "inventoreOrigine": "Trattato di fonetica magica.",
        "descrizione": "Annulla gli incantesimi che agiscono sul suono o sulla voce e consente di modulare una voce completamente differente."
    },
    {
        "id": "pot-antidoto-filtri-amore",
        "nome": "Antidoto ai Filtri d'Amore",
        "nomeAlternativo": "Love Potion Antidote",
        "anno": 4,
        "annoLabel": "IV Anno",
        "tipologia": "Antidoto Specifico",
        "coloreFinale": "Rosso rubino",
        "tempoPreparazione": "14 ore e 20 minuti",
        "difficolta": "Avanzato",
        "metodoAssunzione": "Ingestione",
        "ingredienti": [
            "Estratto di Radigorda agitato (4 cl)",
            "Olio di Ricino (1 cucchiaio)",
            "Rametti di Sorbo Magico (12)"
        ],
        "preparazione": [
            "1. Aggiungere 4 ramoscelli di Sorbo Magico al calderone con 1 litro d'acqua a fuoco basso.",
            "2. Aggiungere 1 cucchiaio di olio di ricino e mescolare finché non assume colorazione violacea; cuocere per 3 ore.",
            "3. Aggiungere 2 cl di estratto di Radigorda agitato, mescolare 4 volte in senso antiorario, unire un altro ramoscello di Sorbo e attendere 10 minuti.",
            "4. Spegnere, aggiungere il restante estratto di Radigorda e mescolare lentamente per 12 volte in senso antiorario finché vira al verde.",
            "5. Aggiungere i restanti rametti di Sorbo Magico, riaccendere a fiamma bassa e lasciare in infusione per 11 ore prima di filtrare e imbottigliare."
        ],
        "avvertenze": "Se assunto a vuoto spegne ogni libido e desiderio sessuale per giorni portando marcata apatia. Non cancella i ricordi delle azioni compiute.",
        "inventoreOrigine": "Impiegata dal professor Lumacorno per curare Ron Weasley intossicato dai Calderotti di Romilda Vane.",
        "descrizione": "Spezza all'istante l'infatuazione morbosa e la coercizione emotiva prodotte da filtri e pozioni amorose."
    },
    {
        "id": "pot-antidoto-burrobirra",
        "nome": "Antidoto alla Burrobirra",
        "nomeAlternativo": "Butterbeer Sobriety Draught for House-Elves",
        "anno": 4,
        "annoLabel": "IV Anno",
        "tipologia": "Antidoto Specifico Veterinario",
        "coloreFinale": "Giallo paglierino",
        "tempoPreparazione": "20 minuti",
        "difficolta": "Base",
        "metodoAssunzione": "Ingestione per elfi domestici",
        "ingredienti": ["Infuso di menta piperita", "Radici di cicoria", "Sale minerale"],
        "preparazione": ["Decotto a fuoco vivo."],
        "avvertenze": "Calibrato per il metabolismo degli elfi domestici (molto sensibili alla gradazione della Burrobirra).",
        "inventoreOrigine": "Cucine di Hogwarts (usato per Winky).",
        "descrizione": "Smaltisce all'istante l'ebbrezza alcolica e la depressione negli elfi domestici causate dall'abuso di Burrobirra."
    },
    {
        "id": "pot-antidoto-billywig",
        "nome": "Antidoto alle Punture di Billywig",
        "nomeAlternativo": "Billywig Sting Antidote",
        "anno": 4,
        "annoLabel": "IV Anno",
        "tipologia": "Antidoto Specifico",
        "coloreFinale": "Azzurro limpido",
        "tempoPreparazione": "30 minuti",
        "difficolta": "Base",
        "metodoAssunzione": "Ingestione",
        "ingredienti": ["Pungiglione essiccato di Billywig (lo stesso elemento che causa il sintomo)", "Acqua distillata"],
        "preparazione": ["Omeopatia alchemica a base del medesimo catalizzatore."],
        "avvertenze": "Arresta immediatamente levitazione incontrollata e senso di vertigine.",
        "inventoreOrigine": "Medimagia australiana.",
        "descrizione": "Neutralizza gli effetti collaterali di galleggiamento e capogiro provocati dalle punture di Billywig."
    },
    {
        "id": "pot-antidoto-prurito-bocca",
        "nome": "Antidoto per il Prurito alla Bocca",
        "nomeAlternativo": "Mouth-Itch Antidote",
        "anno": 4,
        "annoLabel": "IV Anno",
        "tipologia": "Antidoto Specifico",
        "coloreFinale": "Rosa tenue",
        "tempoPreparazione": "15 minuti",
        "difficolta": "Base",
        "metodoAssunzione": "Sciacqui orali",
        "ingredienti": ["Foglie di alchemilla", "Miele magico", "Acqua di rose"],
        "preparazione": ["Emulsione lenitiva a freddo."],
        "avvertenze": "Antidoto ufficiale alle Palline Acide di Mielandia.",
        "inventoreOrigine": "Dolciumi magici da difesa.",
        "descrizione": "Placa l'irritazione e il bruciore alla lingua e al palato provocati da incantesimi o caramelle scherzo."
    },
    {
        "id": "pot-antiveleno-asiatico",
        "nome": "Antiveleno Asiatico",
        "nomeAlternativo": "Asian Serpent Antivenom",
        "anno": 4,
        "annoLabel": "IV Anno",
        "tipologia": "Antidoto Aspecifico Animale",
        "coloreFinale": "Ambrato",
        "tempoPreparazione": "1 ora",
        "difficolta": "Intermedio",
        "metodoAssunzione": "Ingestione",
        "ingredienti": ["Radici di ginseng magico", "Bile di vipera", "Corno di unicorno polverizzato"],
        "preparazione": ["Decotto concentrato."],
        "avvertenze": "Largamente impiegato in Asia contro veleni ofidici e di rettili magici.",
        "inventoreOrigine": "Medimagia orientale.",
        "descrizione": "Neutralizza una vasta gamma di tossine emotossiche e neurotossiche inoculate da morsi di serpente."
    },
    {
        "id": "pot-densa-pozione-oro",
        "nome": "Densa Pozione d’Oro",
        "nomeAlternativo": "Thick Golden Potion for Dark Magic Curses",
        "anno": 4,
        "annoLabel": "IV Anno",
        "tipologia": "Antidoto Curativo Supremo",
        "coloreFinale": "Oro denso brillante",
        "tempoPreparazione": "3 ore con canalizzazione da bacchetta",
        "difficolta": "Avanzato / Maestro",
        "metodoAssunzione": "Ingestione e frizione",
        "ingredienti": ["Polvere d'oro alchemico", "Sangue di fenice", "Dittamo distillato"],
        "preparazione": ["Fonderia alchemica combinata con incanti curativi ad alta voce."],
        "avvertenze": "Utilizzata in combinazione con potenti incantesimi guaritivi avanzati.",
        "inventoreOrigine": "Pronto soccorso per lesioni da Maledizioni Oscure.",
        "descrizione": "Rimedio prezioso e denso per bloccare e rimarginare lesioni profonde provocate da magia oscura avanzata."
    },
    {
        "id": "pot-metodo-francese-cane-pazzo",
        "nome": "Famoso Metodo Francese per Morso di Cane Pazzo",
        "nomeAlternativo": "French Antidote for Rabid Beast Bites",
        "anno": 4,
        "annoLabel": "IV Anno",
        "tipologia": "Antidoto Complesso",
        "coloreFinale": "Bruno speziato",
        "tempoPreparazione": "4 ore",
        "difficolta": "Avanzato",
        "metodoAssunzione": "Ingestione",
        "ingredienti": ["Composta da più di 20 ingredienti naturali ed animali calibrati"],
        "preparazione": ["Composizione multi-fase a bagnomaria."],
        "avvertenze": "Nata per contrastare gli effetti nocivi derivati dal morso di creature magiche rabide.",
        "inventoreOrigine": "Scuola di Pozioni dell'Accademia di Beauxbatons.",
        "descrizione": "Formula complessa che arresta la proliferazione del virus della rabbia magica nell'organismo umano."
    },
    {
        "id": "pot-regulus-moonshine",
        "nome": "Pozione di Regulus Moonshine",
        "nomeAlternativo": "Hag-Flesh Inhibitor",
        "anno": 4,
        "annoLabel": "IV Anno",
        "tipologia": "Antidoto Comportamentale",
        "coloreFinale": "Grigio acciaio",
        "tempoPreparazione": "2 ore e mezza",
        "difficolta": "Avanzato",
        "metodoAssunzione": "Ingestione per Megere",
        "ingredienti": ["Radici di mandragola", "Carne di drago marinata", "Assenzio"],
        "preparazione": ["Distillazione lenta a vaso chiuso."],
        "avvertenze": "L'inventore perse diversi arti durante i collaudi con megere volontarie.",
        "inventoreOrigine": "Creata a metà degli anni '90 dal professor Regulus Moonshine.",
        "descrizione": "Inibisce il costante e primordiale appetito delle Megere di cibarsi di carne umana."
    }
]

# Append to data_pozioni.py
with open('/Users/andreamorachioli/.gemini/antigravity/scratch/portale-incantesimi/scripts/data_pozioni.py', 'r', encoding='utf-8') as f:
    current_content = f.read()

# remove trailing print and replace with extended list
current_content = current_content.replace('print(f"Totale Pozioni caricate (Parte 1 e 2): {len(pozioni_data)}")', '')

with open('/Users/andreamorachioli/.gemini/antigravity/scratch/portale-incantesimi/scripts/data_pozioni.py', 'w', encoding='utf-8') as f:
    f.write(current_content)
    f.write('\n# POZIONI ANNI IV AGGIUNTE:\n')
    f.write('pozioni_data.extend(' + json.dumps(pozioni_restanti, ensure_ascii=False, indent=4) + ')\n')
    f.write('print(f"Pozioni dopo aggiunta IV Anno: {len(pozioni_data)}")\n')

print("Fase IV completata!")
