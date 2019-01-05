from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('news/', views.news_crawler, name='news'),
]