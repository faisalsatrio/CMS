from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('user/', views.listUser, name='listUser'),
    path('user/add/', views.addUser, name='addUser'),
    path('user/edit/id=<int:id>/', views.editUser, name='editUser'),
    path('user/activate/id=<int:id>/', views.activateUser, name='activateUser'),
    path('user/deactivate/id=<int:id>/', views.deactivateUser, name='deactivateUser'),
]
