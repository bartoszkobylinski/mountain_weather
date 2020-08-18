import logging
<<<<<<< HEAD

=======
import datetime
from time import time
from django.conf import settings
from django.utils.timezone import make_aware
>>>>>>> cba6b96ca00e15638d0ee52b7aec50927b70034b
from django_cron import CronJobBase, Schedule
from zakopane_weather.avalanche import get_avalanche_status
from zakopane_weather.mountain import (get_zakopane_daily_weather,
                                       get_zakopane_hourly_weather)
from zakopane_weather.scraper import get_pekas_detailed_weather
<<<<<<< HEAD
from zakopane_weather.models import (DailyForecast,
=======
from zakopane_weather.models import (DailyForecast, 
>>>>>>> cba6b96ca00e15638d0ee52b7aec50927b70034b
                                     HourlyForecast,
                                     AvalancheStatus,
                                     AreaWeatherForecast,
                                     PeakForecast)
<<<<<<< HEAD
=======
from zakopane_weather.location import location
>>>>>>> cba6b96ca00e15638d0ee52b7aec50927b70034b
from zakopane_weather.area_scraper import get_tatras_areas_weather_forecast

logging.basicConfig(filename="cron.log", level=logging.WARNING)


<<<<<<< HEAD
class DailyForecastAccuweatherJob(CronJobBase):
    """
    class for cron job to upload daily weather forecast from
    Accuweather.
    """
    RUN_EVERY_MINS = 1440
    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'zakopane_weather.daily_forecast_accuweather_job'

    def do(self):
        """
        method describing procedure to upload and save
        current weather forecast for next 5 days.
        """
        DailyForecast.objects.all().delete()
        daily_weather_forecast_from_accuweather = get_zakopane_daily_weather()
        daily_objects = [DailyForecast(**element)
                         for element in
                         daily_weather_forecast_from_accuweather]
        DailyForecast.objects.bulk_create(daily_objects)


class HourlyForecastAccuweatherJob(CronJobBase):
    """
    class for cron job to upload hourly weather forecast from
    Accuweather.
    """
    RUN_EVERY_MINS = 1440
    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'zakopane_weather.hourly_forecast_accuweather_job'

    def do(self):
        """
        method describing procedure to upload and save
        current weather forecast for next 11 hours.
        """
        HourlyForecast.objects.all().delete()
        hourly_weatherforecast_from_accuweather = get_zakopane_hourly_weather()
        hourly_objects = [HourlyForecast(**element)
                          for element in
                          hourly_weatherforecast_from_accuweather]
        HourlyForecast.objects.bulk_create(hourly_objects)


class AvalancheStatusJob(CronJobBase):
    """
    class for cron job to upload avalanche status in Tatras Mountain
=======
class MyCronJob(CronJobBase):
    """
    class for uploading database 
>>>>>>> cba6b96ca00e15638d0ee52b7aec50927b70034b
    """
    RUN_EVERY_MINS = 1440
    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'zakopane_weather.avalanche_status'

    def do(self):
        """
        method describing procedure to upload and save avalanche status
        """
        if len(AvalancheStatus.objects.all()) > 0:
            AvalancheStatus.objects.all().delete()
        avalanche_status = get_avalanche_status()
        avalanche = AvalancheStatus(**avalanche_status)
        avalanche.save()


class PeakForecastJob(CronJobBase):
    """
    class for cron job to upload and update peak weather forecast in Tatras
    Mountain
    """
    RUN_EVERY_MINS = 1440
    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
<<<<<<< HEAD
    code = 'zakopane_weather.peakforecast'

    def do(self):
        """
        method describing procedure to upload and save peaks weather
        forecast
        """
=======
    code = 'zakopane_weather.my_cron_job'

    # Add function sending mail when cron jobs failed!

    def do(self):
        start = time()
        print(start)
        
        naive_datetime = datetime.datetime.now()
        naive_datetime.tzinfo

        settings.TIME_ZONE
        aware_datetime = make_aware(naive_datetime)
        aware_datetime.tzinfo
        

        print("I started cron jobs")

        try:
            DailyForecast.objects.all().delete()
            print('delete')
        except Exception as err:
            print(err)

        try:
            daily_weather_forecast_from_accuweather = get_zakopane_daily_weather()
            print(f"that is {daily_weather_forecast_from_accuweather}")
        except Exception as err:
            print(f"som as: {err}")
        try:
            daily_objects = [DailyForecast(**element) for element in daily_weather_forecast_from_accuweather]
        except Exception as err:
            print(f"while cron trying to unpack objects to daily_objects an error occur: {err}")
        try:
            DailyForecast.objects.bulk_create(daily_objects)
        except Exception as error:
            print(error)
        print("I have finished scraping and uploading daily weather")
>>>>>>> cba6b96ca00e15638d0ee52b7aec50927b70034b

        PeakForecast.objects.all().delete()
        for forecast in get_pekas_detailed_weather():
            for peak in forecast:
                peak_weatherforecast = PeakForecast(
                    name_of_peak=peak['name_of_peak'],
                    elevation=peak['elevation'],
                    date=peak['date'],
                    windspeed=peak['windspeed'],
                    summary=peak['summary'],
                    rain=peak['rain'],
                    snow=peak['snow'],
                    temperature=peak['temperature'],
                    chill_temperature=peak['chill_temperature'])
                peak_weatherforecast.save()


class AreaWeatherForecastJob(CronJobBase):
    """
    class for cron job to upload and update areas weather forecast in Tatras
    Mountain
    """
    RUN_EVERY_MINS = 1440
    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'zakopane_weather.areas_weather'

    def do(self):
        """
        method describing procedure to upload and save peaks weather
        forecast
        """
        AreaWeatherForecast.objects.all().delete()
        tatras_areas_weather_forecast = get_tatras_areas_weather_forecast()
        weather_forecasts_areas = [AreaWeatherForecast(**element)
                                   for element in
                                   tatras_areas_weather_forecast]
        AreaWeatherForecast.objects.bulk_create(weather_forecasts_areas)
