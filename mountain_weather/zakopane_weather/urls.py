from django.urls import path, include
from django.views.generic import TemplateView
from rest_framework import routers

from zakopane_weather.views import IndexView,HourlyForecastViewset, DailyForecastViewset, MountainViewset, OctaveOfDayViewset

'''
urlpatterns = [
    path('index/', IndexView.as_view(template_name="index.html")),
]
'''
router = routers.DefaultRouter()
router.register('hourlyforecast', HourlyForecastViewset)
router.register('dailyforecast', DailyForecastViewset)
router.register('mountain', MountainViewset)
router.register('octaveofday', OctaveOfDayViewset)

urlpatterns =[
    path('index/', IndexView.as_view(template_name="index1.html")),
    path('viewset/', include(router.urls)),
    path('viewset/hourlyforecast/<int:pk>/', include(router.urls))
]