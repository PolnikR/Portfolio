# Generated by Django 5.1 on 2024-08-21 11:38

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('IndustryApp', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CV',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(blank=True, max_length=255, null=True)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('years', models.IntegerField()),
                ('position', models.CharField(blank=True, max_length=255, null=True)),
                ('content', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'CV',
                'verbose_name_plural': 'CV',
            },
        ),
        migrations.CreateModel(
            name='Element',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('element_title', models.CharField(blank=True, max_length=255, null=True)),
                ('element_content', models.TextField(blank=True, null=True)),
                ('order', models.PositiveIntegerField()),
            ],
            options={
                'verbose_name': 'Element',
                'verbose_name_plural': 'Elements',
            },
        ),
        migrations.CreateModel(
            name='ProjectResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_id', models.PositiveIntegerField()),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('content', models.TextField(blank=True, null=True)),
                ('results', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Project Result',
                'verbose_name_plural': 'Project Results',
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_name', models.CharField(blank=True, max_length=255, null=True)),
                ('service_description', models.TextField(blank=True, null=True)),
                ('service_icon', models.ImageField(upload_to='service_images/')),
            ],
            options={
                'verbose_name': 'Service',
                'verbose_name_plural': 'Services',
            },
        ),
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='element_images/')),
                ('element', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='ProjectApp.element')),
            ],
            options={
                'verbose_name': 'Picture',
                'verbose_name_plural': 'Pictures',
            },
        ),
        migrations.CreateModel(
            name='ProjectDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_id', models.PositiveIntegerField()),
                ('time_spent', models.PositiveIntegerField()),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='project_details', to='IndustryApp.company')),
                ('elements', models.ManyToManyField(related_name='project_details', to='ProjectApp.element')),
                ('result', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='project_details', to='ProjectApp.projectresult')),
            ],
            options={
                'verbose_name': 'Project Detail',
                'verbose_name_plural': 'Project Details',
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(blank=True, max_length=255, null=True)),
                ('project_icon', models.ImageField(blank=True, null=True, upload_to='project_files/project_icons/')),
                ('project_image', models.ImageField(blank=True, null=True, upload_to='project_files/project_images/')),
                ('project_description', models.TextField(blank=True, null=True)),
                ('customers', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='customer_projects', to='IndustryApp.customer')),
                ('project_detail', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='projects', to='ProjectApp.projectdetail')),
            ],
            options={
                'verbose_name': 'Project',
                'verbose_name_plural': 'Projects',
            },
        ),
        migrations.CreateModel(
            name='Reference',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reference_name', models.CharField(blank=True, max_length=255, null=True)),
                ('reference_position', models.CharField(blank=True, max_length=255, null=True)),
                ('reference_content', models.TextField(blank=True, null=True)),
                ('reference_person', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Reference',
                'verbose_name_plural': 'References',
            },
        ),
        migrations.AddField(
            model_name='projectdetail',
            name='references',
            field=models.ManyToManyField(related_name='project_details', to='ProjectApp.reference'),
        ),
    ]
