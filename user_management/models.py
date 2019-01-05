from django.db import models

# Create your models here.
class TambahPengguna(models.Model):
    topic = models.CharField(max_length=200) 

class UbahPengguna(models.Model):
    userid = models.CharField(max_length=30)
    username = models.CharField(max_length=40, unique=True)
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=20)

class AddUser(models.Model):
    username = models.CharField(max_length=40, unique=True)
    fullname = models.CharField(max_length=200)
    password = models.CharField(max_length=20)