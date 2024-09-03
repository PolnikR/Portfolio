from django.urls import path
from . import views

urlpatterns = [
    path('', views.projects, name='projects'),
    path('<int:project_id>/', views.project, name='project')

    #path('detail/', views.projectDetail, name='project'),
]