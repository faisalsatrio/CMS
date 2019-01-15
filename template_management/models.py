from django.db import models

# Create your models here.
class Platform(models.Model):
    platform_name = models.CharField(max_length=50)
    config_template = models.FileField()
    config_upload_date = models.DateTimeField(null=True)
    deploy_template = models.FileField()
    deploy_upload_date = models.DateTimeField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
