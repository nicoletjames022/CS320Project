# -*- coding: utf-8 -*-
from django import forms
from .models import Transportation, Dinner, Lunch, Activities

class TransportationForm(forms.ModelForm):
    class Meta:
        model = Transportation
        fields = ['number_buses', 'cost_transportation']
        labels = {'number_buses': 'Number of busses (or other) taken', 'cost_transportation': 'Total cost of transportation'}

class LunchForm(forms.ModelForm):
    class Meta:
        model = Lunch
        fields = ['name_restaurant_lunch', 'cost_lunch', 'satisfaction_lunch']
        labels = {'name_restaurant_lunch': 'Restourant name', 'cost_lunch': 'Lunch cost', 'satisfaction_lunch': "Rate 1-5"}

class DinnerForm(forms.ModelForm):
    class Meta:
        model = Dinner
        fields = ['name_restaurant_dinner', 'cost_dinner', 'satisfaction_dinner']
        labels = {'name_restaurant_dinner': 'Restourant name', 'cost_dinner': 'Dinner cost', 'satisfaction_dinner': "Rate 1-5"}


class ActivityForm(forms.ModelForm):
    class Meta:
        model = Activities
        fields = ['name_activity', 'cost_activity', 'satisfaction_activity']
        labels = {'name_activity': 'Name of the activity', 'cost_activity': 'Cost of activity', 'satisfaction_activity': "Rate 1-5"}






