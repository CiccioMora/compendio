# -*- coding: utf-8 -*-
"""
sync_trasfigurazione_curriculum.py
Allinea il database di Trasfigurazione ai 5 screenshot ufficiali di Arcane GDR:
- I ANNO: Chartanimus (pratica), Transfiguro, Muto, Verto (teoria forme)
- II ANNO: Acutus, Malum, Gommosus, Vermiculus, Snufflifors, Incarcifors, Feraverto, Inferacus
- III ANNO: Reparifarge, Lapifors, Avifors, Avis, Farfallus Explodit, Furunculus, Glisseo
- IV ANNO: Draconifors, Duro, Piertotum Locomotor, Engorgio, Diminuendo
- V ANNO: Epoximise, Orchideus, Melofors, Incarceramus
- VI ANNO: Adduco Maxima, Obstringo Circulum, Crinus Muto, Pullus, Densaugeo, Paperante, Piscofors, Entomorphis, Furitum, Geminio, Inflatus
- VII ANNO: Animaleus Nobodyx, Reverto
"""

import json

BASE_DIR = '/Users/andreamorachioli/.gemini/antigravity/scratch/portale-incantesimi'

with open(f'{BASE_DIR}/spellsData.js', 'r', encoding='utf-8') as f:
    text = f.read()

spells = json.loads(text[text.find('['):text.rfind(']')+1])
by_id = {s['id']: s for s in spells}

# 1. Spostamenti per anno
year_reassignments = {
    # I ANNO
    "chartanimus": (1, "I Anno"),
    "transfiguro": (1, "I Anno"),
    "muto": (1, "I Anno"),
    "verto": (1, "I Anno"),
    
    # II ANNO
    "feraverto": (2, "II Anno"),
    "inferacus": (2, "II Anno"),
    
    # III ANNO
    "reparifarge": (3, "III Anno"),
    "avis": (3, "III Anno"),
    "farfallus-explodit": (3, "III Anno"),
    "furunculus": (3, "III Anno"),
    "glisseo": (3, "III Anno"),
    
    # IV ANNO
    "draconifors": (4, "IV Anno"),
    "piertotum-locomotor": (4, "IV Anno"),
    
    # V ANNO
    "epoximise": (5, "V Anno"),
    "orchideus": (5, "V Anno"),
    "melofors": (5, "V Anno"),
    "incarceramus": (5, "V Anno"),
    
    # VI ANNO
    "obstringo-circulum": (6, "VI Anno")
}

for sid, (y, label) in year_reassignments.items():
    if sid in by_id:
        old_y = by_id[sid].get('anno')
        by_id[sid]['anno'] = y
        by_id[sid]['annoLabel'] = label
        print(f"Riassegnato {sid}: Anno {old_y} -> Anno {y} ({label})")

# 2. Aggiunta Engorgio e Diminuendo in IV Anno (se assenti)
VALENCE_RUNES_MAP = {
    1: "ᚠ Fehu (Pos. 1ª), ᚾ Nauthiz (Pos. 10ª), ᛖ Ehwaz (Pos. 19ª)",
    2: "ᚢ Uruz (Pos. 2ª), ᛁ Isa (Pos. 11ª), ᛗ Mannaz (Pos. 20ª)",
    3: "ᚦ Thurisaz (Pos. 3ª), ᛃ Jera (Pos. 12ª), ᛚ Laguz (Pos. 21ª)",
    4: "ᚨ Ansuz (Pos. 4ª), ᛇ Eihwaz (Pos. 13ª), ᛜ Inguz (Pos. 22ª)",
    5: "ᚱ Raido (Pos. 5ª), ᛈ Perthr (Pos. 14ª), ᛟ Othila (Pos. 23ª), ○ Runa Bianca",
    6: "ᚲ Kenaz (Pos. 6ª), ᛉ Algiz (Pos. 15ª), ᛞ Dagaz (Pos. 24ª)",
    7: "ᚷ Gebo (Pos. 7ª), ᛋ Sowilo (Pos. 16ª)",
    8: "ᚹ Wunjo (Pos. 8ª), ᛏ Teiwaz (Pos. 17ª)",
    9: "ᚺ Hagalaz (Pos. 9ª), ᛒ Berkana (Pos. 18ª)"
}

if "engorgio" not in by_id:
    engorgio = {
        "id": "engorgio",
        "anno": 4,
        "annoLabel": "IV Anno",
        "nome": "Incantesimo di Ingrandimento (Engorgio)",
        "formula": "Engorgio",
        "ripetibile": True,
        "tipologia": "Trasfigurazione / Alterazione Dimensionale",
        "inDuello": True,
        "duelloNote": "Utilizzabile in duello per ingigantire ostacoli fisici, scudi di fortuna o disorientare l'avversario alterando le proporzioni del campo di scontro.",
        "movimento": "Cerchio ascendente tracciato verso l'esterno con puntamento deciso della punta della bacchetta.",
        "movimentoSvg": "M 75,90 C 55,90 40,75 40,60 C 40,40 60,30 75,30 C 95,30 115,45 115,65 C 115,85 95,105 75,105 L 120,60",
        "descrizione": "Incluso nel programma didattico di IV Anno (Trasfigurazione - Pratica: Engorgio e Diminuendo). Induce un rigonfiamento volumetrico uniforme del bersaglio inanimato o vivente, accrescendone massa apparente e dimensioni fisiche.",
        "etimologia": "Dall'inglese arcaico engorge (ingrossare, rigonfiare, saziare).",
        "valenza": 9,
        "sommaLettere": 54,
        "valenzaOpposta": 1,
        "maxRipetizioni": 9,
        "figuraGeometrica": "Ellisse (Reincarnazione / Totalità)",
        "runeAssociate": VALENCE_RUNES_MAP[9],
        "noteAritmantiche": "Valenza Magica 9 (somma pitagorica 54 ridotta a 9). Valenza opposta di simmetria: 1. Figura operativa per Signo: Ellisse. Limite di reiterazione: 9 volte."
    }
    spells.append(engorgio)
    by_id["engorgio"] = engorgio
    print("Aggiunto Engorgio (IV Anno)")

if "diminuendo" not in by_id:
    diminuendo = {
        "id": "diminuendo",
        "anno": 4,
        "annoLabel": "IV Anno",
        "nome": "Incantesimo di Rimpicciolimento (Diminuendo)",
        "formula": "Diminuendo",
        "ripetibile": True,
        "tipologia": "Trasfigurazione / Compressione Dimensionale",
        "inDuello": True,
        "duelloNote": "Utilizzabile in duello per comprimere proiettili, armi o pericoli fisici in arrivo, o rimpicciolire l'equipaggiamento dell'avversario.",
        "movimento": "Spirale centripeta contratta verso l'interno terminante con tocco lieve della punta.",
        "movimentoSvg": "M 115,45 C 115,85 75,115 55,95 C 35,75 45,45 75,45 C 95,45 95,75 75,75",
        "descrizione": "Incluso nel programma didattico di IV Anno (Trasfigurazione - Pratica: Engorgio e Diminuendo). Sortilegio complementare di Engorgio: comprime volumetricamente la materia del bersaglio riducendone le dimensioni a scala miniaturizzata.",
        "etimologia": "Dal latino diminuere / italiano musicale diminuendo (decrescere gradualmente di volume).",
        "valenza": 9,
        "sommaLettere": 54,
        "valenzaOpposta": 1,
        "maxRipetizioni": 9,
        "figuraGeometrica": "Ellisse (Reincarnazione / Totalità)",
        "runeAssociate": VALENCE_RUNES_MAP[9],
        "noteAritmantiche": "Valenza Magica 9 (somma pitagorica 54 ridotta a 9). Valenza opposta di simmetria: 1. Figura operativa per Signo: Ellisse. Limite di reiterazione: 9 volte."
    }
    spells.append(diminuendo)
    by_id["diminuendo"] = diminuendo
    print("Aggiunto Diminuendo (IV Anno)")

# 3. Ordinamento
def sort_key(s):
    y = s.get('anno', 0)
    order = {1:1, 2:2, 3:3, 4:4, 5:5, 6:6, 7:7, 0:8, 8:9}.get(y, 99)
    return (order, s.get('nome', ''))

spells.sort(key=sort_key)

new_spells_data_content = f"""// spellsData.js - Archivio Completo dei {len(spells)} Incantesimi e Rune dell'Antico Futhark
// Sincronizzato con il Programma Ufficiale di Studio di Arcane GDR, Trattati Didattici, Astronomia, Erbologia e Codex Arithmantiae

const SPELLS_DATA = {json.dumps(spells, ensure_ascii=False, indent=2)};

if (typeof module !== 'undefined' && module.exports) {{
  module.exports = SPELLS_DATA;
}}
"""

with open(f'{BASE_DIR}/spellsData.js', 'w', encoding='utf-8') as f:
    f.write(new_spells_data_content)

print(f"spellsData.js aggiornato con {len(spells)} entità.")
