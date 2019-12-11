from django.db import models
from datetime import datetime

# Create your models here.
class Day(models.Model):
    date = models.DateField(auto_now=True)

    def __str__(self):
        return str(self.date)

    

class HourlyForecast(models.Model):
    min_temp = models.IntegerField()
    max_temp = models.IntegerField()
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