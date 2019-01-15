from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('news/', views.listNews, name='listNews'),
    path('news/add/', views.addNews, name='addNews'),
    path('news/edit/id=<int:id>/', views.editNews, name='editNews'),
    path('news/delete/id=<int:id>/', views.deleteNews, name='deleteNews'),
]
