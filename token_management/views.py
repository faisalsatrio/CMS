from django.shortcuts import render, redirect
from .models import AddToken, EditToken
from .forms import AddTokenForm, EditTokenForm
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
def listToken(request):
	return render(request, 'listToken.html')

def addToken(request):
    form = AddTokenForm(request.POST or None)
    regis = AddToken.objects.all()
    response = {
        "regis" : regis
    }
    response['form'] = form

    if(request.method == "POST" and form.is_valid()):
	    tokenName = request.POST.get("tokenName")
	    consumerKey = request.POST.get("consumerKey")
	    consumerSecret = request.POST.get("consumerSecret")
	    accessKey = request.POST.get("accessKey")
	    accessSecret = request.POST.get("accessSecret")
	    AddToken.objects.create(token_name=tokenName, consumer_key=consumerKey, consumer_secret=consumerSecret, access_key=accessKey, access_secret=accessSecret)
	    return redirect('addToken')
    else :
        return render(request, 'addToken.html', response)

def editToken(request):
    form = EditTokenForm(request.POST or None)
    regis = EditToken.objects.all()
    response = {
        "regis" : regis
    }
    response['form'] = form

    if(request.method == "POST" and form.is_valid()):
        tokenName = request.POST.get("tokenName")
        consumerKey = request.POST.get("consumerKey")
        consumerSecret = request.POST.get("consumerSecret")
        accessKey = request.POST.get("accessKey")
        accessSecret = request.POST.get("accessSecret")
        EditToken.objects.create(token_name=tokenName, consumer_key=consumerKey, consumer_secret=consumerSecret, access_key=accessKey, access_secret=accessSecret)
        return redirect('editToken')
    else :
        return render(request, 'editToken.html', response)
