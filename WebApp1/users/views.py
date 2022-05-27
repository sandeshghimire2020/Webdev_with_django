from django.shortcuts import render, redirect
from .models import Profile, Skill
from django.contrib import messages
from django.contrib.auth.decorators import login_required
#from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User

# Create your views here.
def profiles(request):
    profileObj = Profile.objects.all();
    Context={'Profile':profileObj}
    return render(request,'users/profiles.html',Context)

def userProfile(request,pk):
    profileObject = Profile.objects.get(id=pk)
    
    topSkills = profileObject.skill_set.exclude(description__exact="")
    otherSkills=profileObject.skill_set.filter(description="")
    Context={'userProfile':profileObject,'topSkills':topSkills,'otherSkills':otherSkills}
    return render(request,'users/Dev.html',Context)



def loginUser(request):
    page='login'
    if request.user.is_authenticated:
        return redirect('profiles')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username=username) #quering the username out
        except:
            messages.error(request,"Username doesn't exist") #if username doesn't exist print this

        #this will authenticate if password matches username
        #returns either user instance or non
        user=authenticate(request, username = username, password=password) 

        if user is not None:
            # this function will create a session if the user exists
            #after that it will add session key to our browser cookies
            login(request, user)
            return redirect('profiles')
        else:
            messages.error(request,"Username or password is incorrect")

    return render(request, 'users/login_register.html')


def logoutUser(request):
    logout(request) #delete the session
    messages.success(request,"User was logged out!")
    return redirect('login')


def registerUser(request):
    page='register'
    form = CustomUserCreationForm()
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request, 'User Account was created!')
            login(request, user) #login the created user
            return redirect('profiles')
        else:
            messages.success(request, 'ERROR: An error has occured!')

    context={'page':page,'form':form}
    return render(request,'users/login_register.html', context)