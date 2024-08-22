from django.db import models
import os
from io import BytesIO
from PIL import Image, ImageOps
from django.contrib.auth.models import User
from django.core.files.base import ContentFile

from IndustryApp.models import Company, Technology


# Create your models here.
class Element(models.Model):
    element_title = models.CharField(max_length=255, null=True, blank=True)
    element_content = models.TextField(null=True, blank=True)
    order = models.PositiveIntegerField()

    class Meta:
        verbose_name = "Element"
        verbose_name_plural = "Elements"

    def __str__(self):
        return self.element_title or "Untitled Element"

class Picture(models.Model):
    element = models.ForeignKey(Element, related_name='images', on_delete=models.CASCADE)
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
class Reference(models.Model):
    reference_person = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reference', null=True, blank=True)
    reference_name = models.CharField(max_length=255, null=True, blank=True)
    reference_position = models.CharField(max_length=255, null=True, blank=True)
    reference_content = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = "Reference"
        verbose_name_plural = "References"

    def __str__(self):
        return self.reference_name

class Service(models.Model):
    service_name = models.CharField(max_length=255, null=True, blank=True)
    service_description = models.TextField(null=True, blank=True)
    service_icon = models.ImageField(upload_to='service_images/')

    class Meta:
        verbose_name = "Service"
        verbose_name_plural = "Services"

    def __str__(self):
        return self.service_name

    def save(self, *args, **kwargs):
        if self.service_icon:
            # Otvorenie obrázka
            image = Image.open(self.service_icon)

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
            self.service_icon.save(f"{os.path.splitext(self.service_icon.name)[0]}.webp",
                            ContentFile(output.read()), save=False)

        super().save(*args, **kwargs)

class Category(models.Model):
    category_name = models.CharField(max_length=255, null=True, blank=True)
    category_description = models.TextField(null=True, blank=True)
    category_icon = models.ImageField(upload_to='category_files/', null=True,
                                     blank=True)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.category_name

class CV(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='reference', null=True, blank=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    years = models.IntegerField()
    position = models.CharField(max_length=255, null=True, blank=True)
    content = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = "CV"
        verbose_name_plural = "CV"

    def __str__(self):
        return self.name
class ProjectOutcome(models.Model):
    project_id = models.PositiveIntegerField()
    name = models.CharField(max_length=255, null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    results = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = "Project Result"
        verbose_name_plural = "Project Results"

    def __str__(self):
        return self.name


class ProjectDetail(models.Model):
    project = models.ForeignKey('Project', on_delete=models.CASCADE, related_name='project_details', null=True,
                                blank=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='project_details', null=True, blank=True)
    time_spent = models.PositiveIntegerField()
    elements = models.ManyToManyField(Element, related_name='project_details')
    technologies = models.ManyToManyField(Technology, related_name='project_details')
    result = models.ForeignKey(ProjectOutcome, on_delete=models.CASCADE, related_name='project_details', null=True, blank=True)
    references = models.ManyToManyField(Reference, related_name='project_details')

    class Meta:
        verbose_name = "Project Detail"
        verbose_name_plural = "Project Details"


class Customer(models.Model):
    customer_name = models.CharField(max_length=255, null=True, blank=True)
    customer_description = models.TextField(null=True, blank=True)
    customer_image = models.ImageField(upload_to='customer_images/', null=True, blank=True)  # For image widgets
    technologies = models.ManyToManyField(Technology, related_name='customer')

    class Meta:
        verbose_name = "Customer"
        verbose_name_plural = "Customers"

    def __str__(self):
        return self.customer_name

    def save(self, *args, **kwargs):
        if self.customer_image:
            # Otvorenie obrázka
            image = Image.open(self.customer_image)

            # Upravíme orientáciu obrázka podľa EXIF údajov
            image = ImageOps.exif_transpose(image)

            # Zmena veľkosti na 636x508
            image = image.resize((636, 508))

            # Konverzia do WebP formátu
            output = BytesIO()
            image = image.convert('RGB')
            image.save(output, format='WEBP', quality=80)
            output.seek(0)

            # Prepis starého súboru na nový WebP
            self.customer_image.save(f"{os.path.splitext(self.customer_image.name)[0]}.webp",
                                     ContentFile(output.read()), save=False)

        super().save(*args, **kwargs)



class Project(models.Model):
    project_name = models.CharField(max_length=255, null=True, blank=True)
    project_icon = models.ImageField(upload_to='project_files/project_icons/', null=True,
                                     blank=True)  # For image widgets
    project_image = models.ImageField(upload_to='project_files/project_images/', null=True, blank=True)
    project_detail = models.ForeignKey(ProjectDetail, on_delete=models.CASCADE, related_name='projects', null=True, blank=True)
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
            image = image.resize((620, 620))

            # Konverzia do WebP formátu
            output = BytesIO()
            image = image.convert('RGB')
            image.save(output, format='WEBP', quality=80)
            output.seek(0)

            # Prepis starého súboru na nový WebP
            self.project_image.save(f"{os.path.splitext(self.project_image.name)[0]}.webp",
                            ContentFile(output.read()), save=False)

        if self.project_icon:
            # Otvorenie obrázka
            icon = Image.open(self.project_icon)

            # Upravíme orientáciu obrázka podľa EXIF údajov
            icon = ImageOps.exif_transpose(icon)

            # Zmena veľkosti na 636x424
            icon = icon.resize((1096, 695))

            # Konverzia do WebP formátu
            output = BytesIO()
            icon = icon.convert('RGB')
            icon.save(output, format='WEBP', quality=80)
            output.seek(0)

            # Prepis starého súboru na nový WebP
            self.project_icon.save(f"{os.path.splitext(self.project_icon.name)[0]}.webp",
                            ContentFile(output.read()), save=False)

        super().save(*args, **kwargs)





