import json
import os
from collections import defaultdict
import pandas as pd # type: ignore

def read_input_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data

def group_by_industry(data):
    industry_dict = defaultdict(list)
    for item in data:
        industry = item['Отрасль']
        industry_dict[industry].append(item)
    return industry_dict

def write_json_files(industry_dict, output_dir):
    for industry, items in industry_dict.items():
        file_name = f"{industry}.json"
        file_path = os.path.join(output_dir, file_name)
        
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(items, file, ensure_ascii=False, indent=4)

def convert_json_to_xlsx(output_dir):
    for file_name in os.listdir(output_dir):
        if file_name.endswith('.json'):
            file_path = os.path.join(output_dir, file_name)
            xlsx_file_path = os.path.join(output_dir, file_name.replace('.json', '.xlsx'))

            with open(file_path, 'r', encoding='utf-8') as file:
                data = json.load(file)
                df = pd.DataFrame(data)

            df.to_excel(xlsx_file_path, index=False)

            os.remove(file_path)

def main(input_file, output_dir):
    data = read_input_file(input_file)
    industry_dict = group_by_industry(data)
    write_json_files(industry_dict, output_dir)
    convert_json_to_xlsx(output_dir)

if __name__ == "__main__":
    input_file = 'data/edited_names_modern_oks_kgs_ordered_n.json'
    output_dir = 'data/modern_xlsx'
    main(input_file, output_dir)
