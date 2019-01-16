from django.shortcuts import render, redirect, get_object_or_404
from .models import Subject
from topic_management.models import Topic
from template_management.models import Platform
from token_management.models import Token
from django.conf import settings
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
		if platform.platform_name == 'twitter':
			token = Token.objects.get(token_name=request.POST.get("token"))
		configYaml = None
		deployYaml = None

		name = platform.platform_name+'-'+topic.topic_name+'-'+subject
		fs = FileSystemStorage()
		configTemplate = File(open(fs.path(platform.config_template_name), 'r'))
		fileName = fs.save('config-'+name+'.yaml', configTemplate)
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
		fileName = fs.save('crawler-'+name+'.yaml', deployTemplate)
		with fs.open(fileName, 'w') as f:
			deployYaml = File(f)
			for line in deployTemplate:
				if '{{ name }}' in line:
					deployYaml.write(line.replace('{{ name }}', name))
				elif '{{ config_name }}' in line:
					deployYaml.write(line.replace('{{ config_name }}', 'config-'+name))
				else:
					deployYaml.write(line)
		deployTemplate.close()

		configYamlUrl = fs.url(configYaml.name)
		deployYamlName = fileName
		deployYamlUrl = fs.url(deployYaml.name)
		subjectWithId = Subject.objects.create(topic=topic, subject=subject, keyword=keyword, platform=platform, status=status, start_time=startTime, config_yaml_name=configYamlName, config_yaml_url=configYamlUrl, deploy_yaml_name=deployYamlName, deploy_yaml_url=deployYamlUrl, token=token)

		# update token.list_subject and token.count_subject
		token.list_subject = token.list_subject + subjectWithId.subject + ", "
		token.count_subject = token.count_subject + 1
		token.save()

		# activateSubject(request, subjectWithId.id)
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
		# update token.list_subject and token.count_subject
		token.list_subject = token.list_subject.replace(subjectWithId.subject + ", ", "replaceThis")

		# deleteCrawler(request, subjectWithId.id)
		# deleteConfig(requst, subjectWithId.id)
		topic = Topic.objects.get(topic_name=request.POST.get("topic"))
		subject = request.POST.get("subject")
		keyword = request.POST.get("keyword")
		platform = Platform.objects.get(platform_name=request.POST.get("platform"))
		status = 'active'
		startTime = timezone.now()
		endTime = None
		token = None
		if platform.platform_name == 'twitter':
			token = Token.objects.get(token_name=request.POST.get("token"))
		configYaml = None
		deployYaml = None

		name = platform.platform_name+'-'+topic.topic_name+'-'+subject
		fs = FileSystemStorage()
		if subjectWithId.config_yaml_name is not "":
			fs.delete(subjectWithId.config_yaml_name)
		configTemplate = File(open(fs.path(platform.config_template_name), 'r'))
		fileName = fs.save('config-'+name+'.yaml', configTemplate)
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
		fileName = fs.save('crawler-'+name+'.yaml', deployTemplate)
		with fs.open(fileName, 'w') as f:
			deployYaml = File(f)
			for line in deployTemplate:
				if '{{ name }}' in line:
					deployYaml.write(line.replace('{{ name }}', name))
				elif '{{ config_name }}' in line:
					deployYaml.write(line.replace('{{ config_name }}', 'config-'+name))
				else:
					deployYaml.write(line)
		deployTemplate.close()

		configYamlUrl = fs.url(configYaml.name)
		deployYamlName = fileName
		deployYamlUrl = fs.url(deployYaml.name)
		subjectWithId = Subject.objects.filter(id=id).update(topic=topic, subject=subject, keyword=keyword, platform=platform, status=status, start_time=startTime, end_time=endTime, config_yaml_name=configYamlName, config_yaml_url=configYamlUrl, deploy_yaml_name=deployYamlName, deploy_yaml_url=deployYamlUrl, token=token)

		# update token.list_subject and token.count_subject
		token.list_subject = token.list_subject.replace("replaceThis", subjectWithId.subject + ", ")
		token.save()

		# activateSubject(request, subjectWithId.id)
		return redirect('index')
	else :
		return render(request, 'editSubject.html', response)

def activateSubject(request, id):
    subject = get_object_or_404(Subject, id=id)
    status = 'active'
    startTime = timezone.now()
    endTime = None

	# update token.list_subject and token.count_subject
    subject.token.list_subject = subject.token.list_subject + subject.subject + ", "
    subject.token.count_subject = subject.token.count_subject + 1
    subject.token.save()

    Subject.objects.filter(id=subject.id).update(status=status, start_time=startTime, end_time=endTime)
    # deployConfig(request, id)
    # deployCrawler(request, id)
    return redirect('index')

def deactivateSubject(request, id):
	subject = get_object_or_404(Subject, id=id)
	status = 'inactive'
	endTime = timezone.now()

	# update token.list_subject and token.count_subject
	subject.token.list_subject = subject.token.list_subject.replace(subject.subject + ", ", "")
	subject.token.count_subject = subject.token.count_subject - 1
	subject.token.save()

	Subject.objects.filter(id=subject.id).update(status=status, end_time=endTime)
	# deleteCrawler(request, id)
	# deleteConfig(requst, id)
	return redirect('index')

def deployConfig(request, id):
	subject = Subject.objects.get(id=id)
	config.load_kube_config()

	with open(path.join(settings.MEDIA_ROOT, "config-"+subject.platform.platform_name+"-"+subject.topic.topic_name+"-"+subject.subject+".yaml")) as f:
		dep = yaml.load(f)
		k8s_beta = client.CoreV1Api()
		resp = k8s_beta.create_namespaced_config_map(body=dep, namespace="staging")
		print("Config created. status='%s'" % str(resp))
	return redirect('activateSubject', id)

def deleteConfig(request, id):
	subject = Subject.objects.get(id=id)
	config.load_kube_config()

	with open(path.join(settings.MEDIA_ROOT, "config-"+subject.platform.platform_name+"-"+subject.topic.topic_name+"-"+subject.subject+".yaml")) as f:
		dep = yaml.load(f)
		k8s_beta = client.CoreV1Api()
		resp = k8s_beta.delete_namespaced_config_map(name="config-"+subject.platform.platform_name+"-"+subject.topic.topic_name+"-"+subject.subject, namespace="staging")
		print("Config deleted. status='%s'" % str(resp))
	return redirect('deactivateSubject', id)

def deployCrawler(request, id):
	subject = Subject.objects.get(id=id)
	config.load_kube_config()

	with open(path.join(settings.MEDIA_ROOT, "crawler-"+subject.platform.platform_name+"-"+subject.topic.topic_name+"-"+subject.subject+".yaml")) as f:
		dep = yaml.load(f)
		k8s_beta = client.ExtensionsV1beta1Api()
		resp = k8s_beta.create_namespaced_deployment(body=dep, namespace="staging")
		print("Deployment created. status='%s'" % str(resp.status))
	return redirect('activateSubject', id)

def deleteCrawler(request, id):
	subject = Subject.objects.get(id=id)
	config.load_kube_config()

	with open(path.join(settings.MEDIA_ROOT, "crawler-"+subject.platform.platform_name+"-"+subject.topic.topic_name+"-"+subject.subject+".yaml")) as f:
		dep = yaml.load(f)
		k8s_beta = client.ExtensionsV1beta1Api()
		resp = k8s_beta.delete_namespaced_deployment(name="crawler-"+subject.platform.platform_name+"-"+subject.topic.topic_name+"-"+subject.subject, namespace="staging", body=dep)
		print("Deployment created. status='%s'" % str(resp.status))
	return redirect('deactivateSubject', id)
