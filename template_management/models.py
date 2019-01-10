from django.db import models

# Create your models here.
class UploadConfig(models.Model):
    title = models.CharField(max_length=50)
    file = models.FileField()

class UploadDeployment(models.Model):
    title = models.CharField(max_length=50)
    file = models.FileField()
