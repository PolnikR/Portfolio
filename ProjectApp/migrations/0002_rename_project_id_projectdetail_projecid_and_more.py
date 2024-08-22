# Generated by Django 5.1 on 2024-08-21 11:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProjectApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='projectdetail',
            old_name='project_id',
            new_name='projecId',
        ),
        migrations.AddField(
            model_name='projectdetail',
            name='project',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='project_details', to='ProjectApp.project'),
        ),
    ]
