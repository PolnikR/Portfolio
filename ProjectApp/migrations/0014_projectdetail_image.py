# Generated by Django 5.1 on 2024-08-23 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProjectApp', '0013_remove_projectoutcome_project_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectdetail',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media/detail_projektu/'),
        ),
    ]
