import json
import re

# change for your device
input_file = 'data/names_ussr_oks_kgs_ordered.json'
output_file = 'edited_names_ussr_oks_kgs_ordered.json'

with open(input_file, 'r', encoding='utf-8') as file:
    data = json.load(file)

pattern_term = r'термин.+'
pattern_method = r'метод.+'
pattern_methodic = r'методик.+'

for item in data:
    name = item.get('Наименование', '').lower()
    
    match_term = re.search(pattern_term, name)
    match_method = re.search(pattern_method, name)
    match_methodic = re.search(pattern_methodic, name)

    if match_term:
        item['Группа'] = 'термины'
    elif (match_method) and (not(match_methodic)):
        item['Группа'] = 'методы'
    else:
        item['Группа'] = 'прочее'

with open(output_file, 'w', encoding='utf-8') as file:
    json.dump(data, file, ensure_ascii=False, indent=4)

print("Updated JSON file with 'Группа' key added to each dictionary.")
