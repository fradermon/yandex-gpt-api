import json

with open('data/names_ussr_oks_kgs_ordered.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

kgs_to_use = [item.get("КГС") for item in data if item.get("Отрасль") == "прочее"]

# for item in data:
#     if item.get("Отрасль") == "прочее":
#         kgs_to_use.append(item.get("КГС"))

with open('kgs_only.json', 'w', encoding='utf-8') as output_file:
    for entry in kgs_to_use:
        output_file.write(json.dumps(entry, ensure_ascii=False)+'\n')
        # output_file.write('\n')