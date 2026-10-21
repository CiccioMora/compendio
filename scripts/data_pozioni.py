# -*- coding: utf-8 -*-
"""
Dati esaustivi per la macro-categoria Arte delle Pozioni (Manuale di Pozioni Avanzate - Libatius Borage).
Contiene 127 voci complete con ricette integrali, ingredienti, preparazioni, precauzioni e colori finali.
Suddivise per anno (I - VII Anno), senza valenza.
"""

pozioni_data = [
    # ==========================================
    # I ANNO
    # ==========================================
    {
        "id": "pot-scacciabrufoli",
        "nome": "Pozione Scacciabrufoli",
        "nomeAlternativo": "Cura per Foruncoli ed Eruzioni Cutanee (Cure for Boils)",
        "anno": 1,
        "annoLabel": "I Anno",
        "tipologia": "Curativa / Trasformante",
        "coloreFinale": "Rosa con presenza di fumi dello stesso colore",
        "tempoPreparazione": "45-60 minuti",
        "difficolta": "Base / Principiante",
        "metodoAssunzione": "Applicazione Topica",
        "ingredienti": [
            "Aculei di Porcospino (2)",
            "Cipolle Pungose (2)",
            "Lumache Cornute Stufate (0,05 ml)",
            "Muco di Vermicoli (0,05 ml)",
            "Ortiche Essiccate (4)",
            "Radice di Zenzero (1)",
            "Spine di Shrake (3)",
            "Zanne di Serpente (6)"
        ],
        "preparazione": [
            "1. Stufare le Lumache Cornute tenendole in acqua bollente per 20 minuti.",
            "2. Ridurre in polvere finissima 6 zanne di Serpente con coltellino d'argento e mortaio.",
            "3. Aggiungere 4 misurini del composto ottenuto a mezzo litro d'acqua.",
            "4. Mescolare 2 volte in senso orario.",
            "5. Cuocere a fiamma molto alta per 10 secondi, poi abbassare la fiamma e lasciare in infusione per 40 minuti.",
            "6. Tagliare finemente le Cipolle Pungose con occhialetti e guanti, poi metterle nel calderone.",
            "7. Aggiungere 4 ortiche essiccate e una goccia di Muco di Vermicoli.",
            "8. Mescolare energicamente per 7 volte in senso orario.",
            "9. Polverizzare una radice di zenzero e inserirne un misurino nel composto, mescolando 7 volte in senso orario.",
            "10. Aggiungere 3 spine di Shrake e mescolare molto lentamente per 10 volte in senso orario.",
            "11. Pestare le lumache cornute e aggiungerne un goccio al composto (la pozione prenderà una colorazione bluastra).",
            "12. Mescolare lentamente per 9 volte in senso orario finché non torna rossa.",
            "13. TOGLIERE LA POZIONE DAL FUOCO.",
            "14. Aggiungere due aculei di porcospino a fuoco spento.",
            "15. Attendere 5 minuti prima di imbottigliare."
        ],
        "avvertenze": "CRITICA: Gli aculei di porcospino DEVONO essere aggiunti categoricamente dopo aver spento il fuoco. Se aggiunti sul fuoco sciolgono il calderone producendo fumi caustici che coprono la pelle di enormi pustole purulente.",
        "inventoreOrigine": "Formula classica insegnata agli allievi del Primo Anno. Varianti: Pasta Tolipan (1907) e Pozione Sparisci-Brufoli in 10 secondi di Fred e George Weasley.",
        "descrizione": "Rimedio efficace contro pustole, foruncoli, orticaria e infiammazioni acute della cute. Classificata sia come pozione curativa che trasformante per il suo duplice effetto: lenisce l'agente infiammatorio e rigenera l'epidermide nascondendo l'inestetismo."
    },

    # ==========================================
    # II ANNO
    # ==========================================
    {
        "id": "pot-soporifera",
        "nome": "Pozione Soporifera",
        "nomeAlternativo": "Distillato Soporifero (Sleeping Draught)",
        "anno": 2,
        "annoLabel": "II Anno",
        "tipologia": "Soporifera / Sonno",
        "coloreFinale": "Viola scuro",
        "tempoPreparazione": "80 minuti",
        "difficolta": "Intermedio",
        "metodoAssunzione": "Ingestione",
        "ingredienti": [
            "Ingrediente Standard (6 misurini)",
            "Lavanda (4 rametti)",
            "Muco di Vermicoli (2 gocce)",
            "Valeriana (4 rametti)"
        ],
        "preparazione": [
            "1. Pestare 4 rametti di Lavanda con 2 misurini di Ingrediente Standard in mortaio fino a ottenere una pasta omogenea.",
            "2. Inserire un litro d'acqua nel calderone a fiamma bassa.",
            "3. Aggiungere 2 gocce di Muco di Vermicoli e 2 misurini di Ingrediente Standard scaldando per 30 secondi.",
            "4. Versare 3 misurini della pasta di lavanda nel calderone e lasciare in infusione per 70 minuti.",
            "5. Aggiungere gli ultimi 2 misurini di Ingrediente Standard e alzare la temperatura.",
            "6. Dopo un minuto, aggiungere i rametti di Valeriana e mescolare in senso orario per 7 volte.",
            "7. Spegnere il fuoco, lasciar raffreddare e filtrare per 2 volte prima di imbottigliare."
        ],
        "avvertenze": "Da non confondere col Distillato della Morte Vivente; garantisce un sonno ristoratore profondo ma temporaneo. L'antidoto è la Pozione Risvegliante.",
        "inventoreOrigine": "Formula tradizionale per insonnia e stati di agitazione febbrile.",
        "descrizione": "Permette di far addormentare istantaneamente chi la beve garantendo un riposo profondo e privo di incubi. Può essere diluita in bevande o cibi per mascherarne il sapore."
    },
    {
        "id": "pot-drizzacapelli",
        "nome": "Pozione Drizzacapelli",
        "nomeAlternativo": "Hair-Raising Potion",
        "anno": 2,
        "annoLabel": "II Anno",
        "tipologia": "Trasformante",
        "coloreFinale": "Verde brillante (consistenza pasta)",
        "tempoPreparazione": "150 minuti",
        "difficolta": "Intermedio",
        "metodoAssunzione": "Applicazione Topica sul cuoio capelluto",
        "ingredienti": [
            "Aculei di Porcospino (3)",
            "Code di topo (3)",
            "Fagiolo Engorgiante (1)",
            "Muco di Vermicoli (1 ml)",
            "Pungiglione di Billywig (1)"
        ],
        "preparazione": [
            "1. Inserire 3 code di topo nel calderone con un litro d'acqua e portare a bollore.",
            "2. Inserire il pungiglione di Billywig e mescolare lentamente per 5 volte in senso antiorario.",
            "3. Lasciare in infusione per 60 minuti.",
            "4. Spremere il Fagiolo Engorgiante con coltellino d'argento e versarne il succo nel calderone.",
            "5. Mescolare per 5 volte in senso orario, spegnere il fuoco e far riposare per 20 minuti.",
            "6. A fuoco spento aggiungere i 3 aculei di porcospino e mescolare in senso orario per 5 volte.",
            "7. Far riposare per 60 minuti, filtrare, aggiungere 1 ml di muco di vermicoli e mescolare in senso antiorario fino a consistenza pastosa."
        ],
        "avvertenze": "Aggiungere sempre gli aculei a fuoco spento. Tenuta di 12 ore.",
        "inventoreOrigine": "Composto goliardico e di costume molto popolare tra i giovani studenti.",
        "descrizione": "Preparato pastoso che, spalmato sui capelli, li solleva verticalmente rendendoli rigidi e duri come la pietra per almeno 12 ore."
    },
    {
        "id": "pot-abbellente",
        "nome": "Pozione Abbellente",
        "nomeAlternativo": "Beautification Potion (Sacharissa Tugwood)",
        "anno": 2,
        "annoLabel": "II Anno",
        "tipologia": "Trasformante / Cosmetica",
        "coloreFinale": "Color arcobaleno brillante con emissione di bolle multicolori",
        "tempoPreparazione": "40 minuti",
        "difficolta": "Intermedio",
        "metodoAssunzione": "Ingestione",
        "ingredienti": [
            "Alchemilla (1 rametto)",
            "Ali di fata (6)",
            "Crini di Unicorno (1 ciocca)",
            "Pelle di Boomslang (4 cm)",
            "Petali di rosa freschissima (7)",
            "Radice di zenzero (1)",
            "Rugiada mattutina pura (1/2 litro)"
        ],
        "preparazione": [
            "1. Tagliare la radice di zenzero, essiccarla con l'Incantesimo Essiccante per due volte e ridurla in polvere finissima.",
            "2. Polverizzare 6 ali di fata e triturare 4 cm di pelle di Boomslang, aggiungendole al calderone.",
            "3. Mescolare lentamente versando a filo la rugiada mattutina fino a rendere il composto denso.",
            "4. Mescolare con vigore per 10 minuti, accendere il fuoco e aggiungere mezzo litro d'acqua.",
            "5. Aggiungere 7 petali di rosa e l'Alchemilla tritata, mescolando lentamente per 3 volte.",
            "6. Aggiungere una ciocca di crini di Unicorno e mescolare energicamente per 7 volte in senso antiorario.",
            "7. Aggiungere 4 cucchiaini di zenzero in polvere, spegnere il fuoco e imbottigliare."
        ],
        "avvertenze": "Un bicchiere ha effetto per 24 ore; assumibile periodicamente senza effetti collaterali.",
        "inventoreOrigine": "Creata dalla celebre pozionista Sacharissa Tugwood (1874-1966), celebrata sulle figurine delle Cioccorane.",
        "descrizione": "Rende i lineamenti del viso attraenti, radiosi e armoniosi per un giorno intero, addolcendo la conformazione epidermica."
    },
    {
        "id": "pot-erbicida",
        "nome": "Pozione Erbicida",
        "nomeAlternativo": "Herbicide Potion / Diserbante Magico",
        "anno": 2,
        "annoLabel": "II Anno",
        "tipologia": "Veleno per Piante / Diserbante",
        "coloreFinale": "Verde smeraldo scuro",
        "tempoPreparazione": "60 minuti",
        "difficolta": "Base",
        "metodoAssunzione": "Nebulizzazione sul suolo o fogliame",
        "ingredienti": [
            "Ingrediente Standard (2 misurini)",
            "Muco di Vermicoli (2 gocce)",
            "Spine di Pesce Leone (4)",
            "Succo di Horklump (2 misurini)"
        ],
        "preparazione": [
            "1. Triturare le spine di pesce leone in mortaio con 2 misurini di Ingrediente Standard.",
            "2. Aggiungere 3 misurini della miscela al calderone con un litro d'acqua.",
            "3. Mescolare per 10 volte in senso orario e far riposare per 45 minuti.",
            "4. Aggiungere 2 misurini di succo di Horklump, cuocere a fiamma media per 10 secondi.",
            "5. Aggiungere 2 gocce di Muco di Vermicoli sul fuoco, mescolare 4 volte in senso orario, spegnere e imbottigliare."
        ],
        "avvertenze": "Tossica e disgustosa per l'uomo; bonifica grandi aree infestate senza danneggiare il suolo.",
        "inventoreOrigine": "Formula classica d'Erbologia; le piante danneggiate per errore possono essere curate con Pozione Rigerminante di Tilden Toots.",
        "descrizione": "Uccide le piante parassite non magiche e danneggia gravemente le piante magiche infestanti erodendo i loro apparati radicali."
    },
    {
        "id": "pot-pompion",
        "nome": "Pozione Pompion",
        "nomeAlternativo": "Pozione Testa di Zucca",
        "anno": 2,
        "annoLabel": "II Anno",
        "tipologia": "Trasformante",
        "coloreFinale": "Arancione vivido",
        "tempoPreparazione": "30 minuti",
        "difficolta": "Intermedio",
        "metodoAssunzione": "Ingestione nascosta in cibi o bevande",
        "ingredienti": [
            "Falena Flitterby (1)",
            "Bulbo Balzellante (1)",
            "Digitale (1 foglia)"
        ],
        "preparazione": [
            "1. Triturare la falena Flitterby in poltiglia e aggiungerla al calderone con 50 cc d'acqua.",
            "2. Fuoco basso, mescolare 6 volte in senso orario fino a colorazione verde.",
            "3. Pestare il bulbo balzellante, aggiungerlo e mescolare in senso antiorario per 6 volte finché non diventa rosso.",
            "4. Spegnere il fuoco e far riposare per 16 minuti.",
            "5. Sminuzzare mezza foglia di digitale, aggiungerla e mescolare 4 volte in senso orario finché non vira all'arancione.",
            "6. Filtrare una volta e imbottigliare."
        ],
        "avvertenze": "Antidoto: Pozione Restaurante. Impedisce temporaneamente di parlare chiaramente.",
        "inventoreOrigine": "Preparato trasformante analogo all'incanto 'Melofors', ma con durata prolungata.",
        "descrizione": "Trasfigura temporaneamente la testa del bevitore in una zucca vera e propria, impedendo la vista nitida e la corretta articolazione verbale."
    },
    {
        "id": "pot-ghiaccio",
        "nome": "Pozione del Ghiaccio",
        "nomeAlternativo": "Fire Protection Potion (François Melefoix)",
        "anno": 2,
        "annoLabel": "II Anno",
        "tipologia": "Trasformante / Protezione Termica",
        "coloreFinale": "Blu ceruleo",
        "tempoPreparazione": "75 minuti",
        "difficolta": "Intermedio",
        "metodoAssunzione": "Ingestione (dose consigliata: circa 15 cl)",
        "ingredienti": [
            "Fungo Arroventoso (2)",
            "Ghiaccio tritato (15 scaglie)",
            "Polvere di Cappernuncolo (4 misurini)",
            "Sangue di Tritone (6 gocce)"
        ],
        "preparazione": [
            "1. Versare 1 litro d'acqua freddissima e portare lentamente a ebollizione a fiamma bassa.",
            "2. Affettare i Funghi Arroventosi privati dell'effetto esplosivo con coltellino d'argento e inserirli nel calderone.",
            "3. Mescolare 6 volte in senso orario fino a blu ceruleo, poi aggiungere 6 gocce di Sangue di Tritone.",
            "4. Mescolare 4 volte in senso antiorario, unire 4 misurini di polvere di Cappernuncolo e mescolare 6 volte in senso orario fino a color rossastro.",
            "5. Spegnere il fuoco, lasciar riposare per 1 ora, imbottigliare e aggiungere 15 scaglie di ghiaccio tritato."
        ],
        "avvertenze": "Indossare guanti di drago per maneggiare funghi e cappernuncolo. Non superare i 15 cl per evitare ipotermia sistemica. Assumibile nuovamente solo dopo 72 ore.",
        "inventoreOrigine": "Inventata da François Melefoix per i suoi spettacoli di magia con fiamme.",
        "descrizione": "Crea una barriera termica invisibile attorno al corpo e alle vesti che rende totalmente immuni alle fiamme e al calore per un'ora intera."
    },
    {
        "id": "pot-rinforzante",
        "nome": "Soluzione Rinforzante",
        "nomeAlternativo": "Pozione Corroborante (Strengthening Solution)",
        "anno": 2,
        "annoLabel": "II Anno",
        "tipologia": "Alteratrice di Stato / Vigore Fisico",
        "coloreFinale": "Arancione",
        "tempoPreparazione": "Oltre 48 ore (fermentazione)",
        "difficolta": "Intermedio / Avanzato",
        "metodoAssunzione": "Ingestione",
        "ingredienti": [
            "Acqua di sorgente (1 litro)",
            "Artigli di Grifone (3)",
            "Omero umano (1)",
            "Sangue di Tritone (5 gocce)",
            "Zanne di Geranio Zannuto (6)",
            "Zanne di Serpente (3)"
        ],
        "preparazione": [
            "1. Tritare finemente gli artigli di Grifone; aggiungere un litro d'acqua di sorgente al calderone.",
            "2. Inserire 6 zanne di Geranio Zannuto e un misurino di artigli di Grifone.",
            "3. Mescolare 15 volte in senso orario usando l'omero umano come mestolo e poi lasciarlo cadere nel calderone.",
            "4. Fuoco bassissimo: lasciar fermentare per almeno 48 ore consecutive.",
            "5. Spegnere il fuoco, lasciar raffreddare e filtrare il liquido.",
            "6. Unire 5 gocce di sangue di Tritone e mescolare 7 volte in senso antiorario.",
            "7. Aggiungere le zanne di serpente tritate, accendere a fiamma altissima per 30 secondi, spegnere e imbottigliare."
        ],
        "avvertenze": "Bandita categoricamente nelle competizioni sportive ufficiali (doping magico). Non conferisce abilità marziali ignote ma spinge i muscoli al massimo.",
        "inventoreOrigine": "Formula tradizionale per minatori magici e soldati.",
        "descrizione": "Conferisce una forza muscolare sorprendente per un'ora, spingendo le potenzialità fisiche al loro culmine naturale senza provocare strappi o contratture."
    },
    {
        "id": "pot-resistenza",
        "nome": "Pozione della Resistenza",
        "nomeAlternativo": "Endurance Potion",
        "anno": 2,
        "annoLabel": "II Anno",
        "tipologia": "Alteratrice di Stato / Resistenza",
        "coloreFinale": "Verde smeraldo brillante",
        "tempoPreparazione": "110 minuti",
        "difficolta": "Intermedio",
        "metodoAssunzione": "Ingestione (massimo 2 fiale)",
        "ingredienti": [
            "Ali di Fata (2)",
            "Cavallucci Marini Volanti (4)",
            "Toraci di Libellula tostati (3)",
            "Uova di Doxy (10)"
        ],
        "preparazione": [
            "1. Portare a bollore 1 litro d'acqua, spegnere e aggiungere 2 ali di Fata.",
            "2. Triturare 10 uova di Doxy in mortaio e aggiungerne un misurino al composto.",
            "3. Scaldare per 31 minuti finché non diventa rosa.",
            "4. Tostare a parte i toraci di libellula per 12 secondi a lato.",
            "5. Aggiungere un torace di libellula (la pozione vira all'arancione), spegnere e lasciar fermentare per 20 minuti.",
            "6. Aggiungere 1 cavalluccio marino volante e il secondo torace di libellula; scaldare per 15 minuti finché diventa rossa.",
            "7. Aggiungere 3 misurini di uova di Doxy, l'ultimo torace e i restanti cavallucci; spegnere e lasciare in infusione per 1 ora fino a viraggio verde."
        ],
        "avvertenze": "Maneggiare le uova di Doxy con guanti in pelle di drago. Vietata nelle gare di Quidditch per effetto dopante.",
        "inventoreOrigine": "Variante minore: Pozione Vitamix.",
        "descrizione": "Non accresce la forza bruta, ma eleva straordinariamente la soglia di sopportazione alla fatica, al dolore e allo sforzo continuato per 3 ore."
    },
    {
        "id": "pot-dilatante",
        "nome": "Pozione Dilatante",
        "nomeAlternativo": "Swelling Solution",
        "anno": 2,
        "annoLabel": "II Anno",
        "tipologia": "Trasformante / Ingrandimento",
        "coloreFinale": "Giallo acceso",
        "tempoPreparazione": "3 ore e 15 minuti",
        "difficolta": "Base / Intermedio",
        "metodoAssunzione": "Contatto topico o aspersione",
        "ingredienti": [
            "Milza di Pipistrello (1)",
            "Occhi di Pesce Palla (3)",
            "Ortiche Essiccate (2 cucchiai)"
        ],
        "preparazione": [
            "1. Essiccare 3 ortiche, unirle a 3 occhi di pesce palla in mortaio e triturare in polvere media.",
            "2. Versare 2 misurini del composto nel calderone con 2 cucchiai d'acqua.",
            "3. Scaldare a fiamma media per 4 minuti, poi aggiungere mezzo litro d'acqua e mescolare 4 volte in senso orario.",
            "4. Spegnere e lasciar riposare per 3 ore intere.",
            "5. Aggiungere la milza di pipistrello e mescolare 4 volte in senso antiorario.",
            "6. Scaldare a fiamma altissima per 30 secondi, spegnere e imbottigliare."
        ],
        "avvertenze": "Basta una sola goccia per innescare la dilatazione immediata. Antidoto: Pozione Sgonfiotto.",
        "inventoreOrigine": "Composto fondamentale studiato nel Secondo Anno di Pozioni.",
        "descrizione": "A contatto con tessuti o oggetti ne provoca un rigonfiamento colossale immediato e progressivo."
    },
    {
        "id": "pot-sgonfiotto",
        "nome": "Pozione Sgonfiotto",
        "nomeAlternativo": "Deflating Draught / Antidoto Dilatante",
        "anno": 2,
        "annoLabel": "II Anno",
        "tipologia": "Antidoto / Rimpicciolimento",
        "coloreFinale": "Arancione acceso",
        "tempoPreparazione": "6 ore e 15 minuti",
        "difficolta": "Intermedio",
        "metodoAssunzione": "Contatto topico (pasta con lumache) o ingestione",
        "ingredienti": [
            "Aculei di Porcospino (6)",
            "Bruco (1)",
            "Grinzafico (1)",
            "Lumache Cornute pestate (3, opzionali per uso cutaneo)",
            "Milza di Gatto disidratata (1)",
            "Radici di Viola (4)"
        ],
        "preparazione": [
            "1. Portare a bollore 1 litro d'acqua a fiamma bassa; sminuzzare le radici di viola e sbucciare il Grinzafico dividendolo in 4 parti.",
            "2. Aggiungerli al calderone assieme a 8 rondelle di bruco affettato.",
            "3. Abbassare la fiamma fino a spegnerla nell'arco di due minuti.",
            "4. Pestare la milza di gatto su tagliere trattenendo i tessuti ed eliminando i succhi.",
            "5. A fuoco spento aggiungere 6 aculei di porcospino e la milza disidratata.",
            "6. [Per pasta cutanea unire 3 lumache pestate e mescolare 36 volte in senso orario].",
            "7. Dopo 6 ore filtrare e imbottigliare."
        ],
        "avvertenze": "Non agisce su corpi o oggetti trasfigurati naturalmente, ma solo su ciò che è stato gonfiato magicamente.",
        "inventoreOrigine": "Antidoto specifico complementare alla Pozione Dilatante.",
        "descrizione": "Annulla all'istante l'effetto rigonfiante della Pozione Dilatante riportando oggetti, membra o corpi alla loro naturale volumetria."
    },
    {
        "id": "pot-lisciariccio",
        "nome": "Tricopozione Lisciariccio",
        "nomeAlternativo": "Sleekeazy’s Hair Potion (Fleamont Potter)",
        "anno": 2,
        "annoLabel": "II Anno",
        "tipologia": "Cosmetica / Cura dei Capelli",
        "coloreFinale": "Trasparente (consistenza gelatinosa)",
        "tempoPreparazione": "75 minuti",
        "difficolta": "Intermedio",
        "metodoAssunzione": "Applicazione Topica sulla chioma",
        "ingredienti": [
            "Crini di Petardo Cinese (4)",
            "Gomas Barbadensis (3 misurini di poltiglia)",
            "Vasellina magica (4 misurini)"
        ],
        "preparazione": [
            "1. Pestare in mortaio le foglie di Gomas Barbadensis fino a ottenere una pasta omogenea.",
            "2. Versare mezzo litro d'acqua nel calderone a fuoco basso con 4 crini di Petardo Cinese.",
            "3. Mescolare velocemente per 15 volte in senso orario e 15 volte in senso antiorario.",
            "4. Aggiungere 3 misurini di Gomas Barbadensis e spegnere il fuoco.",
            "5. Mescolare velocemente per 15 volte in senso antiorario e far riposare per 50 minuti.",
            "6. Aggiungere 4 misurini di vasellina mescolando lentamente per 7 minuti fino a consistenza gelatinosa.",
            "7. Imbottigliare con spatola di legno."
        ],
        "avvertenze": "Completamente inefficace su chi possiede capelli rossi naturali. Tenuta garantita di 24 ore (teme l'umidità eccessiva).",
        "inventoreOrigine": "Inventata attorno al 1940 da Fleamont Potter (nonno di Harry Potter) a seguito di viaggi in Cina, quadruplicando la ricchezza di famiglia.",
        "descrizione": "Doma all'istante le chiome più ribelli e arruffate con sole due gocce, permettendo di modellarle in acconciature eleganti e ordinate."
    },
    {
        "id": "pot-prestocalvo",
        "nome": "Pozione Prestocalvo",
        "nomeAlternativo": "Depilatorio Magico da Combattimento",
        "anno": 2,
        "annoLabel": "II Anno",
        "tipologia": "Cosmetica / Veleno o Antidoto",
        "coloreFinale": "Ambrato con riflessi argentei",
        "tempoPreparazione": "35 minuti",
        "difficolta": "Intermedio",
        "metodoAssunzione": "Ingestione o contatto",
        "ingredienti": [
            "Estratto di Sangue di Drago 'Prestocalvo' (1 goccia)",
            "Foglie di Rosa (10)",
            "Milza di Ratto sezionata (1)",
            "Radici di Cardo (4)"
        ],
        "preparazione": [
            "1. Portare a bollore mezzo litro d'acqua nel calderone.",
            "2. Tagliare e pestare le radici di cardo con le 10 foglie di rosa fino a pasta omogenea, unendola al calderone.",
            "3. Mescolare 6 volte in senso orario, spegnere e lasciare in infusione per 15 minuti.",
            "4. Sezionare in 4 la milza di ratto e inserirne i pezzi uno alla volta, mescolando 6 volte in senso orario.",
            "5. Filtrare, imbottigliare e aggiungere infine la goccia di estratto di sangue di drago Prestocalvo."
        ],
        "avvertenze": "Se assunta senza fattura tricologica attiva provoca la caduta repentina e irreversibile di tutti i capelli per mesi. Antidoto: Pozione Fulvoadesso.",
        "inventoreOrigine": "Distillato brevettato da maestri pozionisti del XVII secolo.",
        "descrizione": "Arresta all'istante le fatture di ricrescita incontrollata dei capelli; funge da veleno depilatorio se assunta impropriamente."
    },
    {
        "id": "pot-fulvoadesso",
        "nome": "Pozione Fulvoadesso",
        "nomeAlternativo": "Pozione Manegro (Hair-Raising Restorer)",
        "anno": 2,
        "annoLabel": "II Anno",
        "tipologia": "Curativa / Antidoto Tricologico",
        "coloreFinale": "Ambrato con riflessi argentei",
        "tempoPreparazione": "35 minuti",
        "difficolta": "Intermedio",
        "metodoAssunzione": "Ingestione",
        "ingredienti": [
            "Estratto di Sangue di Drago 'Fulvoadesso' (1 goccia)",
            "Foglie di Rosa (10)",
            "Milza di Ratto (1)",
            "Radici di Cardo (4)"
        ],
        "preparazione": [
            "1. Portare a bollore mezzo litro d'acqua, unendo radici di cardo e foglie di rosa pestate.",
            "2. Mescolare 8 volte in senso orario (differenza cardinale rispetto a Prestocalvo).",
            "3. Spegnere e lasciare in infusione per 15 minuti.",
            "4. Inserire le 4 sezioni di milza di ratto e mescolare 6 volte in senso orario.",
            "5. Filtrare, imbottigliare e aggiungere la goccia di estratto di Sangue di Drago Fulvoadesso."
        ],
        "avvertenze": "Se assunta senza calvizie magica da curare genera una crescita abnorme di capelli per settimane.",
        "inventoreOrigine": "Antidoto complementare ufficiale alla Pozione Prestocalvo.",
        "descrizione": "Stimola la ricrescita immediata dei capelli persi a causa di incantesimi oscuri, fatture o pozioni depilatorie."
    },
    {
        "id": "pot-singhiozzante",
        "nome": "Soluzione Singhiozzante",
        "nomeAlternativo": "Hiccuping Solution",
        "anno": 2,
        "annoLabel": "II Anno",
        "tipologia": "Alteratrice di Stato / Goliardica",
        "coloreFinale": "Giallo canarino",
        "tempoPreparazione": "45 minuti",
        "difficolta": "Base",
        "metodoAssunzione": "Ingestione",
        "ingredienti": [
            "Capelli di Banshee (4)",
            "Mughetto (10 fiori)",
            "Pungiglione di Billywig essiccato (1)"
        ],
        "preparazione": [
            "1. Triturare 10 fiori di mughetto in pasta omogenea.",
            "2. Riscaldare il calderone con 1 litro d'acqua; tagliare ogni capello di Banshee in 3 parti.",
            "3. Inserire 2 capelli e mescolare 6 volte in senso antiorario.",
            "4. Essiccare il pungiglione di Billywig con l'Incantesimo Essiccante per 3 volte e aggiungerlo al composto con i restanti capelli.",
            "5. Mescolare 6 volte in senso orario, unire 4 misurini di pasta di mughetto, spegnere e lasciare in infusione per 30 minuti."
        ],
        "avvertenze": "Spesso scambiata per la Pozione Dilatante per via del colore giallo. L'effetto dura 20 minuti; in caso di sovradosaggio somministrare Infuso di Anice.",
        "inventoreOrigine": "Scherzo classico tra studenti di Hogwarts.",
        "descrizione": "Scatena violenti e rumorosi spasmi diaframmatici con singhiozzo continuo e incontrollabile."
    },
    {
        "id": "pot-restaurante",
        "nome": "Pozione Restaurante",
        "nomeAlternativo": "Restoration Potion / Contro-Incantesimo Universale",
        "anno": 2,
        "annoLabel": "II Anno",
        "tipologia": "Contro-Incantesimo / Antidoto Aspecifico",
        "coloreFinale": "Viola glicine",
        "tempoPreparazione": "3 ore e 30 minuti",
        "difficolta": "Avanzato",
        "metodoAssunzione": "Contatto topico o aspersione su bersagli incantati",
        "ingredienti": [
            "Bocca di Leone (3 fiori)",
            "Corno di Bicorno (1, scaglie sottili)",
            "Milza di Pipistrello intera (1)",
            "Pelle di Boomslang tagliata a listarelle (4x4 cm)"
        ],
        "preparazione": [
            "1. Tagliare la pelle di Boomslang in listarelle fini; separare i petali di Bocca di Leone e ricavare scaglie sottili dal corno di Bicorno.",
            "2. Mettere 1 litro d'acqua a bollire nel calderone con la milza intera di pipistrello.",
            "3. Al bollore unire i petali di Bocca di Leone e lasciare in infusione per 3 ore.",
            "4. Spegnere, filtrare e rimettere a fiamma bassissima.",
            "5. Inserire le scaglie di Bicorno e mescolare 7 volte in senso antiorario.",
            "6. Inserire le listarelle di Boomslang, mescolare 7 volte in senso orario, spegnere e filtrare."
        ],
        "avvertenze": "Efficace solo su incantesimi e pozioni trasfigurative blande o generiche (non agisce su Maledizioni Senza Perdono o veleni complessi).",
        "inventoreOrigine": "Trattato classico di alchimia difensiva.",
        "descrizione": "Agisce per contatto annullando incantesimi minori attivi e sortilegi blandi presenti su una persona, oggetto o creatura magica."
    },
    # Raccolta Principianti II Anno
    {
        "id": "pot-distillato-smorzante",
        "nome": "Distillato Smorzante",
        "nomeAlternativo": "Silenziatore Vocale Inalatorio",
        "anno": 2,
        "annoLabel": "II Anno",
        "tipologia": "Alteratrice di Stato / Fumi",
        "coloreFinale": "Fluttuanti vapori azzurri traslucidi",
        "tempoPreparazione": "25 minuti",
        "difficolta": "Base",
        "metodoAssunzione": "Inalazione",
        "ingredienti": ["Vapori di assenzio distillato", "Radici di malva", "Polvere di roccia silicea"],
        "preparazione": ["Distillare a caldo i componenti convogliando i vapori azzurri in ampolle ermetiche."],
        "avvertenze": "Annulla la voce impedendo la pronuncia di formule verbali. Antidoto: Pozione Volubilis.",
        "inventoreOrigine": "Raccolta di Pozioni per Principianti (pag. 33).",
        "descrizione": "I suoi vapori azzurri azzerano momentaneamente le corde vocali impedendo del tutto di parlare per un'ora."
    },
    {
        "id": "pot-alito-cane",
        "nome": "Pozione Alito di Cane",
        "nomeAlternativo": "Sputafuoco Rudimentale",
        "anno": 2,
        "annoLabel": "II Anno",
        "tipologia": "Offensiva Minore / Goliardica",
        "coloreFinale": "Violacea",
        "tempoPreparazione": "30 minuti",
        "difficolta": "Base",
        "metodoAssunzione": "Ingestione",
        "ingredienti": ["Peperoncino comune", "Zanne di serpente", "Zolfo vegetale"],
        "preparazione": ["Bollire a fiamma viva per 15 minuti mescolando in senso orario."],
        "avvertenze": "Lascia persistente sapore di bruciato e bruciore alla gola per un'ora.",
        "inventoreOrigine": "Versione rudimentale della ben più potente Pozione Sputafuoco.",
        "descrizione": "Consente di sputare un singolo getto di fiamma dalla bocca subito dopo averla ingoiata."
    },
    {
        "id": "pot-capelli-urlanti",
        "nome": "Pozione dei Capelli Urlanti",
        "nomeAlternativo": "Medusa Minore",
        "anno": 2,
        "annoLabel": "II Anno",
        "tipologia": "Cosmetica / Trasformante",
        "coloreFinale": "Oleosa scura",
        "tempoPreparazione": "20 minuti",
        "difficolta": "Base",
        "metodoAssunzione": "Applicazione Topica sul cuoio capelluto",
        "ingredienti": ["Olio di ricino", "Pelle di serpente del grano", "Squame di drago polverizzate"],
        "preparazione": ["Emulsionare a freddo e lasciare sedimentare per 12 ore."],
        "avvertenze": "Totalmente innocua, durata fissa di 6 ore.",
        "inventoreOrigine": "Raccolta di Pozioni per Principianti (pag. 33).",
        "descrizione": "Trasforma temporaneamente le ciocche di capelli in piccoli serpenti sibilanti che ondeggiano sulla testa."
    },
    {
        "id": "pot-ringhio-caxambu",
        "nome": "Pozione del Ringhio di Caxambu",
        "nomeAlternativo": "Grumble Draught of Caxambu",
        "anno": 2,
        "annoLabel": "II Anno",
        "tipologia": "Alteratrice di Stato / Scherzo",
        "coloreFinale": "Marrone torbido",
        "tempoPreparazione": "20 minuti",
        "difficolta": "Base",
        "metodoAssunzione": "Ingestione",
        "ingredienti": ["Radici di rabarbaro", "Lievito magico brasiliano", "Acqua effervescente"],
        "preparazione": ["Miscelare a freddo in calderone d'ottone."],
        "avvertenze": "Induce voracità improvvisa senza conseguenze mediche.",
        "inventoreOrigine": "Creata nella cittadina brasiliana di Caxambu.",
        "descrizione": "Genera nello stomaco un fragoroso e imbarazzante ringhio continuo stimolando un'incontenibile sensazione di fame."
    },
    {
        "id": "pot-fungina",
        "nome": "Pozione Fungina",
        "nomeAlternativo": "Sprout-Fungus Potion",
        "anno": 2,
        "annoLabel": "II Anno",
        "tipologia": "Trasformante / Goliardica",
        "coloreFinale": "Grigio verdognolo",
        "tempoPreparazione": "35 minuti",
        "difficolta": "Base",
        "metodoAssunzione": "Aspersione spray sulla pelle",
        "ingredienti": ["Spore di fungo saltellante", "Polvere di rospo", "Acqua stagnante"],
        "preparazione": ["Far macerare le spore al buio prima dell'ebollizione."],
        "avvertenze": "I funghi scompaiono spontaneamente dopo pochi giorni.",
        "inventoreOrigine": "Raccolta di Pozioni per Principianti (pag. 33).",
        "descrizione": "Spruzzata sulla pelle, fa spuntare all'istante funghi innocui di varie dimensioni su braccia e volto."
    },
    {
        "id": "pot-granbulbo",
        "nome": "Pozione Granbulbo",
        "nomeAlternativo": "Bulbo-Oculi Draught",
        "anno": 2,
        "annoLabel": "II Anno",
        "tipologia": "Alteratrice di Stato / Visiva",
        "coloreFinale": "Verde smeraldo",
        "tempoPreparazione": "40 minuti",
        "difficolta": "Base",
        "metodoAssunzione": "Contatto con gli occhi",
        "ingredienti": ["Succo di bulbo balzellante", "Ortica", "Occhi di anguilla"],
        "preparazione": ["Decotto a fuoco rapido filtrato su lino."],
        "avvertenze": "Causa emicrania e vista sfocata. Antidoto: Pozione della Vista.",
        "inventoreOrigine": "Raccolta di Pozioni per Principianti (pag. 33).",
        "descrizione": "Fa gonfiare smisuratamente i bulbi oculari rendendoli sporgenti come quelli di un rospo."
    },
    {
        "id": "pot-lassativa",
        "nome": "Pozione Lassativa",
        "nomeAlternativo": "Purga Magica all'Agrimonia",
        "anno": 2,
        "annoLabel": "II Anno",
        "tipologia": "Medicinale / Evacuativa",
        "coloreFinale": "Giallo bruno",
        "tempoPreparazione": "30 minuti",
        "difficolta": "Base",
        "metodoAssunzione": "Ingestione in piccolissime dosi",
        "ingredienti": ["Agrimonia essiccata", "Corteccia di frangula", "Sale marino"],
        "preparazione": ["Infuso prolungato in acqua calda non bollente."],
        "avvertenze": "Assumere solo a gocce per scongiurare disidratazione grave.",
        "inventoreOrigine": "Rimedi popolari medievali.",
        "descrizione": "Potente purga magica che libera integralmente l'intestino in pochi minuti."
    },
    {
        "id": "pot-massima-flatulenza",
        "nome": "Pozione Massima Flatulenza",
        "nomeAlternativo": "Gaseous Concoction",
        "anno": 2,
        "annoLabel": "II Anno",
        "tipologia": "Alteratrice di Stato / Scherzosa",
        "coloreFinale": "Verdastro torbido",
        "tempoPreparazione": "25 minuti",
        "difficolta": "Base",
        "metodoAssunzione": "Ingestione furtiva",
        "ingredienti": ["Semi di cavolo carnivoro", "Acqua solforosa", "Cipolla pungosa"],
        "preparazione": ["Fermentazione anaerobica rapida in calderone chiuso."],
        "avvertenze": "Provoca costante e rumorosa emissione di gas intestinali per ore.",
        "inventoreOrigine": "Scherzo classico tra allievi.",
        "descrizione": "Induce un'incessante e incontenibile produzione di gas intestinali con imbarazzanti effetti sonori."
    },
    {
        "id": "pot-sniffante",
        "nome": "Pozione Sniffante",
        "nomeAlternativo": "Nose-Sharpener Potion",
        "anno": 2,
        "annoLabel": "II Anno",
        "tipologia": "Alteratrice Sensoriale",
        "coloreFinale": "Fumi limpidi e perlacei",
        "tempoPreparazione": "30 minuti",
        "difficolta": "Base",
        "metodoAssunzione": "Inalazione dei fumi",
        "ingredienti": ["Foglie di menta piperita", "Semi di finocchio magico", "Sale cristallino"],
        "preparazione": ["Scaldare a fiamma dolce inalando i vapori emergenti."],
        "avvertenze": "Non abusare per non sviluppare ipersensibilità e riniti croniche.",
        "inventoreOrigine": "Raccolta di Pozioni per Principianti (pag. 33).",
        "descrizione": "Potenzia straordinariamente il senso dell'olfatto per trenta minuti, permettendo di distinguere odori distanti e tracce invisibili."
    },
    {
        "id": "pot-vertiginosa",
        "nome": "Pozione Vertiginosa",
        "nomeAlternativo": "Dizziness Draught",
        "anno": 2,
        "annoLabel": "II Anno",
        "tipologia": "Alteratrice di Stato",
        "coloreFinale": "Azzurro cangiante",
        "tempoPreparazione": "30 minuti",
        "difficolta": "Base",
        "metodoAssunzione": "Ingestione",
        "ingredienti": ["Ali di Billywig", "Acqua di sorgente", "Semi di papavero sonnifero"],
        "preparazione": ["Bollire le ali a fuoco rapido e filtrare."],
        "avvertenze": "Un sovradosaggio porta alla perdita dei sensi. Antidoto aspecifico.",
        "inventoreOrigine": "Raccolta di Pozioni per Principianti (pag. 34).",
        "descrizione": "Provoca improvviso disorientamento vestibolare, vertigini acute e perdita totale dell'equilibrio per un'ora."
    },
    {
        "id": "pot-trismatica",
        "nome": "Pozione Trismatica",
        "nomeAlternativo": "Jaw-Lock Potion",
        "anno": 2,
        "annoLabel": "II Anno",
        "tipologia": "Alteratrice Muscolare / Inalazione",
        "coloreFinale": "Blu profondo con fumi bluastri",
        "tempoPreparazione": "40 minuti",
        "difficolta": "Base",
        "metodoAssunzione": "Inalazione",
        "ingredienti": ["Fiori di Mezereo", "Radici di cardo essiccate", "Allume di rocca"],
        "preparazione": ["Sublimazione a vapore con alambicco."],
        "avvertenze": "Paralizza mandibola e mascella per 3 ore impedendo di lanciare formule verbali.",
        "inventoreOrigine": "Raccolta di Pozioni per Principianti (pag. 34).",
        "descrizione": "I suoi fumi blu paralizzano temporaneamente i muscoli masticatori impedendo la parola e la masticazione."
    },
    {
        "id": "pot-luscious-locks",
        "nome": "Soluzione di Luscious Locks",
        "nomeAlternativo": "Lozione Duplice di Zenith Xeep",
        "anno": 2,
        "annoLabel": "II Anno",
        "tipologia": "Cosmetica / Neuro-degenerativa",
        "coloreFinale": "Biondo dorato",
        "tempoPreparazione": "50 minuti",
        "difficolta": "Avanzato",
        "metodoAssunzione": "Topica (capelli) o Ingestione (veleno di memoria)",
        "ingredienti": ["Pozione Obliviosa (come base)", "Lacrime di Wampus", "Olio di noci magiche"],
        "preparazione": ["Incorporare le lacrime di Wampus nella Pozione Obliviosa a freddo."],
        "avvertenze": "Ingerita per via orale distrugge progressivamente la memoria in modo assai più aggressivo della semplice Obliviosa. Esiste un antidoto per fermare il decorso ma i ricordi persi non tornano.",
        "inventoreOrigine": "Creata dalla strega Zenith Xeep.",
        "descrizione": "Ha un micidiale duplice effetto: per via topica dona una lucentezza impareggiabile ai capelli, ma se ingerita dissolve inesorabilmente i ricordi."
    },

    # ==========================================
    # III ANNO
    # ==========================================
    {
        "id": "pot-essenza-dittamo",
        "nome": "Essenza di Dittamo",
        "nomeAlternativo": "Essence of Dittany",
        "anno": 3,
        "annoLabel": "III Anno",
        "tipologia": "Curativa / Medimagica",
        "coloreFinale": "Liquido limpido bruno-verdognolo",
        "tempoPreparazione": "Distillazione continua in alambicco (12 ore)",
        "difficolta": "Avanzato",
        "metodoAssunzione": "Applicazione Topica a gocce su ferite aperte",
        "ingredienti": [
            "Foglie di Origanum Dictamnus essiccate",
            "Sale marino purissimo"
        ],
        "preparazione": [
            "1. Essiccare le foglie fresche di Dittamo al riparo dalla luce solare diretta.",
            "2. Unire le foglie essiccate con sale marino in rapporto 3:1.",
            "3. Caricare l'alambicco e procedere a una lenta distillazione a vapore a fiamma controllata per 12 ore.",
            "4. Raccogliere l'essenza pura condensata nel refrigeratore e sigillare in fiale di vetro scuro."
        ],
        "avvertenze": "Altamente infiammabile: tenere lontana da qualsiasi scintilla. In caso di sovradosaggio provoca effetto caustico da curare con gocce di Infuso di Mandragola.",
        "inventoreOrigine": "Pilastro universale della Medimagia dai tempi dei druidi celtici.",
        "descrizione": "Una delle pozioni curative più potenti e risolutive al mondo: bastano 3 gocce applicate su una ferita aperta per arrestare istantaneamente qualsiasi emorragia e rigenerare uno strato di pelle nuova e sana su ustioni, tagli profondi e lacerazioni."
    },
    {
        "id": "pot-sanagola",
        "nome": "Pozione Sanagola",
        "nomeAlternativo": "Pozione per la Tosse (Cough Draught)",
        "anno": 3,
        "annoLabel": "III Anno",
        "tipologia": "Curativa / Respiratoria",
        "coloreFinale": "Verde scuro",
        "tempoPreparazione": "24 ore di riposo",
        "difficolta": "Intermedio",
        "metodoAssunzione": "Ingestione",
        "ingredienti": [
            "Fiori di Viola Selvatica (20 g)",
            "Foglie di Eucalipto (30 g)",
            "Foglie di Menta (30 g)",
            "Foglie di Parietaria (30 g)",
            "Foglie di Ruta (30 g)",
            "Foglie di Salvia (30 g)",
            "Rametti di Timo (30 g)"
        ],
        "preparazione": [
            "1. Essiccare Salvia, Ruta e Menta con l'Incantesimo Essiccante per 2 volte ciascuno; essiccare Parietaria ed Eucalipto ripetendolo per 4 volte.",
            "2. Ridurre in polvere 30g Salvia, 30g Ruta, 30g Menta, 30g Parietaria e 15g Eucalipto.",
            "3. Portare a bollore mezzo litro d'acqua, dopo 3 minuti aggiungere la polvere e mescolare per 18 volte in senso antiorario (l'acqua diventa rosa tenue).",
            "4. Spegnere e lasciare in infusione per 45 minuti senza mescolare.",
            "5. Tritare 30g timo e 15g eucalipto con acqua rendendoli densi, unirli al calderone, riaccendere il fuoco.",
            "6. Aggiungere 20g fiori di Viola Selvatica lasciandoli sedimentare sul fondo per 2 minuti.",
            "7. Spegnere, lasciar raffreddare, filtrare e imbottigliare dopo 24 ore esatte."
        ],
        "avvertenze": "Conservare rigorosamente lontano da fonti di calore per non degradare i principi balsamici.",
        "inventoreOrigine": "Infuso officinale tradizionale.",
        "descrizione": "Calma istantaneamente tosse stizzosa, mal di gola e infiammazioni alle corde vocali."
    },
    {
        "id": "pot-pepata",
        "nome": "Pozione Pepata",
        "nomeAlternativo": "Decotto Tiramisù (Pepperup Potion)",
        "anno": 3,
        "annoLabel": "III Anno",
        "tipologia": "Curativa / Riscaldante",
        "coloreFinale": "Rosso vermiglio",
        "tempoPreparazione": "45 minuti",
        "difficolta": "Intermedio",
        "metodoAssunzione": "Ingestione",
        "ingredienti": [
            "Corno di Bicorno polverizzato (1)",
            "Erbagioiello (2 fiori)",
            "Radice di Mandragola (1)",
            "Sangue di Tritone (5 gocce)",
            "Semi di Fuoco (4)",
            "Pepe nero macinato (facoltativo, in caso di raffreddori magici)"
        ],
        "preparazione": [
            "1. Inserire 500ml d'acqua nel calderone; unire due pizzichi di polvere finissima di Corno di Bicorno e lasciar decantare per 5 minuti.",
            "2. Tagliare a metà la radice di Mandragola, aggiungerla e mescolare una volta in senso antiorario.",
            "3. Accendere a fuoco lento, portare a bollore e lasciar fermentare per mezz'ora.",
            "4. Spegnere il fuoco, aggiungere due fiori di Erbagioiello e mescolare 4 volte in senso orario.",
            "5. Versare 5 gocce di Sangue di Tritone e mescolare 2 volte in senso antiorario.",
            "6. Aggiungere 4 Semi di Fuoco a intervalli di 3 secondi, riaccendere a fuoco vivo per 60 secondi, spegnere e imbottigliare."
        ],
        "avvertenze": "Fa fumare le orecchie per molte ore dopo l'assunzione. Non assumere per due giorni consecutivi.",
        "inventoreOrigine": "Inventata nel XII secolo da Linfred di Stinchcombe e perfezionata da Glover Hipworth tra il XVIII e XIX secolo.",
        "descrizione": "Rimedio sovrano contro raffreddori e stati febbrili; riscalda istantaneamente il corpo e funge da antidoto alla Maledizione delle Caccole (*Mucus ad Nauseam*)."
    },
    {
        "id": "pot-rimpolpasangue",
        "nome": "Pozione Rimpolpasangue",
        "nomeAlternativo": "Blood-Replenishing Potion (Fabius Eyre)",
        "anno": 3,
        "annoLabel": "III Anno",
        "tipologia": "Curativa / Salvavita",
        "coloreFinale": "Rosso scarlatto",
        "tempoPreparazione": "12 ore di infusione",
        "difficolta": "Avanzato",
        "metodoAssunzione": "Ingestione",
        "ingredienti": [
            "Corteccia di Salice in scaglie (20 g)",
            "Rametto di Biancospino (1)",
            "Sangue di Tritone (10 cucchiai)",
            "Tuorlo d'uovo di Emù (1)"
        ],
        "preparazione": [
            "1. Separare il tuorlo dall'albume di un uovo di Emù e versarlo nel calderone.",
            "2. Mescolare vigorosamente per 30 volte in senso antiorario creando un composto omogeneo.",
            "3. Accendere il fuoco e aggiungere acqua a filo mescolando per non coagulare il tuorlo.",
            "4. Alla comparsa di bollicine giallognole unire il rametto di biancospino e 15 gocce (1 cucchiaio) di Sangue di Tritone.",
            "5. Mescolare lentamente per 9 volte in senso orario evitando grumi.",
            "6. Unire le scaglie di corteccia di salice lunghe un mignolo, spegnere e lasciare in infusione per 12 ore.",
            "7. Aggiungere i restanti 9 cucchiai di Sangue di Tritone, mescolare 12 volte in senso antiorario, filtrare e imbottigliare."
        ],
        "avvertenze": "Agisce efficacemente solo se la ferita originaria è stata prima cauterizzata o sigillata (es. con Dittamo).",
        "inventoreOrigine": "Creata dal celebre guaritore Fabius Eyre.",
        "descrizione": "Pozione salvavita che reintegra istantaneamente i livelli ematici persi in seguito a traumi gravi, ferite profonde o estese ustioni."
    },
    {
        "id": "pot-risvegliante",
        "nome": "Pozione Risvegliante",
        "nomeAlternativo": "Pozione Occhiopallato (Wideye Potion / Awakening Draught)",
        "anno": 3,
        "annoLabel": "III Anno",
        "tipologia": "Curativa / Antidoto Soporifero",
        "coloreFinale": "Blu petrolio",
        "tempoPreparazione": "24 ore",
        "difficolta": "Intermedio",
        "metodoAssunzione": "Poche gocce sulla lingua",
        "ingredienti": [
            "Aconito (2 rametti)",
            "Ingrediente Standard (4 misurini)",
            "Pungiglioni di Billywig essiccati (6)",
            "Zanne di Serpente in scaglie (6)"
        ],
        "preparazione": [
            "1. Scagliare le zanne di serpente con coltellino d'argento e tritarle in mortaio con l'Ingrediente Standard fino a polvere finissima.",
            "2. Essiccare i pungiglioni di Billywig con l'Incantesimo Essiccante e aggiungerne 2 misurini al calderone.",
            "3. Scaldare a fiamma alta per 30 secondi, abbassare e unire 1 litro d'acqua.",
            "4. Aggiungere 4 misurini della polvere di zanne e mescolare 3 volte in senso orario.",
            "5. Dopo 45 minuti spegnere il fuoco e lasciar in infusione per 23 ore (in calderone di peltro).",
            "6. Unire 2 rametti di Aconito (maneggiare con guanti di drago), mescolare 3 volte in senso antiorario, filtrare e imbottigliare."
        ],
        "avvertenze": "Dosi massicce inducono insonnia cronica e lesioni neurologiche.",
        "inventoreOrigine": "Antidoto ufficiale alla Pozione Soporifera.",
        "descrizione": "Previene i colpi di sonno e ridesta all'istante persone cadute in stato comatoso o sonno indotto magicamente."
    },
    {
        "id": "pot-rinvigorante",
        "nome": "Pozione Rinvigorente",
        "nomeAlternativo": "Invigoration Draught",
        "anno": 3,
        "annoLabel": "III Anno",
        "tipologia": "Curativa / Energetica",
        "coloreFinale": "Blu intenso",
        "tempoPreparazione": "2 ore e mezza",
        "difficolta": "Avanzato",
        "metodoAssunzione": "Ingestione",
        "ingredienti": [
            "Acqua di Miele (2 gocce)",
            "Coclearia (2 foglie)",
            "Foglie di Alioto (3)",
            "Infuso di Assenzio (10 cl)",
            "Infuso di Verbena (10 cl)",
            "Levistico (2 foglie)",
            "Menta Piperita (2 foglie)",
            "Mandragola in umido (1)",
            "Pungiglioni di Billywig (1)"
        ],
        "preparazione": [
            "1. Scaldare 10 cl d'Infuso di Assenzio per 5 minuti a fiamma bassa; unire 10 cl d'Infuso di Verbena e mescolare lentamente per 6 volte in senso orario.",
            "2. Portare a bollore per 20 minuti.",
            "3. Essiccare il pungiglione di Billywig e pestarlo in mortaio con 3 foglie di Alioto, unendone 1 misurino al calderone.",
            "4. Mescolare 3 volte in senso antiorario, spegnere e far riposare per 1 ora.",
            "5. Inserire la Mandragola in umido, portare a bollore per 40 minuti, poi aggiungere 2 gocce di Acqua di Miele.",
            "6. Mescolare 10 volte in senso orario, spegnere, filtrare in calderone pulito.",
            "7. Pestare insieme Coclearia, Levistico e Menta piperita, aggiungerne 2 misurini, mescolare 8 volte in senso antiorario e imbottigliare."
        ],
        "avvertenze": "Indossare maschere per non inalare pollini di Alioto durante la lavorazione.",
        "inventoreOrigine": "Composto classico tra i più richiesti nell'infermeria di Hogwarts.",
        "descrizione": "Rigenera l'energia vitale consumata da traumi, prolungata veglia o forte stress fisico e psicologico."
    },
    {
        "id": "pot-idratante",
        "nome": "Pozione Idratante",
        "nomeAlternativo": "Hydration Solution for Nocturnals",
        "anno": 3,
        "annoLabel": "III Anno",
        "tipologia": "Curativa / Reidratante",
        "coloreFinale": "Verde brillante",
        "tempoPreparazione": "2 ore e 30 minuti",
        "difficolta": "Intermedio",
        "metodoAssunzione": "Ingestione (massimo 4 dosi giornaliere)",
        "ingredienti": [
            "Acqua Cristallizzata (200 ml)",
            "Essenza di Dittamo (18 ml)",
            "Foglie di Aloe Vera (3)",
            "Sale Marino purissimo (5 g)"
        ],
        "preparazione": [
            "1. Scaldare il calderone a fuoco alto per 45 secondi, poi versare 200 ml di Acqua cristallizzata.",
            "2. Al bollore spegnere il fuoco e inserire una foglia di Aloe Vera.",
            "3. Mescolare 5 volte in senso orario e 7 volte in senso antiorario.",
            "4. Versare 6 ml di Essenza di Dittamo e mescolare per 12 volte in senso orario.",
            "5. Ripetere i punti 2-3-4 per altre 2 volte raddoppiando e triplicando i giri (5, 10, 15 - 7, 14, 21 - 12, 24, 36).",
            "6. Accendere a fiamma bassa, unire 5g di sale marino, spegnere e lasciar riposare per 2 ore prima di imbottigliare."
        ],
        "avvertenze": "Consente a Vampiri e discendenti dei Maridi di resistere alla luce solare diretta per 12 ore consecutive senza ustioni se assunta un'ora prima dell'esposizione.",
        "inventoreOrigine": "Medimagia dermatologica avanzata.",
        "descrizione": "Rigenera sali minerali e liquidi fisiologici nei tessuti disidratati da ustioni o maledizioni termiche."
    },
    {
        "id": "pot-vista",
        "nome": "Pozione della Vista",
        "nomeAlternativo": "Pozione Oculus (Sight-Restoring Potion)",
        "anno": 3,
        "annoLabel": "III Anno",
        "tipologia": "Curativa / Antidoto Oftalmico",
        "coloreFinale": "Arancione",
        "tempoPreparazione": "25 ore",
        "difficolta": "Avanzato",
        "metodoAssunzione": "Applicazione oftalmica a gocce",
        "ingredienti": [
            "Acqua Cristallizzata (1 litro)",
            "Corno di Unicorno in polvere (1)",
            "Infuso di Assenzio (5 cucchiai)",
            "Mandragola in umido (1)",
            "Pietra di Luna blu (1)"
        ],
        "preparazione": [
            "1. Mettere la Pietra di Luna blu in 1 litro d'acqua cristallizzata in infusione per 24 ore, poi rimuoverla.",
            "2. Aggiungere 3 cucchiai d'Infuso di Assenzio (vira al verde), accendere a fiamma media e mescolare 8 volte in senso antiorario.",
            "3. Macinare il corno di Unicorno in mortaio di granito, aggiungerne 3 misurini (la pozione vira al rosso).",
            "4. Attendere 20 minuti fino al giallo ocra, unire i restanti 2 cucchiai d'Assenzio e mescolare 8 volte in senso orario.",
            "5. Spegnere, far raffreddare, aggiungere la Mandragola in umido e riportare a bollore.",
            "6. Dopo 5 minuti aggiungere altri 2 misurini di corno d'Unicorno, mescolare 6 volte in senso orario fino all'arancione, spegnere e filtrare 3 volte."
        ],
        "avvertenze": "Non può restituire la vista a chi l'ha persa per cause naturali o dalla nascita. Antidoto alla Fattura Conjunctivitis e alla Pozione Granbulbo.",
        "inventoreOrigine": "Trattato classico di Oftalmo-magia.",
        "descrizione": "Restituisce la vista perduta a causa di incantesimi oscuri, infiammazioni magiche o ustioni chimiche."
    },
    {
        "id": "pot-ossofast",
        "nome": "Ossofast",
        "nomeAlternativo": "Skele-Gro (Linfred di Stinchcombe)",
        "anno": 3,
        "annoLabel": "III Anno",
        "tipologia": "Curativa / Rigenerazione Ossea",
        "coloreFinale": "Biancastro fumo denso (sapore disgustoso e rovente)",
        "tempoPreparazione": "26 ore",
        "difficolta": "Avanzato",
        "metodoAssunzione": "Ingestione dolorosa",
        "ingredienti": [
            "Cavolo Carnivoro Cinese (1)",
            "Occhi di Pesce Palla (3)",
            "Osso di braccio umano - ulna (1)",
            "Ragno rosso vivo (1)",
            "Scarabei essiccati e polverizzati (3)",
            "Zanne di Geranio Zannuto (3)"
        ],
        "preparazione": [
            "1. Mettere il Cavolo Carnivoro Cinese in acqua fredda, portare a bollore a fuoco basso mescolando 8 volte in senso antiorario.",
            "2. Lasciare in infusione per 24 ore a fuoco spento.",
            "3. Inserire l'osso di braccio nel calderone; dopo un'ora aggiungere una dopo l'altra le 3 zanne di Geranio Zannuto.",
            "4. Accendere a fiamma altissima mescolando per 12 volte in senso orario.",
            "5. Essiccare 3 scarabei per 3 volte, polverizzarli e spremerne gli occhi di pesce palla nel calderone; mescolare 12 volte in senso antiorario.",
            "6. Aggiungere il ragno rosso vivo, mescolare 12 volte in senso orario, spegnere e richiamare a sé l'osso con un incanto d'appello (*Accio*). Imbottigliare."
        ],
        "avvertenze": "Provoca un bruciore lacerante alla gola e dolori lancinanti durante la ricrescita scheletrica (si consiglia l'assunzione preliminare di Pozione Soporifera).",
        "inventoreOrigine": "Inventata nel XII secolo dal capostipite dei Potter, Linfred di Stinchcombe.",
        "descrizione": "Fa ricrescere da zero ossa interamente rimosse da incantesimi (come l'*Evanesco* scheletrico di Gilderoy Allock) e salda fratture scomposte in una sola notte."
    },
    {
        "id": "pot-bevanda-pace",
        "nome": "Bevanda della Pace",
        "nomeAlternativo": "Distillato della Pace (Draught of Peace)",
        "anno": 3,
        "annoLabel": "III Anno",
        "tipologia": "Curativa / Sedativo Neurologico",
        "coloreFinale": "Perlaceo con emissione di vapore argenteo (leggermente densa)",
        "tempoPreparazione": "40 minuti",
        "difficolta": "Avanzato (esami G.U.F.O.)",
        "metodoAssunzione": "Ingestione",
        "ingredienti": [
            "Aculei di Porcospino (4)",
            "Corno di Unicorno in polvere (3 misurini)",
            "Pietra di Luna in polvere (3 misurini)",
            "Radici di Valeriana (2)",
            "Sciroppo di Elleboro (2 gocce)"
        ],
        "preparazione": [
            "1. Riempire il calderone con 1 litro d'acqua, unire radici di valeriana e corno di unicorno in polvere.",
            "2. Portare a bollore a fiamma bassissima fino a color viola scurissimo.",
            "3. Attendere 10 minuti e aggiungere 2 misurini di Pietra di Luna, mescolando 7 volte in senso antiorario finché diventa rossa.",
            "4. Unire l'ultimo misurino di Pietra di Luna e far sobbollire esattamente per 7 minuti.",
            "5. Unire con contagocce 2 gocce di Sciroppo di Elleboro, spegnere e lasciar raffreddare (deve emettere fumi argentei).",
            "6. Dopo 15 minuti aggiungere a fuoco spento gli aculei di porcospino uno alla volta, mescolare 3 volte in senso antiorario molto lentamente e imbottigliare."
        ],
        "avvertenze": "Invertire l'ordine o eccedere con l'elleboro induce un sonno profondo e irreversibile.",
        "inventoreOrigine": "Pozione classica per calmare ansia da esame e panico incontrollato.",
        "descrizione": "Placa l'agitazione, l'ansia acuta e il tremore emotivo distendendo l'intero sistema neurologico dell'assuntore."
    },
    # Raccolta Curative III Anno
    {
        "id": "pot-balsamo-radice-amara",
        "nome": "Balsamo Lenitivo di Radice Amara",
        "nomeAlternativo": "Bitter-Root Balm",
        "anno": 3,
        "annoLabel": "III Anno",
        "tipologia": "Curativa / Antidolorifica",
        "coloreFinale": "Pasta bruna densa",
        "tempoPreparazione": "30 minuti",
        "difficolta": "Base",
        "metodoAssunzione": "Applicazione Topica su contusioni",
        "ingredienti": ["Radice Amara pestata", "Grasso vegetale", "Cera d'api magica"],
        "preparazione": ["Pestare a freddo la radice incorporando la cera fusa."],
        "avvertenze": "Solo per uso cutaneo esterno.",
        "inventoreOrigine": "Raccolta di Pozioni Curative (pag. 47).",
        "descrizione": "Pasta lenitiva per assorbire traumi contusivi ed ematomi muscolari."
    },
    {
        "id": "pot-cura-vaiolo-drago",
        "nome": "Cura al Vaiolo di Drago",
        "nomeAlternativo": "Dragon Pox Cure (Gunhilda di Gorsemoore)",
        "anno": 3,
        "annoLabel": "III Anno",
        "tipologia": "Curativa / Epidemica",
        "coloreFinale": "Violaceo scuro",
        "tempoPreparazione": "4 ore",
        "difficolta": "Avanzato",
        "metodoAssunzione": "Ingestione e frizione cutanea",
        "ingredienti": ["Fegato di drago", "Ali di pipistrello", "Polvere di scarabeo", "Infuso di menta"],
        "preparazione": ["Decotto a fuoco alto filtrato ripetutamente."],
        "avvertenze": "Salvò il mondo magico da una terribile epidemia nel XIV secolo.",
        "inventoreOrigine": "Creata dalla celebre guaritrice Gunhilda di Gorsemoore.",
        "descrizione": "Eradica il batterio magico del Vaiolo di Drago arrestando l'eruzione cutanea verdastra e le febbri mortali."
    },
    {
        "id": "pot-essenza-purvincolo",
        "nome": "Essenza di Purvincolo",
        "nomeAlternativo": "Murtlap Essence",
        "anno": 3,
        "annoLabel": "III Anno",
        "tipologia": "Curativa / Lenitiva",
        "coloreFinale": "Giallo chiaro traslucido",
        "tempoPreparazione": "45 minuti",
        "difficolta": "Intermedio",
        "metodoAssunzione": "Applicazione Topica o immersione",
        "ingredienti": ["Tentacoli di Purvincolo filtrati e in salamoia", "Acqua distillata"],
        "preparazione": ["Lavorazione a freddo dei tentacoli marinati in salamoia magica."],
        "avvertenze": "Più economica e commerciale dell'Essenza di Dittamo.",
        "inventoreOrigine": "Filtro popolare per ferite e torture (usata da Hermione per la mano di Harry punito dalla Umbridge).",
        "descrizione": "Lenisce istantaneamente tagli, bruciature e ferite da taglio aperte con un benefico senso di freschezza."
    },
    {
        "id": "pot-infuso-mandragola",
        "nome": "Infuso di Mandragola",
        "nomeAlternativo": "Mandragora Leaf Infusion",
        "anno": 3,
        "annoLabel": "III Anno",
        "tipologia": "Curativa / Antidoto Topico",
        "coloreFinale": "Verde pallido",
        "tempoPreparazione": "2 ore",
        "difficolta": "Intermedio",
        "metodoAssunzione": "Applicazione a gocce su scottature chimiche",
        "ingredienti": ["Foglie tenere di Mandragola", "Acqua di sorgente"],
        "preparazione": ["Infusione a bassa temperatura delle sole foglie."],
        "avvertenze": "Il miglior rimedio per contrastare l'eccesso tossico di Essenza di Dittamo.",
        "inventoreOrigine": "Medimagia delle ustioni.",
        "descrizione": "Risana ustioni da caustici magici e ripristina la naturale rigenerazione dell'epidermide."
    },
    {
        "id": "pot-cancellalividi",
        "nome": "Pasta Cancellalividi",
        "nomeAlternativo": "Bruise-Removal Paste (Fred & George Weasley)",
        "anno": 3,
        "annoLabel": "III Anno",
        "tipologia": "Curativa / Cosmetica",
        "coloreFinale": "Densa pasta giallognola",
        "tempoPreparazione": "30 minuti",
        "difficolta": "Intermedio",
        "metodoAssunzione": "Applicazione Topica",
        "ingredienti": ["Pus di Bubotubero diluito", "Gomas Barbadensis", "Tintura di arnica"],
        "preparazione": ["Miscelazione ad alta velocità fino a consistenza burrosa."],
        "avvertenze": "Garantisce la sparizione completa di ematomi e occhi neri entro 60 minuti esatti.",
        "inventoreOrigine": "Creata dai gemelli Fred e George Weasley per i Tiri Vispi Weasley.",
        "descrizione": "Fa riassorbire qualsiasi ecchimosi, trauma periorbitale o livido in un'ora netta."
    },
    {
        "id": "pot-argento-dittamo",
        "nome": "Polvere d'Argento e Dittamo",
        "nomeAlternativo": "Silver & Dittany Paste for Werewolf Wounds",
        "anno": 3,
        "annoLabel": "III Anno",
        "tipologia": "Curativa / Anti-Maledizione",
        "coloreFinale": "Pasta grigio-argentea fumante",
        "tempoPreparazione": "15 minuti",
        "difficolta": "Avanzato",
        "metodoAssunzione": "Cauterizzazione topica diretta su morsi",
        "ingredienti": ["Argento puro in polvere (1 parte)", "Essenza di Dittamo concentrata (3 parti)"],
        "preparazione": ["Unire i due reagenti a freddo e applicare immediatamente sulla lesione."],
        "avvertenze": "Applicazione estremamente dolorosa e bruciante a causa dell'infiammabilità del dittamo e della causticità dell'argento.",
        "inventoreOrigine": "Protocollo d'emergenza del San Mungo per le vittime di morsi di Licantropo.",
        "descrizione": "La sola formula in grado di sigillare e rimarginare le lacerazioni provocate dai morsi dei lupi mannari, arrestando l'emorragia letale."
    },
    {
        "id": "pot-pomata-antiscottature",
        "nome": "Pomata Antiscottature",
        "nomeAlternativo": "Burn-Healing Paste",
        "anno": 3,
        "annoLabel": "III Anno",
        "tipologia": "Curativa / Primo Soccorso",
        "coloreFinale": "Arancione densa",
        "tempoPreparazione": "25 minuti",
        "difficolta": "Base",
        "metodoAssunzione": "Applicazione Topica",
        "ingredienti": ["Radici di consolida magica", "Cera d'api", "Olio di ricino"],
        "preparazione": ["Fondere gli unguenti a bagnomaria e lasciar solidificare."],
        "avvertenze": "Completamente inefficace su ustioni generate da Magia Oscura pura.",
        "inventoreOrigine": "Kit ufficiale di pronto soccorso di Hogwarts.",
        "descrizione": "Tratta all'istante scottature provocate da fuoco, calderoni surriscaldati o getti di vapore."
    },
    {
        "id": "pot-pomata-bundimun",
        "nome": "Pomata di Bundimun",
        "nomeAlternativo": "Bundimun Anti-Dandruff Ointment",
        "anno": 3,
        "annoLabel": "III Anno",
        "tipologia": "Curativa / Dermatologica",
        "coloreFinale": "Verde muschio denso",
        "tempoPreparazione": "30 minuti",
        "difficolta": "Intermedio",
        "metodoAssunzione": "Applicazione sul cuoio capelluto",
        "ingredienti": ["Secrezione di Bundimun opportunamente diluita", "Olio di mandorle magiche"],
        "preparazione": ["Diluire la secrezione all'1% in solvente oleoso."],
        "avvertenze": "Se non diluita correttamente risulta fortemente urticante.",
        "inventoreOrigine": "Raccolta di Pozioni Curative (pag. 47).",
        "descrizione": "Eradica desquamazioni e forfora ostinata grazie all'azione cheratolitica del secreto di Bundimun."
    },
    {
        "id": "pot-calmante",
        "nome": "Pozione Calmante",
        "nomeAlternativo": "Calming Draught",
        "anno": 3,
        "annoLabel": "III Anno",
        "tipologia": "Curativa / Emotiva",
        "coloreFinale": "Azzurro cielo",
        "tempoPreparazione": "35 minuti",
        "difficolta": "Intermedio",
        "metodoAssunzione": "Ingestione",
        "ingredienti": ["Cuore di coccodrillo", "Lavanda essiccata", "Olio di menta piperita"],
        "preparazione": ["Bollire lentamente la lavanda unendo il cuore pestato e la menta."],
        "avvertenze": "A differenza della Bevanda della Pace non dà assuefazione, ma non può assolutamente essere usata su animali o creature.",
        "inventoreOrigine": "Pronto soccorso ospedaliero per shock traumatici.",
        "descrizione": "Rasserena persone sotto choc acuto, traumi emotivi violenti o isteria incontrollata."
    },
    {
        "id": "pot-cura-ferite",
        "nome": "Pozione Cura-Ferite",
        "nomeAlternativo": "Wound-Cleaning Potion (Mungo Bonham)",
        "anno": 3,
        "annoLabel": "III Anno",
        "tipologia": "Curativa / Antisettico",
        "coloreFinale": "Liquido violaceo che emette fumo grigiastro",
        "tempoPreparazione": "30 minuti",
        "difficolta": "Intermedio",
        "metodoAssunzione": "Detersione topica diretta",
        "ingredienti": ["Sale marino", "Tintura di timo", "Succo di Horklump"],
        "preparazione": ["Decotto concentrato ad azione purificante."],
        "avvertenze": "Brucia intensamente a contatto con la carne viva.",
        "inventoreOrigine": "Inventata dal leggendario guaritore Mungo Bonham.",
        "descrizione": "Disinfetta a fondo ferite lacere da caduta o sortilegi leggeri scongiurando infezioni batteriche o necrosi."
    },
    {
        "id": "pot-sonno-senza-sogni",
        "nome": "Pozione del Sonno senza Sogni",
        "nomeAlternativo": "Sleeping Draught (Dreamless Sleep)",
        "anno": 3,
        "annoLabel": "III Anno",
        "tipologia": "Curativa / Sonno Puro",
        "coloreFinale": "Viola scuro profondo",
        "tempoPreparazione": "50 minuti",
        "difficolta": "Intermedio / Avanzato",
        "metodoAssunzione": "Ingestione prima di coricarsi",
        "ingredienti": ["Radice di Valeriana", "Polvere di Asfodelo", "Fiori di lavanda"],
        "preparazione": ["Infusione a calore dolce e filtrazione accurata."],
        "avvertenze": "Se usata consecutivamente per troppi giorni può indurre dipendenza da sonnolenza cronica.",
        "inventoreOrigine": "Prescrizione classica per degenti traumatizzati dell'infermeria.",
        "descrizione": "Induce un sonno pesante, continuo e totalmente privo di sogni o incubi notturni."
    },
    {
        "id": "pot-ricostituente",
        "nome": "Pozione Ricostituente",
        "nomeAlternativo": "Restorative Potion (Unghie, Denti, Cute)",
        "anno": 3,
        "annoLabel": "III Anno",
        "tipologia": "Curativa / Rigenerante Blanda",
        "coloreFinale": "Bianco latte",
        "tempoPreparazione": "40 minuti",
        "difficolta": "Base",
        "metodoAssunzione": "Ingestione",
        "ingredienti": ["Muco di Vermicolo", "Polvere di guscio d'uovo", "Radice di zenzero"],
        "preparazione": ["Emulsione a fuoco lento."],
        "avvertenze": "Variante meno aggressiva e più blanda dell'Ossofast.",
        "inventoreOrigine": "Medimagia estetica e ricostitutiva.",
        "descrizione": "Ricostruisce denti scheggiati, unghie spezzate e tessuti epidermici danneggiati."
    },
    {
        "id": "pot-tonico-draghi",
        "nome": "Tonico per Draghi",
        "nomeAlternativo": "Dragon Tonic",
        "anno": 3,
        "annoLabel": "III Anno",
        "tipologia": "Veterinaria Magica / Dragologia",
        "coloreFinale": "Rosso rubino fiammeggiante",
        "tempoPreparazione": "2 ore",
        "difficolta": "Avanzato",
        "metodoAssunzione": "Ingestione per draghi (LETALE PER ESSERI UMANI)",
        "ingredienti": [
            "Piume di gufo",
            "Piume di pavone",
            "Rospo viola gigante intero (1)",
            "Verruche essiccate"
        ],
        "preparazione": ["Decotto in calderone rinforzato con costante infusione di calore."],
        "avvertenze": "LETALE PER GLI ESSERI UMANI. Da somministrare esclusivamente a bestie di classe XXXXX.",
        "inventoreOrigine": "Formula creata dai Guardidraghi delle riserve mondiali.",
        "descrizione": "Rigenera forza vitale, vigore e potenza di fuoco nei draghi affetti da torpore o spossatezza."
    },
    {
        "id": "pot-tonico-topi",
        "nome": "Tonico per Topi",
        "nomeAlternativo": "Rat Tonic",
        "anno": 3,
        "annoLabel": "III Anno",
        "tipologia": "Veterinaria Magica",
        "coloreFinale": "Verde chiaro",
        "tempoPreparazione": "20 minuti",
        "difficolta": "Base",
        "metodoAssunzione": "Gocce nel cibo per roditori",
        "ingredienti": ["Coda di topo", "Radice di dente di leone", "Acqua pura"],
        "preparazione": ["Infuso a bagnomaria."],
        "avvertenze": "Se sovradosato può far gonfiare il roditore fino a dimensioni anomale.",
        "inventoreOrigine": "Venduto comunemente al Serraglio Stregato di Diagon Alley.",
        "descrizione": "Restituisce pelo lucido e vigore a topi, criceti e ratti da compagnia anziani o debilitati."
    },
    {
        "id": "pot-unguento-erbastella",
        "nome": "Unguento di Erba Stella",
        "nomeAlternativo": "Star-Grass Salve",
        "anno": 3,
        "annoLabel": "III Anno",
        "tipologia": "Curativa / Cicatrizzante",
        "coloreFinale": "Verdastro brillante",
        "tempoPreparazione": "30 minuti",
        "difficolta": "Base",
        "metodoAssunzione": "Applicazione Topica su piaghe",
        "ingredienti": ["Foglie fresche di Erba Stella", "Olio d'oliva magico"],
        "preparazione": ["Pestaggio a freddo in mortaio d'agata."],
        "avvertenze": "Ottimo rimedio rurale per lesioni superficiali.",
        "inventoreOrigine": "Erboristeria tradizionale.",
        "descrizione": "Lenisce piaghe cutanee, sbucciature ed escoriazioni accelerando la ricrescita epiteliale."
    },
    {
        "id": "pot-unguento-smemorello",
        "nome": "Unguento Smemorello del Dottor Ubby",
        "nomeAlternativo": "Dr Ubbly’s Oblivious Unction",
        "anno": 3,
        "annoLabel": "III Anno",
        "tipologia": "Curativa / Neuro-Protettiva",
        "coloreFinale": "Balsamo azzurrognolo soffice",
        "tempoPreparazione": "45 minuti",
        "difficolta": "Avanzato",
        "metodoAssunzione": "Applicazione Topica sulle tempie e sul cranio",
        "ingredienti": ["Essenza di Dittamo", "Lacrime di Selma", "Polvere di pietra di luna"],
        "preparazione": ["Emulsione a freddo sigillata in contenitori schermati."],
        "avvertenze": "Indispensabile per i dipendenti del Dipartimento dei Misteri.",
        "inventoreOrigine": "Inventato dal Dottor Ubby per i guaritori del San Mungo.",
        "descrizione": "Cura e lenisce le ferite e le ustioni provocate dai tentacoli generati dai pensieri aggressivi dei cervelli viventi della Stanza dei Cervelli."
    }
]



# POZIONI ANNI IV AGGIUNTE:

# POZIONI ANNI IV AGGIUNTE:
pozioni_data.extend([
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
        "ingredienti": [
            "Pianta Tromba d'Angelo distillata",
            "Acqua distillata"
        ],
        "preparazione": [
            "Distillazione alchemica a vapore."
        ],
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
        "ingredienti": [
            "Dogbane asiatica",
            "Solvente alcolico"
        ],
        "preparazione": [
            "Macerazione a caldo."
        ],
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
        "ingredienti": [
            "Foglie e radici di Aconito selvatico"
        ],
        "preparazione": [
            "Estrazione con alambicco a circuito chiuso."
        ],
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
        "ingredienti": [
            "Bacche di Actea",
            "Acqua purificata"
        ],
        "preparazione": [
            "Decotto a fuoco rapido."
        ],
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
        "ingredienti": [
            "Zolfo",
            "Radici di assenzio",
            "Foglie di starnutaria"
        ],
        "preparazione": [
            "Sublimazione a calore."
        ],
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
        "ingredienti": [
            "Tentacula Velenosa (semi)",
            "Spine di Pesce Leone"
        ],
        "preparazione": [
            "Macerazione a freddo."
        ],
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
        "ingredienti": [
            "Sciroppo d'Arnica concentrato",
            "Piume di Jobberknoll tritate"
        ],
        "preparazione": [
            "Infusione in soluzione satura."
        ],
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
        "ingredienti": [
            "Sciroppo di Elleboro",
            "Pietra di Luna in polvere"
        ],
        "preparazione": [
            "Sospensione colloidale a caldo."
        ],
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
        "ingredienti": [
            "Sale minerale africano",
            "Cenere di quercia",
            "Succo di Horklump"
        ],
        "preparazione": [
            "Emulsione a freddo."
        ],
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
        "ingredienti": [
            "Rizoma di Sanguinaria essiccato",
            "Alcol purissimo"
        ],
        "preparazione": [
            "Estrazione idroalcolica lenta."
        ],
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
        "ingredienti": [
            "Bacche di Semi di Luna (Moonseed)"
        ],
        "preparazione": [
            "Pestaggio a freddo in mortaio d'agata."
        ],
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
        "ingredienti": [
            "Fosforo magico",
            "Resine velenose",
            "Tasso"
        ],
        "preparazione": [
            "Combustione controllata a vaso chiuso."
        ],
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
        "ingredienti": [
            "Miscela di dieci differenti tipologie di veleno a dosaggio sub-letale"
        ],
        "preparazione": [
            "Composizione complessa bilanciata."
        ],
        "avvertenze": "Facilmente scambiabile per un filtro d'amore; provoca emicrania atroce e confusione.",
        "inventoreOrigine": "Raccolta di Veleni (pag. 60).",
        "descrizione": "Preparato ingannevole che mima l'aspetto di una pozione amorosa scatenando invece un violento collasso cognitivo."
    },
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
        "ingredienti": [
            "Infuso di menta piperita",
            "Radici di cicoria",
            "Sale minerale"
        ],
        "preparazione": [
            "Decotto a fuoco vivo."
        ],
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
        "ingredienti": [
            "Pungiglione essiccato di Billywig (lo stesso elemento che causa il sintomo)",
            "Acqua distillata"
        ],
        "preparazione": [
            "Omeopatia alchemica a base del medesimo catalizzatore."
        ],
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
        "ingredienti": [
            "Foglie di alchemilla",
            "Miele magico",
            "Acqua di rose"
        ],
        "preparazione": [
            "Emulsione lenitiva a freddo."
        ],
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
        "ingredienti": [
            "Radici di ginseng magico",
            "Bile di vipera",
            "Corno di unicorno polverizzato"
        ],
        "preparazione": [
            "Decotto concentrato."
        ],
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
        "ingredienti": [
            "Polvere d'oro alchemico",
            "Sangue di fenice",
            "Dittamo distillato"
        ],
        "preparazione": [
            "Fonderia alchemica combinata con incanti curativi ad alta voce."
        ],
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
        "ingredienti": [
            "Composta da più di 20 ingredienti naturali ed animali calibrati"
        ],
        "preparazione": [
            "Composizione multi-fase a bagnomaria."
        ],
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
        "ingredienti": [
            "Radici di mandragola",
            "Carne di drago marinata",
            "Assenzio"
        ],
        "preparazione": [
            "Distillazione lenta a vaso chiuso."
        ],
        "avvertenze": "L'inventore perse diversi arti durante i collaudi con megere volontarie.",
        "inventoreOrigine": "Creata a metà degli anni '90 dal professor Regulus Moonshine.",
        "descrizione": "Inibisce il costante e primordiale appetito delle Megere di cibarsi di carne umana."
    }
])

# POZIONI ANNI V, VI, VII AGGIUNTE:
pozioni_data.extend([
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
        "ingredienti": [
            "Liscivia magica",
            "Muffa di palude",
            "Essenza di fungo"
        ],
        "preparazione": [
            "Miscelazione a freddo."
        ],
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
        "ingredienti": [
            "Resina di frassino",
            "Polvere d'argento",
            "Corteccia di salice"
        ],
        "preparazione": [
            "Fonderia a caldo e stesura a pennello."
        ],
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
        "ingredienti": [
            "Polvere d'argento",
            "Pigmenti colorati",
            "Polvere pirica magica"
        ],
        "preparazione": [
            "Imbottigliamento sotto pressione controllata."
        ],
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
        "ingredienti": [
            "Nitrato d'argento magico",
            "Essenza di crisopa",
            "Acqua distillata"
        ],
        "preparazione": [
            "Diluzione chimica in camera oscura."
        ],
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
        "ingredienti": [
            "Secrezione di Bundimun purificata",
            "Soda magica",
            "Succo di limone fatato"
        ],
        "preparazione": [
            "Miscela concentrata ad azione solvente."
        ],
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
        "ingredienti": [
            "Polvere di pietra pomice magica",
            "Olio di lino",
            "Cera protettiva"
        ],
        "preparazione": [
            "Emulsione lucidante a freddo."
        ],
        "avvertenze": "Non intacca la finitura magica degli alambicchi.",
        "inventoreOrigine": "Manutenzione argenteria magica.",
        "descrizione": "Lucidante eccezionale che rimuove ogni ossidazione donando splendore perenne a calderoni e calici d'argento."
    },
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
        "preparazione": [
            "Procedura vietata dalle leggi magiche."
        ],
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
        "ingredienti": [
            "Polvere di perle",
            "Essenza di fragola magica",
            "Rugiada mattutina"
        ],
        "preparazione": [
            "Infuso effervescente con perle micro-polverizzate."
        ],
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
        "ingredienti": [
            "Zucchero magico vanigliato",
            "Petali di rosa essiccati",
            "Essenza di cacao fatato"
        ],
        "preparazione": [
            "Cristallizzazione a freddo da sciogliere in acqua calda."
        ],
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
        "ingredienti": [
            "Melassa di Glumbumble",
            "Lacrime di coccodrillo",
            "Acqua distillata"
        ],
        "preparazione": [
            "Decotto a fuoco lento."
        ],
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
        "ingredienti": [
            "Polvere di perle",
            "Zucchero filato fatato",
            "Essenza di menta piperita"
        ],
        "preparazione": [
            "Emulsione idroalcolica dolce."
        ],
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
        "ingredienti": [
            "Acqua di luna",
            "Essenza floreale di gelsomino notturno",
            "Alcol alchemico"
        ],
        "preparazione": [
            "Distillazione cosmetica profumata."
        ],
        "avvertenze": "Creata per superare i controlli ministeriali come comune profumo.",
        "inventoreOrigine": "Fred e George Weasley.",
        "descrizione": "Si fonde con la fragranza cutanea della persona generando un'aura di irresistibile fascino per un giorno intero."
    },
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
        "ingredienti": [
            "Lavorazione integrale di ogni singola parte di Mandragole mature",
            "Alcol purissimo"
        ],
        "preparazione": [
            "Fermentazione alcolica calibrata su precise fasi astronomiche."
        ],
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
        "ingredienti": [
            "Base alcolica al 25%",
            "Essenze vegetali speziate",
            "Polvere d'ambra"
        ],
        "preparazione": [
            "Infusione idroalcolica profumata."
        ],
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
        "ingredienti": [
            "Base alcolica al 46%",
            "Peperoncini magici concentrati",
            "Semi di fuoco"
        ],
        "preparazione": [
            "Distillazione alcolica ad alta gradazione."
        ],
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
        "preparazione": [
            "Rituale di Magia Oscura pura protetto da Azkaban."
        ],
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
        "preparazione": [
            "Custodita dagli Indicibili del Dipartimento dei Misteri americano."
        ],
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
    },
    {
        "id": "pot-elisir-indomito",
        "nome": "Elisir dell'Indomito",
        "nomeAlternativo": "Juggernaut Alchemico / Furia del Graphorn",
        "anno": 0,
        "annoLabel": "Altri",
        "tipologia": "Alteratrice di Stato / Potenziamento / Resistenza Fisica Estrema",
        "coloreFinale": "Grigio-violaceo denso, con l'aspetto della pietra di montagna bagnata",
        "tempoPreparazione": "Circa 13-14 ore (sobbollitura 45 min + riposo 12 ore)",
        "difficolta": "Altamente avanzata e intrinsecamente instabile",
        "metodoAssunzione": "Ingestione (in fiale di vetro spesso)",
        "ingredienti": [
                "Acqua di Sorgente Montana",
                "Dente di Graphorn (1 intero)",
                "Fiele di Armadillo (1 oncia)",
                "Radice di Zenzero",
                "Succo di Fire Crab (2 once)",
                "Sangue di Re'em (3 gocce)",
                "Essenza di Dittamo (3 misurini)",
                "Barra di ferro freddo (per la sigillatura fisica finale)"
        ],
        "preparazione": [
                "1. Versare nel calderone l'Acqua di Sorgente Montana e l'oncia di fiele di Armadillo, portando a un'ebollizione lenta e costante.",
                "2. Avvolgere saldamente il dente di Graphorn in un panno di pelle di drago.",
                "3. Frantumare il dente colpendolo con un pesante martello di ferro fino a ridurlo in schegge irregolari e appuntite (non polverizzare).",
                "4. Aggiungere le schegge nel calderone; il liquido inizierà a sibilare violentemente e virerà su un colore grigio chiaro.",
                "5. Affettare la radice di zenzero a colpi netti e decisi con un coltello, per poi aggiungerla al composto.",
                "6. Versare le 2 once di succo di Fire Crab; il composto sfrigolerà emettendo scintille rosse e fumo scuro, mentre la temperatura salirà drasticamente.",
                "7. Mescolare 7 volte in senso orario con un mestolo di legno robusto (il metallo verrebbe corroso dall'acidità in questa fase).",
                "8. Lasciare sobbollire per 45 minuti, prestando attenzione agli schizzi bollenti, finché le schegge non iniziano a consumarsi e il liquido assume un colore ruggine scuro.",
                "9. Aggiungere le 3 gocce di sangue di Re'em, rigorosamente una alla volta, aspettando che il calderone smetta di tremare dopo ogni singola goccia.",
                "10. Mescolare 5 volte in senso antiorario; la pozione assumerà una consistenza densa e fragorosa.",
                "11. Versare i 3 misurini di Essenza di Dittamo per bloccare la reazione caustica interna; la pozione smetterà istantaneamente di fumare e si raffredderà di scatto.",
                "12. Attendere 12 ore, finché il liquido non diventerà di un denso grigio-violaceo, simile alla spessa pelle del Graphorn.",
                "13. Immergere una barra di ferro freddo fino al fondo del calderone per esattamente tre secondi per 'domare' e sigillare definitivamente l'instabilità magica con un atto di dominazione fisica sulla materia.",
                "14. Imbottigliare l'elisir in fiale di vetro spesso."
        ],
        "avvertenze": "CRITICO / CROLLO PSICOFISICO: Sotto l'effetto della pozione, il soggetto perde quasi totalmente la capacità di provare empatia o formulare pensieri razionali complessi, agendo in una condizione di 'visione a tunnel' dominata dall'istinto di sopravvivenza (è impossibile lanciare incantesimi che richiedano concentrazione o finezza). Un sovradosaggio o utilizzo prolungato causa danni muscolari irreversibili e lacerazioni interne che il bevitore aggraverebbe inavvertitamente durante lo scontro non avvertendo dolore. Durante la lavorazione a caldo l'acidità estrema e i fumi caustici possono corrodere il metallo o provocare esplosioni violente.",
        "inventoreOrigine": "Pozione inventata nel 2026 da Harvey Specter, nata dallo studio e dalla raffinazione di pratiche magiche rudimentali e oscure utilizzate in passato dai bracconieri del Nord Europa. L'ingrediente focale è il dente di Graphorn recuperato da una collana sottratta a trafficanti, elemento che conserva al suo interno la ferocia predatoria e la memoria del trauma fisico della creatura.",
        "descrizione": "Provoca la soppressione totale del sistema nervoso per quanto riguarda la percezione del dolore, unita a un indurimento dermico temporaneo. Il bevitore diviene capace di ignorare ferite debilitanti e respingere incantesimi minori o fatture di disturbo, trasformando il proprio corpo in un'arma inarrestabile paragonabile al Graphorn. A differenza delle comuni pozioni rinvigorenti (come l'Elisir Rinforzante), sopprime la psiche razionale in favore dell'istinto primordiale della bestia, rendendo il soggetto un vero e proprio 'juggernaut' insensibile a quasi ogni disturbo esterno."
},
    {
        "id": "pot-elisir-solis-igniti",
        "nome": "Elisir Solis Igniti",
        "nomeAlternativo": "Elisir Rigenerativo della Fenice",
        "anno": 0,
        "annoLabel": "Altri",
        "tipologia": "Curativa Suprema / Rigenerazione Mirata & Oftalmica",
        "coloreFinale": "Dorato e cangiante, con riflessi rossi perlacei che ricordano il piumaggio di una fenice",
        "tempoPreparazione": "Circa 45-60 minuti (con decantazione di 30s e sobbollitura finale di 12 min)",
        "difficolta": "Altamente avanzata",
        "metodoAssunzione": "Ingestione / Applicazione mirata in dosaggi micrometrici",
        "ingredienti": [
                "Acqua di Luna filtrata (250 ml)",
                "Corno di Bicorno (1 intero, polverizzato molto finemente)",
                "Essenza di Dittamo (10 ml)",
                "Filtro di Eufrasia (5 gocce)",
                "Moly Essiccati (2 fiori)",
                "Lacrima di Fenice (1 pura)",
                "Radice di Mandragora matura (1, tritata 15g con coltellino d'argento)",
                "Spire di Artemisia (5 g)"
        ],
        "preparazione": [
                "1. Versare nel calderone l'Acqua di Luna filtrata, portandola a ebollizione leggera.",
                "2. Nel mentre, tritare 15g di Radice di Mandragora matura con un coltellino d'argento.",
                "3. Aggiungere l'Essenza di Dittamo, la Radice di Mandragora tritata e i Moly essiccati.",
                "4. Mescolare delicatamente per 7 volte in senso orario, seguito da 1 volta in senso antiorario.",
                "5. Attendere che il fumo emesso assuma una colorazione argentea e un profumo erbaceo e pungente.",
                "6. Polverizzare il Corno di Bicorno finemente, prima ottenendo delle scaglie con coltellino d'argento e successivamente pestandole con mortaio e pestello.",
                "7. Aggiungere 10g della polvere ottenuta nel calderone.",
                "8. Versare le 5 gocce di Filtro di Eufrasia.",
                "9. Mescolare lentamente finché la pozione non assume una consistenza densa e un colore blu indaco.",
                "10. Aggiungere 5g di Spire di Artemisia.",
                "11. Spegnere la fiamma e lasciar decantare per 30 secondi.",
                "12. Introdurre la Lacrima di Fenice direttamente al centro del calderone.",
                "13. Utilizzando un mestolo d'argento puro, eseguire 3 movimenti lenti in senso antiorario.",
                "14. Riaccendere la fiamma al minimo e lasciar sobbollire per esattamente 12 minuti.",
                "15. Imbottigliare l'infuso."
        ],
        "avvertenze": "ESTREMA PUREZZA: Le lacrime di fenice hanno natura pura e incorruttibile. In nessun caso va combinata con ingredienti di origine oscura (come sangue di unicorno prelevato con la forza o veleni sintetici), pena la corruzione della lacrima o esplosioni acide corrosive. L'inserimento del corno di bicorno e del filtro di eufrasia deve avvenire a temperature controllate (se troppo calda al momento dell'inserimento della lacrima, il nucleo magico evapora all'istante in fumo dorato privo di efficacia). Somministrare in dosaggi estremamente precisi: il sovradosaggio causa reazioni gravissime dovute alla straripante energia vitale della fenice. Consigliati calderoni in oro puro, argento o peltro.",
        "inventoreOrigine": "Elisir inventato nel 2026 da Harvey Specter, con l'aiuto del docente di Pozioni Alfred Knight. Ispirato dal caso della Vicepreside Lorraine Muriel Mhara (che riacquisì la vista persa dopo un attentato del Teschio Nero grazie alla lacrima di fenice donatale dalla docente di Divinazione). Specter ricevette una seconda lacrima da Beatrix Manson e scoprì come stabilizzarne il principio attivo attraverso l'azione isolante dei fiori di Moly e sintonizzarlo con l'Eufrasia per renderlo conservabile e fruibile.",
        "descrizione": "Rigeneratore cellulare e magico ad ampio spettro e alta precisione: ricostruisce da zero tessuti cutanei, muscolari ed ossei distrutti da incantesimi offensivi e scioglie i residui magici corrosivi delle maledizioni oscure. Grazie alla sintonizzazione ottica con l'Eufrasia, è in grado di riparare cornee e nervi ottici compromessi da fiamme, acidi o cecità traumatica, restituendo interamente e perfettamente la vista."
},
    {
        "id": "pot-filtro-eufrasia",
        "nome": "Filtro di Eufrasia",
        "nomeAlternativo": "Base Alchemica Oculare / Eyebright Filter",
        "anno": 0,
        "annoLabel": "Altri",
        "tipologia": "Curativa / Base Alchemica Semilavorata / Oftalmica",
        "coloreFinale": "Azzurro cristallino e limpido",
        "tempoPreparazione": "15-20 minuti (sobbollitura 5 min)",
        "difficolta": "Base-Intermedio",
        "metodoAssunzione": "Base semilavorata da combinare in elisir / Gocce oftalmiche diluite",
        "ingredienti": [
                "Acqua sorgiva pura (150 ml)",
                "Fiori freschi di Eufrasia (10)",
                "Pietra di Luna in polvere (1 misurino)",
                "Garza sottile di ortica (per la filtrazione)"
        ],
        "preparazione": [
                "1. Versare l'Acqua sorgiva pura in un piccolo calderone.",
                "2. Riscaldare a fuoco bassissimo fino a raggiungere un'ebollizione appena accennata.",
                "3. Aggiungere i 10 fiori freschi di Eufrasia uno alla volta, tenendoli delicatamente per il gambo.",
                "4. Mescolare lentamente per 3 volte in senso orario.",
                "5. Aggiungere il misurino di polvere di Pietra Lunare.",
                "6. Lasciar sobbollire l'infuso per esattamente 5 minuti (il liquido virerà lentamente verso una tonalità azzurro cristallina).",
                "7. Spegnere la fiamma.",
                "8. Filtrare accuratamente il decotto con una garza sottile di ortica per separare i residui solidi dai fiori.",
                "9. Lasciar raffreddare e conservare il liquido in una fialetta di vetro scuro per proteggerlo dai raggi solari diretti."
        ],
        "avvertenze": "I fiori freschi devono essere raccolti tassativamente alle prime luci dell'alba (quando la rugiada mattutina stabilizza i petali sensibili alla luce del sole). Non superare la temperatura di ebollizione dell'acqua per evitare di scottare i petali e distruggerne la firma magica. L'applicazione diretta e non diluita del filtro puro provoca un forte bruciore temporaneo per via della concentrazione acida dei principi attivi. Nota: è una base alchemica semilavorata che funge da conduttore e 'puntamento' oculare all'interno di pozioni più complesse come l'Elisir Solis Igniti.",
        "inventoreOrigine": "Preparazione curativa ideata nel 2026 da Harvey Specter. L'Eufrasia è nota anche ai Babbani (Eyebright / Casse-lunettes) che le attribuivano proprietà chiaroveggenti e oftalmiche secondo la 'dottrina delle segnature', distorsione della sua reale affinità magica con l'apparato visivo.",
        "descrizione": "Estrae e purifica i principi attivi della pianta di Eufrasia agendo come un catalizzatore di luce, concentrando le proprietà rigeneratrici del fiore per renderle assimilabili in composti alchemici complessi dedicati alla cura della vista e amplificando la ricettività sensoriale dell'apparato oculare."
},
    {
        "id": "pot-somnus",
        "nome": "Pozione Somnus",
        "nomeAlternativo": "Conduttore Onirico Lucido / Amplificatore Psichico",
        "anno": 0,
        "annoLabel": "Altri",
        "tipologia": "Alteratrice di Stato / Psicoattiva / Onirica & Sonno Indotto",
        "coloreFinale": "Blu profondo con riflessi argentei (lievemente viscosa ma fluida, emette vapore sottile argenteo)",
        "tempoPreparazione": "Circa 25 ore (sobbollitura 7 min + riposo di 24 ore)",
        "difficolta": "Avanzata",
        "metodoAssunzione": "Ingestione (in quantità micrometriche sotto stretta supervisione)",
        "ingredienti": [
                "Acqua di Luna",
                "Alihotsy macinato finemente (foglie e spore)",
                "Infuso di Lavanda",
                "Polvere di radice di Asfodelo",
                "Essenza di Valeriana (3 gocce)",
                "Ingrediente Standard (6 misurini)",
                "Muco di Vermicoli (2 gocce)",
                "Polvere di Pietra di Luna (1 misurino)",
                "Capello del soggetto destinatario (1 capello - opzionale ma fortemente consigliato)"
        ],
        "preparazione": [
                "1. Versare nel calderone l'Acqua di Luna, portandola a ebollizione.",
                "2. Versare delicatamente l'infuso di Lavanda.",
                "3. Aggiungere i 6 misurini di Ingrediente Standard, uno alla volta.",
                "4. Mescolare 13 volte in senso orario in modo preciso e determinato.",
                "5. Versare le 3 gocce di essenza di Valeriana.",
                "6. Mescolare 13 volte in senso antiorario; il colore del liquido diverrà viola tenue e uniforme.",
                "7. Pestare la radice di Asfodelo con mortaio e pestello.",
                "8. Aggiungere al composto la polvere ottenuta dalla radice di Asfodelo.",
                "9. Attendere 7 minuti, lasciando sobbollire l'infuso; il composto diventerà di colore viola più profondo con venature grigie.",
                "10. Abbassare la fiamma al minimo.",
                "11. Macinare finemente a pioggia l'Alihotsy, prima con un coltellino d'argento, successivamente con mortaio e pestello in granito.",
                "12. Inserire la polvere ottenuta al composto; la pozione inizierà ad emettere dei lievi vapori e il suo colore virerà sul blu-violaceo.",
                "13. Versare 2 gocce di muco di vermicoli.",
                "14. Spegnere il fuoco e attendere il raffreddamento del composto.",
                "15. Aggiungere il misurino di polvere di Pietra di Luna.",
                "16. Attendere per 24 ore, finché la pozione non diventerà di un blu profondo, con riflessi argentei ed emissione di vapore sottile argenteo.",
                "17. Introdurre il capello della persona che dovrà bere la pozione per sintonizzarne il legame psichico.",
                "18. Concludere categoricamente con l'incantesimo di stabilizzazione mentale Morfèus (per guidare il flusso dei sogni ed evitarne degenerazioni).",
                "19. Imbottigliare l'infuso."
        ],
        "avvertenze": "PERICOLO SOVRACCARICO PSICHICO: Se la lavorazione dell'Alihotsy o le proporzioni degli agenti calmanti sono errate, riemerge l'effetto originario con stati di isteria incontrollata, confusione e sovraccarico mentale. Se la pozione non è tenuta a temperatura costante durante l'infusione, la componente fungina può ribellarsi alterando l'esito. Somministrare in dosi minime: un sovradosaggio può intrappolare il soggetto in uno stato onirico persistente con incapacità di tornare alla piena coscienza. La chiusura con l'incantesimo Morfèus è indispensabile per impedire la degenerazione caotica dei sogni.",
        "inventoreOrigine": "Pozione inventata nel 2026 da Harvey Specter con l'aiuto del docente di Pozioni Alfred Knight. Nata da studi extracurriculari sull'inversione di polarità magica dell'Alihotsy (invertendo le risate isteriche in calma introspettiva profonda tramite agenti calmanti e macinatura fine).",
        "descrizione": "Non induce semplicemente il sonno, ma agisce come un conduttore psichico che amplifica attivamente l'ambiente onirico trasformandolo in uno stato di sogno lucido, vivido e prolungato. La mente del bevitore diviene altamente ricettiva e capace di generare immagini, memorie e narrazioni di straordinaria complessità con lievi riflessi argentei pulsanti."
},
    {
        "id": "pot-zitto-e-lava",
        "nome": "Pozione Zitto-e-lava",
        "nomeAlternativo": "Solvente Alchemico Disincrostante da Serra",
        "anno": 0,
        "annoLabel": "Altri",
        "tipologia": "Per Oggetti / Detersione Estrema / Disincrostante Botanico",
        "coloreFinale": "Verde lime spento e opaco",
        "tempoPreparazione": "20-30 minuti (lavorazione a freddo ed emulsione meccanica con 3 min di riposo)",
        "difficolta": "Intermedio (richiede sangue freddo e massima cautela)",
        "metodoAssunzione": "Uso topico su pavimentazioni in pietra e terracotta (DIVIETO ASSOLUTO DI INGESTIONE)",
        "ingredienti": [
                "Acqua fresca di sorgente o cisterna di serra (10 litri)",
                "Pus puro di Bubotubero appena estratto (300 ml)",
                "Cristalli di sale marino grosso (2 manciate)",
                "Linfa chiarificata di corteccia o Frullobulbo (1 misurino)",
                "Macerato di Timo selvatico (3 gocce)",
                "Frazione di alcool puro distillato (1/2 caraffa - opzionale, per ambienti umidi)"
        ],
        "preparazione": [
                "1. Indossare guanti protettivi in pelle di drago o cuoio spesso prima di approcciare i vegetali.",
                "2. Riempire un capiente secchio di legno o calderone da lavoro con 10 litri d'acqua fresca di sorgente.",
                "3. Raccogliere con cautela i baccelli carnosi di Bubotubero maturi posti nelle aiuole della serra.",
                "4. Con un punteruolo di legno o un coltellino da erbologia, incidere delicatamente le protuberanze bulbose, lasciando defluire il denso pus giallastro in una caraffa graduata.",
                "5. Filtrare con cura il pus attraverso un setaccio di tela fine per eliminare impurità grossolane o pezzetti di corteccia fibrosa.",
                "6. Versare a filo continuo e molto lentamente il pus di Bubotubero nell'acqua, mantenendo il beccuccio della caraffa rasente al bordo interno del recipiente.",
                "7. Impugnare un bastone di legno o il manico di uno spazzolone di saggina pulito.",
                "8. Mescolare 13 volte in senso orario in modo energico e costante per avviare la dispersione delle componenti oleose.",
                "9. Aggiungere le due manciate di cristalli di sale marino grosso per bilanciare la densità del fluido e conferire la componente abrasiva.",
                "10. Aggiungere il misurino di linfa chiarificata di corteccia per fungere da tensioattivo legante.",
                "11. Mescolare 7 volte in senso antiorario; il composto inizierà a perdere l'intensa colorazione gialla originaria.",
                "12. Versare le 3 gocce di macerato di Timo selvatico per smorzare l'odore acre e pungente di idrocarburi esalato dal baccello.",
                "13. Versare delicatamente la mezza caraffa di alcool puro distillato (qualora si desideri l'asciugatura rapida in serre umide).",
                "14. Mescolare energicamente per altri 30 secondi con moto a vortice fino alla comparsa di una leggera schiuma superficiale.",
                "15. Lasciare riposare il composto per 3 minuti: la miscela dovrà apparire perfettamente amalgamata, priva di grumi lipidici separati e con consistenza fluida ma vellutata (colore verde lime spento e opaco).",
                "16. Immergere lo spazzolone di saggina o gli stracci di cuoio nella miscela e distribuire generosamente sulla pavimentazione da detergere.",
                "17. Frizionare energicamente le mattonelle per sciogliere la lordura decennale.",
                "18. Concludere con l'utilizzo dell'incantesimo Tergeo per assorbire istantaneamente i residui melmosi e la pozione esausta, lasciando il pavimento asciutto, igienizzato e splendente.",
                "19. Imbottigliare l'eventuale miscela residua in damigiane di vetro scuro sigillate con ceralacca."
        ],
        "avvertenze": "RISCHIO USTIONI E PIAGHE CHIMICHE: Il pus puro di Bubotubero è caustico e instabile. Indossare obbligatoriamente guanti in pelle di drago o cuoio spesso e maniche rimboccate. È categoricamente vietata qualsiasi forma di ingestione o contatto con la cute nuda. In caso di contatto accidentale con la frazione pura, sciacquare subito con acqua fresca e medicare con pasta di calendula o essenza di Murtlap. Se la soluzione non è lavorata con moto vorticoso costante, la frazione lipidica si separa potendo corrodere setole e indumenti.",
        "inventoreOrigine": "Pozione inventata nel 2026 da Harvey M. Specter durante una punizione collettiva nelle Serre di Hogwarts, per detergere superfici lapidee secolari e pavimentazioni degradate, invertendo la polarità distruttiva del pus di Bubotubero tramite diluizione acquosa a freddo ed emulsione meccanica. Eccellente sinergia catalitica con Tergeo e Scourgify.",
        "descrizione": "Solvente alchemico da contatto che disgrega all'istante muffe parassite, alghe, muschi e residui di terriccio magico stratificati nei decenni su pietra e terracotta, senza intaccare le malte né la porosità della pietra e inibendo la ricomparsa di colonie fungine. A differenza dei comuni detergenti domestici (come il Detergente della Signora Scower), agisce come un aggressivo presidio sgrassante e disincrostante di grado botanico."
}
])
print(f"Totale Pozioni caricate nel compendio finale: {len(pozioni_data)}")
