from django.urls import path
from . import views

app_name = 'voyage' 

urlpatterns = [
    path('', views.home, name='home'),
    path('trips/',views.trips, name='trips'),
    path('trips/days',views.trips, name='days'),
    path('trips/days/transportation',views.trips, name='transportation'),
    path('trips/days/lunch',views.trips, name='lunch'),
    path('trips/days/dinner',views.trips, name='dinner'),
    path('trips/days/activities',views.trips, name='activities'),
]