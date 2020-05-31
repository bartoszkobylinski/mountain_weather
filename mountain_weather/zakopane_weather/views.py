from django.views.generic import TemplateView
from django.db.models.functions import TruncDay
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from zakopane_weather.models import HourlyForecast, DailyForecast, Mountain, OctaveOfDay, AvalancheStatus
from users_app.models import Post
from . import models
from . import serializers

from datetime import datetime, date

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
        context['Post'] = Post.objects.all().order_by('date')
        context['Mountain'] = Mountain.objects.all().order_by('name_of_peak')
        context['Avalanche'] = AvalancheStatus.objects.all()

        try:
            context['First'] = OctaveOfDay.objects.filter(name_of_peak__name_of_peak='Volovec').order_by('date')
            context['Second'] = OctaveOfDay.objects.filter(name_of_peak__name_of_peak='Volovec').filter(date__range=(today,tommorow)).order_by('date')
            print(context['Second'])
            #print(context['First'])
        except Exception as err:
            print(f"That is error {err}")
    
        '''
        context.update(
            HourlyForecast=HourlyForecast.objects.all(),
            FirstDay=DailyForecast.objects.order_by('date').first(),
            DailyForecast=DailyForecast.objects.order_by('date')[1:],
            OctaveOfDay=OctaveOfDay.objects.all().order_by('name_of_peak', 'date'),
            First=OctaveOfDay.objects.all()
            Mountain=Mountain.objects.all(),
            Avalanche=AvalancheStatus.objects.all()
            )
        '''
        return context

class HourlyForecastViewset(viewsets.ModelViewSet):
    queryset = models.HourlyForecast.objects.all()
    serializer_class = serializers.HourlyForecastSerializer
    permission_classes = [IsAuthenticated]

class DailyForecastViewset(viewsets.ModelViewSet):
    queryset = models.DailyForecast.objects.all()
    serializer_class = serializers.DailyForecastSerializer
    permission_classes = [IsAuthenticated]

class MountainViewset(viewsets.ModelViewSet):
    queryset = models.Mountain.objects.all()
    serializer_class = serializers.MountainSerializer
    permission_classes = [IsAuthenticated]

class OctaveOfDayViewset(viewsets.ModelViewSet):
    queryset = models.OctaveOfDay.objects.all()
    serializer_class = serializers.OctaveOfDaySerializer
    permission_classes = [IsAuthenticated]
