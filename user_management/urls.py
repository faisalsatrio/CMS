from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('tambah/', views.tambah, name='tambah'),
    path('ubahpengguna/', views.ubahpengguna, name='ubahpengguna'),
    path('list/', views.list, name='list'),
    path('user/', views.user, name='user'),
]