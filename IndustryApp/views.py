from django.shortcuts import render
from ProjectApp.models import Project
# Create your views here.

def industry(request):
    projects = Project.objects.all()
    project_details = projects[0].project_details.all()
    print(projects[0].project_icon.url)
    technologies = project_details[0].technologies.all()
    print(technologies[0].technology_image.url)

    context = {
        'projects': projects
    }
    return render(request, 'IndustryApp/industry.html', context)
