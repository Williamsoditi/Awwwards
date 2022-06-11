from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
import datetime as dt

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_photo = CloudinaryField("Profile Image")
    bio = models.TextField(max_length=300)
    location = models.CharField(max_length = 40)
    email = models.EmailField(max_length=200)
    contact = models.CharField(max_length=100, blank=True)

    def save_profile(self):
        self.save()
    
    def update_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    @classmethod
    def filter_by_id(cls, id):
        profile = Profile.objects.filter(user=id).first()
        return profile

    def __str__(self):
        return self.user.username

class Project(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=600)
    image = CloudinaryField("Project Image/Screenshot")
    url = models.URLField(null=True)
    date = models.DateTimeField(auto_now_add=True, null=True)

    def save_project(self):
        self.save()

    def delete_project(self):
        self.delete()

    def __str__(self):
        return self.title

    @classmethod
    def search_project_name(cls, search_term):
        projects = cls.objects.filter(
        title__icontains=search_term)
        return projects 

class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    design = models.IntegerField(default=0, blank=True, null=True)
    usability = models.IntegerField(default=0, blank=True, null=True)
    content = models.IntegerField(default=0, blank=True, null=True)
    average = models.IntegerField(default=0, blank=True, null=True)

    def __str__(self):
        return self.project

