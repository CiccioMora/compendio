# -*- coding: utf-8 -*-
"""
Script per aggiungere le pozioni nella sezione 'Altri' (anno: 0, annoLabel: 'Altri')
al compendio di Pozioni (data_pozioni.py).
Include:
1. Elisir dell'Indomito (Harvey Specter, 2026)
2. Elisir Solis Igniti (Harvey Specter, Alfred Knight, 2026)
3. Filtro di Eufrasia (Harvey Specter, 2026)
4. Pozione Somnus (Harvey Specter, Alfred Knight, 2026)
5. Pozione Zitto-e-lava (Harvey M. Specter, 2026)
6. Garza di Ortica (Manufatto alchemico / Filtro e Bendaggio)
"""

import os, json

POZIONI_ALVEARE = [
    {
        "id": "pot-garza-ortica",
        "nome": "Garza di Ortica",
        "nomeAlternativo": "Manufatto Tessile Alchemico / Filtro Purificante",
        "anno": 0,
        "annoLabel": "Altri",
        "tipologia": "Per Oggetti / Strumentazione Alchemica / Filtro & Bendaggio",
        "coloreFinale": "Bianco sporco o avorio naturale, con riflessi opachi",
        "tempoPreparazione": "Circa 1 ora (sobbollitura 30 min, battitura, pettinatura e tessitura)",
        "difficolta": "Base",
        "metodoAssunzione": "Strumento di filtraggio alchemico / Bendaggio sterile per ferite aperte",
        "ingredienti": [
            "Fusti di Ortica matura freschi (5)",
            "Acqua sorgiva (150 ml)",
            "Cenere di legno di Quercia (1 tazza)",
            "Strumenti consigliati: Coltello d'argento affilato, mazzuolo di legno, pettine a denti fitti (in legno o osso), guanti in pelle di drago, piccolo telaio da tessitura (o bacchetta magica)"
        ],
        "preparazione": [
            "1. Indossare i guanti in pelle di drago e raccogliere i 5 fusti di Ortica matura, scegliendo quelli più alti e fibrosi.",
            "2. Con il coltello d'argento, rimuovere delicatamente tutte le foglie e le diramazioni laterali, conservando le foglie per altri decotti.",
            "3. Adagiare i fusti puliti in un calderone riempito d'Acqua sorgiva, assicurandosi che siano completamente sommersi.",
            "4. Versare la tazza di cenere di legno di Quercia per favorire il processo di macerazione e distacco dalla corteccia.",
            "5. Accendere un fuoco vivace e portare ad ebollizione rapida, lasciando sobbollire per esattamente 30 minuti per distruggere completamente l'acido urticante dei peli e ammorbidire i fusti.",
            "6. Scolare i fusti e lasciarli raffreddare su un ripiano di pietra pulito.",
            "7. Utilizzando le dita o la punta del coltello d'argento, sbucciare la corteccia esterna ormai macerata per mettere a nudo le lunghe fibre biancastre interne (fibre liberiane).",
            "8. Battere delicatamente le fibre estratte con il mazzuolo di legno per renderle soffici e flessibili.",
            "9. Pettinare ripetutamente le fibre con il pettine a denti fitti per eliminare le parti legnose residue e allineare i filamenti più sottili.",
            "10. Prendere i filamenti così ottenuti e disporli sul piccolo telaio, procedendo a intrecciarli a trama rada (incrociando ordito e trama ogni 2 millimetri) per formare la garza. I maghi più esperti sono soliti incantare il telaio affinché lavori in autonomia.",
            "11. Lavare la garza finita in pura acqua corrente fredda per eliminare i residui di cenere.",
            "12. Stendere la garza ad asciugare al sole o al vento."
        ],
        "avvertenze": "MANIPOLAZIONE INIZIALE: I fusti freschi di ortica possiedono peli urticanti attivi e dolorosi; è indispensabile l'uso di guanti protettivi in pelle di drago fino al completamento dell'ebollizione con cenere. Una volta completato il processo termico e di filatura, la garza perde completamente ogni proprietà urticante risultando morbidissima, anallergica e sicura su piaghe e ferite aperte. A differenza delle comuni garze di cotone babbano o lino, questo tessuto non assorbe né altera i principi attivi delle pozioni filtrate, trattenendo solo impurità fisiche e scorie magiche.",
        "inventoreOrigine": "Manufatto tessile alchemico tradizionale a trama rada. Strumento d'elezione indispensabile per la chiarificazione e il filtraggio di infusi corrosivi o preparazioni oftalmiche (come il Filtro di Eufrasia), nonché bendaggio sterile che previene il rigetto magico dei tessuti rigenerati.",
        "descrizione": "Manufatto tessile alchemico a trama rada ottenuto dalla filatura delle fibre liberiane interne del fusto dell'ortica. Grazie alla straordinaria resistenza chimica e alla carica magica purificante, è lo strumento d'elezione per il filtro di infusi acidi, corrosivi o destinati all'uso oculare, oltre a essere impiegato come bendaggio sterile che previene il rigetto magico dei tessuti rigenerati senza assorbire i principi attivi."
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
