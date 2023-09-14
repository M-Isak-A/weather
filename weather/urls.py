from django.urls import path
# Import the get_weather function from your views module
from .views import get_weather

urlpatterns = [
    # Set landing page to Leicester weather
    path('', get_weather, name='landing_page'),
]
