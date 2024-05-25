# data/edited_names_ussr_oks_kgs_ordered_n.json
# data/edited_names_modern_oks_kgs_ordered_n.json
import json


def developer_only(source_file='', out_file=''):
    with open(source_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    devs = []

    for item in data:
        developer = str(item.get("Разработчик"))
        devs.append({"Разработчик": developer})

    with open(out_file, 'w', encoding='utf-8') as f:
            json.dump(devs, f, ensure_ascii=False, indent=4)

developer_only(source_file='data/developers/modern_with_devs.json',
               out_file='data/developers/developers_only/developers_modern.json')
