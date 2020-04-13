from rest_framework import viewsets
from .models import News
from .serializers import NewsSerializer

class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all() # News not in objects ... ??
    serializer_class = NewsSerializer