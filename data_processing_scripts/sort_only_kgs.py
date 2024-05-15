import json
import re
import os

data = []
with open('data/kgs.json', 'r', encoding='utf-8') as file:
    for line in file.readlines():
        data.append(json.loads(line))
    
def files_by_letter(pattern, output_file):
    list = []

    for item in data:
        # print(re.match(pattern, item['КГС']))
        if item and re.match(pattern, item['КГС']):
            list.append(item)
    # print(list)
    with open(output_file, 'w', encoding='utf-8') as output_file:
        for entry in list:
            print(entry)
            json.dump(entry, output_file, ensure_ascii=False)
            output_file.write('\n') 


pattern_output = {
    r'Т.*': 'data/only_kgs_by_letter/Т_file.json',
    r'С.*': 'data/only_kgs_by_letter/С_file.json',
    r'У.*': 'data/only_kgs_by_letter/У_file.json',
    r'И.*': 'data/only_kgs_by_letter/И_file.json',
    r'А.*': 'data/only_kgs_by_letter/А_file.json',
    r'К.*': 'data/only_kgs_by_letter/К_file.json',
    r'Г.*': 'data/only_kgs_by_letter/Г_file.json',
    r'Э.*': 'data/only_kgs_by_letter/Э_file.json',
    r'Б.*': 'data/only_kgs_by_letter/Б_file.json',
    r'Е.*': 'data/only_kgs_by_letter/Е_file.json',
    r'Д.*': 'data/only_kgs_by_letter/Д_file.json',
    r'Ф.*': 'data/only_kgs_by_letter/Ф_file.json',
    r'Ж.*': 'data/only_kgs_by_letter/Ж_file.json'
}

for key, value in pattern_output.items():
    files_by_letter(pattern=key, output_file=value)

# os.remove('kgs.json')
