from django.shortcuts import render, redirect
from .models import Trip, Day
from .forms import TripForm

def home(request):
    return render(request, 'voyage/index.html')

def trips(request):
    tripsList = Trip.objects.order_by('id')
    context = {'trips': tripsList}
    return render(request, 'voyage/trips.html', context)

def addTrip(request):
    if request.method != 'POST':
        form = TripForm()
    else: 
        form = TripForm(data=request.POST)
        if form.is_valid():
            form.save()

            return redirect('voyage:trips')
    context = {'form': form} 
    return render(request, 'voyage/trips.html', context)
    

def days(request, trip_id):
   
    tripObj = Trip.objects.get(id = trip_id)
    
    daysList = tripObj.day_set.all()

    context = {'days': daysList}
    
    return render(request, 'voyage/.html', context)
