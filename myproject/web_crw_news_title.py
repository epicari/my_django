import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myproject.settings")
import django
django.setup()
from abc import ABCMeta, abstractmethod

from news.models import D_news

import requests
from bs4 import BeautifulSoup

class news_titles(metaclass=ABCMeta):
    def news_titles(self): pass

class daum_titles(news_titles):
    def __init__(self, url, data):
        self.url = url
        self.data = data

    def daum_news(self):
        r = requests.get(self.url)
        html = r.content

        soup = BeautifulSoup(html, 'html.parser')
        titles = soup.select('strong.tit_thumb > a')

        for title in titles:
            self.data[title.text] = title.get('href')

        for t, l in self.data.items():
            D_news(dnews_titles=t, dnews_links=l).save()
        
        return

class main:
    url = ['https://news.daum.net/breakingnews/digital']
    data = {}
    for i in url:
        news = daum_titles(i, data)
        news.daum_news()

if __name__ == "__main__":
    main()