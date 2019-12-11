import django
import requests
import json
import os
from urllib.parse import urljoin

from zakopane_weather.location import location
from zakopane_weather.models import Day, DailyForecast

os.environ['DJANGO_SETTINGS_MODULE'] = 'project.settings'

django.setup()

from zakopane_weather.models import Day, DailyForecast


accu_api = os.environ.get('ACCU_API_KEY')

class FiveDaysWeatherForecast:
    days = None
    
    def __init__(self,location):
        self.location = location

    def _parsing_url(self,accu_api):
        url1 = f"http://dataservice.accuweather.com/forecasts/v1/daily/5day/"
        url2 = f"{self.location}?apikey={accu_api}&details=true"
        absolute_url = urljoin(url1, url2)
        return absolute_url

    def get_forecast(self):
        url = self._parsing_url(accu_api)

        api_response = requests.get(url)
        weather_forcast = api_response.json()
        return weather_forcast

    def weather_details(self, weather_forcast, days=5):
        forecast = self.get_forecast()
        headers = ['min_temp','max_temp','phrase','probability','wind_speed']
        for i in range(days):
            data = []
            min_temp = round((int(forecast['DailyForecasts'][i]['Temperature']['Minimum']['Value']) - 32)/1.8)
            data.append(min_temp)
            max_temp = round((int(forecast['DailyForecasts'][i]['Temperature']['Maximum']['Value']) - 32)/1.8)
            data.append(max_temp)
            phrase = forecast['DailyForecasts'][i]['Day']['LongPhrase']
            data.append(phrase)
            probability = forecast['DailyForecasts'][i]['Day']['RainProbability']
            data.append(probability)
            wind_speed = round((int(forecast['DailyForecasts'][i]['Day']['Wind']['Speed']['Value'])/1.6),1)
            data.append(wind_speed)
            yield dict(zip(headers,data))
    
    def save_five_day_weather_to_database(self):
        pass

class TwelveHoursWeatherForecast:
    hours = None

    days = None
    
    def __init__(self,location):
        self.location = location

    def _parsing_url(self,accu_api):
        url1 = f"http://dataservice.accuweather.com/forecasts/v1/hourly/12hour/"
        url2 = f"{self.location}?apikey={accu_api}&details=true"
        absolute_url = urljoin(url1, url2)
        return absolute_url

    def get_forecast(self):
        url = self._parsing_url(accu_api)

        api_response = requests.get(url)
        weather_forcast = api_response.json()
        return weather_forcast

    def weather_details(self, weather_forcast, hours=12):
        forecast = self.get_forecast()
        headers = ['min_temp','max_temp','phrase','probability','wind_speed']
        for i in range(hours):
            data = []
            min_temp = round((int(forecast['DailyForecasts'][i]['Temperature']['Minimum']['Value']) - 32)/1.8)
            data.append(min_temp)
            max_temp = round((int(forecast['DailyForecasts'][i]['Temperature']['Maximum']['Value']) - 32)/1.8)
            data.append(max_temp)
            phrase = forecast['DailyForecasts'][i]['Day']['LongPhrase']
            data.append(phrase)
            probability = forecast['DailyForecasts'][i]['Day']['RainProbability']
            data.append(probability)
            wind_speed = round((int(forecast['DailyForecasts'][i]['Day']['Wind']['Speed']['Value'])/1.6),1)
            data.append(wind_speed)
            yield dict(zip(headers,data))

    def get_twelve_hours_weather_forecast_from_accu(self):
        pass
    def get_twelve_hours_weather_forecast_from_yr(self):
        pass
    def save_twelve_hours_weather_to_database(self):
        pass

def get_daily_weather():
    zakopane = FiveDaysWeatherForecast(location.get('zakopane',''))
    weather = zakopane.get_forecast()
    detailed_weather = zakopane.weather_details(weather)
    weather_data = []
    for data in detailed_weather:
        weather_data.append(data)
    return weather_data
