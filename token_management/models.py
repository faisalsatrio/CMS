from django.db import models

# Create your models here.
class AddToken(models.Model):
    tokenName = models.CharField(max_length=100)
    consumerKey = models.CharField(max_length=100)
    consumerSecret = models.CharField(max_length=100)
    accessKey = models.CharField(max_length=100)
    accessSecret = models.CharField(max_length=100)

class EditToken(models.Model):
    tokenName = models.CharField(max_length=100)
    consumerKey = models.CharField(max_length=100)
    consumerSecret = models.CharField(max_length=100)
    accessKey = models.CharField(max_length=100)
    accessSecret = models.CharField(max_length=100)
