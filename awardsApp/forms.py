from django.forms import ModelForm
from django import forms
from .models import Project,Profile

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ('image','title','description','url')