# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 15:13:59 2023

@author: jmenichincheri
"""

from django import forms
from .models import Trips

class TeamForm(forms.ModelForm):
    class Meta:
        model = Trips
        fields = ['Destination', 'Time']
        labels = {'Destination': 'Destination of trip', 'Time': 'Dates of your trip'}

