from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from zakopane_weather.models import DailyForecast,Day

# Create your views here.

class IndexView(ListView):

    model = DailyForecast
