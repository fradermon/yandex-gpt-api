import json
import re
import os

data = []
with open('kgs.json', 'r', encoding='utf-8') as file:
    for line in file.readlines():
        data.append(json.loads(line))

def files_by_letter(pattern, output_file):
    list = []

    for item in data:
        kgs_value = item.get("KGS")
        if kgs_value and re.match(pattern, kgs_value):
            list.append(item)

    with open(output_file, 'w', encoding='utf-8') as output_file:
        for entry in list:
            json.dump(entry, output_file, ensure_ascii=False)
            output_file.write('\n') 


pattern_output = {
    r'Т[0-9]{2}': 'data/kgs_by_letter/Т_file.json',
    r'С[0-9]{2}': 'data/kgs_by_letter/С_file.json',
    r'У[0-9]{2}': 'data/kgs_by_letter/У_file.json',
    r'И[0-9]{2}': 'data/kgs_by_letter/И_file.json',
    r'А[0-9]{2}': 'data/kgs_by_letter/А_file.json',
    r'К[0-9]{2}': 'data/kgs_by_letter/К_file.json',
    r'Г[0-9]{2}': 'data/kgs_by_letter/Г_file.json',
    r'Э[0-9]{2}': 'data/kgs_by_letter/Э_file.json',
    r'Б[0-9]{2}': 'data/kgs_by_letter/Б_file.json',
    r'Е[0-9]{2}': 'data/kgs_by_letter/Е_file.json',
    r'Д[0-9]{2}': 'data/kgs_by_letter/Д_file.json',
    r'Ф[0-9]{2}': 'data/kgs_by_letter/Ф_file.json',
    r'Ж[0-9]{2}': 'data/kgs_by_letter/Ж_file.json'
}

for key, value in pattern_output.items():
    files_by_letter(pattern=key, output_file=value)

os.remove('kgs.json')
