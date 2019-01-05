from django.shortcuts import render, redirect
from .models import AddSubject, EditSubject
from .forms import SubjectForm, EditForm
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.

def addsubject(request):
    form = SubjectForm(request.POST or None)
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
        return redirect('addsubject')
    else :
        return render(request, 'addsubject.html', response)

def editsubject(request):
    form = EditForm(request.POST or None)
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
        return redirect('editsubject')
    else :
        return render(request, 'editsubject.html', response)