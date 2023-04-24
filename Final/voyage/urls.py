from django.urls import path
from . import views

app_name = 'voyage' 

urlpatterns = [
    path('', views.home, name='home'),
    path('trips/',views.trips, name='trips'),
]