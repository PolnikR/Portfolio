# Generated by Django 5.1 on 2024-08-23 07:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IndustryApp', '0008_customerdetail'),
        ('ProjectApp', '0011_remove_reference_reference_desc_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='element',
            name='customer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='customer_elements', to='IndustryApp.customer'),
        ),
        migrations.AddField(
            model_name='element',
            name='project_detail',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='project_elements', to='ProjectApp.projectdetail'),
        ),
        migrations.AlterField(
            model_name='element',
            name='order',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
