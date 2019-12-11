from django_cron import CronJobBase, Schedule
from zakopane_weather.mountain import get_daily_weather, get_hourly_weather
from zakopane_weather.models import Day, DailyForecast, HourlyForecast
from zakopane_weather.location import location
class MyCronJob(CronJobBase):
    RUN_EVERY_MINS = 1440

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'zakopane_weather.my_cron_job' 
    def do(self):
        daily_weather_forecast_from_accuweather = get_daily_weather()
        current_date = Day()
        current_date.save()
        daily_objects = [DailyForecast(**element, date=current_date) for element in daily_weather_forecast_from_accuweather]
        DailyForecast.objects.bulk_create(daily_objects)
        hourly_weather_forecast_from_accuweather = get_hourly_weather()
        hourly_objects = [HourlyForecast(**element, date=current_date) for element in hourly_weather_forecast_from_accuweather]
        HourlyForecast.objects.bulk_create(hourly_objects)
        print("job is done")
