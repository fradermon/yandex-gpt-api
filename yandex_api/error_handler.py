import requests # type: ignore

# Исключение ошибки клиента (коды 4xx)
class ClientError(Exception):
    def __init__(self, status_code):
        self.status_code = status_code
        super().__init__("Ошибка клиента. Код ответа: {}".format(status_code))

# Исключение ошибки сервера (коды 5xx)
class ServerError(Exception):
    def __init__(self, status_code):
        self.status_code = status_code
        super().__init__("Ошибка сервера. Код ответа: {}".format(status_code))

# Исключение неверного ответа от сервера
class InvalidResponseFormatError(Exception):
    pass

# Исключение для ответа вне списка ОТРАСЛЕЙ
class InvalidResultError(Exception):
    pass

# class NpaClassifierBot:
#     def __init__(self, request_string, headers, url, industries):
#         self.request_string = request_string
#         self.url = url
#         self.headers = headers
#         self.industries = industries

#     def classify_npa(self, prompt):
        
#         response = requests.post(self.url, headers=self.headers, json=prompt)
        
#         # Проверка кода ответа сервера и обработка ошибок
#         if response.status_code == 200:
#             result = response.json()
#             try:
#                 industry = result["result"]['alternatives'][0]['message']['text']
#                 if industry.lower() not in self.industries:
#                     raise InvalidResultError(f"Результат '{industry}' не относится к списку отраслей.")
#                 return industry
#             except (KeyError, IndexError):
#                 raise InvalidResponseFormatError("Неверный формат ответа.")
#         elif response.status_code // 100 == 4:
#             raise ClientError(response.status_code)
#         elif response.status_code // 100 == 5:
#             raise ServerError(response.status_code)
#         else:
#             raise InvalidResponseFormatError("Неверный формат ответа.")
