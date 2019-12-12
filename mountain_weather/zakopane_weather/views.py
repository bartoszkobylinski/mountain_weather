from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from zakopane_weather.models import DailyForecast,Day, HourlyForecast

# Create your views here.

class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['DailyForecast'] = DailyForecast.objects.all()
        context['HourlyForecast'] = HourlyForecast.objects.all()
        return context
    
    
