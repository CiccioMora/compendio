# -*- coding: utf-8 -*-
"""
Script per aggiungere le 5 nuove pozioni nella sezione 'Altri' (anno: 0, annoLabel: 'Altri')
al compendio di Pozioni (data_pozioni.py).
Pozioni da aggiungere:
1. Elisir dell'Indomito (Harvey Specter, 2026)
2. Elisir Solis Igniti (Harvey Specter, Alfred Knight, 2026)
3. Filtro di Eufrasia (Harvey Specter, 2026)
4. Pozione Somnus (Harvey Specter, Alfred Knight, 2026)
5. Pozione Zitto-e-lava (Harvey M. Specter, 2026)
"""

import os, re

POZIONI_ALVEARE = [
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
]

# 1. Aggiorna data_pozioni.py
with open('scripts/data_pozioni.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Verifica se sono già presenti
for pot in POZIONI_ALVEARE:
    if pot['id'] in content:
        print(f"Pozione {pot['id']} già presente in data_pozioni.py, skipping...")
    else:
        # Trova la fine della lista pozioni_data
        pos = content.rfind(']')
        if pos != -1:
            import json
            pot_code = json.dumps(pot, ensure_ascii=False, indent=8)
            # rimuovi parentesi quadra finale e aggiungi la pozione
            prefix = content[:pos].rstrip()
            if not prefix.endswith(','):
                prefix += ','
            content = prefix + '\n' + ' ' * 4 + pot_code + '\n' + content[pos:]
            print(f"Aggiunta pozione {pot['nome']} a data_pozioni.py")

with open('scripts/data_pozioni.py', 'w', encoding='utf-8') as f:
    f.write(content)

print("data_pozioni.py aggiornato con successo!")
