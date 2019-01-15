from django.db import models

# Create your models here.
class User(models.Model):
    user_id = models.CharField(max_length=30)
    username = models.CharField(max_length=40, unique=True)
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=20)
    status = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
