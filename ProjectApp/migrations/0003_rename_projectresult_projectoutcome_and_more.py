# Generated by Django 5.1 on 2024-08-21 12:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ProjectApp', '0002_rename_project_id_projectdetail_projecid_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ProjectResult',
            new_name='ProjectOutcome',
        ),
        migrations.RemoveField(
            model_name='projectdetail',
            name='projecId',
        ),
    ]
