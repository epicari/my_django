from django.db import models

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