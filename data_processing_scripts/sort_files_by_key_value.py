import json

def filter_data(input_file, output_file, condition_key, condition_value):
    with open(input_file, 'r', encoding='utf-8') as file:
        data = json.load(file)
    
    filtered_data = [item for item in data if item.get(condition_key) == condition_value]
    
    with open(output_file, 'w', encoding='utf-8') as file:
        json.dump(filtered_data, file, ensure_ascii=False, indent=4)


input_filename = 'data/edited_names_modern_oks_kgs_ordered.json'
output_filename = 'data/other_edited_names_modern_oks_kgs_ordered.json'
filter_key = 'Отрасль'
filter_value = 'прочее'

filter_data(input_filename, output_filename, filter_key, filter_value)
