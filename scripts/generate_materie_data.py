# -*- coding: utf-8 -*-
"""
Generatore completo del dataset unificato per il Portale Materie:
- Creature Magiche (73 voci)
- Erbologia & Piante Magiche (56 voci)
- Pozioni Avanzate (127 voci)
Tutte con suddivisione per anno didattico (I - VII Anno), senza valenza.
"""

import json

creature = [
    # III ANNO
    {
        "id": "c-horklump",
        "nome": "Horklump",
        "nomeAlternativo": "Fungo Carnoso da Giardino",
        "anno": 3,
        "annoLabel": "III Anno",
        "classificazione": "XX",
        "classificazioneLabel": "Innocuo / Addomesticabile",
        "habitat": "Originario della Scandinavia, diffuso nei giardini d'Europa",
        "commerciabilita": "Libero / Infestante comune",
        "dieta": "Lombrichi e detriti organici sotterranei",
        "tratti": "Aspetto simile a un fungo rosa carnoso coperto da peli neri e setole",
        "descrizione": "L'Horklump somiglia moltissimo a un fungo rosa ricoperto da peli neri e sottili. Cresce spontaneamente nel terreno e si confonde con i funghi babbani. Usa tentacoli simili a radici per scavare alla ricerca di lombrichi. Si riproduce a velocità esponenziale infestando interi appezzamenti. I gnomi da giardino sono i suoi predatori naturali e ne vanno matti, motivo per cui è utile per attirare e trappolare gli gnomi. Nonostante la natura animale, per la maggior parte dei maghi è noioso da studiare.",
        "utilizziMagici": "Il succo di Horklump possiede eccezionali proprietà cicatrizzanti e viene usato come catalizzatore in decotti curativi, nell'Erbicida e nella Pozione Rigeneratrice.",
        "regolamentazione": "Nessuna restrizione di possesso. Sconsigliato farlo proliferare nei giardini babbani per evitare infestazioni visibili."
    },
    {
        "id": "c-vermicolo",
        "nome": "Vermicolo",
        "nomeAlternativo": "Flobberworm",
        "anno": 3,
        "annoLabel": "III Anno",
        "classificazione": "X",
        "classificazioneLabel": "Noioso",
        "habitat": "Fossati umidi, paludi e terreni melmosi di tutto il mondo magico",
        "commerciabilita": "Libero commercio",
        "dieta": "Vegetazione in decomposizione e lattuga marcescente",
        "tratti": "Verme cilindrico marrone lungo circa 10 cm, privo di denti, occhi e zampe",
        "descrizione": "Il Vermicolo è una creatura segmentata, viscida e tozza, lunga circa 10 centimetri. Totalmente privo di capacità offensive o difensive, trascorre l'intera esistenza a strisciare lentamente nel fango senza reagire ad alcuno stimolo esterno. A Hogwarts viene comunemente introdotto nei primi anni di studio di Cura delle Creature Magiche per la totale assenza di pericoli associati.",
        "utilizziMagici": "Secerne costantemente una sostanza densa e appiccicosa nota come 'Muco di Vermicolo', impiegata universalmente nelle pozioni come addensante, legante idrocolloidale e stabilizzante chimico (es. Pozione Scacciabrufoli, Soporifera, Erbicida).",
        "regolamentazione": "Completamente libero da licenze e controlli ministeriali."
    },

    # IV ANNO
    {
        "id": "c-asticello",
        "nome": "Asticello",
        "nomeAlternativo": "Bowtruckle / Custode degli Alberi",
        "anno": 4,
        "annoLabel": "IV Anno",
        "classificazione": "XX",
        "classificazioneLabel": "Innocuo / Pacifico",
        "habitat": "Foreste della Germania, Inghilterra occidentale e Scandinavia",
        "commerciabilita": "Richiede Licenza Ministeriale di Custodia",
        "dieta": "Porcellini di terra (oniscoidi) e uova di fata",
        "tratti": "Corpo a stecco di corteccia e ramoscelli con 4 dita affilatissime, altezza circa 20 cm",
        "descrizione": "Custode silenzioso e fedele degli alberi il cui legname è adatto alla fabbricazione di bacchette magiche (sorbo, frassino, tasso). Si mimetizza perfettamente tra i rami e le foglie. Pacifico di natura, diviene furioso se il suo albero ospite viene minacciato o reciso con violenza da taglialegna o bracconieri, scagliandosi contro gli occhi dell'intruso con le lunghe dita unghiate.",
        "utilizziMagici": "Per prelevare legno da un albero custodito senza incidenti, i maghi offrono porcellini di terra o uova di fata. Un gruppo di Asticelli è chiamato scientificamente 'ramo'.",
        "regolamentazione": "Creatura protetta. Possesso consentito solo con brevetto per erboristi e fabbricanti di bacchette."
    },
    {
        "id": "c-augurey",
        "nome": "Augurey",
        "nomeAlternativo": "Fringuello Irlandese",
        "anno": 4,
        "annoLabel": "IV Anno",
        "classificazione": "XX",
        "classificazioneLabel": "Innocuo",
        "habitat": "Gran Bretagna, Irlanda e tratti boschivi della Scandinavia",
        "commerciabilita": "Richiede Licenza Ministeriale",
        "dieta": "Grossi insetti, vermi e Fate",
        "tratti": "Uccello magro e lugubre, piumaggio nero-verde petrolio, nidi a forma di lacrima",
        "descrizione": "Creatura timida e riservata che nidifica tra fitti cespugli spinosi di rosa canina. Vola esclusivamente durante piogge torrenziali e temporali. In passato si riteneva erroneamente che il suo verso cavernoso e pulsante presagisse una morte imminente; ricerche approfondite hanno provato che l'Augurey canta unicamente all'approssimarsi di perturbazioni atmosferiche, divenendo un rinomato barometro vivente.",
        "utilizziMagici": "Le piume di Augurey respingono categoricamente ogni inchiostro magico o terreno, risultando inutili per la scrittura ma preziosissime in alchimia e nella composizione della Pozione Antilupo.",
        "regolamentazione": "Possesso soggetto a licenza per evitare l'abbattimento indiscriminato dovuto a superstizioni."
    },
    {
        "id": "c-chizpurfle",
        "nome": "Chizpurfle",
        "nomeAlternativo": "Parassita Mangiamagia",
        "anno": 4,
        "annoLabel": "IV Anno",
        "classificazione": "XX",
        "classificazioneLabel": "Innocuo",
        "habitat": "Dimore magiche, calderoni incrostati, mantelli di Crup e Augurey",
        "commerciabilita": "Infestante (prodotti derivati commerciabili)",
        "dieta": "Residui di pozioni e nuclei magici di bacchette o oggetti fatati",
        "tratti": "Minuscolo aracno-crostaceo di 1,5 mm con grandi zanne anteriori",
        "descrizione": "Piccoli parassiti lunghi fino a un millimetro e mezzo, simili a granchietti provvisti di possenti chele e zanne. Spinti dall'irresistibile attrazione per l'energia magica, s'introducono nei calderoni lasciati sporchi per divorare le gocce residue di pozioni. Possono intaccare il fusto delle bacchette rodendo il legno fino al nucleo fatato. Se si nutrono di troppa magia possono gonfiarsi e resistere agli incantesimi ordinari.",
        "utilizziMagici": "Le zanne e i gusci essiccati di Chizpurfle sono impiegati nell'Antidoto ai Veleni Rari e nella Pozione Rigeneratrice.",
        "regolamentazione": "In caso di infestazioni gravi interviene la Sottosezione Animali Nocivi dell'Ufficio Regolazione e Controllo."
    },
    {
        "id": "c-clabbert",
        "nome": "Clabbert",
        "nomeAlternativo": "Scimmia-Rana d'America",
        "anno": 4,
        "annoLabel": "IV Anno",
        "classificazione": "XX",
        "classificazioneLabel": "Innocuo",
        "habitat": "Foreste e giardini dell'America Meridionale e Nord America",
        "commerciabilita": "Beni Commerciabili di Classe B (pustola)",
        "dieta": "Piccoli uccelli, lucertole e insetti",
        "tratti": "Ibrido arboricolo scimmia-rana, pelle verde chiazzata, pustola frontale sensoriale",
        "descrizione": "Creatura arboricola dal bizzarro profilo intermedio tra una scimmia e una rana. È dotata di braccia e gambe elastiche con dita palmate che gli consentono mirabolanti acrobazie tra i rami. La testa reca corte corna e una bocca ridente irta di denti affilati. Il tratto distintivo è una grossa pustola rubino al centro della fronte, che pulsa e lampeggia vividamente non appena avverte l'avvicinarsi di un pericolo o di intrusi babbani.",
        "utilizziMagici": "In passato i maghi americani tenevano i Clabbert in giardino come sentinelle contro i No-Mag; la pratica fu sanzionata poiché gli alberi illuminati attiravano troppi curiosi festivi.",
        "regolamentazione": "Beni Commerciabili di Classe B. Detenzione regolamentata dalla Confederazione Internazionale."
    },
    {
        "id": "c-diricawl",
        "nome": "Diricawl",
        "nomeAlternativo": "Dodo Babbano",
        "anno": 4,
        "annoLabel": "IV Anno",
        "classificazione": "XX",
        "classificazioneLabel": "Innocuo",
        "habitat": "Isola di Mauritius e riserve magiche insulari",
        "commerciabilita": "Specie Protetta Internazionale",
        "dieta": "Bacche, semi e frutti tropicali",
        "tratti": "Uccello grassoccio dal piumaggio vaporoso e ali atrofizzate per il volo ordinario",
        "descrizione": "Uccello tozzo e piumato incapace di volare con le ali ordinarie, ma dotato del prodigioso potere di smaterializzarsi in uno sbuffo di piume per riapparire istantaneamente altrove (capacità condivisa con la Fenice). Nel mondo babbano era conosciuto come 'Dodo': i babbani credono di averlo cacciato fino all'estinzione, e il Ministero ha ritenuto saggio mantenere l'illusione per sensibilizzare la coscienza babbana.",
        "utilizziMagici": "Piume utilizzate per amuleti di fuga rapida e incantesimi di mimesi istantanea.",
        "regolamentazione": "Specie strettamente tutelata dalla Clausola 73 dello Statuto di Segretezza."
    },
    {
        "id": "c-jobberknoll",
        "nome": "Jobberknoll",
        "nomeAlternativo": "Uccello della Memoria",
        "anno": 4,
        "annoLabel": "IV Anno",
        "classificazione": "X",
        "classificazioneLabel": "Noioso",
        "habitat": "Boschi montani e laghi incantati dell'Europa settentrionale e centrale",
        "commerciabilita": "Beni Commerciabili di Classe B (piume)",
        "dieta": "Piccoli insetti volanti",
        "tratti": "Piccolo volatile blu cobalto brillante con punteggiature dorate sul dorso",
        "descrizione": "Uccellino silenzioso che non emette alcun suono per l'intero arco della sua esistenza. Nel preciso istante che precede la sua morte naturale, tuttavia, spalanca il becco ed emette un grido prolungato e melodrammatico, riproducendo all'incontrario ogni singola parola, verso o rumore udito durante tutta la vita.",
        "utilizziMagici": "Le sue splendide piume blu e oro sono il reagente cardinale per la distillazione dei Sieri della Verità, delle Pozioni Mnestiche e dei filtri di richiamo della memoria.",
        "regolamentazione": "Cattura regolata: lo stress da cattività può indurre morte prematura con emissioni sonore caotiche."
    },
    {
        "id": "c-mooncalf",
        "nome": "Mooncalf",
        "nomeAlternativo": "Vitello Lunare",
        "anno": 4,
        "annoLabel": "IV Anno",
        "classificazione": "XX",
        "classificazioneLabel": "Innocuo",
        "habitat": "Tane sotterranee isolate in tutto il mondo",
        "commerciabilita": "Libero commercio (escrementi argentati)",
        "dieta": "Graminacee notturne e radici tenere",
        "tratti": "Pelle liscia grigio perla, quattro zampe snodate con enormi piedi palmati e occhi a palla",
        "descrizione": "Creatura timidissima che abbandona la tana sotterranea esclusivamente durante le notti di plenilunio. Alla luce della luna piena si erge sulle zampe posteriori ed esegue complicate danze rituali aeree e coreografiche nei campi di grano, lasciando intricati disegni geometrici che disorientano la comunità babbana.",
        "utilizziMagici": "I suoi escrementi color argento liquido, raccolti prima del sorgere dell'aurora, costituiscono il fertilizzante magico più formidabile per piante esigenti come il Fagiolo Sopoforoso.",
        "regolamentazione": "Nessuna restrizione particolare; tutelato per preservare le colture agrarie magiche."
    },
    {
        "id": "c-puffskein",
        "nome": "Puffskein",
        "nomeAlternativo": "Puffola Tradizionale",
        "anno": 4,
        "annoLabel": "IV Anno",
        "classificazione": "XX",
        "classificazioneLabel": "Innocuo / Addomesticabile",
        "habitat": "Case dei maghi di tutto il mondo",
        "commerciabilita": "Animale da compagnia libero (licenza commerciale)",
        "dieta": "Spazzino onnivoro: avanzi, briciole, ragni e caccole del naso",
        "tratti": "Sfera di soffice pelliccia color crema, ronzio continuo, lingua rosea lunghissima",
        "descrizione": "Docile sfera di pelliccia soffice che emette un sommesso e pacificatore ronzio quando si sente accarezzata. È un formidabile spazzino domestico che ripulisce la stanza da briciole e insetti, ma la sua inclinazione preferita è intrufolare la lingua flessibile nel naso dei maghi addormentati per cibarsi delle loro secrezioni secche.",
        "utilizziMagici": "Animale da compagnia prediletto per i bambini. Da esso Zygmunt Budge e successivamente i fratelli Weasley selezionarono la variante Puffola Pigmea per pozioni euforizzanti.",
        "regolamentazione": "Vendita autorizzata in tutti i serragli magici autorizzati."
    },
    {
        "id": "c-ramora",
        "nome": "Ramora",
        "nomeAlternativo": "Pesce Guardiano dei Mari",
        "anno": 4,
        "annoLabel": "IV Anno",
        "classificazione": "XX",
        "classificazioneLabel": "Innocuo",
        "habitat": "Oceano Indiano e mari tropicali profondi",
        "commerciabilita": "Specie Protetta ad Altissimo Valore Tutelare",
        "dieta": "Plancton magico e alghe iridescenti",
        "tratti": "Corpo affusolato argenteo riflettente e grandi occhi neri ipnotici",
        "descrizione": "Pesce marino nobile e leggendario che nuota a fianco delle navi magiche fungendo da guardiano delle acque. Possiede l'innato e misterioso potere di ancorare e stabilizzare le navi in tempesta, calmando le onde anomale e dissipando i vortici magici marini.",
        "utilizziMagici": "Simbolo supremo di buon auspicio per la navigazione. Rigorosamente protetto dalle convenzioni magizoologiche internazionali: vietata la pesca, la cattura o la detenzione.",
        "regolamentazione": "Severissime sanzioni penali e pecuniarie dal Dipartimento per chi arreca disturbo alla specie."
    }
]

print("Creature base count:", len(creature))
