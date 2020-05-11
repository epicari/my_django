import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myproject.settings")
import django
django.setup()

from news.models import News

import requests
from bs4 import BeautifulSoup

def news_titles():
    url = 'https://news.daum.net/breakingnews/digital'
    r = requests.get(url)
    html = r.content

    soup = BeautifulSoup(html, 'html.parser')
    titles = soup.select('div.cont_thumb > strong > a')

    data = {}

    for title in titles:
        data[title.text] = title.get('href')
    
    return data

if __name__ == "__main__": # 이 파일이 단독 실행 할 경우
    news_dict = news_titles()
    for t, l in news_dict.items():
        News(news_titles=t, news_link=l).save()
