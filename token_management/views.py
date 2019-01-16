from django.shortcuts import render, redirect, get_object_or_404
from .models import Token
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
def listToken(request):
	context = Token.objects.all()
	response = {
        "context" : context
    }
	return render(request, 'listToken.html', response)

def addToken(request):
	if(request.method == "POST"):
		tokenName = request.POST.get("tokenName")
		consumerKey = request.POST.get("consumerKey")
		consumerSecret = request.POST.get("consumerSecret")
		accessKey = request.POST.get("accessKey")
		accessSecret = request.POST.get("accessSecret")
		listSubject = ""
		countSubject = 0
		Token.objects.create(token_name=tokenName, consumer_key=consumerKey, consumer_secret=consumerSecret, access_key=accessKey, access_secret=accessSecret, list_subject=listSubject, count_subject=countSubject)
		return redirect('listToken')
	else :
		return render(request, 'addToken.html')

def editToken(request, id):
    token = get_object_or_404(Token, id=id)

    response = {
		'token' : token
	}

    if(request.method == "POST"):
        tokenName = request.POST.get("tokenName")
        consumerKey = request.POST.get("consumerKey")
        consumerSecret = request.POST.get("consumerSecret")
        accessKey = request.POST.get("accessKey")
        accessSecret = request.POST.get("accessSecret")
        Token.objects.filter(id=id).update(token_name=tokenName, consumer_key=consumerKey, consumer_secret=consumerSecret, access_key=accessKey, access_secret=accessSecret)
        return redirect('listToken')
    else :
        return render(request, 'editToken.html', response)

def deleteToken(request, id):
	token = get_object_or_404(Token, id=id)
	token.delete()
	return redirect('listToken')
