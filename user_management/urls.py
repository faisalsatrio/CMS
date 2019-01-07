from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('user/', views.listUser, name='listUser'),
    path('user/add', views.addUser, name='addUser'),
    path('user/edit', views.editUser, name='editUser'),
]