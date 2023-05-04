from django.urls import path
from . import views

app_name = 'voyage' 

urlpatterns = [
    path('', views.home, name='home'),
    path('trips/',views.trips, name='trips'),
    path('trips/addTrip',views.addTrip, name='addTrip'),
    path('trips/<int:trip_id>/', views.showTrip, name='showTrip'),
    path('trips/showItinerary/', views.showItinerary, name='showItinerary'),
    path('trips/showItinerary/new_Activity', views.new_Activity, name='new_Activity'),
    path('trips/showItinerary/new_Transportation', views.new_Transportation, name='new_Transportation'),
    path('trips/showItinerary/new_Lunch', views.new_Lunch, name='new_Lunch'),
    path('trips/showItinerary/new_Dinner', views.new_Dinner, name='new_Dinner'),
]