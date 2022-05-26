from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Project
from .forms import ProjectForm
# Create your views here.



##Projects = Project.objects.all();

def home(request):
    Projects = Project.objects.all()
    return render(request,'base/home.html', {'Projects':Projects})

def project(request,pk):
    
    ProjectObj=Project.objects.get(id=pk)
    return render(request,'base/Project.html',{'cont':ProjectObj})

@login_required(login_url="login")
def createProject(request):
    form = ProjectForm()
    if request.method =='POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    Context={'form':form}
    return render(request,"base/project_form.html",Context )

@login_required(login_url="login")
def updateProject(request, pk):
    editProject = Project.objects.get(id=pk) #we are taking pk of the project where user clicked edit
    forms = ProjectForm(instance = editProject) #sending the instance that we got to the form
    if request.method =='POST':
        forms = ProjectForm(request.POST,request.FILES, instance = editProject)
        if forms.is_valid():
            forms.save()
            return redirect('home')
    Context={'form':forms}
    return render(request,"base/project_form.html",Context)

@login_required(login_url="login")
def deleteProject (request, pk):
    deleteProject = Project.objects.get(id=pk)
    if request.method == 'POST':
        deleteProject.delete()
        return redirect('home')
    context = {'delete':deleteProject}
    return render (request, "base/delete_confirm.html",context)