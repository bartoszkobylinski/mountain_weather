from django_cron import CronJobBase, Schedule
from zakopane_weather.mountain import get_zakopane_daily_weather, get_zakopane_hourly_weather
from zakopane_weather.scraper import get_pekas_detailed_weather, get_peaks_information, peaks
from zakopane_weather.models import DailyForecast, HourlyForecast, OctaveOfDay, Mountain
from zakopane_weather.location import location


class MyCronJob(CronJobBase):
    RUN_EVERY_MINS = 1440

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'zakopane_weather.my_cron_job' 
    
    #Add function sending mail when cron jobs failed!

    def do(self):
        
        '''
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
        '''
        '''
        print("aaaaaaaaa")
        try:
            peaks = Mountain.objects.all()
            for peak in peaks:
                for mountain in get_pekas_detailed_weather():
                    print("That is type of mountain and mountain is: " + mountain)
                    print(type(mountain))
                    
                #mountains = [OctaveOfDay(**element, name_of_peak=peaks_detail['name_of_peak']) for element in mountain]
                    for octave in mountain:
                        print(type(octave))
                        print("That is octave type and octave is: " +octave)
                        try:
                            a = OctaveOfDay(**octave,name_of_peak = peak)
                            print('That is a: ' + a)
                        except Exception as error:
                            print("Exception occured: " + str(error))
                        try:
                            if a.save() is False:
                                print("Faaaaaaaaaaaasle")
                        except Exception as error:
                            print("that is warning when i try save a : " +str(error))
                          
          
                #kolejna wersja
        
    all_peaks = Mountain.objects.all()
    for top in all_peaks:
        for data in get_pekas_detailed_weather():
            for i in data:
                for elem in i:
                    try: 
                        b = Mountain.objects.get(top.name_of_peak)
                        print("That is b: " + b)
                    except Exception as error:
                        print('that is ex: ' + str(error))
                    a =OctaveOfDay(elem, name_of_peak=top.name_of_peak)
                    print(a)
         ''' 
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
            except Exception as error:
                print("I tried assign a to Octave of a day but some error occured: " + str(error))
            a.save()
            print("I am after saving")

    '''
    forecasts = [OctaveOfDay(**element) for element in forecast_for_all_peaks]
    print(forecasts)
    print("after daily")
    try:
        OctaveOfDay.objects.bulk_create(forecasts)
    except Exception as error:
        print(error)           
    '''





