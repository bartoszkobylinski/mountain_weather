import logging
from time import time

from django_cron import CronJobBase, Schedule
from zakopane_weather.avalanche import get_avalanche_status
from zakopane_weather.mountain import get_zakopane_daily_weather, get_zakopane_hourly_weather
from zakopane_weather.scraper import get_pekas_detailed_weather, get_peaks_information, peaks
from zakopane_weather.models import DailyForecast, HourlyForecast, OctaveOfDay, Mountain, AvalancheStatus
from zakopane_weather.location import location

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
        
        print("he")
        try:
            DailyForecast.objects.all().delete()
        except Exception as err:
            print(err)
        try:
            daily_weather_forecast_from_accuweather = get_zakopane_daily_weather()
        except Exception as err:
            print(f"som as {err}")
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

        OctaveOfDay.objects.all().delete()
        Mountain.objects.all().delete()
        
        print("I have deleted databases of mountain and octaveofday")
        peaks_detail = []
        peaks_data = get_peaks_information()
        try:
            for peaks  in peaks_data:
                mountain = Mountain(elevation = peaks['elevation'], name_of_peak = peaks['name_of_peak'])
                mountain.save()
                peaks_detail.append(peaks)
        except Exception as error:
            print(error)
        print("I have finished scraping and uploading mountain")
        
        forecast_for_all_peaks = get_pekas_detailed_weather()
        
        for peak in forecast_for_all_peaks:
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
        print("I have finised scraping octave of day and uploading to database")
        end = time()
        result = end - start
        print(f"time is {result}")
        logging.info(f"Scraping operation has been executing {result} seconds.")
        logging.info("That is time to run procces: " + str(end - start))

    





