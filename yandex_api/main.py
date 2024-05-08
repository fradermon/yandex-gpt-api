import json
import time
import re
import requests # type: ignore
from config import *
from request_handler import generate_prompt, remove_special_symbols
from error_handler import ClientError, ServerError, InvalidResultError

# читаем все три файла (list of dicts)
with open(FILE_STAT_JSON, 'r', encoding='utf-8') as file_stat_json:
    file_stat = json.load(file_stat_json)

with open(FILE_NAMES_JSON, 'r', encoding='utf-8') as file_names_json:
    file_names = json.load(file_names_json)

counter = 0

for id, status in file_stat.items():
    if status == 'no':
        name = next(item['name'] for item in file_names if item['id'] == int(id))
        scope = next(item['scope'] for item in file_names if item['id'] == int(id))
        print(name)

        file_res = []

        try:
            response = requests.post(url=URL, headers=HEADERS, json=generate_prompt(name, scope))
            result = eval(response.text)

            answer = remove_special_symbols((result["result"]['alternatives'][0]['message']['text'])).lower()
            print(id, answer)

            found = False
            for category, pattern in CATEGORY_CHECK.items():
                if isinstance(pattern, list):
                    for pat in pattern:
                        if re.search(pat, answer):
                            answer = category
                            result_dict = {"id": id, "result": answer}
                            file_res.append(result_dict)
                            file_stat[id] = 'yes'
                            found = True
                            break
                    if found:
                        break
                else:
                    if re.search(pattern, answer):
                        answer = category
                        result_dict = {"id": id, "result": answer}
                        file_res.append(result_dict)
                        file_stat[id] = 'yes'
                        found = True
                        break

            if not found:
                answer = "другое"
                result_dict = {"id": id, "result": answer}
                file_res.append(result_dict)
                file_stat[id] = 'in progress'

        except (ClientError, ServerError, InvalidResultError) as e:
            error_type = e.__class__.__name__
            print(f"Ошибка при обработке '{name}': {e}")
            answer = str(e)
            result_dict = {"id": id, "result": answer}
            file_res.append(result_dict)
            file_stat[id] = 'error'

        except Exception as e:
            print(f"Ошибка при обработке группы '{name}': {e}")
            answer = str(e)
            result_dict = {"id": id, "result": answer}
            file_res.append(result_dict)
            file_stat[id] = 'error'

        with open(FILE_RES_JSON, 'a') as file_res_json:
            for line in file_res:
                file_res_json.write(json.dumps(line, ensure_ascii=False) + '\n')

        with open(FILE_STAT_JSON, 'w', encoding='utf-8') as file_stat_json:
            json.dump(file_stat, file_stat_json, ensure_ascii=False, indent=4)

        counter += 1
        if counter >= 2:
            break

        time.sleep(0.2)
