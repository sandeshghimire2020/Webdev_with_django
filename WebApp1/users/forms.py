from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CustomUserCreationForm(UserCreationForm): #inherating from UserCreationfORM which is given by django
    class Meta: #meta class to edit the fields required
        model = User
        fields=[
            'first_name', 'email', 'username', 'password1', 'password2'
        ]

        #changing the fields label
        labels = { 
            'first_name':'Name',

        }