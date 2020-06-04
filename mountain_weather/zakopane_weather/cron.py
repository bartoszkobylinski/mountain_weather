import logging
from time import time

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
        daily_objects = [DailyForecast(**element) for element in daily_weather_forecast_from_accuweather]
        try:
            DailyForecast.objects.bulk_create(daily_objects)
        except Exception as error:
            print(error)
        print("I have finished scraping and uploading daily weather")

        HourlyForecast.objects.all().delete()

        hourly_weather_forecast_from_accuweather = get_zakopane_hourly_weather()
        try:
            hourly_objects = [HourlyForecast(**element) for element in hourly_weather_forecast_from_accuweather]
        except Exception as error:
            print(error)
        HourlyForecast.objects.bulk_create(hourly_objects)
        print("I have finished scraping and uploading hourly weather")
        AvalancheStatus.objects.all().delete()

        avalanche_status = get_avalanche_status()
        try:
            avalanche = AvalancheStatus(**avalanche_status)
        except Exception as error:
            print(f"Error occured {error}")
        try:
            avalanche.save()
        except Exception as error:
            print(f"Occured error while saving {error}")
        print("I have finished scraping and uploadnig avalanche warning")
        
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
                                                chill_temperature=peak['chill_temperature']
                                                )
                print(peak_weatherforecast)
                peak_weatherforecast.save()
            '''
            for forecast in peak:
                try:
                    name = Mountain.objects.get(name_of_peak = forecast['name_of_peak'])   
                except Exception as error:
                    print("I tried assign name to mountain object but some error occured: " + str(error))
                try:
                    print(f"I have printed a datetime:{forecast['date']}")
                    a = OctaveOfDay(
                        name_of_peak=name,
                        date=forecast['date'],
                        windspeed=forecast['windspeed'],
                        summary=forecast['summary'],
                        rain=forecast['rain'],
                        snow=forecast['snow'],
                        temperature=forecast['temperature'],
                        chill_temperature=forecast['chill_temperature'])
                except Exception as error:
                    print("I tried assign a to Octave of a day but some error occured: " + str(error))
                try:
                    a.save()
                    print("I have saved data")
                except Exception as error:
                    logging.warning("Error ocured: " + str(error))
            '''
        print("I have finised scraping octave of day and uploading to database")
        AreaWeatherForecast.objects.all().delete()
        tatras_areas_weather_forecast = get_tatras_areas_weather_forecast()
        weather_forecasts_areas = [AreaWeatherForecast(**element) for element in tatras_areas_weather_forecast]
        AreaWeatherForecast.objects.bulk_create(weather_forecasts_areas)
        print("I have finished scraping TPN")
        end = time()
        result = end - start
        
        print(f"time is {result}")
        logging.info(f"Scraping operation has been executing in {result} seconds.")
