# -*- coding: utf-8 -*-
from django import forms
from .models import Transportation, Dinner, Lunch, Activities, Trip, Day

class TransportationForm(forms.ModelForm):
    class Meta:
        model = Transportation
        fields = ['number_buses', 'cost_transportation']
        labels = {'number_buses': 'Number of busses (or other) taken', 'cost_transportation': 'Total cost of transportation'}

class LunchForm(forms.ModelForm):
    class Meta:
        model = Lunch
        fields = ['name_restaurant_lunch', 'completed_lunch', 'cost_lunch', 'satisfaction_lunch']
        labels = {'name_restaurant_lunch': 'Restourant name', 'completed_lunch': 'Completed', 'cost_lunch': 'Lunch cost', 'satisfaction_lunch': "Rate 1-5"}

class DinnerForm(forms.ModelForm):
    class Meta:
        model = Dinner
        fields = ['name_restaurant_dinner', 'completed_dinner', 'cost_dinner', 'satisfaction_dinner']
        labels = {'name_restaurant_dinner': 'Restourant name', 'completed_lunch': 'Completed', 'cost_dinner': 'Dinner cost', 'satisfaction_dinner': "Rate 1-5"}


class ActivityForm(forms.ModelForm):
    class Meta:
        model = Activities
        fields = ['name_activity', 'completed_activity', 'cost_activity', 'satisfaction_activity']
        labels = {'name_activity': 'Name of the activity', 'completed_activity': 'Completed', 'cost_activity': 'Cost of activity', 'satisfaction_activity': "Rate 1-5"}

class TripForm(forms.ModelForm):
    class Meta:
        model = Trip
        fields = ['destination', 'time']
        labels = {'destination': 'Destination of trip', 'time': 'How many days is your trip?'}

class DayForm(forms.ModelForm):
    class Meta:
        model = Day
        fields = ['trip_id', 'date']
        labels = {'trip_id': 'Insert trip', 'date': 'Insert date'}