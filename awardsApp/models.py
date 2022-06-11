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
