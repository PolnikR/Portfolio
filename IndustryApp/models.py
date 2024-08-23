from django.db import models
import os
from io import BytesIO
from PIL import Image, ImageOps
from django.core.files.base import ContentFile


# Create your models here.
class Technology(models.Model):
    technology_name = models.CharField(max_length=255, null=True, blank=True)
    technology_image = models.FileField(upload_to='technology_images/', null=True, blank=True)
    technology_description = models.TextField(blank=True, null=True)
    main_technology = models.BooleanField(default=False, null=True, blank=True)

    class Meta:
        verbose_name = "Technology"
        verbose_name_plural = "Technologies"

    def __str__(self):
        return self.technology_name


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


class CustomerElement(models.Model):
    element_name = models.CharField(max_length=255)
    element_description = models.TextField(null=True, blank=True)
    order = models.PositiveIntegerField(default=0, blank=True, null=True)

    def __str__(self):
        return self.element_name

    def get_customers(self):
        return ",".join([str(detail.customer) for detail in self.customer_details.all()])

    class Meta:
        verbose_name = "Customer Element"
        verbose_name_plural = "Customer Elements"


class CustomerDetail(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='details')
    elements = models.ManyToManyField(CustomerElement, related_name='customer_details')

    def __str__(self):
        return f"Detail pre zákazníka: {self.customer.customer_name}"

    class Meta:
        verbose_name = "Customer Detail"
        verbose_name_plural = "Customer Details"
