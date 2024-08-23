import os
from io import BytesIO
from PIL import Image, ImageOps
from django.contrib.auth.models import User
from django.core.files.base import ContentFile
from django.db import models


# Create your models here.
class LifeCircumstance(models.Model):
    name = models.CharField(max_length=255,  null=True, blank=True)
    images = models.ImageField(upload_to='media/life_circumstances/', null=True, blank=True )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Life Circumstance"
        verbose_name_plural = "Life Circumstances"

class Biography(models.Model):
    life_circumstance = models.ForeignKey(LifeCircumstance, on_delete=models.CASCADE)
    name = models.CharField(max_length=255,  null=True, blank=True)
    years = models.PositiveIntegerField(null=True, blank=True)
    job_role = models.CharField(max_length=255, null=True, blank=True)
    job_description = models.TextField(null=True, blank=True)
    what_i_learned = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Biography"
        verbose_name_plural = "Biographies"

