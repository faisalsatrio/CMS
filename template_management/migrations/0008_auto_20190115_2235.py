# Generated by Django 2.1.3 on 2019-01-15 15:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('template_management', '0007_auto_20190115_2136'),
    ]

    operations = [
        migrations.RenameField(
            model_name='platform',
            old_name='config_template_name',
            new_name='config_yaml_name',
        ),
        migrations.RenameField(
            model_name='platform',
            old_name='config_template_url',
            new_name='config_yaml_url',
        ),
        migrations.RenameField(
            model_name='platform',
            old_name='deploy_template_name',
            new_name='deploy_yaml_name',
        ),
        migrations.RenameField(
            model_name='platform',
            old_name='deploy_template_url',
            new_name='deploy_yaml_url',
        ),
    ]