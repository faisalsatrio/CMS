from django.db import models

# Create your models here.
class Topic(models.Model):
    topic_name = models.CharField(max_length=100)
    client_name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
