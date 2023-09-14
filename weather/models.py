# weather/models.py

from django.db import models

class Weather(models.Model):
    location = models.CharField(max_length=100)
    temperature = models.FloatField()
    condition = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.location}: {self.temperature}°C, {self.condition}"

