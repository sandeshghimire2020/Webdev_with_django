from django.shortcuts import render
from django.http import HttpResponse
from .models import Project
# Create your views here.



Projects = Project.objects.all();

def home(request):
    return render(request,'base/home.html', {'Projects':Projects})

def project(request,pk):
    
    ProjectObj=Project.objects.get(id=pk)
    return render(request,'base/Project.html',{'cont':ProjectObj})
