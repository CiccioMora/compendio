# -*- coding: utf-8 -*-
"""
integrate_runes_database.py
1. Crea le 25 voci di Antiche Rune (24 Futhark + Runa Bianca) con posizione, valenza, domini, SVG.
2. Associa a ciascun incantesimo di spellsData.js le rune corrispondenti alla sua valenza:
   "la valenza dell'incantesimo corrisponde alla posizione della runa nell'alfabeto runico"
3. Aggiunge le 25 rune a spellsData.js (anno: 8, annoLabel: "Antiche Rune").
4. Aggiorna app.js con la ricerca estesa alle rune e visualizzazione nel modale e calcolatore.
5. Aggiorna index.html, dist/portale_standalone.html e gli artefatti.
"""

import json
import re

BASE_DIR = '/Users/andreamorachioli/.gemini/antigravity/scratch/portale-incantesimi'
ARTIFACT_DIR = '/Users/andreamorachioli/.gemini/antigravity/brain/3a4f7fa7-8206-4f51-b303-aa9b9d9eaf5c'

# Definizione delle corrispondenze di valenza per le rune (Valenza 1..9)
VALENCE_TO_RUNES = {
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

# 24 Rune dell'Antico Futhark + 1 Runa Bianca
RUNES_CATALOG = [
    {
        "id": "runa-fehu",
        "nome": "Runa Fehu (ᚠ)",
        "formula": "ᚠ Fehu",
        "posizioneAlfabeto": "1ª",
        "posizioneNum": 1,
        "aett": "1° Aett (Urd)",
        "thootPos": "1ª Posizione (con Hagalaz e Teiwaz)",
        "valenza": 1,
        "sommaLettere": 1,
        "valenzaOpposta": 9,
        "figuraGeometrica": "Circonferenza (Unità / Origine / Acqua)",
        "pietraConsacrata": "Topazio / Luce",
        "movimento": "Incisione lineare verso l'alto con due aste oblique ascendenti a destra. Tracciabile su materia con Sìgno o nell'etere con Persìgno.",
        "movimentoSvg": "M 50,125 L 50,25 M 50,55 L 95,30 M 50,85 L 90,60",
        "descrizione": "1ª Runa dell'Alfabeto Runico (1° Aett di Urd). Posizione alfabetica: 1. Dominio: Inizio, creazione ex-nihilo, energia vitale cosmica, lavoro, ricchezza mobile, spirito primigenio. Corrispondenza di Canone: la valenza dell'incantesimo corrisponde alla posizione della runa nell'alfabeto runico (Posizione 1 = Valenza 1).",
        "etimologia": "Dal proto-germanico *fehu (bestiame, ricchezza, energia creatrice del cosmo).",
        "incantesimiEsempio": "Incendio (1), Reparo (1), Signo (1), Coerceo (1), Colligo (1)"
    },
    {
        "id": "runa-uruz",
        "nome": "Runa Uruz (ᚢ)",
        "formula": "ᚢ Uruz",
        "posizioneAlfabeto": "2ª",
        "posizioneNum": 2,
        "aett": "1° Aett (Urd)",
        "thootPos": "2ª Posizione (con Nauthiz e Berkana)",
        "valenza": 2,
        "sommaLettere": 2,
        "valenzaOpposta": 8,
        "figuraGeometrica": "Angolo / Linea (Dualismo / Forza)",
        "pietraConsacrata": "Ambra / Quarzo",
        "movimento": "Asta verticale sinistra scendente, fendente obliquo a destra e seconda asta verticale scendente più breve.",
        "movimentoSvg": "M 50,25 L 50,125 M 50,25 L 95,50 L 95,125",
        "descrizione": "2ª Runa dell'Alfabeto Runico (1° Aett di Urd). Posizione alfabetica: 2. Dominio: Incremento, potenza primordiale del toro (uro), salute, vigore muscolare, accrescimento strutturale, tenacia. Corrispondenza di Canone: Posizione 2 = Valenza 2.",
        "etimologia": "Dal proto-germanico *ūruz (uro, toro primordiale selvaggio, forza tellurica).",
        "incantesimiEsempio": "Expelliarmus (2), Innerva (2), Fumos (2), Riddikulus (2)"
    },
    {
        "id": "runa-thurisaz",
        "nome": "Runa Thurisaz (ᚦ)",
        "formula": "ᚦ Thurisaz",
        "posizioneAlfabeto": "3ª",
        "posizioneNum": 3,
        "aett": "1° Aett (Urd)",
        "thootPos": "3ª Posizione (con Isa ed Ehwaz)",
        "valenza": 3,
        "sommaLettere": 3,
        "valenzaOpposta": 7,
        "figuraGeometrica": "Triangolo equilatero (Caos / Spina)",
        "pietraConsacrata": "Agata / Ossidiana",
        "movimento": "Asta verticale centrale con spina triangolare acuta protesa verso destra a metà altezza.",
        "movimentoSvg": "M 50,25 L 50,125 M 50,50 L 95,75 L 50,100",
        "descrizione": "3ª Runa dell'Alfabeto Runico (1° Aett di Urd). Posizione alfabetica: 3. Dominio: Spina, dolore lacerante, caos, abbattimento di ostacoli, follia difensiva, liberazione violenta. Corrispondenza di Canone: Posizione 3 = Valenza 3.",
        "etimologia": "Dal proto-germanico *þurisaz (gigante di ghiaccio, spina acuta).",
        "incantesimiEsempio": "Arresto Momentum (3), Orchideus (3), Incipio (3), Iungo (3)"
    },
    {
        "id": "runa-ansuz",
        "nome": "Runa Ansuz (ᚨ)",
        "formula": "ᚨ Ansuz",
        "posizioneAlfabeto": "4ª",
        "posizioneNum": 4,
        "aett": "1° Aett (Urd)",
        "thootPos": "4ª Posizione (con Jera e Mannaz)",
        "valenza": 4,
        "sommaLettere": 4,
        "valenzaOpposta": 6,
        "figuraGeometrica": "Quadrato (Risoluzione / Immanenza)",
        "pietraConsacrata": "Opale / Aria",
        "movimento": "Asta verticale principale con due segmenti obliqui discendenti sul lato destro.",
        "movimentoSvg": "M 50,25 L 50,125 M 50,45 L 95,70 M 50,75 L 95,100",
        "descrizione": "4ª Runa dell'Alfabeto Runico (1° Aett di Urd). Posizione alfabetica: 4. Dominio: La bocca, il verbo sacro, la parola incantata, la formula vocale, l'ordine cosmico, la saggezza di Odino. Corrispondenza di Canone: Posizione 4 = Valenza 4.",
        "etimologia": "Dal proto-germanico *ansuz (divinità Asir, soffio vitale, verbo sacro).",
        "incantesimiEsempio": "Liberacorpus (4), Diffindo (4), Persigno (4), Stigma Exsequor (4)"
    },
    {
        "id": "runa-raido",
        "nome": "Runa Raido (ᚱ)",
        "formula": "ᚱ Raido",
        "posizioneAlfabeto": "5ª",
        "posizioneNum": 5,
        "aett": "1° Aett (Urd)",
        "thootPos": "5ª Posizione (con Eihwaz e Laguz)",
        "valenza": 5,
        "sommaLettere": 5,
        "valenzaOpposta": 5,
        "figuraGeometrica": "Pentagono regolare (Moto Perpetuo / Aria)",
        "pietraConsacrata": "Azzurrite / Etere",
        "movimento": "Asta verticale, ansa superiore ad angolo e zampa diagonale discendente a destra.",
        "movimentoSvg": "M 50,25 L 50,125 M 50,25 L 90,50 L 50,75 M 50,75 L 95,125",
        "descrizione": "5ª Runa dell'Alfabeto Runico (1° Aett di Urd). Posizione alfabetica: 5. Dominio: La ruota, il viaggio, il sentiero, la cinetica, il messaggio, il ciclo senza fine dello spazio. Runa speculare autonoma su valenza 5. Corrispondenza di Canone: Posizione 5 = Valenza 5.",
        "etimologia": "Dal proto-germanico *raidō (cavalcata, ruota del carro, viaggio).",
        "incantesimiEsempio": "Levicorpus (5), Immobilus (5), Finge (5), Deleo (5), Dominium Evoco (5)"
    },
    {
        "id": "runa-kenaz",
        "nome": "Runa Kenaz (ᚲ)",
        "formula": "ᚲ Kenaz",
        "posizioneAlfabeto": "6ª",
        "posizioneNum": 6,
        "aett": "1° Aett (Urd)",
        "thootPos": "6ª Posizione (con Perthr e Inguz)",
        "valenza": 6,
        "sommaLettere": 6,
        "valenzaOpposta": 4,
        "figuraGeometrica": "Esagono regolare (Equilibrio / Armonia)",
        "pietraConsacrata": "Agata / Molibdenite",
        "movimento": "Cuspide angolare aperta verso destra (fendente discendente poi ascendente).",
        "movimentoSvg": "M 95,35 L 50,75 L 95,115",
        "descrizione": "6ª Runa dell'Alfabeto Runico (1° Aett di Urd). Posizione alfabetica: 6. Dominio: Fiaccola viva, fiamma controllata di purificazione, guarigione delle ferite, ristoro spirituale, luce rivelatrice. Corrispondenza di Canone: Posizione 6 = Valenza 6.",
        "etimologia": "Dal proto-germanico *kaunan (torcia, fiaccola, calore benefico).",
        "incantesimiEsempio": "Protego (6), Verdimillious (6), Adultero (6), Surge et expandi (6)"
    },
    {
        "id": "runa-gebo",
        "nome": "Runa Gebo (ᚷ)",
        "formula": "ᚷ Gebo",
        "posizioneAlfabeto": "7ª",
        "posizioneNum": 7,
        "aett": "1° Aett (Urd)",
        "thootPos": "7ª Posizione (con Algiz e Othila)",
        "valenza": 7,
        "sommaLettere": 7,
        "valenzaOpposta": 3,
        "figuraGeometrica": "Ettagono regolare (Opposizione / Dono)",
        "pietraConsacrata": "Ambra / Quarzo",
        "movimento": "Croce diagonale perfetta a X (intersezione al centro).",
        "movimentoSvg": "M 40,30 L 110,120 M 110,30 L 40,120",
        "descrizione": "7ª Runa dell'Alfabeto Runico (1° Aett di Urd). Posizione alfabetica: 7. Dominio: Il dono, l'unione, l'incontro, la generosità, la reciprocità, l'equilibrio simmetrico. Fondamento del Trivio di Compositum con Isa. Corrispondenza di Canone: Posizione 7 = Valenza 7.",
        "etimologia": "Dal proto-germanico *gebō (dono, scambio ospitale, patto sacro).",
        "incantesimiEsempio": "Stupeficium (7), Vulnera Sanentur (7), Exsequor (7), Invenio (7)"
    },
    {
        "id": "runa-wunjo",
        "nome": "Runa Wunjo (ᚹ)",
        "formula": "ᚹ Wunjo",
        "posizioneAlfabeto": "8ª",
        "posizioneNum": 8,
        "aett": "1° Aett (Urd)",
        "thootPos": "8ª Posizione (con Sowilo e Dagaz)",
        "valenza": 8,
        "sommaLettere": 8,
        "valenzaOpposta": 2,
        "figuraGeometrica": "Ottagono regolare (Infinito / Fuoco)",
        "pietraConsacrata": "Topazio / Opale",
        "movimento": "Asta verticale sinistra con triangolo superiore acuto proteso verso destra.",
        "movimentoSvg": "M 50,25 L 50,125 M 50,25 L 95,55 L 50,80",
        "descrizione": "8ª Runa dell'Alfabeto Runico (1° Aett di Urd). Posizione alfabetica: 8. Dominio: Gioia profonda, benessere, armonia spirituale, preghiera, celebrazione, assenza di sofferenza. Corrispondenza di Canone: Posizione 8 = Valenza 8.",
        "etimologia": "Dal proto-germanico *wunjō (gioia, delizia, armonia del cuore).",
        "incantesimiEsempio": "Lumos (8), Alohomora (8), Plasma (8), Exstinguo (8), Occulto (8)"
    },
    {
        "id": "runa-hagalaz",
        "nome": "Runa Hagalaz (ᚺ)",
        "formula": "ᚺ Hagalaz",
        "posizioneAlfabeto": "9ª",
        "posizioneNum": 9,
        "aett": "2° Aett (Verdandi)",
        "thootPos": "1ª Posizione (con Fehu e Teiwaz)",
        "valenza": 9,
        "sommaLettere": 9,
        "valenzaOpposta": 1,
        "figuraGeometrica": "Ellisse (Reincarnazione / Tempesta)",
        "pietraConsacrata": "Opale / Aria",
        "movimento": "Due aste verticali parallele congiunte da un fendente diagonale discendente verso destra.",
        "movimentoSvg": "M 50,25 L 50,125 M 100,25 L 100,125 M 50,85 L 100,60",
        "descrizione": "9ª Runa dell'Alfabeto Runico (apre il 2° Aett di Verdandi). Posizione alfabetica: 9. Dominio: Grandine, tempesta aerea, rottura di schemi, forze mutevoli del destino, mutamento inesorabile. Runa dell'Elemento Aria nel Codex. Corrispondenza di Canone: Posizione 9 = Valenza 9.",
        "etimologia": "Dal proto-germanico *haglaz (grandine, catastrofe celeste feconda).",
        "incantesimiEsempio": "Flipendo (9), Petrificus Totalus (9), Glacius (9), Compositum (9)"
    },
    {
        "id": "runa-nauthiz",
        "nome": "Runa Nauthiz (ᚾ)",
        "formula": "ᚾ Nauthiz",
        "posizioneAlfabeto": "10ª",
        "posizioneNum": 10,
        "aett": "2° Aett (Verdandi)",
        "thootPos": "2ª Posizione (con Uruz e Berkana)",
        "valenza": 1,
        "sommaLettere": 10,
        "valenzaOpposta": 9,
        "figuraGeometrica": "Circonferenza (Unità / Vincolo)",
        "pietraConsacrata": "Ossidiana / Vincolo",
        "movimento": "Asta verticale centrale attraversata diagonalmente da un segmento fendente inclinato.",
        "movimentoSvg": "M 75,25 L 75,125 M 45,60 L 105,90",
        "descrizione": "10ª Runa dell'Alfabeto Runico (2° Aett di Verdandi). Posizione alfabetica: 10 (riduzione teosofica: 1+0 = 1). Dominio: Necessità ineluttabile, vincolo stoico, controllo delle emozioni, carattere ferreo, salvezza nella prova. Corrispondenza di Canone: Posizione 10 -> Valenza 1.",
        "etimologia": "Dal proto-germanico *naudiz (bisogno, necessità stringente, costrizione).",
        "incantesimiEsempio": "Incendio (1), Reparo (1), Signo (1), Coerceo (1), Colligo (1)"
    },
    {
        "id": "runa-isa",
        "nome": "Runa Isa (ᛁ)",
        "formula": "ᛁ Isa",
        "posizioneAlfabeto": "11ª",
        "posizioneNum": 11,
        "aett": "2° Aett (Verdandi)",
        "thootPos": "3ª Posizione (con Thurisaz ed Ehwaz)",
        "valenza": 2,
        "sommaLettere": 11,
        "valenzaOpposta": 8,
        "figuraGeometrica": "Angolo / Linea Retta (Stasi / Gelo)",
        "pietraConsacrata": "Acquamarina / Ghiaccio",
        "movimento": "Singola asta verticale retta scendente, perfettamente pura.",
        "movimentoSvg": "M 75,25 L 75,125",
        "descrizione": "11ª Runa dell'Alfabeto Runico (2° Aett di Verdandi). Posizione alfabetica: 11 (riduzione teosofica: 1+1 = 2). Dominio: Ghiaccio, stasi molecolare, immobilità, arresto del tempo e del moto, freddo, notte, luna. Asse centrale di Compositum. Corrispondenza di Canone: Posizione 11 -> Valenza 2.",
        "etimologia": "Dal proto-germanico *īsaz (ghiaccio, stasi cristallina).",
        "incantesimiEsempio": "Expelliarmus (2), Innerva (2), Fumos (2), Riddikulus (2)"
    },
    {
        "id": "runa-jera",
        "nome": "Runa Jera (ᛃ)",
        "formula": "ᛃ Jera",
        "posizioneAlfabeto": "12ª",
        "posizioneNum": 12,
        "aett": "2° Aett (Verdandi)",
        "thootPos": "4ª Posizione (con Ansuz e Mannaz)",
        "valenza": 3,
        "sommaLettere": 12,
        "valenzaOpposta": 7,
        "figuraGeometrica": "Triangolo equilatero (Tempo Ciclico)",
        "pietraConsacrata": "Quarzo / Terra",
        "movimento": "Due punte angolari contrapposte che non si toccano, orientate a vortice orario.",
        "movimentoSvg": "M 50,45 L 75,25 L 100,45 M 50,105 L 75,125 L 100,105",
        "descrizione": "12ª Runa dell'Alfabeto Runico (2° Aett di Verdandi). Posizione alfabetica: 12 (riduzione teosofica: 1+2 = 3). Dominio: Ciclo delle stagioni, raccolto fecondo, giustizia del tempo, rotazione, pazienza. Corrispondenza di Canone: Posizione 12 -> Valenza 3.",
        "etimologia": "Dal proto-germanico *jēran (anno, buon raccolto, ciclo stagionale).",
        "incantesimiEsempio": "Arresto Momentum (3), Orchideus (3), Incipio (3), Iungo (3)"
    },
    {
        "id": "runa-eihwaz",
        "nome": "Runa Eihwaz (ᛇ)",
        "formula": "ᛇ Eihwaz",
        "posizioneAlfabeto": "13ª",
        "posizioneNum": 13,
        "aett": "2° Aett (Verdandi)",
        "thootPos": "5ª Posizione (con Raido e Laguz)",
        "valenza": 4,
        "sommaLettere": 13,
        "valenzaOpposta": 6,
        "figuraGeometrica": "Quadrato (Albero Cosmico / Stabilità)",
        "pietraConsacrata": "Ambra / Quarzo",
        "movimento": "Asta verticale centrale con uncino superiore verso sinistra e uncino inferiore verso destra.",
        "movimentoSvg": "M 50,40 L 75,25 L 75,125 L 100,110",
        "descrizione": "13ª Runa dell'Alfabeto Runico (2° Aett di Verdandi). Posizione alfabetica: 13 (riduzione teosofica: 1+3 = 4). Dominio: L'albero del tasso (Yggdrasil), asse del cosmo, trionfo sulle difficoltà, resurrezione, protezione magica millenaria. Corrispondenza di Canone: Posizione 13 -> Valenza 4.",
        "etimologia": "Dal proto-germanico *eihwaz (albero del tasso, asse sacro del mondo).",
        "incantesimiEsempio": "Liberacorpus (4), Diffindo (4), Persigno (4), Stigma Exsequor (4)"
    },
    {
        "id": "runa-perthr",
        "nome": "Runa Perthr (ᛈ)",
        "formula": "ᛈ Perthr",
        "posizioneAlfabeto": "14ª",
        "posizioneNum": 14,
        "aett": "2° Aett (Verdandi)",
        "thootPos": "6ª Posizione (con Kenaz e Inguz)",
        "valenza": 5,
        "sommaLettere": 14,
        "valenzaOpposta": 5,
        "figuraGeometrica": "Pentagono regolare (Mistero / Destino)",
        "pietraConsacrata": "Labradorite / Onice",
        "movimento": "Asta verticale sinistra con profilo ad ansa angolare aperta verso destra.",
        "movimentoSvg": "M 50,25 L 50,125 M 50,25 L 85,45 L 65,75 L 85,105 L 50,125",
        "descrizione": "14ª Runa dell'Alfabeto Runico (2° Aett di Verdandi). Posizione alfabetica: 14 (riduzione teosofica: 1+4 = 5). Dominio: Il fato, il bussolotto dei dadi, il segreto celato, l'estrazione della memoria, la profezia, la chiusura arcana. Corrispondenza di Canone: Posizione 14 -> Valenza 5.",
        "etimologia": "Dal proto-germanico *perþr- (bussolotto oracolare, mistero celato, fato).",
        "incantesimiEsempio": "Levicorpus (5), Immobilus (5), Deleo (5), Dominium Evoco (5)"
    },
    {
        "id": "runa-algiz",
        "nome": "Runa Algiz (ᛉ)",
        "formula": "ᛉ Algiz",
        "posizioneAlfabeto": "15ª",
        "posizioneNum": 15,
        "aett": "2° Aett (Verdandi)",
        "thootPos": "7ª Posizione (con Gebo e Othila)",
        "valenza": 6,
        "sommaLettere": 15,
        "valenzaOpposta": 4,
        "figuraGeometrica": "Esagono regolare (Scudo / Purezza)",
        "pietraConsacrata": "Ossidiana / Protezione",
        "movimento": "Asta verticale eretta con due rami ascendenti divaricati simmetricamente in alto (corna d'alce).",
        "movimentoSvg": "M 75,25 L 75,125 M 40,35 L 75,65 L 110,35",
        "descrizione": "15ª Runa dell'Alfabeto Runico (2° Aett di Verdandi). Posizione alfabetica: 15 (riduzione teosofica: 1+5 = 6). Dominio: Baluardo di difesa inviolabile, scudo arcano assoluto, purezza incontaminata, guardia, allontanamento del pericolo. Corrispondenza di Canone: Posizione 15 -> Valenza 6 (perfetta risonanza con Protego!).",
        "etimologia": "Dal proto-germanico *algiz (alce, protezione sacra, difesa inviolabile).",
        "incantesimiEsempio": "Protego (6), Verdimillious (6), Adultero (6), Surge et expandi (6)"
    },
    {
        "id": "runa-sowilo",
        "nome": "Runa Sowilo (ᛋ)",
        "formula": "ᛋ Sowilo",
        "posizioneAlfabeto": "16ª",
        "posizioneNum": 16,
        "aett": "2° Aett (Verdandi)",
        "thootPos": "8ª Posizione (con Wunjo e Dagaz)",
        "valenza": 7,
        "sommaLettere": 16,
        "valenzaOpposta": 3,
        "figuraGeometrica": "Ettagono regolare (Folgore / Sole)",
        "pietraConsacrata": "Topazio / Luce",
        "movimento": "Tracciato a saetta o fulmine a tre tratti diagonali a zigzag.",
        "movimentoSvg": "M 95,30 L 55,55 L 95,95 L 55,120",
        "descrizione": "16ª Runa dell'Alfabeto Runico (chiude il 2° Aett di Verdandi). Posizione alfabetica: 16 (riduzione teosofica: 1+6 = 7). Dominio: Sole trionfante, vittoria della ragione, scintilla elettrica, fulmine, lucidità e trionfo sulle tenebre. Corrispondenza di Canone: Posizione 16 -> Valenza 7 (risonanza con Stupeficium!).",
        "etimologia": "Dal proto-germanico *sōwilō (sole splendente, fuoco celeste).",
        "incantesimiEsempio": "Stupeficium (7), Vulnera Sanentur (7), Exsequor (7), Invenio (7)"
    },
    {
        "id": "runa-teiwaz",
        "nome": "Runa Teiwaz (ᛏ)",
        "formula": "ᛏ Teiwaz",
        "posizioneAlfabeto": "17ª",
        "posizioneNum": 17,
        "aett": "3° Aett (Skuld)",
        "thootPos": "1ª Posizione (con Fehu e Hagalaz)",
        "valenza": 8,
        "sommaLettere": 17,
        "valenzaOpposta": 2,
        "figuraGeometrica": "Ottagono regolare (Volontà / Giustizia)",
        "pietraConsacrata": "Onice / Acciaio",
        "movimento": "Asta verticale centrale sormontata da una cuspide a freccia verso l'alto (spada eretta).",
        "movimentoSvg": "M 75,25 L 75,125 M 40,55 L 75,25 L 110,55",
        "descrizione": "17ª Runa dell'Alfabeto Runico (apre il 3° Aett di Skuld). Posizione alfabetica: 17 (riduzione teosofica: 1+7 = 8). Dominio: Il dio del cielo Tyr, la spada della giustizia cosmica, forza di volontà inflessibile, maledizione, sacrificio d'onore. Corrispondenza di Canone: Posizione 17 -> Valenza 8.",
        "etimologia": "Dal proto-germanico *tīwaz (dio Tyr, cielo splendente, giustizia infallibile).",
        "incantesimiEsempio": "Lumos (8), Alohomora (8), Plasma (8), Exstinguo (8), Occulto (8)"
    },
    {
        "id": "runa-berkana",
        "nome": "Runa Berkana (ᛒ)",
        "formula": "ᛒ Berkana",
        "posizioneAlfabeto": "18ª",
        "posizioneNum": 18,
        "aett": "3° Aett (Skuld)",
        "thootPos": "2ª Posizione (con Uruz e Nauthiz)",
        "valenza": 9,
        "sommaLettere": 18,
        "valenzaOpposta": 1,
        "figuraGeometrica": "Ellisse (Rigenerazione / Terra)",
        "pietraConsacrata": "Ambra / Smeraldo",
        "movimento": "Asta verticale sinistra con due lobi triangolari convessi a destra (forma simile a B).",
        "movimentoSvg": "M 50,25 L 50,125 M 50,25 L 90,50 L 50,75 L 90,100 L 50,125",
        "descrizione": "18ª Runa dell'Alfabeto Runico (3° Aett di Skuld). Posizione alfabetica: 18 (riduzione teosofica: 1+8 = 9). Dominio: La betulla sacra, la terra viva (Elemento Terra Codex), nascita, fertilità, rigenerazione vegetale, protezione della dimora. Corrispondenza di Canone: Posizione 18 -> Valenza 9.",
        "etimologia": "Dal proto-germanico *berkanan (betulla, dea della fertilità e rinascita terrena).",
        "incantesimiEsempio": "Flipendo (9), Petrificus Totalus (9), Glacius (9), Compositum (9)"
    },
    {
        "id": "runa-ehwaz",
        "nome": "Runa Ehwaz (ᛖ)",
        "formula": "ᛖ Ehwaz",
        "posizioneAlfabeto": "19ª",
        "posizioneNum": 19,
        "aett": "3° Aett (Skuld)",
        "thootPos": "3ª Posizione (con Thurisaz e Isa)",
        "valenza": 1,
        "sommaLettere": 19,
        "valenzaOpposta": 9,
        "figuraGeometrica": "Circonferenza (Cinetica / Cavallo)",
        "pietraConsacrata": "Quarzo / Ambra",
        "movimento": "Due aste verticali congiunte in alto da due segmenti a V (forma simile a M).",
        "movimentoSvg": "M 45,25 L 45,125 M 105,25 L 105,125 M 45,25 L 75,55 L 105,25",
        "descrizione": "19ª Runa dell'Alfabeto Runico (3° Aett di Skuld). Posizione alfabetica: 19 (riduzione teosofica: 1+9 = 10 -> 1). Dominio: Il cavallo destriero, avanzamento rapido, cinetica animale, svolta repentina, alleanza leale cavaliere-destriero. Corrispondenza di Canone: Posizione 19 -> Valenza 1.",
        "etimologia": "Dal proto-germanico *ehwaz (cavallo, destriero sacro, compagno di viaggio).",
        "incantesimiEsempio": "Incendio (1), Reparo (1), Snufflifors (1), Signo (1), Colligo (1)"
    },
    {
        "id": "runa-mannaz",
        "nome": "Runa Mannaz (ᛗ)",
        "formula": "ᛗ Mannaz",
        "posizioneAlfabeto": "20ª",
        "posizioneNum": 20,
        "aett": "3° Aett (Skuld)",
        "thootPos": "4ª Posizione (con Ansuz e Jera)",
        "valenza": 2,
        "sommaLettere": 20,
        "valenzaOpposta": 8,
        "figuraGeometrica": "Angolo / Linea (Mente Umana / Ragione)",
        "pietraConsacrata": "Topazio / Zaffiro",
        "movimento": "Due aste verticali parallele congiunte da una grande croce a X nella parte superiore.",
        "movimentoSvg": "M 45,25 L 45,125 M 105,25 L 105,125 M 45,25 L 105,80 M 105,25 L 45,80",
        "descrizione": "20ª Runa dell'Alfabeto Runico (3° Aett di Skuld). Posizione alfabetica: 20 (riduzione teosofica: 2+0 = 2). Dominio: L'uomo, l'intelletto, la mente razionale, la coscienza umana, la cooperazione sociale, la scienza, l'equilibrio interiore. Corrispondenza di Canone: Posizione 20 -> Valenza 2.",
        "etimologia": "Dal proto-germanico *mannaz (essere umano, uomo saggio, mente pensante).",
        "incantesimiEsempio": "Expelliarmus (2), Innerva (2), Fumos (2), Riddikulus (2)"
    },
    {
        "id": "runa-laguz",
        "nome": "Runa Laguz (ᛚ)",
        "formula": "ᛚ Laguz",
        "posizioneAlfabeto": "21ª",
        "posizioneNum": 21,
        "aett": "3° Aett (Skuld)",
        "thootPos": "5ª Posizione (con Raido ed Eihwaz)",
        "valenza": 3,
        "sommaLettere": 21,
        "valenzaOpposta": 7,
        "figuraGeometrica": "Triangolo equilatero (Acqua / Abisso)",
        "pietraConsacrata": "Acquamarina / Acqua",
        "movimento": "Asta verticale scendente con ramo destro obliquo discendente dalla cima (amo d'acqua).",
        "movimentoSvg": "M 60,25 L 60,125 M 60,25 L 100,65",
        "descrizione": "21ª Runa dell'Alfabeto Runico (3° Aett di Skuld). Posizione alfabetica: 21 (riduzione teosofica: 2+1 = 3). Dominio: Spirito Arausio, acqua primordiale, onde dell'oceano, abisso, trappola liquida, confinamento insidioso. Runa cardine delle gabbie con Colligo. Corrispondenza di Canone: Posizione 21 -> Valenza 3 (Elemento Acqua 1 nel Codex).",
        "etimologia": "Dal proto-germanico *laguz (acqua, lago, marea, oceano profondo).",
        "incantesimiEsempio": "Arresto Momentum (3), Orchideus (3), Incipio (3), Iungo (3)"
    },
    {
        "id": "runa-inguz",
        "nome": "Runa Inguz (ᛜ)",
        "formula": "ᛜ Inguz",
        "posizioneAlfabeto": "22ª",
        "posizioneNum": 22,
        "aett": "3° Aett (Skuld)",
        "thootPos": "6ª Posizione (con Kenaz e Perthr)",
        "valenza": 4,
        "sommaLettere": 22,
        "valenzaOpposta": 6,
        "figuraGeometrica": "Quadrato / Rombo (Varco / Portale)",
        "pietraConsacrata": "Topazio / Opale",
        "movimento": "Rombo perfetto o losanga chiusa a quattro tratti obliqui simmetrici.",
        "movimentoSvg": "M 75,35 L 110,75 L 75,115 L 40,75 Z",
        "descrizione": "22ª Runa dell'Alfabeto Runico (3° Aett di Skuld). Posizione alfabetica: 22 (riduzione teosofica: 2+2 = 4). Dominio: Luce primordiale dell'anima, seme della gestazione, portale magico, varco tra dimensioni, ponte arcano. Corrispondenza di Canone: Posizione 22 -> Valenza 4.",
        "etimologia": "Dal proto-germanico *ingwaz (dio ancestrale Yngvi-Freyr, fecondità, luce vitale).",
        "incantesimiEsempio": "Liberacorpus (4), Diffindo (4), Persigno (4), Stigma Exsequor (4)"
    },
    {
        "id": "runa-othila",
        "nome": "Runa Othila (ᛟ)",
        "formula": "ᛟ Othila",
        "posizioneAlfabeto": "23ª",
        "posizioneNum": 23,
        "aett": "3° Aett (Skuld)",
        "thootPos": "7ª Posizione (con Gebo e Algiz)",
        "valenza": 5,
        "sommaLettere": 23,
        "valenzaOpposta": 5,
        "figuraGeometrica": "Pentagono regolare (Soglia / Patrimonio)",
        "pietraConsacrata": "Ossidiana / Onice",
        "movimento": "Rombo superiore con aste inferiori incrociate prolungate verso il basso.",
        "movimentoSvg": "M 45,125 L 75,95 L 105,65 L 75,35 L 45,65 L 75,95 L 105,125",
        "descrizione": "23ª Runa dell'Alfabeto Runico (3° Aett di Skuld). Posizione alfabetica: 23 (riduzione teosofica: 2+3 = 5). Dominio: La proprietà avita, la soglia sacra della casa, le radici familiari, il guardiano domestico, l'eredità. Runa speculare autonoma su valenza 5. Corrispondenza di Canone: Posizione 23 -> Valenza 5.",
        "etimologia": "Dal proto-germanico *ōþalan (patrimonio ancestrale, terra natia, lignaggio).",
        "incantesimiEsempio": "Levicorpus (5), Immobilus (5), Deleo (5), Dominium Evoco (5)"
    },
    {
        "id": "runa-dagaz",
        "nome": "Runa Dagaz (ᛞ)",
        "formula": "ᛞ Dagaz",
        "posizioneAlfabeto": "24ª",
        "posizioneNum": 24,
        "aett": "3° Aett (Skuld)",
        "thootPos": "8ª Posizione (con Wunjo e Sowilo)",
        "valenza": 6,
        "sommaLettere": 24,
        "valenzaOpposta": 4,
        "figuraGeometrica": "Esagono regolare (Giorno / Fuoco Vivente)",
        "pietraConsacrata": "Agata / Molibdenite",
        "movimento": "Forma a clessidra orizzontale o farfalla ad ali incrociate (due triangoli congiunti al vertice).",
        "movimentoSvg": "M 45,30 L 45,120 L 105,30 L 105,120 Z",
        "descrizione": "24ª Runa dell'Alfabeto Runico (chiude l'antico Futhark). Posizione alfabetica: 24 (riduzione teosofica: 2+4 = 6). Dominio: Spirito Sulis, elemento Fuoco vivente nel Codex (Numero 8 rituale), trasformazione all'alba, pienezza del giorno, incendio risanatore. Corrispondenza di Canone: Posizione 24 -> Valenza 6.",
        "etimologia": "Dal proto-germanico *dagaz (giorno, luce dell'aurora, compimento trasformatore).",
        "incantesimiEsempio": "Protego (6), Verdimillious (6), Adultero (6), Surge et expandi (6)"
    },
    {
        "id": "runa-bianca",
        "nome": "Runa Bianca (○)",
        "formula": "○ Runa Bianca",
        "posizioneAlfabeto": "Speciale",
        "posizioneNum": 25,
        "aett": "Centro del Wyrd",
        "thootPos": "Asse Centrale del Destino",
        "valenza": 5,
        "sommaLettere": 5,
        "valenzaOpposta": 5,
        "figuraGeometrica": "Pentagono regolare (Etere Cosmico / Il Nulla)",
        "pietraConsacrata": "Ciottolo Levigato privo di segni",
        "movimento": "Imposizione delle mani senza tracciato visibile, proiezione del vuoto mentale con Percèptio Ìntimo.",
        "movimentoSvg": "M 75,35 A 40,40 0 1,1 74.9,35 Z",
        "descrizione": "Runa Misterica del Wyrd (priva di glifo inciso). Collocata al Centro del Wyrd, rappresenta l'assenza trasfigurata in potere supremo, il vuoto fecondo, l'illusione totale (Percèptio Ìntimo). Valenza Esoterica 5 (speculare perfetta). Corrispondenza di Canone: Valenza 5.",
        "etimologia": "Dal mistero delle tre Norne (ciò che ancora non è e che può divenire tutto).",
        "incantesimiEsempio": "Perceptio Intimo (7), Levicorpus (5), Deleo (5), Revelio (5)"
    }
]

# 1. Carica spellsData.js esistente
with open(f'{BASE_DIR}/spellsData.js', 'r', encoding='utf-8') as f:
    text = f.read()

start = text.find('[')
end = text.rfind(']') + 1
spells = json.loads(text[start:end])

# Filtra eventuali rune preesistenti per idempotenza
spells = [s for s in spells if not s.get('isRune')]

# 2. Arricchisci ogni incantesimo con runeAssociate basate sulla regola canone
for s in spells:
    v = s.get('valenza', 1)
    s['runeAssociate'] = VALENCE_TO_RUNES.get(v, "ᚠ Fehu (Pos. 1ª)")

# 3. Trasforma le 25 rune in oggetti compatibili con spellsData
formatted_runes = []
for r in RUNES_CATALOG:
    v = r['valenza']
    opp = r['valenzaOpposta']
    rune_entry = {
        "id": r["id"],
        "isRune": True,
        "anno": 8,
        "annoLabel": "Antiche Rune",
        "posizioneAlfabeto": r["posizioneAlfabeto"],
        "posizioneNum": r["posizioneNum"],
        "aett": r["aett"],
        "thootPos": r["thootPos"],
        "nome": r["nome"],
        "formula": r["formula"],
        "ripetibile": True,
        "tipologia": "Antiche Rune / Glifo Sacro",
        "inDuello": False,
        "duelloNote": f"Utilizzabile per la creazione di talismani consacrati con Exsèquor, legami di Thoot con Iùngo e cerchi di confinamento o protezione rituale.",
        "movimento": r["movimento"],
        "movimentoSvg": r["movimentoSvg"],
        "descrizione": r["descrizione"],
        "etimologia": r["etimologia"],
        "valenza": v,
        "sommaLettere": r["sommaLettere"],
        "valenzaOpposta": opp,
        "maxRipetizioni": 8,
        "figuraGeometrica": r["figuraGeometrica"],
        "pietraConsacrata": r["pietraConsacrata"],
        "runeAssociate": VALENCE_TO_RUNES.get(v, ""),
        "noteAritmantiche": f"Posizione nell'Alfabeto Runico: {r['posizioneAlfabeto']}. Valenza Magica: {v} (la valenza dell'incantesimo corrisponde alla posizione della runa nell'alfabeto runico). Triade di Thoot: {r['thootPos']}. Pietra consacrata: {r['pietraConsacrata']}. Incantesimi di Hogwarts in risonanza: {r['incantesimiEsempio']}."
    }
    formatted_runes.append(rune_entry)

# Combina: prima gli incantesimi di Hogwarts (1-7 e Altri 0), poi le 25 Rune (anno: 8)
all_items = spells + formatted_runes

# Salva spellsData.js
js_output = f"// spellsData.js - Archivio Completo dei {len(all_items)} Incantesimi e Rune dell'Antico Futhark\n"
js_output += f"// Sincronizzato con il Programma Ufficiale di Studio di Arcane GDR, Trattati Didattici e Codex Arithmantiae\n\n"
js_output += "const SPELLS_DATA = " + json.dumps(all_items, ensure_ascii=False, indent=2) + ";\n"

with open(f'{BASE_DIR}/spellsData.js', 'w', encoding='utf-8') as f:
    f.write(js_output)

print(f"Salvati {len(all_items)} elementi in spellsData.js (di cui {len(formatted_runes)} rune)!")

# 4. Aggiorna app.js
with open(f'{BASE_DIR}/app.js', 'r', encoding='utf-8') as f:
    app_js = f.read()

# Assicuriamoci che la ricerca cerchi anche in runeAssociate e isRune
old_search_logic = '''        // 5. Search Query (searches in: name, formula, description, movement, type)
        if (searchQuery.trim() !== "") {
          const q = searchQuery.toLowerCase();
          const matchName = spell.nome.toLowerCase().includes(q);
          const matchFormula = spell.formula.toLowerCase().includes(q);
          const matchDesc = spell.descrizione.toLowerCase().includes(q);
          const matchMov = spell.movimento.toLowerCase().includes(q);
          const matchTipo = spell.tipologia.toLowerCase().includes(q);
          if (!matchName && !matchFormula && !matchDesc && !matchMov && !matchTipo) return false;
        }'''

new_search_logic = '''        // 5. Search Query (searches in: name, formula, description, movement, type, runeAssociate, aett)
        if (searchQuery.trim() !== "") {
          const q = searchQuery.toLowerCase();
          const matchName = spell.nome.toLowerCase().includes(q);
          const matchFormula = spell.formula.toLowerCase().includes(q);
          const matchDesc = spell.descrizione.toLowerCase().includes(q);
          const matchMov = spell.movimento.toLowerCase().includes(q);
          const matchTipo = spell.tipologia.toLowerCase().includes(q);
          const matchRune = (spell.runeAssociate || "").toLowerCase().includes(q);
          const matchAett = (spell.aett || "").toLowerCase().includes(q);
          if (!matchName && !matchFormula && !matchDesc && !matchMov && !matchTipo && !matchRune && !matchAett) return false;
        }'''

if old_search_logic in app_js:
    app_js = app_js.replace(old_search_logic, new_search_logic)

# Riconoscimento badge runa in renderSpells
old_type_badge = '''        } else if (spell.tipologia.includes("Trasfigurazione")) {
          typeBadgeClass = "bg-teal-500/10 text-teal-300 border-teal-500/30";
        }'''

new_type_badge = '''        } else if (spell.tipologia.includes("Trasfigurazione")) {
          typeBadgeClass = "bg-teal-500/10 text-teal-300 border-teal-500/30";
        } else if (spell.tipologia.includes("Rune") || spell.isRune) {
          typeBadgeClass = "bg-indigo-500/20 text-indigo-300 border-indigo-500/40";
        }'''

if old_type_badge in app_js:
    app_js = app_js.replace(old_type_badge, new_type_badge)

# Badge duello / posizione runa
old_duel_badge = '''        // Duel badge
        const duelBadge = spell.inDuello
          ? `<span class="inline-flex items-center gap-1 px-2.5 py-0.5 rounded-full text-[11px] font-bold bg-emerald-500/15 text-emerald-300 border border-emerald-500/30 shadow-sm">
               <span>⚔️</span> Duello: SÌ
             </span>`
          : `<span class="inline-flex items-center gap-1 px-2.5 py-0.5 rounded-full text-[11px] font-bold bg-slate-800 text-slate-400 border border-slate-700">
               <span>⛔</span> Duello: NO
             </span>`;'''

new_duel_badge = '''        // Duel / Runic badge
        let duelBadge;
        if (spell.isRune) {
          duelBadge = `<span class="inline-flex items-center gap-1 px-2.5 py-0.5 rounded-full text-[11px] font-bold bg-indigo-500/20 text-indigo-300 border border-indigo-500/40 shadow-sm">
                         <span>ᛟ</span> Futhark: Pos. ${spell.posizioneAlfabeto}
                       </span>`;
        } else {
          duelBadge = spell.inDuello
            ? `<span class="inline-flex items-center gap-1 px-2.5 py-0.5 rounded-full text-[11px] font-bold bg-emerald-500/15 text-emerald-300 border border-emerald-500/30 shadow-sm">
                 <span>⚔️</span> Duello: SÌ
               </span>`
            : `<span class="inline-flex items-center gap-1 px-2.5 py-0.5 rounded-full text-[11px] font-bold bg-slate-800 text-slate-400 border border-slate-700">
                 <span>⛔</span> Duello: NO
               </span>`;
        }'''

if old_duel_badge in app_js:
    app_js = app_js.replace(old_duel_badge, new_duel_badge)

# Modale: aggiornamento blocco runeAssociate
old_modal_notes = '''      modalLetterBreakdown.textContent = `${breakdown} = ${spell.sommaLettere} ➔ Riduzione: Valenza ${spell.valenza}`;
      modalArithNotes.textContent = spell.noteAritmantiche || "";'''

new_modal_notes = '''      modalLetterBreakdown.textContent = spell.isRune 
        ? `Posizione nell'Alfabeto: ${spell.posizioneAlfabeto} ➔ Valenza Magica: ${spell.valenza} (Canone: Valenza corrisponde alla Posizione)`
        : `${breakdown} = ${spell.sommaLettere} ➔ Riduzione: Valenza ${spell.valenza}`;
      modalArithNotes.textContent = spell.noteAritmantiche || "";

      // Elemento Runa Associata nel Modale
      const modalRuneBox = document.getElementById("modalRuneAssociation");
      const modalRunePos = document.getElementById("modalRunePosition");
      if (modalRuneBox && modalRunePos) {
        modalRunePos.textContent = `Valenza ${spell.valenza}`;
        modalRuneBox.innerHTML = spell.isRune
          ? `<strong>Runa Primaria dell'Alfabeto:</strong> ${spell.nome} (${spell.aett})<br><span class="text-xs text-amber-200/90">Incantesimi in risonanza: ${spell.incantesimiAssociati || spell.runeAssociate}</span>`
          : `<strong>Runa dell'Alfabeto Associata:</strong> <span class="text-amber-300">${spell.runeAssociate || "—"}</span>`;
      }'''

if old_modal_notes in app_js:
    app_js = app_js.replace(old_modal_notes, new_modal_notes)

with open(f'{BASE_DIR}/app.js', 'w', encoding='utf-8') as f:
    f.write(app_js)
print("Salvato app.js!")

# 5. Aggiorna index.html
with open(f'{BASE_DIR}/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Conteggi per categoria d'anno
counts = {}
for item in all_items:
    counts[item['anno']] = counts.get(item['anno'], 0) + 1

new_year_select = f'''<select id="yearSelect" class="w-full px-3 py-2.5 rounded-xl bg-slate-950/90 border border-slate-700 text-xs text-slate-200 focus:outline-none focus:border-amber-500 transition">
            <option value="ALL">Tutti gli Incantesimi & Rune ({len(all_items)})</option>
            <option value="1">I Anno — Fondamenti & Cinetica ({counts.get(1, 0)})</option>
            <option value="2">II Anno — Fatture & Inanimati ({counts.get(2, 0)})</option>
            <option value="3">III Anno — Gelo & Locomozione ({counts.get(3, 0)})</option>
            <option value="4">IV Anno — Tattiche & Medimagia ({counts.get(4, 0)})</option>
            <option value="5">V Anno — Esplosivi & G.U.F.O. ({counts.get(5, 0)})</option>
            <option value="6">VI Anno — Sesto Anno: Maledizioni, Trasfigurazione & Incantesimi ({counts.get(6, 0)})</option>
            <option value="7">VII Anno — Settimo Anno: Incantesimi Superiori, Difesa & Arti Oscure ({counts.get(7, 0)})</option>
            <option value="0">Altri — Formule Senza Riferimento d\'Anno ({counts.get(0, 0)})</option>
            <option value="8">ᚠ Antiche Rune — Alfabeto Futhark & Glifi Sacri ({counts.get(8, 0)})</option>
          </select>'''

html = re.sub(r'<select id="yearSelect"[\s\S]*?</select>', new_year_select, html)

new_year_tabs = f'''<div class="flex items-center gap-1.5 overflow-x-auto pb-1.5 scrollbar-none" id="yearTabsContainer">
            <button data-year="ALL" class="year-tab px-3 py-1.5 rounded-lg text-xs font-semibold transition whitespace-nowrap bg-amber-500 text-slate-950 shadow-md">
              Tutti ({len(all_items)})
            </button>
            <button data-year="1" class="year-tab px-3 py-1.5 rounded-lg text-xs font-semibold transition whitespace-nowrap bg-slate-800 text-slate-300 hover:bg-slate-700">
              I Anno ({counts.get(1, 0)})
            </button>
            <button data-year="2" class="year-tab px-3 py-1.5 rounded-lg text-xs font-semibold transition whitespace-nowrap bg-slate-800 text-slate-300 hover:bg-slate-700">
              II Anno ({counts.get(2, 0)})
            </button>
            <button data-year="3" class="year-tab px-3 py-1.5 rounded-lg text-xs font-semibold transition whitespace-nowrap bg-slate-800 text-slate-300 hover:bg-slate-700">
              III Anno ({counts.get(3, 0)})
            </button>
            <button data-year="4" class="year-tab px-3 py-1.5 rounded-lg text-xs font-semibold transition whitespace-nowrap bg-slate-800 text-slate-300 hover:bg-slate-700">
              IV Anno ({counts.get(4, 0)})
            </button>
            <button data-year="5" class="year-tab px-3 py-1.5 rounded-lg text-xs font-semibold transition whitespace-nowrap bg-slate-800 text-slate-300 hover:bg-slate-700">
              V Anno ({counts.get(5, 0)})
            </button>
            <button data-year="6" class="year-tab px-3 py-1.5 rounded-lg text-xs font-semibold transition whitespace-nowrap bg-slate-800 text-slate-300 hover:bg-slate-700">
              VI Anno ({counts.get(6, 0)})
            </button>
            <button data-year="7" class="year-tab px-3 py-1.5 rounded-lg text-xs font-semibold transition whitespace-nowrap bg-slate-800 text-slate-300 hover:bg-slate-700">
              VII Anno ({counts.get(7, 0)})
            </button>
            <button data-year="0" class="year-tab px-3 py-1.5 rounded-lg text-xs font-semibold transition whitespace-nowrap bg-slate-800 text-slate-300 hover:bg-slate-700">
              Altri ({counts.get(0, 0)})
            </button>
            <button data-year="8" class="year-tab px-3 py-1.5 rounded-lg text-xs font-semibold transition whitespace-nowrap bg-indigo-950 text-indigo-300 border border-indigo-700/60 hover:bg-indigo-900">
              ᚠ Antiche Rune ({counts.get(8, 0)})
            </button>
          </div>'''

html = re.sub(r'<div class="flex items-center gap-1\.5 overflow-x-auto pb-1\.5 scrollbar-none" id="yearTabsContainer">[\s\S]*?</div>', new_year_tabs, html)

# Aggiungi blocco nel modale per l'associazione runica se non presente
if 'id="modalRuneAssociation"' not in html:
    rune_modal_block = '''          <!-- Letters to Numbers Breakdown -->
          <div class="text-xs space-y-1.5 bg-slate-900/60 p-3 rounded-lg border border-slate-800">
            <div class="text-slate-400 font-semibold">Scomposizione Numerica delle Lettere:</div>
            <div id="modalLetterBreakdown" class="font-code text-amber-200/90 text-xs break-all">
              <!-- Scomposizione -->
            </div>
            <p id="modalArithNotes" class="text-[11px] text-slate-400 mt-2 italic leading-relaxed">
              <!-- Note arimantiche approfondite -->
            </p>
          </div>

          <!-- Runic Alphabet Association Block -->
          <div class="text-xs space-y-1.5 bg-indigo-950/40 p-3 rounded-lg border border-indigo-700/40">
            <div class="text-indigo-300 font-semibold flex items-center justify-between">
              <span>ᛟ Corrispondenza nell'Alfabeto Runico (Valenza = Posizione):</span>
              <span id="modalRunePosition" class="font-code text-amber-300 font-bold"></span>
            </div>
            <div id="modalRuneAssociation" class="font-magic text-slate-200 text-sm">
              <!-- Rune associate -->
            </div>
          </div>'''

    target = '''          <!-- Letters to Numbers Breakdown -->
          <div class="text-xs space-y-1.5 bg-slate-900/60 p-3 rounded-lg border border-slate-800">
            <div class="text-slate-400 font-semibold">Scomposizione Numerica delle Lettere:</div>
            <div id="modalLetterBreakdown" class="font-code text-amber-200/90 text-xs break-all">
              <!-- Scomposizione -->
            </div>
            <p id="modalArithNotes" class="text-[11px] text-slate-400 mt-2 italic leading-relaxed">
              <!-- Note arimantiche approfondite -->
            </p>
          </div>'''

    html = html.replace(target, rune_modal_block)

with open(f'{BASE_DIR}/index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Salvato index.html con sezione Rune!")

# 6. Rigenera dist/portale_standalone.html e artifact portale_incantesimi.html
with open(f'{BASE_DIR}/style.css', 'r', encoding='utf-8') as f:
    css_content = f.read()

with open(f'{BASE_DIR}/app.js', 'r', encoding='utf-8') as f:
    app_js_fresh = f.read()

standalone = html
standalone = standalone.replace('<link rel="stylesheet" href="style.css">', f'<style>\n{css_content}\n</style>')
standalone = standalone.replace('<script src="spellsData.js"></script>', f'<script>\n{js_output}\n</script>')
standalone = standalone.replace('<script src="app.js"></script>', f'<script>\n{app_js_fresh}\n</script>')

with open(f'{BASE_DIR}/dist/portale_standalone.html', 'w', encoding='utf-8') as f:
    f.write(standalone)

with open(f'{ARTIFACT_DIR}/portale_incantesimi.html', 'w', encoding='utf-8') as f:
    f.write(standalone)

print("Rigenerati dist/portale_standalone.html e artifact portale_incantesimi.html con successo!")
