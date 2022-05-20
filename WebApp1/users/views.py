from django.shortcuts import render
from .models import Profile, Skill

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


