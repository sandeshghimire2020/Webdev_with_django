from django.shortcuts import render, redirect
from .models import Profile, Skill
from django.contrib import messages
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
    messages.error(request,"User was logged out!")
    return redirect('login')

