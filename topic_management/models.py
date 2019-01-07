from django.db import models

# Create your models here.
class AddTopic(models.Model):
    topicName = models.CharField(max_length=100)
    clientName = models.CharField(max_length=100)
    description = models.CharField(max_length=100)

class EditTopic(models.Model):
    topicName = models.CharField(max_length=100)
    clientName = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
