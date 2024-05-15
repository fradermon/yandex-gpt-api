import json

allowed_values = []
with open('data/kgs_only.json', 'r', encoding='utf-8') as file:
    for line in file.readlines():
        line = line.rstrip('\n')
        allowed_values.append(line)
print(allowed_values)

kgs_data = []
with open('data/kgs.json', 'r') as kgs_file:
    for line in kgs_file.readlines():
        kgs_data.append(json.loads(line.strip()))

filtered_data = [entry for entry in kgs_data if entry['КГС'] in allowed_values]

with open('data/unique_kgs.json', 'w', encoding='utf-8') as output_file:
    for entry in filtered_data:
        json.dump(entry, output_file, ensure_ascii=False)
        output_file.write('\n') 



