# Generated by Django 5.1 on 2024-08-23 07:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ProjectApp', '0010_company_company_services'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reference',
            name='reference_desc',
        ),
        migrations.RemoveField(
            model_name='reference',
            name='reference_person',
        ),
    ]
