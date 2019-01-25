from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Platform
from django.core.files.storage import FileSystemStorage
from django.core.files import File
from django.utils import timezone
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='login')
def template(request):
	context = Platform.objects.all()
	response = {
        "context" : context
    }
	if request.method == 'POST':
		id = request.POST.get("configId")
		if id is None:
			id = request.POST.get("deployId")
			uploadDeployment(request, id)
		else:
			uploadConfig(request, id)
		return redirect('template')
	else:
		return render(request, 'template.html', response)

def uploadConfig(request, id):
	platform = get_object_or_404(Platform, id=id)

	configTemplate = request.FILES['configTemplate']
	configUploadDate = None
	if configTemplate is not None:
		fs = FileSystemStorage()
		if platform.config_template_name is not "":
			fs.delete(platform.config_template_name)
		configName = fs.save(configTemplate.name, configTemplate)
		configUrl = fs.url(configName)
		configUploadDate = timezone.now()

	Platform.objects.filter(id=id).update(config_template_name=configName, config_template_url=configUrl, config_upload_date=configUploadDate)

	return redirect('template')

def uploadDeployment(request, id):
	context = Platform.objects.all()
	response = {
        "context" : context
    }
	platform = get_object_or_404(Platform, id=id)

	deployTemplate = request.FILES['deployTemplate']
	deployUploadDate = None
	if deployTemplate is not None:
		fs = FileSystemStorage()
		if platform.deploy_template_name is not "":
			fs.delete(platform.deploy_template_name)
		deployName = fs.save(deployTemplate.name, deployTemplate)
		deployUrl = fs.url(deployName)
		deployUploadDate = timezone.now()

	Platform.objects.filter(id=id).update(deploy_template_name=deployName, deploy_template_url=deployUrl, deploy_upload_date=deployUploadDate)

	return redirect('template')

@login_required(login_url='login')
def addPlatform(request):
    if(request.method == "POST"):
        platformName = request.POST.get("platformName")
        Platform.objects.create(platform_name=platformName)
        return redirect('template')
    else :
        return render(request, 'addPlatform.html')

@login_required(login_url='login')
def editPlatform(request, id):
    platform = get_object_or_404(Platform, id=id)

    response = {
		'platform' : platform
	}

    if(request.method == "POST"):
        platformName = request.POST.get("platformName")
        Platform.objects.filter(id=id).update(platform_name=platformName)
        return redirect('template')
    else :
        return render(request, 'editPlatform.html', response)

@login_required(login_url='login')
def deletePlatform(request, id):
	platform = get_object_or_404(Platform, id=id)
	platform.delete()
	return redirect('template')
