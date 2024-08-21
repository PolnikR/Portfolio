from django.urls import path
from . import views

urlpatterns = [
    path('', views.projects, name='projects'),
    path('detail/', views.projectDetail, name='project'),
]