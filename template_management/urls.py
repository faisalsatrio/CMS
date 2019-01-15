from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('template/', views.template, name='template'),
    path('template/add/', views.addPlatform, name='addPlatform'),
    path('template/edit/id=<int:id>/', views.editPlatform, name='editPlatform'),
    path('template/delete/id=<int:id>/', views.deletePlatform, name='deletePlatform'),
]
