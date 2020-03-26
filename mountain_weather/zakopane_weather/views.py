from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from zakopane_weather.models import DailyForecast, HourlyForecast
from rest_framework import viewsets
from zakopane_weather.models import HourlyForecast, DailyForecast, Mountain, OctaveOfDay
from . import models
from . import serializers

# Create your views here.


class IndexView(TemplateView):
    template_name = 'index2.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['HourlyForecast'] = HourlyForecast.objects.all()
        context['FirstDay'] = DailyForecast.objects.order_by('date').first()
        context['DailyForecast'] = DailyForecast.objects.order_by('date')[1:]
        context['OctaveOfDay'] = OctaveOfDay.objects.all()
        context['Mountain'] = Mountain.objects.all()
        print(context['Mountain'])
        print(context['OctaveOfDay'])
        return context
    
class HourlyForecastViewset(viewsets.ModelViewSet):
    queryset = models.HourlyForecast.objects.all()
    serializer_class = serializers.HourlyForecastSerializer

class DailyForecastViewset(viewsets.ModelViewSet):
    queryset = models.DailyForecast.objects.all()
    serializer_class = serializers.DailyForecastSerializer

class MountainViewset(viewsets.ModelViewSet):
    queryset = models.Mountain.objects.all()
    serializer_class = serializers.MountainSerializer

class OctaveOfDayViewset(viewsets.ModelViewSet):
    queryset = models.OctaveOfDay.objects.all()
    serializer_class = serializers.OctaveOfDaySerializer

