import json
import re

acronyms = [r'ВНИИ', r'ВЦСПС', r'ВИНИТИ', r'МВД', r'ВИЛС', r'ВЦНИИОТ', r'РГБ', r'АН.+ССР', r'СНИИП', r'ЦНИИ', r'СМ СССР', r'СССР']
full_names = [
    r'министерство.*', r'.*госкомтитет.*', r'.*госкомитет.*', r'мин\w+', r'гос\w+', r'всероссийск.+',
    r'государственн.+', r'госстандарт.*', r'федерал\w+', r'всероссийский научно.*исследовательский институт.*',
    r'всесоюзн.+', r'комитет.*', r'гостандарт.*', r'центросоюз.*', r'.*управление.+ссср.*', r'академия наук.+сср.*'
]

def add_source(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    result = []

    for item in data:
        developer = str(item.get('Разработчик')).strip()
        categorized = False

        for acronym in acronyms:
            if re.search(acronym, developer):
                item['Средства'] = 'ФБ'
                categorized = True
                break

        if not categorized:
            developer_lower = developer.lower()

            for name in full_names:
                if re.match(name, developer_lower):
                    item['Средства'] = 'ФБ'
                    categorized = True
                    break

        if not categorized:
            if developer == 'nan':
                item['Средства'] = 'Не указано'
            else:
                item['Средства'] = 'Ср.Р'

        result.append(item)

    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(result, f, ensure_ascii=False, indent=4)

    print(f"Открывай {output_file}")


def get_source_Cp(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    result = []

    for item in data:
        if item.get('Средства') == 'Ср.Р':
            result.append({'Разработчик': item.get('Разработчик')})

    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(result, f, ensure_ascii=False, separators=(',\n', ':'))

    print(f"Открывай {output_file}")


#add_source(input_file = 'data/developers/ussr_with_devs.json', output_file = 'data/developers/classified_ussr_with_devs.json')
#get_source_Cp(input_file = 'data/developers/classified_ussr_with_devs.json', output_file = 'data/developers/file_developers_sr_r_only.json')