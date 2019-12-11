from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from zakopane_weather.models import DailyForecast,Day

# Create your views here.

class IndexView(ListView):

    model = DailyForecast
'''
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #context = {"1":2, "3":4}
        print("ouoeuoeuoeaoau")
        print(context)
        return context
        '''
