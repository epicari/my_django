import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myproject.settings")
import django
django.setup()

from news.models import D_news

import requests
from bs4 import BeautifulSoup

def news_titles():
    url = 'https://news.daum.net/breakingnews/digital'
    r = requests.get(url)
    html = r.content

    soup = BeautifulSoup(html, 'html.parser')
    titles = soup.select('strong.tit_thumb > a')

    data = {}

    for title in titles:
        data[title.text] = title.get('href')
    
    return data

if __name__ == "__main__":
    news_dict = news_titles()
    for t, l in news_dict.items():
        D_news(dnews_titles=t, dnews_links=l).save()
