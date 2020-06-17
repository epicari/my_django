from django.db import models

# Create your models here.
# 이 클래스는 추후 DB의 Table로 사용함
# titles와 link 라는 column을 가진 News라는 이름의 Table 

class D_news(models.Model):
    dnews_titles = models.CharField(max_length=255)
    dnews_links = models.URLField()

    def __str__(self):
        return self.dnews_titles

class N_news(models.Model):
    nnews_titles = models.CharField(max_length=255)
    nnews_links = models.URLField()

    def __str__(self):
        return self.nnews_titles