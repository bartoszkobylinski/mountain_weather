from django_cron import CronJobBase, Schedule
from zakopane_weather.mountain import get_data
from zakopane_weather.models import Day, DailyForecast
from zakopane_weather.location import location
class MyCronJob(CronJobBase):
    RUN_EVERY_MINS = 1440

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'zakopane_weather.my_cron_job' 
    def do(self):
        weather_forecast_from_accuweather = get_data()
        current_date = Day()
        current_date.save()
        daily_objects = [DailyForecast(**element, date=current_date) for element in weather_forecast_from_accuweather]
        DailyForecast.objects.bulk_create(daily_objects)
        print("job is done")
