from django.core.exceptions import ValidationError
from django.db import models
import os
from io import BytesIO
from PIL import Image, ImageOps
from django.contrib.auth.models import User
from django.core.files.base import ContentFile

from IndustryApp.models import Technology, Customer


# Create your models here.

class Project(models.Model):
    project_name = models.CharField(max_length=255, null=True, blank=True)
    project_image = models.ImageField(upload_to='project_files/project_images/', null=True, blank=True)
    customers = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='customer_projects', null=True, blank=True)
    project_description = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = "Project"
        verbose_name_plural = "Projects"

    def __str__(self):
        return self.project_name

    def save(self, *args, **kwargs):
        if self.project_image:
            # Otvorenie obrázka
            image = Image.open(self.project_image)

            # Upravíme orientáciu obrázka podľa EXIF údajov
            image = ImageOps.exif_transpose(image)

            # Zmena veľkosti na 636x424
            image = image.resize((620, 629))

            # Konverzia do WebP formátu
            output = BytesIO()
            image = image.convert('RGB')
            image.save(output, format='WEBP', quality=80)
            output.seek(0)

            # Prepis starého súboru na nový WebP
            self.project_image.save(f"{os.path.splitext(self.project_image.name)[0]}.webp",
                            ContentFile(output.read()), save=False)



        super().save(*args, **kwargs)

class Company(models.Model):
    company_name = models.CharField(max_length=255, null=True, blank=True)
    company_sphere = models.CharField(max_length=255, null=True, blank=True)
    company_services = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = "Company"
        verbose_name_plural = "Companies"

    def __str__(self):
        return self.company_name

class Reference(models.Model):
    reference_name = models.CharField(max_length=255, null=True, blank=True)
    reference_position = models.CharField(max_length=255, null=True, blank=True)
    reference_content = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = "Reference"
        verbose_name_plural = "References"

    def __str__(self):
        return self.reference_name

class Picture(models.Model):
    element = models.ForeignKey('Element', related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='element_images/')


    def __str__(self):
        return f"Image for {self.element.element_title or 'Untitled Element'}"

    class Meta:
        verbose_name = "Picture"
        verbose_name_plural = "Pictures"
    def save(self, *args, **kwargs):
        if self.image:
            # Otvorenie obrázka
            image = Image.open(self.image)

            # Upravíme orientáciu obrázka podľa EXIF údajov
            image = ImageOps.exif_transpose(image)

            # Zmena veľkosti na 636x424
            image = image.resize((636, 424))

            # Konverzia do WebP formátu
            output = BytesIO()
            image = image.convert('RGB')
            image.save(output, format='WEBP', quality=80)
            output.seek(0)

            # Prepis starého súboru na nový WebP
            self.image.save(f"{os.path.splitext(self.image.name)[0]}.webp",
                            ContentFile(output.read()), save=False)

        super().save(*args, **kwargs)
class Element(models.Model):
    element_title = models.CharField(max_length=255, null=True, blank=True)
    element_content = models.TextField(null=True, blank=True)
    order = models.PositiveIntegerField(null=True, blank=True)
    project_detail = models.ForeignKey('ProjectDetail', on_delete=models.CASCADE, null=True, blank=True,
                                       related_name='project_elements')
    customer = models.ForeignKey('IndustryApp.Customer', on_delete=models.CASCADE, null=True, blank=True,
                                 related_name='customer_elements')

    def clean(self):
        if self.project_detail and self.customer:
            raise ValidationError("Prvok nemôže byť priradený k projektu aj zákazníkovi súčasne.")
        if not self.project_detail and not self.customer:
            raise ValidationError("Prvok musí byť priradený buď k projektu alebo k zákazníkovi.")
    class Meta:
        verbose_name = "Element"
        verbose_name_plural = "Elements"

    def __str__(self):
        return self.element_title or "Untitled Element"







class ProjectOutcome(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    results = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = "Project Result"
        verbose_name_plural = "Project Results"

    def __str__(self):
        return self.name


class ProjectDetail(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='project_details', null=True,
                                blank=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='project_details', null=True, blank=True)
    image = models.ImageField(upload_to='media/detail_projektu/', null=True, blank=True)
    time_spent = models.PositiveIntegerField()
    elements = models.ManyToManyField(Element, related_name='project_details')
    technologies = models.ManyToManyField(Technology, related_name='project_details')
    result = models.ForeignKey(ProjectOutcome, on_delete=models.CASCADE, related_name='project_details', null=True, blank=True)
    references = models.ManyToManyField(Reference, related_name='project_details')

    def save(self, *args, **kwargs):
        if self.image:
            # Otvorenie obrázka
            image = Image.open(self.image)

            # Upravíme orientáciu obrázka podľa EXIF údajov
            image = ImageOps.exif_transpose(image)

            # Zmena veľkosti na 1296x685
            image = image.resize((1296, 685))

            # Konverzia do WebP formátu
            output = BytesIO()
            image = image.convert('RGB')
            image.save(output, format='WEBP', quality=80)
            output.seek(0)

            # Prepis starého súboru na nový WebP
            self.image.save(f"{os.path.splitext(self.image.name)[0]}.webp", ContentFile(output.read()), save=False)

        super().save(*args, **kwargs)
    class Meta:
        verbose_name = "Project Detail"
        verbose_name_plural = "Project Details"










