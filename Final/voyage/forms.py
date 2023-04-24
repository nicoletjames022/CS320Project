# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 15:13:59 2023

@author: jmenichincheri
"""

from django import forms
from .models import Trip

class TripForm(forms.ModelForm):
    class Meta:
        model = Trip
        fields = ['destination', 'time']
        labels = {'destination': 'Destination of trip', 'time': 'Dates of your trip'}



