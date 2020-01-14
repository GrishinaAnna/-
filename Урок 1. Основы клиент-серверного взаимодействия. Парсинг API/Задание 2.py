# 2. Изучить список открытых API. Найти среди них любое, требующее авторизацию (любого типа).
# Выполнить запросы к нему, пройдя авторизацию. Ответ сервера записать в файл.

import requests
import json
url = 'http://api.travelpayouts.com/v2/statistics/balance?token='
token = 'af9512dd115b1081290b9ca7f0d418a2'
data = json.loads(requests.get(url+token).text)
print(data) # success — запрос завершился успешно (true) или возникла ошибка (false)

with open('success.json', 'w', encoding='utf-8') as f:
    json.dump(data, f)

print('Выполнено')
