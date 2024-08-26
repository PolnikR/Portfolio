from django.shortcuts import render, get_object_or_404

from .models import Project


# Create your views here.

def projects(request):
    return render(request, 'ProjectApp/projects.html')

def project(request, project_id):
    #project = get_object_or_404(Project, id=project_id)
    #print(project)
    return render(request, 'ProjectApp/project.html')
def projectDetail(request):
    return render(request, 'ProjectApp/project.html')

