from django.contrib import admin
from .models import Picture, Element, Reference, ProjectOutcome, ProjectDetail, Project, Service, CV, Customer
from IndustryApp.models import Company


# Register your models here.

class ImageInline(admin.TabularInline):
    model = Picture
    extra = 1


class CompanyInline(admin.TabularInline):
    model = Company
    extra = 1


class ElementInline(admin.TabularInline):
    model = Element
    extra = 1


class ProjectOutcomeInline(admin.TabularInline):
    model = ProjectOutcome
    extra = 1


class ReferenceInline(admin.TabularInline):
    model = Reference
    extra = 1


class ProjectDetailInline(admin.StackedInline):
    model = ProjectDetail
    extra = 1
    inlines = [CompanyInline, ElementInline, ProjectOutcomeInline, ReferenceInline]
    filter_horizontal = ('technologies', 'elements')


@admin.register(Element)
class ElementAdmin(admin.ModelAdmin):
    inlines = [ImageInline]
    list_display = ('element_title', 'element_content', 'image_count')

    @staticmethod
    def image_count(obj):
        return obj.images.count()


@admin.register(Picture)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('element_title',)

    @staticmethod
    def element_title(obj):
        return obj.element.element_title


@admin.register(Reference)
class ReferenceAdmin(admin.ModelAdmin):
    list_display = ('reference_name', 'reference_position')
    search_fields = ('reference_name', 'reference_position')
    list_filter = ('reference_name',)


@admin.register(ProjectOutcome)
class ProjectOutcomeAdmin(admin.ModelAdmin):
    list_display = ('project_id', 'name')
    search_fields = ('project_id', 'name')
    list_filter = ('project_id', 'name')


@admin.register(ProjectDetail)
class ProjectDetailAdmin(admin.ModelAdmin):
    list_display = ('project_id', 'company')
    search_fields = ('project_id', 'company')
    list_filter = ('project_id', 'company')


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    inlines = [ProjectDetailInline]
    list_display = ('project_name',)
    search_fields = ('project_name',)
    list_filter = ('project_name',)


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('customer_name', 'customer_description')
    search_fields = ('customer_name',)
    list_filter = ('customer_name',)


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('service_name', 'service_description')
    search_fields = ('service_name',)
    list_filter = ('service_name',)


@admin.register(CV)
class CVAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'position')
    search_fields = ('name', 'category')
    list_filter = ('name',)
