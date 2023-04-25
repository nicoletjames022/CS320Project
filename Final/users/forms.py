from django import forms
from .models import Person

class PersonForm(forms.ModelForm):

    class meta:
        model = Person

        fields = ["birthdate"]

        labels = {'birthdate': 'Birth date'}