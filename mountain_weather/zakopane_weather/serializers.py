from rest_framework import serializers
from zakopane_weather.models import DailyForecast, HourlyForecast

class HourlyForecastSerializer(serializers.ModelSerializer):
    class Meta:
        model = HourlyForecast
        fields = ['id','temp','real_feel_temp','wind_speed','rain_probability','cloud_cover','date_time']

class DailyForecastSerializer(serializers.ModelSerializer):
    class Meta:
        model = DailyForecast
        fields = ['id','min_temp','max_temp','phrase','probability','wind_speed','date']

