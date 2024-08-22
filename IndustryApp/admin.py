from django.contrib import admin
from .models import Technology, Company


# Register your models here.
@admin.register(Technology)
class TechnologyAdmin(admin.ModelAdmin):
    list_display = ('technology_name',)
    search_fields = ('technology_name',)
    list_filter = ('technology_name',)


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'company_sphere')
    search_fields = ('company_name', 'company_sphere')
    list_filter = ('company_name', 'company_sphere')
