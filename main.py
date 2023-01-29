import requests
from bs4 import BeautifulSoup

url = 'https://www.delfi.lv/'

request = requests.get(url)

page = request.content
html = BeautifulSoup(page, 'lxml')

htmlarticles = html.find_all('a', class_='text-mine-shaft')
articles = []

class Article():
    title = ''
    content = ''
    link = ''

for i in range(50): # number of articles to scrape
    article = Article()
    article.title = htmlarticles[i].get_text()
    articles.append(article)

    article.link = htmlarticles[i]['href']

    requestArticle = requests.get(article.link)
    article_content = requestArticle.content
    html_article = BeautifulSoup(article_content, 'lxml')
    body = html_article.find_all('div', class_='col offset-md-1')
    x = body[0].find_all('p')
    text = []
    for j in range(len(x)):
        paragraph = x[j].get_text()
        text.append(paragraph)
    final_content = ' '.join(text)

    article.content = final_content

print(articles[20].content)