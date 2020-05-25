from django.shortcuts import render
from .forms import NewsForm
from .models import News

# Create your views here.

def news(request):
    form = News.objects.all()
    return render(request, 'news.html', {'form':form})

def index(request):
    return render(request, 'index.html')