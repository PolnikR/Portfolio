# Generated by Django 5.1 on 2024-08-23 06:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProjectApp', '0007_alter_project_customers_delete_customer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(blank=True, max_length=255, null=True)),
                ('company_sphere', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'verbose_name': 'Company',
                'verbose_name_plural': 'Companies',
            },
        ),
        migrations.AlterField(
            model_name='projectdetail',
            name='company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='project_details', to='ProjectApp.company'),
        ),
    ]
