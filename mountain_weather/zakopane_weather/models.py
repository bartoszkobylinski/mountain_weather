from django.db import models
from datetime import datetime, date


# Create your models here.
 

class HourlyForecast(models.Model):
    temp = models.IntegerField()
    real_feel_temp = models.IntegerField()
    wind_speed = models.IntegerField()
    rain_probability = models.IntegerField()
    cloud_cover = models.IntegerField()
    date_time = models.DateTimeField()
    

    def __str__(self):
        return f"Weather forecast for {self.date_time}"

class DailyForecast(models.Model):
    min_temp = models.IntegerField()
    max_temp = models.IntegerField()
    phrase = models.CharField(max_length=150)
    probability = models.IntegerField()
    wind_speed = models.IntegerField()
    date = models.DateField(default=date.today)
    

    def __str__(self):
        return f"Weather forecast for {self.date}"

class Mountain(models.Model):
    name_of_peak = models.CharField(max_length=50, default='Random Peak')
    elevation = models.IntegerField()

    def __str__(self):
        return f"{self.name_of_peak} with elevation {self.elevation} over sea level"

class OctaveOfDay(models.Model):
    name_of_peak = models.ForeignKey(Mountain,on_delete=models.CASCADE)
    date = models.DateField(default=date.today)
    octave_of_a_day = models.CharField(max_length=50)
    windspeed = models.IntegerField()
    summary = models.CharField(max_length=500)
    rain = models.IntegerField()
    snow = models.IntegerField()
    temperature = models.IntegerField()
    chill_temperature = models.IntegerField()

    def __str__(self):
       return f''' At {self.name_of_peak} at {self.date} {self.octave_of_a_day} is going to be
       {self.summary} with {self.rain} of rain and {self.snow} of snow and {self.windspeed} windspeed. Tempereture is going to be
       {self.temperature} Celsius and chilling temp is going to be {self.chill_temperature}.''' 

class AvalancheStatus(models.Model):
    avalanche_level = models.IntegerField()
    avalanche_description = models.CharField(max_length=200)
    avalanche_warning_published = models.DateTimeField()
    avalanche_warning_valid_until = models.DateTimeField()

    date = models.DateField(auto_now_add=True)