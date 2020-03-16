import logging

from django_cron import CronJobBase, Schedule
from zakopane_weather.mountain import get_zakopane_daily_weather, get_zakopane_hourly_weather
from zakopane_weather.scraper import get_pekas_detailed_weather, get_peaks_information, peaks
from zakopane_weather.models import DailyForecast, HourlyForecast, OctaveOfDay, Mountain
from zakopane_weather.location import location

logging.basicConfig(filename="cron.log",level=logging.WARNING)

class MyCronJob(CronJobBase):
    RUN_EVERY_MINS = 1440

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'zakopane_weather.my_cron_job' 
    
    #Add function sending mail when cron jobs failed!

    def do(self):
        
        print("I started job")
        daily_weather_forecast_from_accuweather = get_zakopane_daily_weather()
        daily_objects = [DailyForecast(**element) for element in daily_weather_forecast_from_accuweather]
        print(daily_objects)
        print("after daily")
        try:
            DailyForecast.objects.bulk_create(daily_objects)
        except Exception as error:
            print(error)
        hourly_weather_forecast_from_accuweather = get_zakopane_hourly_weather()
        print(hourly_weather_forecast_from_accuweather)
        print("I'm here")
        try:
            hourly_objects = [HourlyForecast(**element) for element in hourly_weather_forecast_from_accuweather]
        except Exception as error:
            print(error)
        print("and heree")
        HourlyForecast.objects.bulk_create(hourly_objects)
        print("job is done")
        
        peaks_detail = []
        print("after job is done")
       
        peaks_data = get_peaks_information()
        try:
            for peaks  in peaks_data:
                print("i am in")
                mountain = Mountain(elevation = peaks['elevation'], name_of_peak = peaks['name_of_peak'])
                print("i am inside for  loop")
                mountain.save()
                print(" i have saved mountain")
                peaks_detail.append(peaks)
        except Exception as error:
            print(error)
        
        forecast_for_all_peaks = get_pekas_detailed_weather()
        for peak in forecast_for_all_peaks:
            for forecast in peak:
                try:
                    name = Mountain.objects.get(name_of_peak = forecast['name_of_peak'])   
                except Exception as error:
                    print("I tried assign name to mountain object but some error occured: " + str(error))
                try:
                    a = OctaveOfDay(
                        name_of_peak = name,
                        date = forecast['date'],
                        octave_of_a_day = forecast['octave_of_a_day'],
                        windspeed = forecast['windspeed'],
                        summary = forecast['summary'],
                        rain = forecast['rain'],
                        snow = forecast['snow'],
                        temperature = forecast['temperature'],
                        chill_temperature = forecast['chill_temperature'])
                    print(a)
                except Exception as error:
                    print("I tried assign a to Octave of a day but some error occured: " + str(error))
                try:
                    a.save()
                    print("I am after saving")
                except Exception as error:
                    logging.warning("Error ocured: " + str(error))

    





