from django.shortcuts import render, redirect, get_object_or_404
from .models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='login')
def listUser(request):
    context = User.objects.all()
    response = {
        "context" : context
    }
    return render(request, 'listUser.html', response)

@login_required(login_url='login')
def addUser(request):
    if(request.method == "POST"):
        username = request.POST.get("username")
        name = request.POST.get("name")
        password = request.POST.get("password")
        status = 'active'
        user = User.objects.create(username=username, name=name, password=password, status=status)
        User.objects.filter(username=user.username).update(user_id='user'+str(user.id))
        return redirect('listUser')
    else :
        return render(request, 'addUser.html')

@login_required(login_url='login')
def editUser(request, id):
    user = get_object_or_404(User, id=id)

    response = {
		'user' : user
	}

    if(request.method == "POST"):
        username = request.POST.get("username")
        name = request.POST.get("name")
        password = request.POST.get("password")
        User.objects.filter(id=id).update(username=username, name=name, password=password)
        return redirect('listUser')
    else :
        return render(request, 'editUser.html', response)

@login_required(login_url='login')
def activateUser(request, id):
    user = get_object_or_404(User, id=id)
    User.objects.filter(id=user.id).update(status='active')
    return redirect('listUser')

@login_required(login_url='login')
def deactivateUser(request, id):
	user = get_object_or_404(User, id=id)
	User.objects.filter(id=user.id).update(status='inactive')
	return redirect('listUser')
