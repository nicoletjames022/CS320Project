from django.urls import path
from . import views

app_name = 'voyage' 

urlpatterns = [
    path('', views.home, name='home'),
    path('trips/',views.trips, name='trips'),
    path('trips/addTrip',views.addTrip, name='addTrip'),
    path('trips/<int:trip_id>/', views.showTrip, name='showTrip'),
    path('trips/showItinerary/', views.showItinerary, name='showItinerary'),
    path('trips/showItinerary/new_Activity', views.addActivity, name='new_Activity'),
    path('trips/showItinerary/new_Transportation', views.addTransportation, name='new_Transportation'),
    path('trips/showItinerary/new_Lunch', views.addLunch, name='new_Lunch'),
    path('trips/showItinerary/new_Dinner', views.addDinner, name='new_Dinner'),
]