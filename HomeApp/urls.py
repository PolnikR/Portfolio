from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('sluzby/', views.services, name='services'),
    path('omne/', views.about, name='about'),
    path('kontakt/', views.contact, name='contact'),

]