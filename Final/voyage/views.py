from datetime import datetime
from django.shortcuts import render, redirect
from .models import Trip, Day
from .forms import TripForm, TransportationForm, LunchForm, DinnerForm, ActivityForm

def home(request):
    return render(request, 'voyage/index.html')

def trips(request):
    # tripsList = Trip.objects.filter(userOwner=request.user).order_by('id')
    tripsList = Trip.objects.all()

    context = {'trips': tripsList}

    return render(request, 'voyage/trips.html', context)

def addTrip(request):

    if request.method != 'POST':
        form = TripForm()
    else: 
        form = TripForm(data=request.POST)
        if form.is_valid():

            new_trip = form.save(commit=False)
            new_trip.userOwner = request.user
            new_trip.save()

            return redirect('voyage:trips')
    context = {'form': form} 
    return render(request, 'voyage/trips.html', context)

def showTrip(request, trip_id):
    tripObj = Trip.objects.get(id=trip_id)
    numOfDays = tripObj.time
    days_list = list(range(1, numOfDays+1, 1))

    context = {'trip' : tripObj, 'numOfDays': numOfDays, 'days_list':days_list}
    return render(request, 'voyage/showTrip.html', context)


def showItinerary(request):
    # dayObj = Day.objects.get(id=day_id)
    # context = {'day': dayObj}
    return render (request, 'voyage/showItinerary.html')


def addTransportation(request):
   if request.method != 'POST':
       form = TransportationForm()
   else: 
       form = TransportationForm(data=request.POST)
       if form.is_valid():
           form.save()

def addLunch(request):
   if request.method != 'POST':
       form = LunchForm()
   else: 
       form = LunchForm(data=request.POST)
       if form.is_valid():
           form.save()

def addDinner(request):
   if request.method != 'POST':
       form = DinnerForm()
   else: 
       form = DinnerForm(data=request.POST)
       if form.is_valid():
           form.save()

def addActivity(request):
   if request.method != 'POST':
       form = ActivityForm()
   else: 
       form = ActivityForm(data=request.POST)
       if form.is_valid():
           form.save()

#def days(request,day_id ):
    
 #   dayObj = Day.objects.get(id = day_id)
    
  #  dayList = dayObj.
    
   # context = {'days': dayList}
    
    #return render(request, 'voyage/.html', context)
