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

with open(FILE_RES_JSON, 'r', encoding='utf-8') as file_res_json:
    file_res = json.load(file_res_json)

with open(FILE_NAMES_JSON, 'r', encoding='utf-8') as file_names_json:
    file_names = json.load(file_names_json)

filtered_ids = [item['id'] for item in file_res if item.get('result') == 'строематериалы']
for _ in filtered_ids:
    print(_)

counter = 0

# начало цикла
for id in filtered_ids:
    status = file_stat[str(id)]  
    if status == 'yes':
        name = next(item['name'] for item in file_names if item['id'] == id)
        scope = next(item['scope'] for item in file_names if item['id'] == id)
        print(name)
        # print(scope)

        # ЗДЕСЬ ЗАПРОС
        try:
            response = requests.post(url=URL, headers=HEADERS, json=generate_prompt(name, scope))
            result = eval(response.text)
            # print(result)

            answer = remove_special_symbols((result["result"]['alternatives'][0]['message']['text'])).lower()
            print(id, answer)

            file_res_item = None
            for item in file_res:
                if item['id'] == int(id):
                    file_res_item = item
                    break

            found = False
            for category, pattern in CATEGORY_CHECK.items():
                if isinstance(pattern, list):
                    for pat in pattern:
                        if re.search(pat, answer):
                            answer = category
                            file_res_item['result'] = answer
                            file_stat[id] = 'yes'
                            found = True
                            break
                    if found:
                        break
                else:
                    if re.search(pattern, answer):
                        answer = category
                        file_res_item['result'] = answer
                        file_stat[id] = 'yes'
                        found = True
                        break

            if not found:
                answer = "другое"
                file_res_item['result'] = answer
                file_stat[id] = 'in progress'

        except (ClientError, ServerError, InvalidResultError) as e:
            error_type = e.__class__.__name__
            print(f"Ошибка при обработке '{name}': {e}")
            answer = str(e)
            file_res_item['result'] = answer
            file_stat[id] = 'error'

        except Exception as e:
            print(f"Ошибка при обработке группы '{name}': {e}")
            answer = str(e)
            file_res_item['result'] = answer
            file_stat[id] = 'error'

        # обновляем файл file_res
        with open(FILE_RES_JSON, 'w', encoding='utf-8') as file_res_json:
            json.dump(file_res, file_res_json, ensure_ascii=False, indent=4)

        # обновляем файл fle_stat
        with open(FILE_STAT_JSON, 'w', encoding='utf-8') as file_stat_json:
            json.dump(file_stat, file_stat_json, ensure_ascii=False, indent=4)

        # counter += 1
        # if counter >= 2:
        #     break

        time.sleep(0.2)
