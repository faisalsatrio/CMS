from django.shortcuts import render, redirect, get_object_or_404
from .models import Token
from django.http import HttpResponse, HttpResponseRedirect
from kubernetes import client, config
import kubernetes
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='login')
def listToken(request):
	context = Token.objects.all()
	response = {
        "context" : context
    }
	return render(request, 'listToken.html', response)

@login_required(login_url='login')
def addToken(request):
	if(request.method == "POST"):
		tokenName = request.POST.get("tokenName")
		consumerKey = request.POST.get("consumerKey")
		consumerSecret = request.POST.get("consumerSecret")
		accessKey = request.POST.get("accessKey")
		accessSecret = request.POST.get("accessSecret")
		listSubject = ""
		countSubject = 0
		token = Token.objects.create(token_name=tokenName, consumer_key=consumerKey, consumer_secret=consumerSecret, access_key=accessKey, access_secret=accessSecret, list_subject=listSubject, count_subject=countSubject)
		try:
			submitToken(request, token.id)
		except:
			Token.objects.filter(id=token.id).delete()
			messages.error(request, 'There is something wrong with Kubernetes when adding a token')
		return redirect('listToken')
	else :
		return render(request, 'addToken.html')

@login_required(login_url='login')
def editToken(request, id):
	token = get_object_or_404(Token, id=id)

	response = {
		'token' : token
	}

	if(request.method == "POST"):
		try:
			unsubmitToken(request, id)
			tokenName = request.POST.get("tokenName")
			consumerKey = request.POST.get("consumerKey")
			consumerSecret = request.POST.get("consumerSecret")
			accessKey = request.POST.get("accessKey")
			accessSecret = request.POST.get("accessSecret")
			token = Token.objects.filter(id=id).update(token_name=tokenName, consumer_key=consumerKey, consumer_secret=consumerSecret, access_key=accessKey, access_secret=accessSecret)
			submitToken(request, id)
		except:
			messages.error(request, 'There is something wrong with Kubernetes when editing a token')
		return redirect('listToken')
	else :
		return render(request, 'editToken.html', response)

@login_required(login_url='login')
def deleteToken(request, id):
	token = get_object_or_404(Token, id=id)
	try:
		unsubmitToken(request, id)
		token.delete()
	except:
		messages.error(request, 'There is something wrong with Kubernetes when deleting a token')
	return redirect('listToken')

def submitToken(request, id):
	token = get_object_or_404(Token, id=id)

	config.load_kube_config()
	k8s_beta = client.CoreV1Api()

	body = kubernetes.client.V1Secret()
	body.metadata = kubernetes.client.V1ObjectMeta(name=token.token_name)
	body.string_data = {
        "TWITTER_ACCESS_KEY": token.access_key,
        "TWITTER_ACCESS_SECRET": token.access_secret,
        "TWITTER_CONSUMER_KEY": token.consumer_key,
        "TWITTER_CONSUMER_SECRET": token.consumer_secret
    }

	resp = k8s_beta.create_namespaced_secret(body=body, namespace="staging")
	print("Secret created. status='%s'" % str(resp))

def unsubmitToken(request, id):
	token = get_object_or_404(Token, id=id)

	config.load_kube_config()
	k8s_beta = client.CoreV1Api()

	body = kubernetes.client.V1Secret()
	body.metadata = kubernetes.client.V1ObjectMeta(name=token.token_name)

	resp = k8s_beta.delete_namespaced_secret(name=token.token_name, body=body, namespace="staging")
	print("Secret deleted. status='%s'" % str(resp))
