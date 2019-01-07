from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('token/', views.listToken, name='listToken'),
    path('token/add', views.addToken, name='addToken'),
    path('token/edit', views.editToken, name='editToken'),
]
