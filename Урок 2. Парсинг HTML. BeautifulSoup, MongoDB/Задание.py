# используя bs4
# ресурс: https://geekbrains.ru/posts
# получить страницу с статьей, извлеч след данные:
# todoзаголовок статьи
# дата публикации
# url статьи
# список тегов
# имя автора
# url автора
#
# при помощи sqlalchemy сохранить данные в базу.
# обязательно теги и автор должны существовать отдельными таблицами, и должны быть корректно реализованы соответсвующие связи.

import requests
from bs4 import BeautifulSoup as BS
# todo пройти ленту, статей блога
domain = 'https://geekbrains.ru'
start_url = 'https://geekbrains.ru/posts?page=2'

response = requests.get(start_url)
soap = BS(response.text, 'lxml')
li = soap.find('ul', attrs={'class': 'gb__pagination'}).find('li', attrs={'class': 'page'})

print(1)