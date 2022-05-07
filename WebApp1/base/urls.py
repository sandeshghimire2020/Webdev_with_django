from django.urls import path
from . import views
from .models import Project


urlpatterns = [
    path('', views.home, name="home"),
    path('Project/<str:pk>/', views.project, name="Project"),
   
]
