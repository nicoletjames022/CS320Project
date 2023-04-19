from django.shortcuts import render
from .models import Trip, Transportation, Dinner, Luch, Activities
def home(request):
    return render(request, 'voyage/index.html')

def trips(request):
    tripsList = Trip.objects.order_by('id')
    context = {'trips': tripsList}
    return render(request, 'voyage/trips.html', context)

