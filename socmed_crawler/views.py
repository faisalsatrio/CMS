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
	topic = Topic.objects.all()
	platform = Platform.objects.all()
	token = Token.objects.all()
	response = {
		"topic" : topic,
		"platform" : platform,
		"token" : token
    }

	if(request.method == "POST"):
		topic = request.POST.get("topic")
		subject = request.POST.get("subject")
		keyword = request.POST.get("keyword")
		platform = request.POST.get("platform")
		status = 'active'
		startTime = timezone.now()
		endTime = None
		token = None
		if platform == 'Twitter':
			token = request.POST.get("platform")
		configYaml = None
		deployYaml = None

		name = platform+'_'+topic+'_'+subject
		if fs.exist('config_'+name+'.yaml'):
			fs.delete('config_'+name+'.yaml')
		configTemplate = File(Platform.objects.get(platform_name=platform).config_template)
		with open(settings.YAML_ROOT+'config_'+name+'.yaml', 'w') as f:
			configYaml = File(f)
			for line in sumber:
				if '{{ name }}' in line:
					configYaml.write(line.replace('{{ name }}', name))
				elif '{{ project }}' in line:
					configYaml.write(line.replace('{{ project }}', topic))
				elif '{{ subject }}' in line:
					configYaml.write(line.replace('{{ subject }}', subject))
				elif '{{ keywords }}' in line:
					configYaml.write(line.replace('{{ keywords }}', keywords))
				else:
					configYaml.write(line)
		configTemplate.close()

		if fs.exist('deployment_'+name+'.yaml'):
			fs.delete('deployment_'+name+'.yaml')
		deployTemplate = File(Platform.objects.get(platform_name=platform).deploy_template)
		with open(settings.YAML_ROOT+'deployment_'+name+'.yaml', 'w') as f:
			deployYaml = File(f)
			for line in sumber:
				if '{{ name }}' in line:
					deployYaml.write(line.replace('{{ name }}', name))
				elif '{{ config_name }}' in line:
					deployYaml.write(line.replace('{{ config_name }}', 'config_'+name))
				else:
					deployYaml.write(line)
		deployTemplate.close()

		Subject.objects.create(topic=topic, subject=subject, keyword=keyword, platform=platform, status=status, start_time=startTime, endTime=None, config_yaml=configYaml, deploy_yaml=deployYaml, token=token)
		return redirect('index')
	else :
		return render(request, 'addSubject.html', response)

def editSubject(request, id):
	topic = Topic.objects.all()
	subject = get_object_or_404(Subject, id=id)
	platform = Platform.objects.all()
	token = Token.objects.all()

	response = {
		"subject" : subject,
		"topic" : topic,
		"platform" : platform,
		"token" : token
	}

	if(request.method == "POST"):
		topic = request.POST.get("topic")
		subject = request.POST.get("subject")
		keyword = request.POST.get("keyword")
		platform = request.POST.get("platform")
		status = 'active'
		startTime = timezone.now()
		endTime = None
		token = None
		if platform == 'Twitter':
			token = request.POST.get("platform")
		configYaml = None
		deployYaml = None

		name = platform+'_'+topic+'_'+subject
		fs = FileSystemStorage()
		if fs.exist('config_'+name+'.yaml'):
			fs.delete('config_'+name+'.yaml')
		configTemplate = File(Platform.objects.get(platform_name=platform).config_template)
		with open(settings.YAML_ROOT+'config_'+name+'.yaml', 'w') as f:
			configYaml = File(f)
			for line in sumber:
				if '{{ name }}' in line:
					configYaml.write(line.replace('{{ name }}', name))
				elif '{{ project }}' in line:
					configYaml.write(line.replace('{{ project }}', topic))
				elif '{{ subject }}' in line:
					configYaml.write(line.replace('{{ subject }}', subject))
				elif '{{ keywords }}' in line:
					configYaml.write(line.replace('{{ keywords }}', keywords))
				else:
					configYaml.write(line)
		configTemplate.close()

		deployTemplate = File(Platform.objects.get(platform_name=platform).deploy_template)
		with open(settings.YAML_ROOT+'deployment_'+name+'.yaml', 'w') as f:
			deployYaml = File(f)
			for line in sumber:
				if '{{ name }}' in line:
					deployYaml.write(line.replace('{{ name }}', name))
				elif '{{ config_name }}' in line:
					deployYaml.write(line.replace('{{ config_name }}', 'config_'+name))
				else:
					deployYaml.write(line)
		deployTemplate.close()

		Subject.objects.filter(id=id).update(topic=topic, subject=subject, keyword=keyword, platform=platform, status=status, start_time=startTime, endTime=None, config_yaml=configYaml, deploy_yaml=deployYaml, token=token)
		return redirect('index')
	else :
		return render(request, 'editSubject.html', response)

def activateSubject(request, id):
    subject = get_object_or_404(Subject, id=id)
    Subject.objects.filter(id=user.id).update(status='active')
    return redirect('index')

def deactivateSubject(request, id):
	subject = get_object_or_404(Subject, id=id)
	Subject.objects.filter(id=user.id).update(status='inactive')
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
