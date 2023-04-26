from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
#from django.contrib.admin.widgets import AdminDateWidget
#from django.forms.fields import DateField
#import forms


class Trip(models.Model):
    destination = models.CharField(max_length=30)
    arrivalDay = models.DateField(auto_now_add=False, auto_now=False, blank=True)
    returnDay = models.DateField(auto_now_add=False, auto_now=False, blank=True)
   # trip_length= DateField(widget=AdminDateWidget)
   # start_date=forms.DateField(widget = forms.SelectDateWidget())
   # end_date=forms.DateField(widget = forms.SelectDateWidget())
    time = models.IntegerField(max_length=7)
    
    def __str__(self):
        
        return self.destination

class Day(models.Model):
    
    trip_id= models.ForeignKey(Trip, on_delete= models.CASCADE)
    
    date = models.DateField()
    
    def __str__(self):
        
        return self.destination




class Transportation(models.Model):
    
    number_buses = models.IntegerField(max_length=10)
    
    cost_transportation = models.IntegerField(max_length=100)
    
    # day = team = models.ForeignKey(Day, on_delete=models.CASCADE)
    
    def __str__(self):
        
        return self.destination
    
class Lunch(models.Model):
    
    name_restaurant_lunch = models.CharField(max_length=30)
    
    completed_lunch = models.BooleanField()
        
    cost_lunch = models.IntegerField(max_length=1000, null=True)
        
    satisfaction_lunch = models.IntegerField(max_length=5, null=True)
        
    day = models.ForeignKey(Day, on_delete=models.CASCADE)
        
    def __str__(self):
        return self.destination

class Dinner(models.Model):
    
    name_restaurant_dinner = models.CharField(max_length=30)
    
    cost_dinner = models.IntegerField(max_length=1000, null=True)
        
    completed_dinner = models.BooleanField()
        
    satisfaction_dinner = models.IntegerField(max_length=5, null=True)
        
    day = models.ForeignKey(Day, on_delete=models.CASCADE)

    def __str__(self):
        
        return self.destination
    
class Activity(models.Model):
    
    name_activity = models.CharField(max_length=30)
        
    completed_activity = models.BooleanField()
        
    cost_activity = models.IntegerField(max_length=1000, null=True)
        
    satisfaction_activity = models.IntegerField(max_length=5, null=True)
        
    day = models.ForeignKey(Day, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.destination