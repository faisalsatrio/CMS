from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('subject/add/', views.addSubject, name='addSubject'),
    path('subject/edit/id=<int:id>/', views.editSubject, name='editSubject'),
    path('subject/delete/id=<int:id>/', views.deleteSubject, name='deleteSubject'),
    path('subject/activate/id=<int:id>/', views.activateSubject, name='activateSubject'),
    path('subject/deactivate/id=<int:id>/', views.deactivateSubject, name='deactivateSubject'),
]
