from django.db import models
from topic_management.models import Topic
from template_management.models import Platform
from token_management.models import Token

# Create your models here.
class Subject(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.PROTECT)
    subject = models.CharField(max_length=100)
    keyword = models.CharField(max_length=100)
    platform = models.ForeignKey(Platform, on_delete=models.PROTECT)
    status = models.CharField(max_length=100)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField(null=True)
    config_yaml_name = models.CharField(max_length=100)
    config_yaml_url = models.URLField()
    deploy_yaml_name = models.CharField(max_length=100)
    deploy_yaml_url = models.URLField()
    token = models.ForeignKey(Token, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
