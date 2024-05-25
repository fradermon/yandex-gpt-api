import json
import os

def developer_only(source_file, out_file):
    with open(source_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    devs = []
    seen_developers = set()

    for item in data:
        developer = item.get("Разработчик")
        if developer not in seen_developers:
            devs.append({"Разработчик": developer})
            seen_developers.add(developer)

    with open(out_file, 'w', encoding='utf-8') as f:
        json.dump(devs, f, ensure_ascii=False, indent=4)
    
    os.remove(source_file)

developer_only(source_file='data/developers/developers_only/developers_ussr.json',
               out_file='data/developers/developers_only/only_developers_ussr.json')