from django.urls import path
from .views import weather_views

urlpatterns = [
    path('city/<str:city>/', weather_views, name='city') 
]
