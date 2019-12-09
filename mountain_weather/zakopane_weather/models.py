from django.db import models

# Create your models here.
class Day(models.Model):
    date = models.DateField()

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