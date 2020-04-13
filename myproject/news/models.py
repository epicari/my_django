from django.db import models

# Create your models here.

class News(models.Model):
    news_id = models.AutoField(primary_key=True)
    news_heading = models.CharField(max_length=250)
    news_body = models.TextField()