from django.db import models

# Create your models here.
class News(models.Model):
    crawler_name = models.CharField(max_length=100)
    site = models.CharField(max_length=100)
    start_date = models.DateTimeField(max_length=100)
    catch_up = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
