# Generated by Django 4.0.4 on 2022-05-18 04:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0010_project_owner_alter_project_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='userName',
        ),
    ]