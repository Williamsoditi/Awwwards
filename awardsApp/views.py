from django.shortcuts import render, redirect
from .models import *
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .forms import ProjectForm, ProfileForm
import cloudinary.api
import cloudinary.uploader
import cloudinary

# Create your views here.
def welcome(request):
    project = Project.objects.all()
    project = Project.objects.all().order_by('-id')
    return render(request, 'home.html', {'project': project, 'project': project,})
