from django.urls import path
from django.views.generic import TemplateView

from zakopane_weather.views import IndexView

urlpatterns = [
    path('index/', IndexView.as_view(template_name="index.html")),
]
