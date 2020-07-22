from django.contrib import admin
from .models import D_news, N_news, Question, Answer

# Register your models here.

admin.site.register(D_news)
admin.site.register(N_news)
admin.site.register(Question)
admin.site.register(Answer)