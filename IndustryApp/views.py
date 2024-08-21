from django.shortcuts import render

# Create your views here.

def industry(request):
    return render(request, 'IndustryApp/industry.html')