from django.shortcuts import render, get_object_or_404

from .models import Project, ProjectDetail
from IndustryApp.models import Customer


# Create your views here.

def projects(request):
    projs = Project.objects.all()
    customers = Customer.objects.all()
    context = {
        'customers': customers,
        'projects': projs
    }

    return render(request, 'ProjectApp/projects.html', context)


def project(request, project_id):
    proj_detail = get_object_or_404(ProjectDetail, id=project_id)
    print(proj_detail.company.company_services)
    context = {
        'project': proj_detail
    }
    return render(request, 'ProjectApp/project.html', context)


def projectDetail(request):
    return render(request, 'ProjectApp/project.html')
