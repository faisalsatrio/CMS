from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('news', views.listNews, name='listNews'),
    path('news/add', views.addNews, name='addNews'),
    path('news/edit', views.editNews, name='editNews'),
]