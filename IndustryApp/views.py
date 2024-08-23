from django.shortcuts import render
from .models import Customer
# Create your views here.

def industry(request):
    customers = Customer.objects.all()
    """project_details = projects[0].project_details.all()
    print(projects[0].project_icon.url)
    technologies = project_details[0].technologies.all()
    print(technologies[0].technology_name)"""
    print(customers[0].technologies.all())

    context = {
        'customers': customers
    }
    return render(request, 'IndustryApp/industry.html', context)
