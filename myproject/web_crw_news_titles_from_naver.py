import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myproject.settings")
import django
django.setup()

from news.models import N_news

import requests
from bs4 import BeautifulSoup

def news_titles():
    url = 'https://news.naver.com/main/list.nhn?mode=LSD&mid=sec&sid1=105'
    r = requests.get(url)
    html = r.content

    soup = BeautifulSoup(html, 'html.parser')
    #titles = soup.select('cluster_text > a')
    titles = soup.find("div", {"class": "nclicks(fls.list)"})

    data = {}

    for title in titles:
        data[title.text] = title.get('href')
    
    return data

if __name__ == "__main__":
    news_dict = news_titles()
    for t, l in news_dict.items():
        N_news(nnews_titles=t, nnews_links=l).save()
