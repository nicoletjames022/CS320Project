from django import forms
from .models import Team, Player

class TeamForm(forms.ModelForm):
    
    class Meta:
    
        model = Team
        
        fields = ["name", "city"]
        
        labels = {'name': 'Team name', 'city': 'City of the team'}
        
class PlayerForm(forms.ModelForm):
    
    class Meta:
    
        model = Player
        
        fields = ["firstname", "lastname", "team"]
        
        labels = {'firstname': 'First name',
                  'lastname': 'Last name',
                  "team" : "Plays in: "}
        
        
        
        
        
        
        
        