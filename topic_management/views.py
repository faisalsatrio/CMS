from django.shortcuts import render, redirect, get_object_or_404
from .models import Topic
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='login')
def listTopic(request):
	storage = messages.get_messages(request)
	context = Topic.objects.all()
	response = {
        "context" : context,
		"messages" : storage
    }
	return render(request, 'listTopic.html', response)

@login_required(login_url='login')
def addTopic(request):
	if(request.method == "POST"):
		topicName = request.POST.get("topicName")
		clientName = request.POST.get("clientName")
		description = request.POST.get("description")
		try:
			Topic.objects.create(topic_name=topicName, client_name=clientName, description=description)
		except:
			messages.error(request, 'There is something wrong when adding a topic')
		return redirect('listTopic')
	else :
		return render(request, 'addTopic.html')

@login_required(login_url='login')
def editTopic(request, id):
	topic = get_object_or_404(Topic, id=id)

	response = {
		'topic' : topic
	}


	if(request.method == "POST"):
		try:
			topic.delete()
			topicName = request.POST.get("topicName")
			clientName = request.POST.get("clientName")
			description = request.POST.get("description")
			Topic.objects.create(topic_name=topicName, client_name=clientName, description=description)
		except:
			messages.error(request, topic.topic_name + ' is being used by Social Media Crawler')
		return redirect('listTopic')
	else :
		return render(request, 'editTopic.html', response)

@login_required(login_url='login')
def deleteTopic(request, id):
	topic = get_object_or_404(Topic, id=id)
	try:
		topic.delete()
	except:
		messages.error(request, topic.topic_name + ' is being used by Social Media Crawler')
	return redirect('listTopic')
