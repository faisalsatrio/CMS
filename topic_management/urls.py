from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('topic', views.listTopic, name='listTopic'),
    path('topic/add', views.addTopic, name='addTopic'),
    path('topic/edit', views.editTopic, name='editTopic'),
]
