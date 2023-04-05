from django.shortcuts import render, redirect

from .models import Team

from .forms import TeamForm, PlayerForm

# Create your views here.
def home(request):
    
    return render(request, "voyage/index.html")

def teams(request):
    
    teamsList = Team.objects.filter(userOwner=request.user).all()
       
    context = {"teamsList" : teamsList}
    
    return render(request, "voyage/showTeams.html", context)

def playersMan(request, team_id):
    
     #teamName = 1 # for now, the name is hard-coded
    
    teamObj = Team.objects.get(id=team_id); # get the Team object by name
    
    playersList = teamObj.player_set.all(); # get all players associated this team via FK
    
    # it is always <lower case name of the related class>_set
    context = {'players' : playersList, 'team' : teamObj}
    
    return render(request, 'voyage/playersManUnited.html', context)

def addTeam(request):
    
    if request.method != 'POST': # GET: No data submitted; create a blank form to insert
        form = TeamForm()
        
    else: # POST: Data submitted; process data, that is, validate and store
        
        form = TeamForm(data=request.POST)
        
        if form.is_valid():
            
            new_team = form.save(commit=False)
            
            new_team.userOwner = request.user
            
            new_team.save()
            
            return redirect('voyage:teams')
    
    context = {'form': form} # executed if the form was not valid
    
    return render(request, 'voyage/new_team.html', context)

def addPlayer(request):
    
    if request.method != 'POST': # GET: No data submitted; create a blank form to insert
        form = PlayerForm()
        
    else: # POST: Data submitted; process data, that is, validate and store
        
        form = PlayerForm(data=request.POST)
        
        if form.is_valid():
            
            form.save()
            
            return redirect('voyage:teams')
    
    context = {'form': form} # executed if the form was not valid
    
    return render(request, 'voyage/new_player.html', context)




def sumComputation(request):
    
    return render(request, 'voyage/insertNumbers.html')

def computeSum(request):
    
    first = request.POST.get("firstNumber")
    
    second = request.POST.get("secondNumber")
    
    result = int(first) + int(second)
    
    print(result)
    
    context = {"final" : first, "second" : second, "result" : result}
    
    return render(request, 'voyage/showResult.html', context)
    
    
    
    
    
    