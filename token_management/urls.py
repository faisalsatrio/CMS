from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('token/', views.token_crawler, name='token'),
]