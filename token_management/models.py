from django.db import models

# Create your models here.
class Token(models.Model):
    token_name = models.CharField(max_length=100)
    consumer_key = models.CharField(max_length=100)
    consumer_secret = models.CharField(max_length=100)
    access_key = models.CharField(max_length=100)
    access_secret = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
