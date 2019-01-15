from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import UploadConfigForm
from django.core.files.storage import FileSystemStorage
from django.core.files import File
from django.conf import settings

# Create your views here.
def template(request):
	return render(request, 'template.html')

# def handle_uploaded_file(f):
#     with open('some/file/name.txt', 'wb+') as destination:
#         for chunk in f.chunks():
#             destination.write(chunk)

def template(request):
    if request.method == 'POST':
        # form = UploadConfigForm(request.POST, request.FILES)

        # tes = handle_uploaded_file(request.FILES['document'])
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
    return render(request, 'template.html')
