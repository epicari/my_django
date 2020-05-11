from django.db import models

# Create your models here.
# 이 클래스는 추후 DB의 Table로 사용함
# titles와 link 라는 column을 가진 News라는 이름의 Table 

class News(models.Model):
    news_titles = models.CharField(max_length=255)
    news_link = models.URLField()

    def __str__(self):
        return self.news_titles