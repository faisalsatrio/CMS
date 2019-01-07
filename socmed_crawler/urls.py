from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('subject/add/', views.addSubject, name='addSubject'),
    path('subject/edit/', views.editSubject, name='editSubject'),
]
