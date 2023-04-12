from django.shortcuts import render

def home(request):
    return render(request, 'voyage/index.html'); 
