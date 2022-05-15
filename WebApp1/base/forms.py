from django.forms import ModelForm
from .models import Project


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'userName', 'user_image','description',  'demo_link','source_link','tags']

