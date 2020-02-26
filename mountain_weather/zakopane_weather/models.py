from django.db import models
from datetime import datetime

# Create your models here.
class Day(models.Model):
    date = models.DateField(auto_now=True)

    def __str__(self):
        return str(self.date)

    

class HourlyForecast(models.Model):
    temp = models.IntegerField()
    real_feel_temp = models.IntegerField()
    wind_speed = models.IntegerField()
    rain_probability = models.IntegerField()
    cloud_cover = models.IntegerField()
    date = models.ForeignKey(Day, on_delete=models.CASCADE)

class DailyForecast(models.Model):
    min_temp = models.IntegerField()
    max_temp = models.IntegerField()
    phrase = models.CharField(max_length=150)
    probability = models.IntegerField()
    wind_speed = models.IntegerField()
    date = models.ForeignKey(Day, on_delete=models.CASCADE)

    def __str__(self):
        return f"Weather forecast for {self.date}: minimal temperature: {self.min_temp}, maximal temperature: {self.max_temp}, {self.phrase}"

class Mountain(models.Model):
    name_of_peak = models.CharField(max_length=50)
    elevation = models.IntegerField()
    day = models.DateField()

    def __str__(self):
        return f"{self.name_of_peak} with elevation {self.elevation} over sea level"

class OctaveOfDay(models.Model):
    date = models.ForeignKey(Mountain,on_delete=models.CASCADE)
    octave_of_a_day = models.CharField(max_length=50)
    wind_speed = models.IntegerField()
    summary = models.CharField(max_length=50)
    rain = models.IntegerField()
    snow = models.IntegerField()
    temperature = models.IntegerField()
    chill_temperature = models.IntegerField()

    def __str__(self):
        return f'''At {self.date} {self.octave_of_a_day} is going to be
         {self.summary} with {self.rain} of rain and {self.snow} of snow and {self.wind_speed} windspeed. Tempereture is going to be
         {self.temperature} Celsius and chilling temp is going to be {self.chill_temperature}.'''
