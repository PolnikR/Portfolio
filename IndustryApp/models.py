from django.db import models


# Create your models here.
class Technology(models.Model):
    technology_name = models.CharField(max_length=255, null=True, blank=True)
    technology_image = models.FileField(upload_to='technology_images/', null=True, blank=True)

    class Meta:
        verbose_name = "Technology"
        verbose_name_plural = "Technologies"

    def __str__(self):
        return self.technology_name


class Company(models.Model):
    company_name = models.CharField(max_length=255, null=True, blank=True)
    company_sphere = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        verbose_name = "Company"
        verbose_name_plural = "Companies"

    def __str__(self):
        return self.company_name
