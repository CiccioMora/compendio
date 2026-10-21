import json

BASE_DIR = "/Users/andreamorachioli/.gemini/antigravity/scratch/portale-incantesimi"
ARTIFACT_DIR = "/Users/andreamorachioli/.gemini/antigravity/brain/3a4f7fa7-8206-4f51-b303-aa9b9d9eaf5c"

with open(f"{BASE_DIR}/spellsData.js", "r", encoding="utf-8") as f:
    text = f.read()

data = json.loads(text[text.find("["):text.rfind("]")+1])

realigned = 0
for s in data:
    if s["id"] == "reverto":
        s["anno"] = 1
        s["annoLabel"] = "I Anno"
        s["tipologia"] = "Trasfigurazione / Controincantesimo di I Livello"
        s["duelloNote"] = "Abilitato in duello per annullare rapidamente alterazioni trasfigurative semplici inflitte dall'avversario. Trattato prima di Pagina 29 (PDF p. 10) nel manuale di Trasfigurazione come controincanto fondante."
        realigned += 1
    elif s["id"] == "significo":
        s["anno"] = 1
        s["annoLabel"] = "I Anno"
        s["tipologia"] = "Trasfigurazione / Marchiatura Inanimata"
        s["duelloNote"] = "Non da duello. Primo Anno di Trasfigurazione (Pagina 25): applicazione di un marchio semitrasparente identificativo su oggetti inanimati."
        realigned += 1
    elif s["id"] == "plansigno":
        s["anno"] = 1
        s["annoLabel"] = "I Anno"
        s["tipologia"] = "Trasfigurazione / Marchiatura Vegetale"
        s["duelloNote"] = "Non da duello. Primo Anno di Trasfigurazione (Pagina 25): applicazione di un marchio magico su elementi botanici e vegetali."
        realigned += 1
    elif s["id"] == "fersigno":
        s["anno"] = 1
        s["annoLabel"] = "I Anno"
        s["tipologia"] = "Trasfigurazione / Marchiatura Vivente"
        s["duelloNote"] = "Non da duello. Primo Anno di Trasfigurazione (Pagina 25): applicazione di un marchio non lesivo su entità animate o creature viventi."
        realigned += 1
    elif s["id"] == "detecto":
        s["anno"] = 1
        s["annoLabel"] = "I Anno"
        s["tipologia"] = "Trasfigurazione / Diagnostica Molecolare e Marchi"
        s["duelloNote"] = "Non da duello. Primo Anno di Trasfigurazione (Pagine 16 e 25): analisi della perfezione molecolare ed evidenziazione di marchi magici occulti."
        realigned += 1

print(f"Realigned {realigned} Trasfigurazione spells to I Anno (Prima di Pagina 29).")

# Save updated spellsData.js
json_content = json.dumps(data, indent=2, ensure_ascii=False)
js_output = f"// spellsData.js - Archivio Completo dei {len(data)} Incantesimi e Rune dell'Antico Futhark\nconst SPELLS_DATA = {json_content};\n"

with open(f"{BASE_DIR}/spellsData.js", "w", encoding="utf-8") as f:
    f.write(js_output)

print("spellsData.js written successfully.")
