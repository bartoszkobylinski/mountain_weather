import logging
import datetime
from time import time

from django.conf import settings
from django.utils.timezone import make_aware
from django_cron import CronJobBase, Schedule
from zakopane_weather.avalanche import get_avalanche_status
from zakopane_weather.mountain import get_zakopane_daily_weather, get_zakopane_hourly_weather
from zakopane_weather.scraper import get_pekas_detailed_weather
from zakopane_weather.models import DailyForecast, HourlyForecast, AvalancheStatus, AreaWeatherForecast, PeakForecast
from zakopane_weather.location import location
from zakopane_weather.area_scraper import get_tatras_areas_weather_forecast

logging.basicConfig(filename="cron.log",level=logging.WARNING)



class MyCronJob(CronJobBase):
    RUN_EVERY_MINS = 1440

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'zakopane_weather.my_cron_job' 
    
    #Add function sending mail when cron jobs failed!

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

        HourlyForecast.objects.all().delete()
        try:
            hourly_weather_forecast_from_accuweather = get_zakopane_hourly_weather()
        except Exception as err:
            print(f"while cron trying to get from accu hourly forecast an error occured: {err}")

        try:
            hourly_objects = [HourlyForecast(**element) for element in hourly_weather_forecast_from_accuweather]
        except Exception as error:
            print(error)
        try:
            HourlyForecast.objects.bulk_create(hourly_objects)
        except Exception as err:
            print(f"while cron tried bulkcreate objects en error occured: {err}")
        print("I have finished scraping and uploading hourly weather")
        #AvalancheStatus.objects.all().delete()
        try:
            avalanche_status = get_avalanche_status()
        except Exception as err:
            print(f"while trying get avalanche status from avalanche scraper an error occur: {err}")
        try:
            avalanche = AvalancheStatus(**avalanche_status)
        except Exception as error:
            print(f"Error occured {error}")
        try:
            avalanche.save()
        except Exception as error:
            print(f"Occured error while saving {error}")
        print("I have finished scraping and uploadnig avalanche warning")
        PeakForecast.objects.all().delete()
        print("I have removed Peaks info from database")
        try:
            for forecast in get_pekas_detailed_weather():
                print("Im in loop")
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
                                                chill_temperature=peak['chill_temperature']
                                                )
                    try:                            
                        peak_weatherforecast.save()
                    except Exception as err:
                        print(f"while saving error occured {err}")
        except Exception as err:
            print(f"While scraper try get peaks data en error ocurred: {err}")
        print("I have finised scraping octave of day and uploading to database")

        AreaWeatherForecast.objects.all().delete()
        print("I have remove AreaWeeather from database")

        tatras_areas_weather_forecast = get_tatras_areas_weather_forecast()
        weather_forecasts_areas = [AreaWeatherForecast(**element) for element in tatras_areas_weather_forecast]
        AreaWeatherForecast.objects.bulk_create(weather_forecasts_areas)
        print("I have finished scraping TPN")
        end = time()
        result = end - start
        
        print(f"time is {result}")
        logging.info(f"Scraping operation has been executing in {result} seconds.")
