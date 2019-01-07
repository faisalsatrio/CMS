from django.shortcuts import render, redirect
from .models import AddUser, EditUser
from .forms import AddUserForm, EditUserForm
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.

def addUser(request):
    form = AddUserForm(request.POST or None)
    regis = AddUser.objects.all()
    response = {
        "regis" : regis
    }
    response['form'] = form 

    if(request.method == "POST" and form.is_valid()):
        username = request.POST.get("username")
        fullname = request.POST.get("fullname")
        password = request.POST.get("password")
        AddUser.objects.create(username=username, fullname=fullname, password=password)
        return redirect('listUser')
    else :
        return render(request, 'addUser.html', response)

def editUser(request):
    form = EditUserForm(request.POST or None)
    regis = EditUser.objects.all()
    response = {
        "regis" : regis
    }
    response['form'] = form 

    if(request.method == "POST" and form.is_valid()):
        userid = request.POST.get("userid")
        username = request.POST.get("username")
        name = request.POST.get("name")
        password = request.POST.get("password")
        UbahPengguna.objects.create(userid=userid, username=username, name=name, password=password)
        return redirect('listUser')
    else :
        return render(request, 'editUser.html', response)

def listUser(request):
	return render(request, 'listUser.html')