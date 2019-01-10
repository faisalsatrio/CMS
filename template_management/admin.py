from django.contrib import admin
from .models import UploadConfig, UploadDeployment

# Register your models here.
admin.site.register(UploadConfig)
admin.site.register(UploadDeployment)
