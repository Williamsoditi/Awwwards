from django.forms import PasswordInput
from django.test import TestCase
from .models import *
from django.contrib.auth.models import User

# Create your tests here.
class ProjectTestCase(TestCase):
    
    def setUp(self):
        """
        Create a project for testing
        """
        self.user=User(username='williams',email='williamsoditi99@gmail.com',password='qwerty1234')
        self.project=Project(image='SayCheese.jpg',title='SayCheese',description='SayCheese',url='github.com', user=self.user)
        self.rate=Rating(user=self.user, content=0, usability=0, design=0, average=0, project=self.project)


    def test_instance(self):
        self.assertTrue(isinstance(self.user,User))
        self.assertTrue(isinstance(self.project,Project))
        self.assertTrue(isinstance(self.rate,Rating))
    
    def test_save(self):
        self.user.save()
        self.project.save_project()
        self.rate.save()
        
        users = User.objects.all()
        projects = Project.objects.all()
        rates = Rating.objects.all()
        
        self.assertTrue(len(projects) > 0)
        self.assertTrue(len(users) > 0)
        self.assertTrue(len(rates) > 0)
        
    def test_update(self):
        self.user.save()
        self.project.save_project()

    def test_delete(self):
        self.user.save()
        self.project.save_project()
        self.rate.save()
      
        Rating.objects.get(id =self.rate.id).delete()
        Project.objects.get(id =self.project.id).delete()
        User.objects.get(id =self.user.id).delete()
        rates=Rating.objects.all()
        projects=Project.objects.all()
        
        users=User.objects.all()
        self.assertTrue(len(rates) == 0)
        self.assertTrue(len(users) == 0)
        self.assertTrue(len(projects) == 0)

   