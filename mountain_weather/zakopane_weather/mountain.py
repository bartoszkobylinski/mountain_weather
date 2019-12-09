import requests
import requests_cache
import json
import os
from urllib.parse import urljoin

from location import location

requests_cache.install_cache('demo_cache')

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
            probability = int(forecast['DailyForecasts'][i]['Day']['RainProbability'])/100
            data.append(probability)
            wind_speed = round((int(forecast['DailyForecasts'][i]['Day']['Wind']['Speed']['Value'])/1.6),1)
            data.append(wind_speed)
            yield dict(zip(headers,data))
    
    def save_five_day_weather_to_database(self):
        pass

class TwelveHoursWeatherForecast:

    def __init__(self):
        self.key_zakopane = "2700353"
        self.api_request = requests.get("http://dataservice.accuweather.com/forecasts/v1/hourly/12hour/"+self.key_zakopane+"?apikey="+ accu_api +"&details=true")
        self.five_days_weather_forecast = self.api_request
        self.five_days_weather_forecast = json.loads(self.five_days_weather_forecast.text)
        self.hours = 11

    def get_twelve_hours_weather_forecast_from_accu(self):
        pass
    def get_twelve_hours_weather_forecast_from_yr(self):
        pass
    def save_twelve_hours_weather_to_database(self):
        pass

def get_data():
    zakopane = FiveDaysWeatherForecast(location.get('zakopane',''))
    weather = zakopane.get_forecast()
    detailed_weather = zakopane.weather_details(weather)
    weather_data = []
    for data in detailed_weather:
        weather_data.append(data)
    return weather_data