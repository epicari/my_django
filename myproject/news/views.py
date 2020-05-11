from django.shortcuts import render
from .forms import NewsForm

# Create your views here.

def showForm(request):
    form = NewsForm(resuest.POST or None)
    
    if form.is_valid():
        form.save()
    
    context = {'form':form}

    #return render(request, 'templates/index.html', context)
    return rander_to_response('templates/index.html',
                               context, 
                               context_instance=RequestContext(request))