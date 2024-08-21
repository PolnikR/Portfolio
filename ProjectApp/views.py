from django.shortcuts import render

# Create your views here.

def projects(request):
    return render(request, 'ProjectApp/projects.html')

def projectDetail(request):
    return render(request, 'ProjectApp/project.html')

