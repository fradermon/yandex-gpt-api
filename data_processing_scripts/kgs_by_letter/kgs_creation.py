import json

with open('data/names_ussr_oks_kgs_ordered.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

kgs_to_use = []

for item in data:
    if item.get("Отрасль") == "прочее":
        kgs_to_use.append({
            "KGS": item.get("КГС"),
            "USAGE": item.get("Область применения"),
            "NAME": item.get("Наименование")
        })

with open('kgs.json', 'w', encoding='utf-8') as output_file:
    for entry in kgs_to_use:
        json.dump(entry, output_file, ensure_ascii=False)
        output_file.write('\n')