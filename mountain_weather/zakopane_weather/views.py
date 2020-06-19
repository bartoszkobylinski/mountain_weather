import datetime

from datetime import date
from django.views.generic import TemplateView, ListView
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from zakopane_weather.models import DailyForecast, AvalancheStatus, AreaWeatherForecast, PeakForecast, HourlyForecast
from users_app.models import Post
from . import models
from . import serializers



# Create your views here.

class IndexView(TemplateView):
    template_name = 'index1.html'

    def get_context_data(self, **kwargs):
        today = date.today().strftime("%Y-%m-%d").replace(" 0", "")
        morning = datetime.time(5,0)
        now = datetime.datetime.combine(date.today(),morning)

        context = super(IndexView, self).get_context_data(**kwargs)
        context['FirstDay'] = DailyForecast.objects.order_by('date').first()
        context['Post'] = Post.objects.all().order_by('-date')
        context['Avalanche'] = AvalancheStatus.objects.all()
        context['Peaks'] = PeakForecast.objects.filter(date=now)
        context['Areas'] = AreaWeatherForecast.objects.filter(date=today)
        
        return context

class CurrentDayView(TemplateView):
    template_name = 'current-day-detail.html'

    def get_context_data(self, **kwargs):
        context = super(CurrentDayView, self).get_context_data(**kwargs)
        context['HourlyForecast'] = HourlyForecast.objects.all()
        context['FirstDay'] = DailyForecast.objects.order_by('date').first()
        print(context['FirstDay'])
        context['DailyForecast'] = DailyForecast.objects.order_by('date')[1:]

        return context

class MapView(ListView):
    template_name = 'map.html'
    queryset = Post.objects.all()


class ZakopaneAreaWeatherForecastView(TemplateView):
    template_name = 'area_base.html'

    def get_context_data(self, **kwargs):
        context = super(ZakopaneAreaWeatherForecastView, self).get_context_data(**kwargs)
        context['Place'] = AreaWeatherForecast.objects.filter(name='Zakopane').first()
        context['Places'] = AreaWeatherForecast.objects.values_list('name', flat=True).distinct()
        context['Area'] = AreaWeatherForecast.objects.filter(name='Zakopane').order_by('date')
        return context

class DolinaChocholowskaAreaWeatherForecastView(TemplateView):
    template_name = 'area_base.html'

    def get_context_data(self, **kwargs):
        context = super(DolinaChocholowskaAreaWeatherForecastView, self).get_context_data(**kwargs)
        context['Place'] = AreaWeatherForecast.objects.filter(name='Dolina Chocholowska').first()
        context['Places'] = AreaWeatherForecast.objects.values_list('name', flat=True).distinct()
        context['Area'] = AreaWeatherForecast.objects.filter(name='Dolina Chocholowska').order_by('date')
        return context

class DolinaKoscieliskaAreaWeatherForecastView(TemplateView):
    template_name = 'area_base.html'

    def get_context_data(self, **kwargs):
        context = super(DolinaKoscieliskaAreaWeatherForecastView, self).get_context_data(**kwargs)
        context['Place'] = AreaWeatherForecast.objects.filter(name='Dolina Koscieliska').first()
        context['Places'] = AreaWeatherForecast.objects.values_list('name', flat=True).distinct()
        context['Area'] = AreaWeatherForecast.objects.filter(name='Dolina Koscieliska').order_by('date')
        return context

class DolinaPieciuStawowAreaWeatherForecastView(TemplateView):
    template_name = 'area_base.html'

    def get_context_data(self, **kwargs):
        context = super(DolinaPieciuStawowAreaWeatherForecastView, self).get_context_data(**kwargs)
        context['Place'] = AreaWeatherForecast.objects.filter(name='Dolina Pieciu Stawow Polskich').first()
        context['Places'] = AreaWeatherForecast.objects.values_list('name', flat=True).distinct()
        context['Area'] = AreaWeatherForecast.objects.filter(name='Dolina Pieciu Stawow Polskich').order_by('date')
        return context
    
class KasprowyWierchAreaWeatherForecastView(TemplateView):
    template_name = 'area_base.html'

    def get_context_data(self, **kwargs):
        context = super(KasprowyWierchAreaWeatherForecastView, self).get_context_data(**kwargs)
        context['Place'] = AreaWeatherForecast.objects.filter(name='Kasprowy Wierch').first()
        context['Places'] = AreaWeatherForecast.objects.values_list('name', flat=True).distinct()
        context['Area'] = AreaWeatherForecast.objects.filter(name='Kasprowy Wierch').order_by('date')
        return context

class MorskieOkoAreaWeatherForecastView(TemplateView):
    template_name = 'area_base.html'

    def get_context_data(self, **kwargs):
        context = super(MorskieOkoAreaWeatherForecastView, self).get_context_data(**kwargs)
        context['Place'] = AreaWeatherForecast.objects.filter(name='Morskie Oko').first()
        context['Places'] = AreaWeatherForecast.objects.values_list('name', flat=True).distinct() 
        context['Area'] = AreaWeatherForecast.objects.filter(name='Morskie Oko').order_by('date')
        return context

class LomnicaAreaWeatherForecastView(TemplateView):
    template_name = 'area_base.html'

    def get_context_data(self, **kwargs):
        context = super(LomnicaAreaWeatherForecastView, self).get_context_data(**kwargs)
        context['Place'] = AreaWeatherForecast.objects.filter(name='Lomnica').first()
        context['Places'] = AreaWeatherForecast.objects.values_list('name', flat=True).distinct()
        context['Area'] = AreaWeatherForecast.objects.filter(name='Lomnica').order_by('date')
        return context

class BanikovForecastView(TemplateView):
    template_name = 'mountain_base.html'

    def get_context_data(self, **kwargs):
        context = super(BanikovForecastView, self).get_context_data(**kwargs)
        context['Peak'] = PeakForecast.objects.filter(name_of_peak='Banikov').order_by('date')
        return context

class BaranecForecastView(TemplateView):
    template_name = 'mountain_base.html'

    def get_context_data(self, **kwargs):
        context = super(BaranecForecastView, self).get_context_data(**kwargs)
        context['Peak'] = PeakForecast.objects.filter(name_of_peak='Baranec').order_by('date')
        return context

class GerlachForecastView(TemplateView):
    template_name = 'mountain_base.html'

    def get_context_data(self, **kwargs):
        context = super(GerlachForecastView, self).get_context_data(**kwargs)
        context['Peak'] = PeakForecast.objects.filter(name_of_peak='Gerlach').order_by('date')
        return context

class GiewontForecastView(TemplateView):
    template_name = 'mountain_base.html'

    def get_context_data(self, **kwargs):
        context = super(GiewontForecastView, self).get_context_data(**kwargs)
        context['Peak'] = PeakForecast.objects.filter(name_of_peak='Giewont').order_by('date')
        return context

class GubalowkaForecastView(TemplateView):
    template_name = 'mountain_base.html'

    def get_context_data(self, **kwargs):
        context = super(GubalowkaForecastView, self).get_context_data(**kwargs)
        context['Peak'] = PeakForecast.objects.filter(name_of_peak='Gubalowka').order_by('date')
        return context

class KasprowyWierchForecastView(TemplateView):
    template_name = 'mountain_base.html'

    def get_context_data(self, **kwargs):
        context = super(KasprowyWierchForecastView, self).get_context_data(**kwargs)
        context['Peak'] = PeakForecast.objects.filter(name_of_peak='Kasprowy').order_by('date')
        print(context['Peak'])
        return context

class KoscielecForecastView(TemplateView):
    template_name = 'mountain_base.html'

    def get_context_data(self, **kwargs):
        context = super(KoscielecForecastView, self).get_context_data(**kwargs)
        context['Peak'] = PeakForecast.objects.filter(name_of_peak='Koscielec').order_by('date')
        return context

class KrivanForecastView(TemplateView):
    template_name = 'mountain_base.html'

    def get_context_data(self, **kwargs):
        context = super(KrivanForecastView, self).get_context_data(**kwargs)
        context['Peak'] = PeakForecast.objects.filter(name_of_peak='Krivan').order_by('date')
        return context

class MieguszowieckiForecastView(TemplateView):
    template_name = 'mountain_base.html'

    def get_context_data(self, **kwargs):
        context = super(MieguszowieckiForecastView, self).get_context_data(**kwargs)
        context['Peak'] = PeakForecast.objects.filter(name_of_peak='Mieguszowiecki').order_by('date')
        return context

class MnichForecastView(TemplateView):
    template_name = 'mountain_base.html'

    def get_context_data(self, **kwargs):
        context = super(MnichForecastView, self).get_context_data(**kwargs)
        context['Peak'] = PeakForecast.objects.filter(name_of_peak='Mnich').order_by('date')
        return context

class OstryForecastView(TemplateView):
    template_name = 'mountain_base.html'

    def get_context_data(self, **kwargs):
        context = super(OstryForecastView, self).get_context_data(**kwargs)
        context['Peak'] = PeakForecast.objects.filter(name_of_peak='Ostry').order_by('date')
        return context

class RysyForecastView(TemplateView):
    template_name = 'mountain_base.html'

    def get_context_data(self, **kwargs):
        context = super(RysyForecastView, self).get_context_data(**kwargs)
        context['Peak'] = PeakForecast.objects.filter(name_of_peak='Rysy').order_by('date')
        return context

class SlavkovskyForecastView(TemplateView):
    template_name = 'mountain_base.html'

    def get_context_data(self, **kwargs):
        context = super(SlavkovskyForecastView, self).get_context_data(**kwargs)
        context['Peak'] = PeakForecast.objects.filter(name_of_peak='Slavkovsky Stit').order_by('date')
        return context
    
class SwinicaForecastView(TemplateView):
    template_name = 'mountain_base.html'

    def get_context_data(self, **kwargs):
        context = super(SwinicaForecastView, self).get_context_data(**kwargs)
        context['Peak'] = PeakForecast.objects.filter(name_of_peak='Swinica').order_by('date')
        return context

class VolovecForecastView(TemplateView):
    template_name = 'mountain_base.html'

    def get_context_data(self, **kwargs):
        context = super(VolovecForecastView, self).get_context_data(**kwargs)
        context['Peak'] = PeakForecast.objects.filter(name_of_peak='Volovec').order_by('date')
        return context

class VychodnaForecastView(TemplateView):
    template_name = 'mountain_base.html'

    def get_context_data(self, **kwargs):
        context = super(VychodnaForecastView, self).get_context_data(**kwargs)
        context['Peak'] = PeakForecast.objects.filter(name_of_peak='Vychodna').order_by('date')
        return context

class WoloszynForecastView(TemplateView):
    template_name = 'mountain_base.html'

    def get_context_data(self, **kwargs):
        context = super(WoloszynForecastView, self).get_context_data(**kwargs)
        context['Peak'] = PeakForecast.objects.filter(name_of_peak='Woloszyn').order_by('date')
        return context


class HourlyForecastViewset(viewsets.ModelViewSet):
    queryset = models.HourlyForecast.objects.all()
    serializer_class = serializers.HourlyForecastSerializer
    permission_classes = [IsAuthenticated]

class DailyForecastViewset(viewsets.ModelViewSet):
    queryset = models.DailyForecast.objects.all()
    serializer_class = serializers.DailyForecastSerializer
    permission_classes = [IsAuthenticated]
