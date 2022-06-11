from django.shortcuts import render, redirect
from .models import *
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .forms import ProjectForm, ProfileForm, UpdateProfileForm




# Create your views here.
