from django.shortcuts import render, redirect
from .models import AddNews, EditNews
from .forms import AddNewsForm, EditNewsForm
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.

def listNews(request):
	return render(request, 'listNews.html')

def addNews(request):
    form = AddNewsForm(request.POST or None)
    regis = AddNews.objects.all()
    response = {
        "regis" : regis
    }
    response['form'] = form

    if(request.method == "POST" and form.is_valid()):
        crawlerName = request.POST.get("crawlerName")
        site = request.POST.get("site")
        startDate = request.POST.get("startDate")
        AddNews.objects.create(crawlerName=crawlerName, site=site, startDate=startDate)
        return redirect('listNews')
    else :
        return render(request, 'addNews.html', response)

def editNews(request):
    form = EditNewsForm(request.POST or None)
    regis = EditNews.objects.all()
    response = {
        "regis" : regis
    }
    response['form'] = form

    if(request.method == "POST" and form.is_valid()):
        crawlerName = request.POST.get("crawlerName")
        site = request.POST.get("site")
        startDate = request.POST.get("startDate")
        EditNews.objects.create(crawlerName=crawlerName, site=site, startDate=startDate)
        return redirect('listNews')
    else :
        return render(request, 'editNews.html', response)
