from django.shortcuts import render, redirect
from .models import TambahPengguna, UbahPengguna, AddUser
from .forms import PenggunaForm, UbahForm, UserForm
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
def tambah(request):
    form = PenggunaForm(request.POST or None)
    regis = TambahPengguna.objects.all()
    response = {
        "regis" : regis
    }
    response['form'] = form 

    if(request.method == "POST" and form.is_valid()):
        topic = request.POST.get("topic")
        TambahPengguna.objects.create(topic=topic)
        return redirect('tambah')
    else :
        return render(request, 'tambah.html', response)

def ubahpengguna(request):
    form = UbahForm(request.POST or None)
    regis = UbahPengguna.objects.all()
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
        return redirect('ubahpengguna')
    else :
        return render(request, 'ubahpengguna.html', response)

def list(request):
	return render(request, 'list.html')

def user(request):
    form = UserForm(request.POST or None)
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
        return redirect('user')
    else :
        return render(request, 'user.html', response)