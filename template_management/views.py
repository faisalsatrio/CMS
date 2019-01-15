from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Platform
from django.core.files.storage import FileSystemStorage
from django.core.files import File
from django.conf import settings

# Create your views here.
def template(request):
	context = Platform.objects.all()
	response = {
        "context" : context
    }
	if request.method == 'POST':
		tes = request.FILES['document']
		fs = FileSystemStorage()
		name = fs.save(tes.name, tes)

		sumber = File(open(fs.path(name), 'r'))
		pro = "protest"
		sub = "subtest"
		with open(settings.YAML_ROOT+pro+'-'+sub+'.yaml', 'w') as f:
			myfile = File(f)
			for line in sumber:
				if '{{ name }}' in line:
					myfile.write(line.replace('{{ name }}', pro+'-'+sub+'.yaml'))
				else:
					myfile.write(line)
		sumber.close()
	return render(request, 'template.html', response)

def addPlatform(request):
    if(request.method == "POST"):
        platformName = request.POST.get("platformName")
        Platform.objects.create(platform_name=platformName)
        return redirect('template')
    else :
        return render(request, 'addPlatform.html')

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

def deletePlatform(request, id):
	platform = get_object_or_404(Platform, id=id)
	platform.delete()
	return redirect('template')
