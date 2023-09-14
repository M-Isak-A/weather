import requests
from django.shortcuts import render
from weather.models import Weather
from django.conf import settings


def get_image_for_weather(condition):
    if 'clear' in condition.lower():
        return 'images/sunny.png'
    elif 'cloud' in condition.lower():
        return 'images/cloudy.png'
    elif 'rain' in condition.lower():
        return 'images/rainy.png'
    else:
        return 'images/default.png'  # Provide a default image for unknown conditions


def get_weather(request):
    if request.method == 'POST':
        api_key = settings.OPENWEATHER_API_KEY  # Use the API key from settings
        location = request.POST['location']

        url = f'http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric'
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            temperature = data['main']['temp']
            condition = data['weather'][0]['description']
            weather_data, created = Weather.objects.get_or_create(
                location=location, defaults={
                    'temperature': temperature, 'condition': condition}
            )

            image_url = get_image_for_weather(condition)  # Get the image URL
        else:
            weather_data = None
            image_url = get_image_for_weather('default')

        return render(request, 'weather/weather.html', {'weather': weather_data, 'image_url': image_url})

    # Default location: Leicester
    default_location = 'Leicester'
    try:
        weather_data = Weather.objects.get(location=default_location)
    except Weather.DoesNotExist:
        weather_data = None

    image_url = get_image_for_weather(
        weather_data.condition) if weather_data else get_image_for_weather('default')

    return render(request, 'weather/weather.html', {'weather': weather_data, 'image_url': image_url})
