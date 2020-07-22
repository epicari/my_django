
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myproject.settings")
import django
django.setup()

from abc import ABCMeta, abstractmethod

from news.models import D_news, N_news

import requests
from bs4 import BeautifulSoup

class news(metaclass=ABCMeta): 
    @abstractmethod
    def news_titles(self, soup: str): pass

class daum(news):    
    def news_titles(self, soup):
        data = {}
        titles = soup.select('strong.tit_thumb > a')

        for title in titles:
            data[title.text] = title.get('href')

        for t, l in data.items():
            D_news(dnews_titles=t, dnews_links=l).save()
        
        return

class naver(news):    
    def news_titles(self, soup):
        data = {}
        titles = soup.find_all('a', class_='cluster_text_headline nclicks(cls_sci.clsart)')

        for title in titles:
            data[title.text] = title.get('href')

        for t, l in data.items():
            N_news(nnews_titles=t, nnews_links=l).save()
        
        return   

class news_title:
    def getnews(self, soup, name):
        return name.news_titles(soup)

class main:
    def get_obj(self, url):
        r = requests.get(url)
        html = r.content
        soup = BeautifulSoup(html, 'html.parser')
        return soup

    def run(self):
        url = ['https://news.daum.net/breakingnews/digital',
               'https://news.naver.com/main/main.nhn?mode=LSD&mid=shm&sid1=105']
        d = news_title()
        d.getnews(self.get_obj(url[0]), daum())
        n = news_title()
        n.getnews(self.get_obj(url[1]), naver())

main().run()