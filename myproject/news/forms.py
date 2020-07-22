from django import forms
from .models import D_news, N_news, Question, Answer

class DnewsForm(forms.ModelForm):
    class Meta:
        model = D_news
        fields = ["dnews_titles", "dnews_links"]

class NnewsForm(forms.ModelForm):
    class Meta:
        model = N_news
        fields = ["nnews_titles", "nnews_links"]

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['subject', 'content']
        labels = {
            'subject': '제목',
            'content': '내용',
        }
        #자동 폼 쓸 땐 위젯, {{ form.as_p }}
        '''
        widgets = {
            'subject': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 10}),
        } #위젯 추가 시 부트스트랩 적용 가능함
        '''

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['content']
        labels = {
            'content': '내용',
        }