# -*- coding: utf-8 -*-
from django import forms
from .models import Trip, Day

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