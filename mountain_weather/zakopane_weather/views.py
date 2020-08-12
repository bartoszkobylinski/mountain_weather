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


class ZakopaneAreaWeatherForecastView(TemplateView):
    """
    class for rendering view of detailed weather forecast for Zakopane area
    """
    template_name = 'area_base.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Place'] = AreaWeatherForecast.objects.filter(
            name='Zakopane').first()
        context['Places'] = AreaWeatherForecast.objects.values_list(
            'name', flat=True).distinct()
        context['Area'] = AreaWeatherForecast.objects.filter(
            name='Zakopane').order_by('date')
        return context


class DolinaChocholowskaAreaWeatherForecastView(TemplateView):
    """
    class for rendering view of detailed weather forecast for Dolina
    Chocholowska area
    """
    template_name = 'area_base.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Place'] = AreaWeatherForecast.objects.filter(
            name='Dolina Chocholowska').first()
        context['Places'] = AreaWeatherForecast.objects.values_list(
            'name', flat=True).distinct()
        context['Area'] = AreaWeatherForecast.objects.filter(
            name='Dolina Chocholowska').order_by('date')
        return context


class DolinaKoscieliskaAreaWeatherForecastView(TemplateView):
    """
    class for rendering view of detailed weather forecast for Dolina
    Koscieliska area
    """
    template_name = 'area_base.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Place'] = AreaWeatherForecast.objects.filter(
            name='Dolina Koscieliska').first()
        context['Places'] = AreaWeatherForecast.objects.values_list(
            'name', flat=True).distinct()
        context['Area'] = AreaWeatherForecast.objects.filter(
            name='Dolina Koscieliska').order_by('date')
        return context


class DolinaPieciuStawowAreaWeatherForecastView(TemplateView):
    """
    class for rendering view of detailed weather forecast for Dolina
    Pieciu Stawow area
    """
    template_name = 'area_base.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Place'] = AreaWeatherForecast.objects.filter(
            name='Dolina Pieciu Stawow Polskich').first()
        context['Places'] = AreaWeatherForecast.objects.values_list(
            'name', flat=True).distinct()
        context['Area'] = AreaWeatherForecast.objects.filter(
            name='Dolina Pieciu Stawow Polskich').order_by('date')
        return context


class KasprowyWierchAreaWeatherForecastView(TemplateView):
    """
    class for rendering view of detailed weather forecast for Kasprowy
    Wierch area
    """
    template_name = 'area_base.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Place'] = AreaWeatherForecast.objects.filter(
            name='Kasprowy Wierch').first()
        context['Places'] = AreaWeatherForecast.objects.values_list(
            'name', flat=True).distinct()
        context['Area'] = AreaWeatherForecast.objects.filter(
            name='Kasprowy Wierch').order_by('date')
        return context


class MorskieOkoAreaWeatherForecastView(TemplateView):
    """
    class for rendering view of detailed weather forecast for Morskie
    Oko area
    """
    template_name = 'area_base.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Place'] = AreaWeatherForecast.objects.filter(
            name='Morskie Oko').first()
        context['Places'] = AreaWeatherForecast.objects.values_list(
            'name', flat=True).distinct()
        context['Area'] = AreaWeatherForecast.objects.filter(
            name='Morskie Oko').order_by('date')
        return context


class LomnicaAreaWeatherForecastView(TemplateView):
    """
    class for rendering view of detailed weather forecast for
    Lomnica area
    """
    template_name = 'area_base.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Place'] = AreaWeatherForecast.objects.filter(
            name='Lomnica').first()
        context['Places'] = AreaWeatherForecast.objects.values_list(
            'name', flat=True).distinct()
        context['Area'] = AreaWeatherForecast.objects.filter(
            name='Lomnica').order_by('date')
        return context


class BanikovForecastView(TemplateView):
    """
    class for rendering view of detailed weather forecast for
    Banikov peak
    """
    template_name = 'mountain_base.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Peak'] = PeakForecast.objects.filter(
            name_of_peak='Banikov').order_by('date')
        return context


class BaranecForecastView(TemplateView):
    """
    class for rendering view of detailed weather forecast for
    Baranec peak
    """
    template_name = 'mountain_base.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Peak'] = PeakForecast.objects.filter(
            name_of_peak='Baranec').order_by('date')
        return context


class GerlachForecastView(TemplateView):
    """
    class for rendering view of detailed weather forecast for
    Gerlach peak
    """
    template_name = 'mountain_base.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Peak'] = PeakForecast.objects.filter(
            name_of_peak='Gerlach').order_by('date')
        return context


class GiewontForecastView(TemplateView):
    """
    class for rendering view of detailed weather forecast for
    Giewont peak
    """
    template_name = 'mountain_base.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Peak'] = PeakForecast.objects.filter(
            name_of_peak='Giewont').order_by('date')
        return context


class GubalowkaForecastView(TemplateView):
    """
    class for rendering view of detailed weather forecast for
    Gubalowka peak
    """
    template_name = 'mountain_base.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Peak'] = PeakForecast.objects.filter(
            name_of_peak='Gubalowka').order_by('date')
        return context


class KasprowyWierchForecastView(TemplateView):
    """
    class for rendering view of detailed weather forecast for
    Kasprowy Wierch peak
    """
    template_name = 'mountain_base.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Peak'] = PeakForecast.objects.filter(
            name_of_peak='Kasprowy').order_by('date')
        print(context['Peak'])
        return context


class KoscielecForecastView(TemplateView):
    """
    class for rendering view of detailed weather forecast for
        Koscielec peak
    """
    template_name = 'mountain_base.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Peak'] = PeakForecast.objects.filter(
            name_of_peak='Koscielec').order_by('date')
        return context


class KrivanForecastView(TemplateView):
    """
    class for rendering view of detailed weather forecast for Krivan peak
    """
    template_name = 'mountain_base.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Peak'] = PeakForecast.objects.filter(
            name_of_peak='Krivan').order_by('date')
        return context


class MieguszowieckiForecastView(TemplateView):
    """
    class for rendering view of detailed weather forecast for
    Mieguszowiecki peak
    """
    template_name = 'mountain_base.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Peak'] = PeakForecast.objects.filter(
            name_of_peak='Mieguszowiecki').order_by('date')
        return context


class MnichForecastView(TemplateView):
    """
    class for rendering view of detailed weather forecast for
    Mnich peak
    """
    template_name = 'mountain_base.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Peak'] = PeakForecast.objects.filter(
            name_of_peak='Mnich').order_by('date')
        return context


class OstryForecastView(TemplateView):
    """
    class for rendering view of detailed weather forecast for
    Ostry peak
    """
    template_name = 'mountain_base.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Peak'] = PeakForecast.objects.filter(
            name_of_peak='Ostry').order_by('date')
        return context


class RysyForecastView(TemplateView):
    """
    class for rendering view of detailed weather forecast for
    Rysy peak
    """
    template_name = 'mountain_base.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Peak'] = PeakForecast.objects.filter(
            name_of_peak='Rysy').order_by('date')
        return context


class SlavkovskyForecastView(TemplateView):
    """
    class for rendering view of detailed weather forecast for
    Slavkovsky peak
    """
    template_name = 'mountain_base.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Peak'] = PeakForecast.objects.filter(
            name_of_peak='Slavkovsky Stit').order_by('date')
        return context


class SwinicaForecastView(TemplateView):
    """
    class for rendering view of detailed weather forecast for
    Swinica peak
    """
    template_name = 'mountain_base.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Peak'] = PeakForecast.objects.filter(
            name_of_peak='Swinica').order_by('date')
        return context


class VolovecForecastView(TemplateView):
    """
    class for rendering view of detailed weather forecast for
    Volovec peak
    """
    template_name = 'mountain_base.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Peak'] = PeakForecast.objects.filter(
            name_of_peak='Volovec').order_by('date')
        return context


class VychodnaForecastView(TemplateView):
    """
    class for rendering view of detailed weather forecast for
    Vychodnia peak
    """
    template_name = 'mountain_base.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Peak'] = PeakForecast.objects.filter(
            name_of_peak='Vychodna').order_by('date')
        return context


class WoloszynForecastView(TemplateView):
    """
    class for rendering view of detailed weather forecast for
    Woloszyn peak
    """
    template_name = 'mountain_base.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Peak'] = PeakForecast.objects.filter(
            name_of_peak='Woloszyn').order_by('date')
        return context


class HourlyForecastViewset(viewsets.ModelViewSet):
    queryset = models.HourlyForecast.objects.all()
    serializer_class = serializers.HourlyForecastSerializer
    permission_classes = [IsAuthenticated]


class DailyForecastViewset(viewsets.ModelViewSet):
    queryset = models.DailyForecast.objects.all()
    serializer_class = serializers.DailyForecastSerializer
    permission_classes = [IsAuthenticated]
