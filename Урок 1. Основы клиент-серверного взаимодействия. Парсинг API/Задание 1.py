# 1. Посмотреть документацию к API GitHub, разобраться как вывести список репозиториев для конкретного пользователя,
# сохранить JSON-вывод в файле *.json.

import requests
import json
username = input('Enter the github username:')
request = requests.get('https://api.github.com/users/'+username+'/repos')
response = request.json()

repo = {str(i+1):response[i]['name'] for i in range(len(response))}
print(repo)

with open('list_repo.json', 'w', encoding='utf-8') as f:
    json.dump(repo, f)

print('Выполнено')




