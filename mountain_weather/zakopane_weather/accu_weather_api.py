"""
file where all classes and function for geting a weather details from
AccuWeatherAPI
"""
from urllib.parse import urljoin
import os
import logging
import requests

from zakopane_weather.location import location

logging.basicConfig(filename='mountain.log', level=logging.INFO)


class AccuWeatherAPI:
    """
    class represents AccuWeatherAPI connection
    """
    def __init__(self, location):
        self.api_key = os.environ.get("ACCU_API_KEY")
        self.location = location

    def _parsing_url(self, base_url):
        """
        method returns absolute url for given location
        """
        url2 = f"{self.location}?apikey={self.api_key}&details=true"
        absolute_url = urljoin(base_url, url2)
        return absolute_url

    def get_weather_forecast(self, base_url):
        """
        method returns forecast from AccuWeather API external service
        """
        url = self._parsing_url(base_url)
        api_response = requests.get(url)
        if not api_response.ok:
            logging.error(
                """Error occured while trying to get response from AccuWeather
                API""")
        weather_forcast = api_response.json()
        return weather_forcast


class FiveDaysWeatherForecast(AccuWeatherAPI):
    """
    Class represents five day weather forecest for Zakopane city
    in Tatras mountain
    """

    BASE_URL = "http://dataservice.accuweather.com/forecasts/v1/daily/5day/"

    def get_weather_details(self, days: int = None):
        """
        method returns a dictionary with date, minimal temperature,
        maximum temperature, short text weather description like sunny, cloudy,
        rain probability and wind speed
        """
        forecast = super().get_weather_forecast(self.BASE_URL)
        headers = [
            "date",
            "min_temp",
            "max_temp",
            "phrase",
            "probability",
            "wind_speed"]
        if days is None:
            days = 5
        for number in range(days):
            data = []
            date = forecast["DailyForecasts"][number]['Date']
            date = date[:10]
            data.append(date)
            min_temp = round((int(
                (forecast["DailyForecasts"][number]["Temperature"]
                 ["Minimum"]["Value"])) - 32) / 1.8)
            data.append(min_temp)
            max_temp = round((int(
                (forecast["DailyForecasts"][number]["Temperature"]
                 ["Maximum"]["Value"])) - 32) / 1.8)
            data.append(max_temp)
            phrase = forecast["DailyForecasts"][number]["Day"]["LongPhrase"]
            data.append(phrase)
            probability = (forecast["DailyForecasts"][number]["Day"]
                           ["RainProbability"])
            data.append(probability)
            wind_speed = round(int(
                (forecast["DailyForecasts"][number]["Day"]["Wind"]["Speed"]
                 ["Value"]) / 1.6), 1)
            data.append(wind_speed)
            yield dict(zip(headers, data))


class TwelveHoursWeatherForecast(AccuWeatherAPI):
    """
    Class represent twelve hour weather forecast for Zakopane
    city in Tatras Mountain
    """

    BASE_URL = "http://dataservice.accuweather.com/forecasts/v1/hourly/12hour/"

    def get_hourly_weather_details(self, hours: int = None):
        """
        method returns a weather forecast for next 11 hours in a dictionary
        variable with date, minimal temperature, maximum temperature, short
        text weather description like sunny, cloudy, rain probability and
        wind speed
        """
        if hours is None:
            hours = 11
        forecast = super().get_weather_forecast(self.BASE_URL)
        headers = ["date_time",
                   "temp",
                   "real_feel_temp",
                   "wind_speed",
                   "rain_probability",
                   "cloud_cover",
                   ]
        for number in range(hours):
            data = []
            date_time = forecast[number]['DateTime']
            date_time = date_time[:16]
            date_time = date_time.replace('T', ' ')
            data.append(date_time)
            temp = round((int(
                forecast[number]["Temperature"]["Value"]) - 32) / 1.8)
            data.append(temp)
            real_feel_temp = round((int(
                forecast[number]["RealFeelTemperature"]["Value"]) - 32) / 1.8)
            data.append(real_feel_temp)
            wind_speed = forecast[number]["Wind"]["Speed"]["Value"]
            data.append(wind_speed)
            rain_probability = forecast[number]["RainProbability"]
            data.append(rain_probability)
            cloud_cover = forecast[number]["CloudCover"]
            data.append(cloud_cover)
            yield dict(zip(headers, data))


def get_zakopane_daily_weather():
    """
    function returns list of a dictionaries with weather forcast for next
    5 days for Zakopane city based on information provided by AccuWeather
    API Service
    """
    zakopane = FiveDaysWeatherForecast(location.get("zakopane", ""))
    zakopane_weather_detail = zakopane.get_weather_details()
    zakopane_daily_weather_detail = []
    for data in zakopane_weather_detail:
        zakopane_daily_weather_detail.append(data)
    return zakopane_daily_weather_detail


def get_zakopane_hourly_weather():
    """
    function returns list of a dictionaries with weather forcast for next
    11 hours for Zakopane city based on information provided by AccuWeather
    API Service
    """
    zakopane = TwelveHoursWeatherForecast(location.get("zakopane", ""))
    zakopane_weather_detail = zakopane.get_hourly_weather_details()
    zakopane_hourly_weather_detail = []
    for data in zakopane_weather_detail:
        zakopane_hourly_weather_detail.append(data)
    return zakopane_hourly_weather_detail
