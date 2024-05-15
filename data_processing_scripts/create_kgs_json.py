import json

data = []
with open('data/merged_KGS.txt', 'r', encoding='utf-8') as file:
    for line in file.readlines():
        line = line.rstrip('\n')
        data.append(line)

for ele in data:
    print(ele[0:3])
    print(ele[4::])

result = []

for ele in data:
    dict = {
        "КГС": ele[0:3],  
        "Определение": ele[4::]
    }
    result.append(dict)

with open('data/kgs.json', 'w', encoding='utf-8') as output_file:
    for entry in result:
        json.dump(entry, output_file, ensure_ascii=False)
        output_file.write('\n') 
