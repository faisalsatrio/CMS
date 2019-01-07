from django.db import models

# Create your models here.
class AddNews(models.Model):
    crawlerName = models.CharField(max_length=100)
    site = models.CharField(max_length=100)
    startDate = models.CharField(max_length=100)

class EditNews(models.Model):
    crawlerName = models.CharField(max_length=100)
    site = models.CharField(max_length=100)
    startDate = models.CharField(max_length=100)
