from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('addsubject/', views.addsubject, name='addsubject'),
    path('editsubject/', views.editsubject, name='editsubject'),
]