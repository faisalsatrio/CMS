# Generated by Django 2.1.3 on 2019-01-10 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('topic_management', '0005_auto_20190110_1625'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='created_at',
            field=models.DateTimeField(editable=False),
        ),
    ]