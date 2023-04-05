from django.db import models

from django.contrib.auth.models import User

# Create your models here.
class Team(models.Model):
    
    name = models.CharField(max_length=30)
    
    city = models.CharField(max_length=30)
    
    userOwner = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        
        return self.name + " from " + self.city
    
class Player(models.Model):
    
    firstname = models.CharField(max_length=30)
    
    lastname = models.CharField(max_length=30)
    
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    
    teams = models.ManyToManyField(Team)
    
    def __str__(self):
        
        return self.firstname + " " + self.lastname
    
    
    
    
    
    