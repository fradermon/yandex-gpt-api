import json

# # вход
# source_file = ''

# # выход
# no_source_file = ''
# with_source_file = ''

def find_developer(source_file, yes_dev_file):
    with open(source_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    no_source = []
    with_source = []

    for item in data:
        developer = str(item.get("Разработчик"))
        if developer != "nan":
            with_source.append(item)
        else:
            no_source.append(item)

    # with open(no_dev_file, 'w', encoding='utf-8') as f:
    #     json.dump(no_source, f, ensure_ascii=False, indent=4)

    with open(yes_dev_file, 'w', encoding='utf-8') as f:
        json.dump(with_source, f, ensure_ascii=False, indent=4)

find_developer(source_file='data/edited_names_modern_oks_kgs_ordered_n.json', 
                yes_dev_file='data/developers/modern_with_devs.json')