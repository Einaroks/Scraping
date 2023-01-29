import requests
from bs4 import BeautifulSoup

url = 'https://www.delfi.lv/'

request = requests.get(url)

page = request.content
html = BeautifulSoup(page, 'lxml')

articles = html.find_all('a', class_='text-mine-shaft')

class Article():
    title = ''
    content = ''
    link = ''

for i in range(50):
    