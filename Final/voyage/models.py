from django.db import models

# Create your models here.
class Trip(models.Model):
    destination = models.CharField(max_length=30)
    time = models.CharField(max_length=30)

def __str__(self):
    return self.destination