from django.shortcuts import render, redirect, get_object_or_404
from .models import Subject
from topic_management.models import Topic
from template_management.models import Platform
from token_management.models import Token
from django.core.files.storage import FileSystemStorage
from django.core.files import File
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone
from os import path
import yaml
from kubernetes import client, config

# Create your views here.
def index(request):
	context = Subject.objects.all()
	response = {
        "context" : context
    }
	return render(request, 'index.html', response)

def addSubject(request):
	topicAll = Topic.objects.all()
	platformAll = Platform.objects.all()
	tokenAll = Token.objects.all()
	response = {
		"topic" : topicAll,
		"platform" : platformAll,
		"token" : tokenAll
    }

	if(request.method == "POST"):
		topic = Topic.objects.get(topic_name=request.POST.get("topic"))
		subject = request.POST.get("subject")
		keyword = request.POST.get("keyword")
		platform = Platform.objects.get(platform_name=request.POST.get("platform"))
		status = 'active'
		startTime = timezone.now()
		endTime = None
		token = None
		if platform.platform_name == 'Twitter':
			token = Token.objects.get(token_name=request.POST.get("token"))
		configYaml = None
		deployYaml = None

		name = platform.platform_name+'_'+topic.topic_name+'_'+subject
		fs = FileSystemStorage()
		configTemplate = File(open(fs.path(platform.config_template_name), 'r'))
		fileName = fs.save('config_'+name+'.yaml', configTemplate)
		configYamlName = fileName
		with fs.open(fileName, 'w') as f:
			configYaml = File(f)
			for line in configTemplate:
				if '{{ name }}' in line:
					configYaml.write(line.replace('{{ name }}', name))
				elif '{{ project }}' in line:
					configYaml.write(line.replace('{{ project }}', topic.topic_name))
				elif '{{ subject }}' in line:
					configYaml.write(line.replace('{{ subject }}', subject))
				elif '{{ keywords }}' in line:
					configYaml.write(line.replace('{{ keywords }}', keyword))
				else:
					configYaml.write(line)
		configTemplate.close()

		deployTemplate = File(open(fs.path(platform.deploy_template_name), 'r'))
		fileName = fs.save('deployment_'+name+'.yaml', deployTemplate)
		with fs.open(fileName, 'w') as f:
			deployYaml = File(f)
			for line in deployTemplate:
				if '{{ name }}' in line:
					deployYaml.write(line.replace('{{ name }}', name))
				elif '{{ config_name }}' in line:
					deployYaml.write(line.replace('{{ config_name }}', 'config_'+name))
				else:
					deployYaml.write(line)
		deployTemplate.close()

		configYamlUrl = fs.url(configYaml.name)
		deployYamlName = fileName
		deployYamlUrl = fs.url(deployYaml.name)
		Subject.objects.create(topic=topic, subject=subject, keyword=keyword, platform=platform, status=status, start_time=startTime, end_time=endTime, config_yaml_name=configYamlName, config_yaml_url=configYamlUrl, deploy_yaml_name=deployYamlName, deploy_yaml_url=deployYamlUrl, token=token)
		return redirect('index')
	else :
		return render(request, 'addSubject.html', response)

def editSubject(request, id):
	subjectWithId = get_object_or_404(Subject, id=id)
	topicAll = Topic.objects.all()
	platformAll = Platform.objects.all()
	tokenAll = Token.objects.all()

	response = {
		"subject" : subjectWithId,
		"topic" : topicAll,
		"platform" : platformAll,
		"token" : tokenAll
	}

	if(request.method == "POST"):
		topic = Topic.objects.get(topic_name=request.POST.get("topic"))
		subject = request.POST.get("subject")
		keyword = request.POST.get("keyword")
		platform = Platform.objects.get(platform_name=request.POST.get("platform"))
		status = 'active'
		startTime = timezone.now()
		endTime = None
		token = None
		if platform.platform_name == 'Twitter':
			token = Token.objects.get(token_name=request.POST.get("token"))
		configYaml = None
		deployYaml = None

		name = platform.platform_name+'_'+topic.topic_name+'_'+subject
		fs = FileSystemStorage()
		if subjectWithId.config_yaml_name is not "":
			fs.delete(subjectWithId.config_yaml_name)
		configTemplate = File(open(fs.path(platform.config_template_name), 'r'))
		fileName = fs.save('config_'+name+'.yaml', configTemplate)
		configYamlName = fileName
		with fs.open(fileName, 'w') as f:
			configYaml = File(f)
			for line in configTemplate:
				if '{{ name }}' in line:
					configYaml.write(line.replace('{{ name }}', name))
				elif '{{ project }}' in line:
					configYaml.write(line.replace('{{ project }}', topic.topic_name))
				elif '{{ subject }}' in line:
					configYaml.write(line.replace('{{ subject }}', subject))
				elif '{{ keywords }}' in line:
					configYaml.write(line.replace('{{ keywords }}', keyword))
				else:
					configYaml.write(line)
		configTemplate.close()

		if subjectWithId.deploy_yaml_name is not "":
			fs.delete(subjectWithId.deploy_yaml_name)
		deployTemplate = File(open(fs.path(platform.deploy_template_name), 'r'))
		fileName = fs.save('deployment_'+name+'.yaml', deployTemplate)
		with fs.open(fileName, 'w') as f:
			deployYaml = File(f)
			for line in deployTemplate:
				if '{{ name }}' in line:
					deployYaml.write(line.replace('{{ name }}', name))
				elif '{{ config_name }}' in line:
					deployYaml.write(line.replace('{{ config_name }}', 'config_'+name))
				else:
					deployYaml.write(line)
		deployTemplate.close()

		configYamlUrl = fs.url(configYaml.name)
		deployYamlName = fileName
		deployYamlUrl = fs.url(deployYaml.name)
		Subject.objects.filter(id=id).update(topic=topic, subject=subject, keyword=keyword, platform=platform, status=status, start_time=startTime, end_time=endTime, config_yaml_name=configYamlName, config_yaml_url=configYamlUrl, deploy_yaml_name=deployYamlName, deploy_yaml_url=deployYamlUrl, token=token)
		return redirect('index')
	else :
		return render(request, 'editSubject.html', response)

def activateSubject(request, id):
    subject = get_object_or_404(Subject, id=id)
    status = 'active'
    startTime = timezone.now()
    endTime = None
    Subject.objects.filter(id=subject.id).update(status=status, start_time=startTime, end_time=endTime)
    return redirect('index')

def deactivateSubject(request, id):
	subject = get_object_or_404(Subject, id=id)
	status = 'inactive'
	endTime = timezone.now()
	Subject.objects.filter(id=subject.id).update(status=status, end_time=endTime)
	return redirect('index')

def deployConfig(request, name):
    config.load_kube_config()

    with open(path.join(path.dirname(__file__), 'config_'+name+'.yaml')) as f:
        dep = yaml.load(f)
        k8s_beta = client.CoreV1Api()
        resp = k8s_beta.create_namespaced_config_map(body=dep, namespace="staging")
        print("Config created. status='%s'" % str(resp))

def deleteConfig(request, name):
    config.load_kube_config()

    with open(path.join(path.dirname(__file__), 'config_'+name+'.yaml')) as f:
        dep = yaml.load(f)
        k8s_beta = client.CoreV1Api()
        resp = k8s_beta.delete_namespaced_config_map(name=name, namespace="staging")
        print("Config deleted. status='%s'" % str(resp))

def deployCrawler(request, name):
    config.load_kube_config()

    with open(path.join(path.dirname(__file__), 'deployment_'+name+'.yaml')) as f:
        dep = yaml.load(f)
        k8s_beta = client.ExtensionsV1beta1Api()
        resp = k8s_beta.create_namespaced_deployment(body=dep, namespace="staging")
        print("Deployment created. status='%s'" % str(resp.status))

def deleteCrawler(request, name):
    config.load_kube_config()

    with open(path.join(path.dirname(__file__), "deployment_prabowo.yaml")) as f:
        dep = yaml.load(f)
        k8s_beta = client.ExtensionsV1beta1Api()
        resp = k8s_beta.delete_namespaced_deployment(name=name, namespace="staging")
        print("Deployment created. status='%s'" % str(resp.status))
