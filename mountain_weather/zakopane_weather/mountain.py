
from urllib.parse import urljoin
import os
import logging
import requests

from zakopane_weather.location import location

accu_api = os.environ.get("ACCU_API_KEY")

logging.basicConfig(filename='mountain.log', level=logging.INFO)


class FiveDaysWeatherForecast:
    """
    Class represents five day weather forecest for Zakopane city
    in Tatras mountain
    """

    def __init__(self, location):
        self.location = location

    def _parsing_url(self, accu_api):
        """
        method returning absolute url for Zakopane city
        """
        url1 = "http://dataservice.accuweather.com/forecasts/v1/daily/5day/"
        url2 = f"{self.location}?apikey={accu_api}&details=true"
        absolute_url = urljoin(url1, url2)
        return absolute_url

    def get_forecast(self):
        """
        method returns forecast from AccuWeather API external service
        """
        url = self._parsing_url(accu_api)
        api_response = requests.get(url)
        if not api_response.ok:
            logging.error(
                """Error occured while trying to get response from AccuWeather
                API""")
        weather_forcast = api_response.json()
        return weather_forcast

    def weather_details(self, days: int = None):
        """
        method returns a dictionary with date, minimal temperature,
        maximum temperature, short text weather description like sunny, cloudy,
        rain probability and wind speed
        """
        forecast = self.get_forecast()
        headers = [
            "date",
            "min_temp",
            "max_temp",
            "phrase",
            "probability",
            "wind_speed"]
        if days is None:
            days = 5
        for i in range(days):
            data = []
            date = forecast["DailyForecasts"][i]['Date']
            date = date[:10]
            data.append(date)
            min_temp = round((int(
                (forecast["DailyForecasts"][i]["Temperature"]
                 ["Minimum"]["Value"])) - 32) / 1.8)
            data.append(min_temp)
            max_temp = round((int(
                (forecast["DailyForecasts"][i]["Temperature"]
                 ["Maximum"]["Value"])) - 32) / 1.8)
            data.append(max_temp)
            phrase = forecast["DailyForecasts"][i]["Day"]["LongPhrase"]
            data.append(phrase)
            probability = (forecast["DailyForecasts"][i]["Day"]
                           ["RainProbability"])
            data.append(probability)
            wind_speed = round((int(
                (forecast["DailyForecasts"][i]["Day"]["Wind"]["Speed"]
                 ["Value"]) / 1.6), 1))
            data.append(wind_speed)
            yield dict(zip(headers, data))


class TwelveHoursWeatherForecast:
    """
    Class represent twelve hour weather forecast for Zakopane
    city in Tatras Mountain
    """

    def __init__(self, location):
        self.location = location

    def _parsing_url(self, accu_api):
        """
        method returning absolute url for Zakopane city
        """
        url1 = "http://dataservice.accuweather.com/forecasts/v1/hourly/12hour/"
        url2 = f"{self.location}?apikey={accu_api}&details=true"
        absolute_url = urljoin(url1, url2)
        return absolute_url

    def get_forecast(self):
        """
        method returns forecast from AccuWeather API external service
        """
        url = self._parsing_url(accu_api)
        api_response = requests.get(url)
        if not api_response.ok:
            logging.error("""Error occured while trying to get response from
                          AccuWeather API""")
        weather_forcast = api_response.json()
        return weather_forcast

    def hourly_weather_details(self, hours: int = None):
        if hours is None:
            hours = 11
        forecast = self.get_forecast()
        headers = ["date_time",
                   "temp",
                   "real_feel_temp",
                   "wind_speed",
                   "rain_probability",
                   "cloud_cover",
                   ]
        for i in range(hours):
            data = []
            date_time = forecast[i]['DateTime']
            date_time = date_time[:16]
            date_time = date_time.replace('T', ' ')
            data.append(date_time)
            temp = round((int(forecast[i]["Temperature"]["Value"]) - 32) / 1.8)
            data.append(temp)
            real_feel_temp = round(
                (int(forecast[i]["RealFeelTemperature"]["Value"]) - 32) / 1.8
            )
            data.append(real_feel_temp)
            wind_speed = forecast[i]["Wind"]["Speed"]["Value"]
            data.append(wind_speed)
            rain_probability = forecast[i]["RainProbability"]
            data.append(rain_probability)
            cloud_cover = forecast[i]["CloudCover"]
            data.append(cloud_cover)
            yield dict(zip(headers, data))


def get_zakopane_daily_weather():
    zakopane = FiveDaysWeatherForecast(location.get("zakopane", ""))
    weather = zakopane.get_forecast()
    detailed_weather = zakopane.weather_details(weather)
    weather_data = []
    for data in detailed_weather:
        weather_data.append(data)
    return weather_data


def get_zakopane_hourly_weather():
    zakopane = TwelveHoursWeatherForecast(location.get("zakopane", ""))
    weather = zakopane.get_forecast()
    detailed_weather = zakopane.hourly_weather_details(weather)
    weather_data = []
    for data in detailed_weather:
        weather_data.append(data)
    return weather_data
