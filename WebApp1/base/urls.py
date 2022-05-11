from django.urls import path
from . import views
from .models import Project


urlpatterns = [
    path('', views.home, name="home"),
    path('Project/<str:pk>/', views.project, name="Project"),
    path('create-Project/', views.createProject, name="create"),
    path('update-Project/<str:pk>/', views.updateProject, name="update"),
    path('delete-Project/<str:pk>/', views.deleteProject, name="delete"),
   
]
