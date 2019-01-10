from django.shortcuts import render, redirect, get_object_or_404
from .models import Topic
from .forms import TopicForm
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages

# Create your views here.

def listTopic(request):
	context = Topic.objects.all()
	response = {
        "context" : context
    }
	return render(request, 'listTopic.html', response)

def addTopic(request):
    if(request.method == "POST"):
        topicName = request.POST.get("topicName")
        clientName = request.POST.get("clientName")
        description = request.POST.get("description")
        Topic.objects.create(topic_name=topicName, client_name=clientName, description=description)
        return redirect('listTopic')
    else :
        return render(request, 'addTopic.html')

def editTopic(request, id):
    topic = get_object_or_404(Topic, id=id)

    response = {
		'topic' : topic
	}

    if(request.method == "POST"):
        topicName = request.POST.get("topicName")
        clientName = request.POST.get("clientName")
        description = request.POST.get("description")
        Topic.objects.filter(id=id).update(topic_name=topicName, client_name=clientName, description=description)
        return redirect('listTopic')
    else :
        return render(request, 'editTopic.html', response)

def deleteTopic(request, id):
	topic = get_object_or_404(Topic, id=id)
	topic.delete()
	return redirect('listTopic')
