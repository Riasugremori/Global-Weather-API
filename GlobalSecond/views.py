from .serializers import CitySerializer
import requests
from rest_framework import status
from .models import City
from django.http import JsonResponse, HttpResponse

def weather_views(request, city):
    api_key = '3ad6446f6a7caa7a3c209595b95d51f3'
    base_url = 'http://api.openweathermap.org/data/2.5/weather'

    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'
    }

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        weather_data = response.json()
        temperature = weather_data['main']['temp']
        humidity = weather_data['main']['humidity']
 


        city_obj = City.objects.create(name=city, temperature=temperature, humidity=humidity)


        serializer = CitySerializer(city_obj)

        return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
    
    else:
        return HttpResponse('Unable to fetch data', status=status.HTTP_400_BAD_REQUEST)
