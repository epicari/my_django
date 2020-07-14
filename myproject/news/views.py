from django.shortcuts import render
from .forms import DnewsForm
from .models import D_news, N_news

# Create your views here.

def dnews(request):
    d_form = D_news.objects.all()
    return render(request, 'dnews.html', {'d_form':d_form})

def nnews(request):
    n_form = N_news.objects.all()
    return render(request, 'nnews.html', {'n_form':n_form})

def index(request):
    return render(request, 'index.html')