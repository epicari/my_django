from django import forms
from .models import N_news, D_news

class DnewsForm(forms.ModelForm):
    class Meta:
        model = D_news
        fields = ["dnews_titles", "dnews_links"]

class NnewsForm(forms.ModelForm):
    class Meta:
        model = N_news
        fields = ["nnews_titles", "nnews_links"]