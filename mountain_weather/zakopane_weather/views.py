from datetime import datetime

from django.views.generic import TemplateView
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from zakopane_weather.models import DailyForecast, AvalancheStatus, AreaWeatherForecast
from users_app.models import Post
from . import models
from . import serializers



# Create your views here.

class IndexView(TemplateView):
    template_name = 'index1.html'

    def get_context_data(self, **kwargs):
        today = datetime(2020,4,2,0,0)
        print(type(today))
        tommorow = datetime(2020,4,3,0,0)

        context = super(IndexView, self).get_context_data(**kwargs)
        # context['HourlyForecast'] = HourlyForecast.objects.all() ----> probably to remove to detail view of Zakopane
        context['FirstDay'] = DailyForecast.objects.order_by('date').first()
        # context['DailyForecast'] = DailyForecast.objects.order_by('date')[1:] ---> probably to remove to detail view of Zakopane
        
        # context['OctaveOfDay'] = OctaveOfDay.objects.all().order_by('date', 'name_of_peak') ---> probably to remove
        context['Post'] = Post.objects.all().order_by('-date')
        context['Avalanche'] = AvalancheStatus.objects.all()
        #context['Octave'] = OctaveOfDay.objects.filter(date=datetime(2020,4,30,23,00))
        context['Areas'] = AreaWeatherForecast.objects.filter(date=datetime(2020,4,26))
        '''
        try:
            context['First'] = OctaveOfDay.objects.filter(name_of_peak__name_of_peak='Volovec').order_by('date')
            context['Second'] = OctaveOfDay.objects.filter(name_of_peak__name_of_peak='Volovec').filter(date__range=(today,tommorow)).order_by('date')
            print(context['Second'])
            #print(context['First'])
        except Exception as err:
            print(f"That is error")

        context.update(
            HourlyForecast=HourlyForecast.objects.all(),
            FirstDay=DailyForecast.objects.order_by('date').first(),
            DailyForecast=DailyForecast.objects.order_by('date')[1:],
            OctaveOfDay=OctaveOfDay.objects.all().order_by('name_of_peak', 'date'),
            First=OctaveOfDay.objects.all(),
            Avalanche=AvalancheStatus.objects.all(),
            )
        '''
        return context

class DetailDayView(TemplateView):
    template_name = 'day-detail.html'
'''
class BanikovOctaveOfDayView(TemplateView):
    template_name = 'mountain_base.html'

    def get_context_data(self, **kwargs):
        context = super(BanikovOctaveOfDayView, self).get_context_data(**kwargs)
        context['Banikov'] = OctaveOfDay.objects.filter(name_of_peak__name_of_peak='Baníkov').order_by('date')
        return context
'''
class ZakopaneAreaWeatherForecastView(TemplateView):
    template_name = 'mountain_base.html'

    def get_context_data(self, **kwargs):
        context = super(ZakopaneAreaWeatherForecastView, self).get_context_data(**kwargs)
        context['Zakopane'] = AreaWeatherForecast.objects.filter(name='zakopane').order_by('date')
        return context

class DolinaChocholowskaAreaWeatherForecastView(TemplateView):
    template_name = 'mountain_base.html'

    def get_context_data(self, **kwargs):
        context = super(DolinaChocholowskaAreaWeatherForecastView, self).get_context_data(**kwargs)
        context['Dolina_Chocholowska'] = AreaWeatherForecast.objects.filter(name='dolina chocholowska').order_by('date')
        print(context['Dolina_Chocholowska'])
        return context

class DolinaKoscieliskaAreaWeatherForecastView(TemplateView):
    template_name = 'mountain_base.html'

    def get_context_data(self, **kwargs):
        context = super(DolinaKoscieliskaAreaWeatherForecastView, self).get_context_data(**kwargs)
        context['Dolina_Koscieliska'] = AreaWeatherForecast.objects.filter(name='dolina koscieliska').order_by('date')
        print(context['Dolina_Koscieliska'])
        return context

class DolinaPieciuStawowAreaWeatherForecastView(TemplateView):
    template_name = 'mountain_base.html'

    def get_context_data(self, **kwargs):
        context = super(DolinaPieciuStawowAreaWeatherForecastView, self).get_context_data(**kwargs)
        context['Dolina_Pieciu'] = AreaWeatherForecast.objects.filter(name='dolina pieciu stawow').order_by('date')
        print(context['Dolina_Pieciu'])
        return context
    
class KasprowyWierchAreaWeatherForecastView(TemplateView):
    template_name = 'mountain_base.html'

    def get_context_data(self, **kwargs):
        context = super(KasprowyWierchAreaWeatherForecastView, self).get_context_data(**kwargs)
        context['Kasprowy_Wierch'] = AreaWeatherForecast.objects.filter(name='kasprowy wierch').order_by('date')
        print(context['Kasprowy_Wierch'])
        return context

class MorskieOkoAreaWeatherForecastView(TemplateView):
    template_name = 'mountain_base.html'

    def get_context_data(self, **kwargs):
        context = super(MorskieOkoAreaWeatherForecastView, self).get_context_data(**kwargs)
        context['Morskie_Oko'] = AreaWeatherForecast.objects.filter(name='morskie oko').order_by('date')
        print(context['Morskie_Oko'])
        return context

class LomnicaAreaWeatherForecastView(TemplateView):
    template_name = 'mountain_base.html'

    def get_context_data(self, **kwargs):
        context = super(LomnicaAreaWeatherForecastView, self).get_context_data(**kwargs)
        context['Lomnica'] = AreaWeatherForecast.objects.filter(name='lomnica').order_by('date')
        print(context['Lomnica'])
        return context

class HourlyForecastViewset(viewsets.ModelViewSet):
    queryset = models.HourlyForecast.objects.all()
    serializer_class = serializers.HourlyForecastSerializer
    permission_classes = [IsAuthenticated]

class DailyForecastViewset(viewsets.ModelViewSet):
    queryset = models.DailyForecast.objects.all()
    serializer_class = serializers.DailyForecastSerializer
    permission_classes = [IsAuthenticated]
