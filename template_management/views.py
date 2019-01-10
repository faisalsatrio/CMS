from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import UploadConfigForm
from django.core.files.storage import FileSystemStorage

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
        print(tes.name)
        print(tes.size)
        fs = FileSystemStorage()
        fs.save(tes.name, tes)
    return render(request, 'template.html')
