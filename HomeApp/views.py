from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'HomeApp/home.html')

def services(request):
    return render(request, 'HomeApp/services.html')

def about(request):
    return render(request, 'HomeApp/about.html')

def contact(request):
    return render(request, 'HomeApp/kontakt.html')
