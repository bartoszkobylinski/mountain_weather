from rest_framework import serializers
from zakopane_weather.models import OctaveOfDay, DailyForecast, HourlyForecast, Mountain

class HourlyForecastSerializer(serializers.ModelSerializer):
    class Meta:
        model = HourlyForecast
        fields = ['id','temp','real_feel_temp','wind_speed','rain_probability','cloud_cover','date_time']

class DailyForecastSerializer(serializers.ModelSerializer):
    class Meta:
        model = DailyForecast
        fields = ['id','min_temp','max_temp','phrase','probability','wind_speed','date']

class MountainSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mountain
        fields = ['id','name_of_peak','elevation']

class OctaveOfDaySerializer(serializers.ModelSerializer):
    class Meta:
        model = OctaveOfDay
        fields = ['id','name_of_peak','date','octave_of_a_day','windspeed','summary','rain','snow','temperature','chill_temperature']


'''
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url','username','email','groups']

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url','name']
'''