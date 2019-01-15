from django.db import models

# Create your models here.
class Platform(models.Model):
    platform_name = models.CharField(max_length=50)
    config_template_name = models.CharField(max_length=100)
    config_template_url = models.CharField(max_length=100)
    config_upload_date = models.DateTimeField(null=True)
    deploy_template_name = models.CharField(max_length=100)
    deploy_template_url = models.CharField(max_length=100)
    deploy_upload_date = models.DateTimeField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
