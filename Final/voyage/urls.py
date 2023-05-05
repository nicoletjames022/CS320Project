from django.urls import path
from . import views

app_name = 'voyage' 

urlpatterns = [
    path('', views.home, name='home'),
    path('trips/',views.trips, name='trips'),
    path('trips/addTrip',views.addTrip, name='addTrip'),
    path('trips/<int:day_id>/', views.showItinerary, name='showItinerary'),
    path('trips/<int:day_id>/new_Activity', views.new_Activity, name='new_Activity'),
    path('trips/<int:day_id>/new_Transportation', views.new_Transportation, name='new_Transportation'),
    path('trips/<int:day_id>/new_Lunch', views.new_Lunch, name='new_Lunch'),
    path('trips/<int:day_id>/new_Dinner', views.new_Dinner, name='new_Dinner'),
    path('trips/<int:trip_id>/', views.showTrip, name='showTrip'),
    path('trips/<int:day_id>/showActivity/', views.showItinerary, name='showActivity'),
    path('trips/<int:day_id>/showLunch/', views.showItinerary, name='showLunch'),
    path('trips/<int:day_id>/showDinner/', views.showItinerary, name='showDinner'),
    path('trips/<int:day_id>/showTransportation/', views.showItinerary, name='showTransportation'),
]

