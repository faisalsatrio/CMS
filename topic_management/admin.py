from django.contrib import admin
from .models import AddTopic, EditTopic

# Register your models here.
admin.site.register(AddTopic)
admin.site.register(EditTopic)
