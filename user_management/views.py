from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

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
        firstName = request.POST.get("firstName")
        lastName = request.POST.get("lastName")
        password = request.POST.get("password")
        status = 'active'
        user = User.objects.create_user(username=username, first_name=firstName, last_name=lastName, password=password)
        return redirect('listUser')
    else :
        return render(request, 'addUser.html')

@login_required(login_url='login')
def editUser(request, id):
    user = get_object_or_404(User, id=id)

    response = {
		'users' : user
	}

    if(request.method == "POST"):
        username = request.POST.get("username")
        firstName = request.POST.get("firstName")
        lastName = request.POST.get("lastName")
        password = request.POST.get("password")
        User.objects.filter(id=id).update(username=username, first_name=firstName, last_name=lastName, is_active=True)
        user = User.objects.get(id=id)
        user.set_password(password)
        user.save()
        return redirect('listUser')
    else :
        return render(request, 'editUser.html', response)

@login_required(login_url='login')
def activateUser(request, id):
    if request.user.is_superuser == True:
        user = get_object_or_404(User, id=id)
        User.objects.filter(id=user.id).update(is_active=True)
        return redirect('listUser')

@login_required(login_url='login')
def deactivateUser(request, id):
    if request.user.is_superuser == True:
        user = get_object_or_404(User, id=id)
        User.objects.filter(id=user.id).update(is_active=False)
        return redirect('listUser')
