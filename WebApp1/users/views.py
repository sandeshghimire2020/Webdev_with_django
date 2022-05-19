from django.shortcuts import render
from .models import Profile

# Create your views here.
def profiles(request):
    profileObj = Profile.objects.all();
    Context={'Profile':profileObj}
    return render(request,'users/profiles.html',Context)

