from django.shortcuts import render, redirect
from .models import AddTopic, EditTopic
from .forms import AddTopicForm, EditTopicForm
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.

def listTopic(request):
	return render(request, 'listTopic.html')

def addTopic(request):
    form = AddTopicForm(request.POST or None)
    regis = AddTopic.objects.all()
    response = {
        "regis" : regis
    }
    response['form'] = form

    if(request.method == "POST" and form.is_valid()):
        topicName = request.POST.get("topicName")
        clientName = request.POST.get("clientName")
        description = request.POST.get("description")
        AddTopic.objects.create(topicName=topicName, clientName=clientName, description=description)
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
