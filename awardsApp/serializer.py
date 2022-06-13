from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from .models import Profile,Project

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ("profile_photo","bio","location","user")

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ("user","title","description","image","url","date")