from django.contrib import admin

from .models import (HourlyForecast, 
                     DailyForecast, 
                     AvalancheStatus, 
                     PeakForecast,
                     AreaWeatherForecast)

# Register your models here.

admin.site.register(HourlyForecast)
admin.site.register(DailyForecast)
admin.site.register(AvalancheStatus)
admin.site.register(AreaWeatherForecast)
admin.site.register(PeakForecast)
