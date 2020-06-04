from django.contrib import admin

from .models import (HourlyForecast, DailyForecast, OctaveOfDay, AvalancheStatus,
                     AreaWeatherForecast)

# Register your models here.

admin.site.register(HourlyForecast)
admin.site.register(DailyForecast)
admin.site.register(OctaveOfDay)
admin.site.register(AvalancheStatus)
admin.site.register(AreaWeatherForecast)
