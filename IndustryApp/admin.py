from django.contrib import admin
from .models import Technology,  Customer, CustomerElement, CustomerDetail


# Register your models here.
@admin.register(Technology)
class TechnologyAdmin(admin.ModelAdmin):
    list_display = ('technology_name',)
    search_fields = ('technology_name',)
    list_filter = ('technology_name',)



@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('customer_name', 'customer_description')
    search_fields = ('customer_name',)
    list_filter = ('customer_name',)


@admin.register(CustomerElement)
class CustomerElementAdmin(admin.ModelAdmin):
    list_display = ('element_name', 'order', 'get_customers')
    ordering = ('order',)

    def get_customers(self, obj):
        return obj.get_customers()
    get_customers.short_description = "Customers"

@admin.register(CustomerDetail)
class CustomerDetailAdmin(admin.ModelAdmin):
    list_display = ('customer', )
    filter_horizontal = ('elements',)
