from django.shortcuts import render, redirect
from .models import Trip, Day

def home(request):
    return render(request, 'voyage/index.html')

def trips(request):
    tripsList = Trip.objects.order_by('id')
    context = {'trips': tripsList}
    return render(request, 'voyage/trips.html', context)


def days(request,day_id ):
    dayObj = Day.objects.get(id = day_id)
    
    dayList = dayObj
    
    context = {'days': dayList}
    
    return render(request, 'voyage/.html', context)

