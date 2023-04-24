from django.db import models

# Create your models here.
class Trip(models.Model):
    
    destination = models.CharField(max_length=30)
    
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
    
    day = team = models.ForeignKey(Day, on_delete=models.CASCADE)
    
    def __str__(self):
        
        return self.destination
    
class Lunch(models.Model):
    
    name_restaurant_lunch = models.CharField(max_length=30)
    
    completed_lunch = models.BooleanField()
    
    cost_lunch = models.IntegerField(max_length=1000, default=-1)
    
    satisfaction_lunch = models.IntegerField(max_length=5, default=-1)
    
    day = models.ForeignKey(Day, on_delete=models.CASCADE)
    
    def __str__(self):
        
        return self.destination


class Dinner(models.Model):
    
    name_restaurant_dinner = models.CharField(max_length=30)
    
    cost_dinner = models.IntegerField(max_length=1000, default=-1)
    
    completed_dinner = models.BooleanField()
    
    satisfaction_dinner = models.IntegerField(max_length=5, default=-1)
    
    day = models.ForeignKey(Day, on_delete=models.CASCADE)
    
    def __str__(self):
        
        return self.destination
    
class Activity(models.Model):
    
    name_activity = models.CharField(max_length=30)
    
    completed_activity = models.BooleanField()
    
    cost_activity = models.IntegerField(max_length=1000, default=-1)
    
    satisfaction_activity = models.IntegerField(max_length=5, default=-1)
    
    day = models.ForeignKey(Day, on_delete=models.CASCADE)
    
    def __str__(self):
        
        return self.destination
    
    
    
    
    
    
    
    
    
    
    