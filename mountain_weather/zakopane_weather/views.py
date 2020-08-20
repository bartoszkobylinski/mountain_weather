import datetime

from datetime import date
from django.views.generic import TemplateView
from django.core.serializers import serialize
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from zakopane_weather.models import (DailyForecast,
                                     AvalancheStatus,
                                     AreaWeatherForecast,
                                     PeakForecast,
                                     HourlyForecast)
from users_app.models import Post
from . import models
from . import serializers


class IndexView(TemplateView):
    """
    class View for index.html
    """
    template_name = 'index1.html'

    def get_context_data(self, **kwargs):
        today = date.today().strftime("%Y-%m-%d").replace(" 0", "")
        morning = datetime.time(20, 0)
        now = datetime.datetime.combine(date.today(), morning)

        context = super(IndexView, self).get_context_data(**kwargs)
        context['FirstDay'] = DailyForecast.objects.order_by('date').first()
        context['Post'] = Post.objects.all().order_by('-date')
        context['Avalanche'] = AvalancheStatus.objects.all()
        context['Peaks'] = PeakForecast.objects.filter(date=now)
        context['Areas'] = AreaWeatherForecast.objects.filter(date=today)
        return context


class CurrentDayView(TemplateView):
    """
    class view for current-day-detail.html
    """
    template_name = 'current-day-detail.html'

    def get_context_data(self, **kwargs):
        context = super(CurrentDayView, self).get_context_data(**kwargs)
        context['HourlyForecast'] = HourlyForecast.objects.all()
        context['FirstDay'] = DailyForecast.objects.order_by('date').first()
        print(context['FirstDay'])
        context['DailyForecast'] = DailyForecast.objects.order_by('date')[1:]

        return context


class MapView(TemplateView):
    """
    class view for map.html
    """
    template_name = 'map.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Image'] = serialize(
            'json',
            Post.objects.all(),
            fields=['lat', 'lon', 'image'])
        return context


class AreaWeatherForecastView(TemplateView):
    """
    class for rendering view of detailed weather forecast for area
    from name field
    """
    template_name = 'area_base.html'
    area_name = None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Place'] = AreaWeatherForecast.objects.filter(
            name=self.area_name).first()
        context['Places'] = AreaWeatherForecast.objects.values_list(
            'name', flat=True).distinct()
        context['Area'] = AreaWeatherForecast.objects.filter(
            name=self.area_name).order_by('date')
        return context


class ZakopaneAreaWeatherForecastView(AreaWeatherForecastView):
    """
    class for rendering view of detailed weather forecast for
    Zakopane area
    """
    area_name = 'Zakopane'


class DolinaChocholowskaAreaWeatherForecastView(AreaWeatherForecastView):
    """
    class for rendering view of detailed weather forecast for Dolina
    Chocholowska area
    """
    area_name = 'Dolina Chocholowska'


class DolinaKoscieliskaAreaWeatherForecastView(AreaWeatherForecastView):
    """
    class for rendering view of detailed weather forecast for Dolina
    Koscieliska area
    """
    area_name = 'Dolina Koscieliska'


class DolinaPieciuStawowAreaWeatherForecastView(AreaWeatherForecastView):
    """
    class for rendering view of detailed weather forecast for Dolina
    Pieciu Stawow area
    """
    area_name = 'Dolina Pieciu Stawow'


class KasprowyWierchAreaWeatherForecastView(AreaWeatherForecastView):
    """
    class for rendering view of detailed weather forecast for Kasprowy
    Wierch area
    """
    area_name = 'Kasprowy Wierch'


class MorskieOkoAreaWeatherForecastView(AreaWeatherForecastView):
    """
    class for rendering view of detailed weather forecast for Morskie
    Oko area
    """
    area_name = 'Morskie Oko'


class LomnicaAreaWeatherForecastView(AreaWeatherForecastView):
    """
    class for rendering view of detailed weather forecast for
    Lomnica area
    """
    area_name = 'Lomnica'


class PeakForecastView(TemplateView):
    """
    class for rendering view of detailed weather forecast
    for given peak
    """
    template_name = 'mountain_base.html'
    peak_name = None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Peak'] = PeakForecast.objects.filter(
            name_of_peak=self.peak_name).order_by('date')
        return context


class BanikovForecastView(PeakForecastView):
    """
    class for rendering view of detailed weather forecast for
    Banikov peak
    """
    peak_name = 'Banikov'


class BaranecForecastView(PeakForecastView):
    """
    class for rendering view of detailed weather forecast for
    Baranec peak
    """
    peak_name = 'Baranec'


class GerlachForecastView(PeakForecastView):
    """
    class for rendering view of detailed weather forecast for
    Gerlach peak
    """
    peak_name = 'Gerlach'


class GiewontForecastView(PeakForecastView):
    """
    class for rendering view of detailed weather forecast for
    Giewont peak
    """
    peak_name = 'Giewont'


class GubalowkaForecastView(PeakForecastView):
    """
    class for rendering view of detailed weather forecast for
    Gubalowka peak
    """
    peak_name = 'Gubalowka'


class KasprowyWierchForecastView(PeakForecastView):
    """
    class for rendering view of detailed weather forecast for
    Kasprowy Wierch peak
    """
    peak_name = 'Kasprowy'


class KoscielecForecastView(PeakForecastView):
    """
    class for rendering view of detailed weather forecast for
        Koscielec peak
    """
    peak_name = 'Koscielec'


class KrivanForecastView(PeakForecastView):
    """
    class for rendering view of detailed weather forecast for Krivan peak
    """
    peak_name = 'Krivan'


class MieguszowieckiForecastView(PeakForecastView):
    """
    class for rendering view of detailed weather forecast for
    Mieguszowiecki peak
    """
    peak_name = 'Mieguszowiecki'


class MnichForecastView(PeakForecastView):
    """
    class for rendering view of detailed weather forecast for
    Mnich peak
    """
    peak_name = 'Mnich'


class OstryForecastView(PeakForecastView):
    """
    class for rendering view of detailed weather forecast for
    Ostry peak
    """
    peak_name = 'Ostry'


class RysyForecastView(PeakForecastView):
    """
    class for rendering view of detailed weather forecast for
    Rysy peak
    """
    peak_name = 'Rysy'


class SlavkovskyForecastView(PeakForecastView):
    """
    class for rendering view of detailed weather forecast for
    Slavkovsky peak
    """
    peak_name = 'Slavkovsky Stit'


class SwinicaForecastView(PeakForecastView):
    """
    class for rendering view of detailed weather forecast for
    Swinica peak
    """
    peak_name = 'Swinica'


class VolovecForecastView(PeakForecastView):
    """
    class for rendering view of detailed weather forecast for
    Volovec peak
    """
    peak_name = "Volovec"


class VychodnaForecastView(PeakForecastView):
    """
    class for rendering view of detailed weather forecast for
    Vychodnia peak
    """
    peak_name = 'Vychodna'


class WoloszynForecastView(PeakForecastView):
    """
    class for rendering view of detailed weather forecast for
    Woloszyn peak
    """
    peak_name = 'Woloszyn'


class HourlyForecastViewset(viewsets.ModelViewSet):
    queryset = models.HourlyForecast.objects.all()
    serializer_class = serializers.HourlyForecastSerializer
    permission_classes = [IsAuthenticated]


class DailyForecastViewset(viewsets.ModelViewSet):
    queryset = models.DailyForecast.objects.all()
    serializer_class = serializers.DailyForecastSerializer
    permission_classes = [IsAuthenticated]
