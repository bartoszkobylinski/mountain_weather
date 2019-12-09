from django.contrib import admin

from .models import Day, HourlyForecast, DailyForecast

# Register your models here.

admin.site.register(Day)
admin.site.register(HourlyForecast)
admin.site.register(DailyForecast)
