import requests
from bs4 import BeautifulSoup

url = 'https://news.daum.net/breakingnews/digital'
r = requests.get(url)
html = r.content

soup = BeautifulSoup(html, 'html.parser')
titles = soup.select('div.cont_thumb > strong > a')
print(titles)
# 크롤러 된 데이터를 DB에 넣기 위한 작업 필요
# 함수화 필요

