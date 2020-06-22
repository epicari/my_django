from django import forms
from .models import D_news

class DnewsForm(forms.ModelForm):
    class Meta:
        model = D_news
        fields = ["dnews_titles", "dnews_links"]