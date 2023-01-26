import requests
from bs4 import BeautifulSoup

url = 'https://www.delfi.lv/'

request = requests.get(url)

page = request.content
html = BeautifulSoup(page, 'lxml')