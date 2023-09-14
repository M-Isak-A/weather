from django.urls import path
from . import views

urlpatterns = [
    # Set landing page to Leicester weather
    path('', views.get_weather, name='landing_page'),
    path('get_weather/', views.get_weather, name='get_weather'),
]
