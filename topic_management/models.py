from django.db import models

# Create your models here.
class AddSubject(models.Model):
    topic = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    keyword = models.CharField(max_length=100)
    platform = models.CharField(max_length=100)

class EditSubject(models.Model):
    topic = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    keyword = models.CharField(max_length=100)
    platform = models.CharField(max_length=100)