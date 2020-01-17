# todo Пройти ленту блога
# todo Зайти на страницу с записью
# todo Взять заголовок, url, список тегов и автора
# todo Сохранить в базу
import requests
from bs4 import BeautifulSoup

# todo Пройти ленту блога
domain = 'https://geekbrains.ru'
start_url = 'https://geekbrains.ru/posts?page=2'

response = requests.get(start_url)
soap = BeautifulSoup(response.text, 'lxml')
li = soap.find('ul', attrs={'class': 'gb__pagination'}).find('li', attrs={'class': 'page'})

print(1)
