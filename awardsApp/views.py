from django.shortcuts import render, redirect
from .models import *
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .forms import ProjectForm, ProfileForm, UpdateProfileForm
import cloudinary.api
import cloudinary.uploader
import cloudinary

# Create your views here.
def welcome(request):
    project = Project.objects.all()
    project = Project.objects.all().order_by('-id')
    return render(request, 'home.html', {'project': project, 'project': project,})

@login_required(login_url="/accounts/login/")
def profile(request):
    current_user = request.user
    profile = Profile.objects.filter(user_id=current_user.id).first()
    project = Project.objects.filter(user_id=current_user.id).all() 
    return render(request, "profile.html", {"profile": profile, "project": project})

@login_required(login_url='/accounts/login/')
def create_profile(request):
    current_user = request.user
    title = "Create Profile"
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = current_user
            profile.save()
        return HttpResponseRedirect('/')

    else:
        form = ProfileForm()
    return render(request, 'create_profile.html', {"form": form, "title": title})

@login_required(login_url='/accounts/login/')
def update_profile(request,id):
    user = User.objects.get(id=id)
    profile = Profile.objects.get(user_id = user)
    form = UpdateProfileForm(instance=profile)
    if request.method == "POST":
            form = UpdateProfileForm(request.POST,request.FILES,instance=profile)
            if form.is_valid():  
                
                profile = form.save(commit=False)
                profile.save()
                return redirect('profile') 
            
    ctx = {"form":form}
    return render(request, 'update_profile.html', ctx)

@login_required(login_url="/accounts/login/")
def save_project(request):
    if request.method == "POST":
        current_user = request.user

        title = request.POST["title"]
        location = request.POST["location"]
        description = request.POST["description"]
        url = request.POST["url"]
        image = request.FILES["image"]
        image = cloudinary.uploader.upload(image, crop="limit", width=500, height=500)
        image_url = image["url"]

        project = Project(
            user_id=current_user.id,
            title=title,
            location=location,
            description=description,
            url=url,
            image=image_url,
        )
        project.save_project()

        return redirect("/profile", {"success": "Project Saved Successfully"})
    else:
        return render(request, "profile.html", {"danger": "Project Save Failed"})

@login_required(login_url="/accounts/login/")
def delete_project(request, id):
    project = Project.objects.get(id=id)
    project.delete_project()
    return redirect("/profile", {"success": "Deleted Project Successfully"})

@login_required(login_url='/accounts/login/')
def project(request):
    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.save()
        return redirect('/')
    else:
        form = ProjectForm()
    return render(request, 'project.html', {"form": form})


@login_required(login_url='/accounts/login/')
def search_project(request):
    if 'search' in request.GET and request.GET['search']:
        search_term = request.GET.get('search').lower()
        projects = Project.search_project_name(search_term)
        message = f'{search_term}'

        return render(request, 'search.html', {'found': message, 'projects': projects})
    else:
        message = 'Not found'
        return render(request, 'search.html', {'danger': message})

@login_required(login_url='/accounts/login/')
def project_details(request, project_id):
    project = Project.objects.get(id=project_id)
    rating = Rating.objects.filter(project = project)
    return render(request, "project_details.html", {"project": project, 'rating':rating})

@login_required(login_url='/accounts/login/')
def rate(request,id):
    if request.method == 'POST':
        project = Project.objects.get(id = id)
        current_user = request.user
        design = request.POST['design']
        content = request.POST['content']
        usability = request.POST['usability']

        Rating.objects.create(
            project=project,
            user=current_user,
            design=design,
            usability=usability,
            content_rate=content,
            avarage_rate=round((float(design)+float(usability)+float(content))/3,2),)

        return render(request,"project_details.html",{"project":project})
    else:
        project = Project.objects.get(id = id) 
        return render(request,"project_details.html",{"project":project})
