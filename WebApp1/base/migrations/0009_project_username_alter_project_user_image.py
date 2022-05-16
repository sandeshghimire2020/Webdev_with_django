# Generated by Django 4.0.4 on 2022-05-15 01:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0008_alter_project_user_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='userName',
            field=models.CharField(default='Anonymous user', max_length=200),
        ),
        migrations.AlterField(
            model_name='project',
            name='user_image',
            field=models.ImageField(blank=True, default='default.png', null=True, upload_to=''),
        ),
    ]