from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.core.paginator import Paginator
from .forms import DnewsForm, NnewsForm, QuestionForm, AnswerForm
from .models import D_news, N_news, Question, Answer

# Create your views here.

def dnews(request):
    d_form = D_news.objects.all()
    return render(request, 'dnews.html', {'d_form' : d_form})

def nnews(request):
    n_form = N_news.objects.all()
    return render(request, 'nnews.html', {'n_form' : n_form})

def index(request):
    page = request.GET.get('page', '1')
    question_list = Question.objects.order_by('-date')
    paginator = Paginator(question_list, 10)
    page_obj = paginator.get_page(page)
    return render(request, 'index.html', {'question_list' : page_obj})

def detail(request, q_id): #글 디테일
    #question = Question.get(id=q_id)
    question = get_object_or_404(Question, pk=q_id)
    return render(request, 'detail.html', {'question' : question})

def question_create(request):
    if request.method == 'POST':
        q_form = QuestionForm(request.POST)
        if q_form.is_valid():
            question = q_form.save(commit=False)
            question.date = timezone.now()
            question.save()
            return redirect('index')
    else:
        q_form = QuestionForm()
    return render(request, 'question_form.html', {'q_form' : q_form})

def answer_create(request, q_id):
    '''
    question = get_object_or_404(Question, pk=q_id)
    question.answer_set.create(content=request.POST.get('content'), date=timezone.now())
    return redirect('detail', q_id=question.id)
    '''
    question = get_object_or_404(Question, pk=q_id)
    
    if request.method == 'POST':
        q_form = AnswerForm(request.POST)
        if q_form.is_valid():
            answer = q_form.save(commit=False) #date 처럼 자동 생성 값을 가진 객체가 있을 경우 사용
            answer.date = timezone.now()
            answer.question = question
            answer.save()
            return redirect('detail', q_id=question.id)
    else:
        q_form = AnswerForm()
    
    context = {'question' : question, 'q_form' : q_form}
    return render(request, 'detail.html', context)