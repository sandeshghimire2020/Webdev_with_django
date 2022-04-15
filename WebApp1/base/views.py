from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


rooms = [
    {
        'id':'1',
        'name': "Hello World!",
        'description': "This is the description",
    },
    {
        'id':'2',
        'name': "city",
        'description': "This is the description",
    },
    {
        'id':'3',
        'name': "Python",
        'description': "This is the description",
    },
]

def home(request):

    return render(request,'base/home.html', {'rooms':rooms})

def room(request,pk):
    context = None
    for i in rooms:
        if i['id'] == pk:
            context = i

    return render(request,'base/room.html',{'cont':context})
