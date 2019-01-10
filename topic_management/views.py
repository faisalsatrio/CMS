from django.shortcuts import render, redirect
from .models import Topic
from .forms import TopicForm
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.

def listTopic(request):
	context = Topic.objects.all()
	response = {
        "context" : context
    }
	return render(request, 'listTopic.html', response)

def addTopic(request):
    form = TopicForm(request.POST or None)

    response = {}
    response['form'] = form

    if(request.method == "POST" and form.is_valid()):
        topicName = request.POST.get("topicName")
        clientName = request.POST.get("clientName")
        description = request.POST.get("description")
        Topic.objects.create(topic_name=topicName, client_name=clientName, description=description)
        return redirect('listTopic')
    else :
        return render(request, 'addTopic.html', response)

def editTopic(request):
    form = EditTopicForm(request.POST or None)
    regis = EditTopic.objects.all()
    response = {
        "regis" : regis
    }
    response['form'] = form

    if(request.method == "POST" and form.is_valid()):
        topicName = request.POST.get("topicName")
        clientName = request.POST.get("clientName")
        description = request.POST.get("description")
        EditTopic.objects.create(topic_name=topicName, client_name=clientName, description=description)
        return redirect('editTopic')
    else :
        return render(request, 'editTopic.html', response)

def deleteTopic(request, id):
	Topic.objects.get(id=id).delete()
	return redirect('listTopic')
