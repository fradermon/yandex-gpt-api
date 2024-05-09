import json
import os

with open("data/merged_gost_res_08_05.json", "r", encoding="utf-8") as file:
    data = json.load(file)

unique_otrasl_values = set(entry["Отрасль"] for entry in data if entry["Отрасль"] != "NaN")

#куда сохранять json
directory = "create_docs_py/category/category_json"

os.makedirs(directory, exist_ok=True)

for otrasl in unique_otrasl_values:
    filtered_data = [entry for entry in data if entry["Отрасль"] == otrasl]
    filename = os.path.join(directory, f"{otrasl}.json")
    with open(filename, "w", encoding="utf-8") as output_file:
        json.dump(filtered_data, output_file, ensure_ascii=False, indent=4)
    print(f"Данные для'{otrasl}' были сохранены в'{filename}'.")

print("ЦЕНОК.")

