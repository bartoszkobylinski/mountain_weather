"""
Model sturcture
"""

from datetime import date
from django.db import models

class HourlyForecast(models.Model):
    """
    Model for hourly forecast of Zakopane city
    """
    temp = models.IntegerField()
    real_feel_temp = models.IntegerField()
    wind_speed = models.IntegerField()
    rain_probability = models.IntegerField()
    cloud_cover = models.IntegerField()
    date_time = models.DateTimeField()

    def __str__(self):
        return f"Weather forecast for {self.date_time}"

class DailyForecast(models.Model):
    """
    Model for daily forecast of Zakopane city
    """
    min_temp = models.IntegerField()
    max_temp = models.IntegerField()
    phrase = models.CharField(max_length=150)
    probability = models.IntegerField()
    wind_speed = models.IntegerField()
    date = models.DateField(default=date.today)

    def __str__(self):
        return f"Weather forecast for {self.date}"


class PeakForecast(models.Model):
    """
    Model for weatherforecast divided on 8 part in day for specific mountain
    """
    name_of_peak = models.CharField(max_length=50, default='Random Peak')
    elevation = models.IntegerField(default=0)
    date = models.DateTimeField()
    windspeed = models.IntegerField()
    summary = models.CharField(max_length=500)
    rain = models.IntegerField()
    snow = models.IntegerField()
    temperature = models.IntegerField()
    chill_temperature = models.IntegerField()

    def __str__(self):
        return f'{self.name_of_peak}'

class AvalancheStatus(models.Model):
    """
    Model for avalanche status in Tatras mountains
    """
    avalanche_level = models.IntegerField()
    avalanche_description = models.CharField(max_length=1500)
    avalanche_warning_published = models.DateTimeField()
    avalanche_warning_valid_until = models.DateTimeField()

    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f''' Avalanche warnings at {self.date}.'''

class AreaWeatherForecast(models.Model):
    """ Model for particular area in Tatras Mountain """
    name = models.CharField(max_length=40)
    date = models.DateField()
    #weather_icon = models.ImageField()
    temp_min = models.IntegerField()
    temp_max = models.IntegerField()
    pressure = models.FloatField()
    rain = models.FloatField()

    def __str__(self):
        return f"""Weather forecast for {self.name} at {self.date}."""
        