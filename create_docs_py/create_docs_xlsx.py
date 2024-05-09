import json
import os
import pandas as pd # type: ignore

with open("data/merged_gost_res_08_05.json", "r", encoding="utf-8") as file:
    data = json.load(file)

unique_otrasl_values = set(entry["Отрасль"] for entry in data if entry["Отрасль"] != "NaN")

input_directory = "create_docs_py/category/category_json" #откуда берем json
output_directory = "create_docs_py/category/category_xlsx" #куда кидаем xlsx

os.makedirs(output_directory, exist_ok=True)

for filename in os.listdir(input_directory):
    if filename.endswith(".json"):
        input_filepath = os.path.join(input_directory, filename)
        output_filename = os.path.splitext(filename)[0] + ".xlsx"
        output_filepath = os.path.join(output_directory, output_filename)

        with open(input_filepath, "r", encoding="utf-8") as json_file:
            json_data = json.load(json_file)
        df = pd.DataFrame(json_data)

        df.to_excel(output_filepath, index=False, engine='openpyxl')

        print(f"Файл '{filename}' превратился в '{output_filename}'.")

print("ЦЕНОК.")
