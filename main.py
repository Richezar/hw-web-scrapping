import requests
import bs4
from fake_headers import Headers

KEYWORDS = ['дизайн', 'фото', 'web', 'python']

headers = Headers(os="mac", headers=True).generate()

response = requests.get('https://habr.com/ru/articles/', headers=headers)
soup = bs4.BeautifulSoup(response.text, features='lxml')

articles_list = soup.findAll('div', class_='tm-article-snippet')

for article in articles_list:
    span_title = article.find('a', class_='tm-title__link').text
    text = article.find('div', class_='article-formatted-body').text
    for i in KEYWORDS:
        if i.lower() in span_title.lower() or i.lower() in text.lower():
            post_link = article.find('a', class_='tm-title__link')['href']
            public_date = article.find('a', class_='tm-article-datetime-published').time['title']
            print(f'Дата: {public_date} - Заголовок: {span_title} - Ссылка: https://habr.com{post_link}')

