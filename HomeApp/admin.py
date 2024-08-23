from django.contrib import admin
from .models import LifeCircumstance, Biography
# Register your models here.

@admin.register(LifeCircumstance)
class LifeCircumstanceAdmin(admin.ModelAdmin):
    list_display = ('name', )
    search_fields = ('name', )

@admin.register(Biography)
class BiographyAdmin(admin.ModelAdmin):
    list_display = ('name', 'life_circumstance', 'job_role')
    search_fields = ('name', 'life_circumstance__name', 'job_role')
    list_filter = ('life_circumstance', 'job_role')

