from django.shortcuts import render, redirect
from .models import AddSubject, EditSubject
from .forms import AddSubjectForm, EditSubjectForm
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
def index(request):
	return render(request, 'index.html')

def addSubject(request):
    form = AddSubjectForm(request.POST or None)
    regis = AddSubject.objects.all()
    response = {
        "regis" : regis
    }
    response['form'] = form

    if(request.method == "POST" and form.is_valid()):
        topic = request.POST.get("topic")
        subject = request.POST.get("subject")
        keyword = request.POST.get("keyword")
        platform = request.POST.get("platform")
        AddSubject.objects.create(topic=topic, subject=subject, keyword=keyword, platform=platform)
        return redirect('addSubject')
    else :
        return render(request, 'addSubject.html', response)

def editSubject(request):
    form = EditSubjectForm(request.POST or None)
    regis = EditSubject.objects.all()
    response = {
        "regis" : regis
    }
    response['form'] = form

    if(request.method == "POST" and form.is_valid()):
        topic = request.POST.get("topic")
        subject = request.POST.get("subject")
        keyword = request.POST.get("keyword")
        platform = request.POST.get("platform")
        EditSubject.objects.create(topic=topic, subject=subject, keyword=keyword, platform=platform)
        return redirect('editSubject')
    else :
        return render(request, 'editSubject.html', response)
