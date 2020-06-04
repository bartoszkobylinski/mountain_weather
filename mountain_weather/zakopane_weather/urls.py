from django.urls import path, include
from rest_framework import routers

from zakopane_weather.views import (IndexView,
                                    DetailDayView,
                                    BanikovOctaveOfDayView,
                                    ZakopaneAreaWeatherForecastView,
                                    DolinaChocholowskaAreaWeatherForecastView,
                                    DolinaKoscieliskaAreaWeatherForecastView,
                                    DolinaPieciuStawowAreaWeatherForecastView,
                                    KasprowyWierchAreaWeatherForecastView,
                                    MorskieOkoAreaWeatherForecastView,
                                    LomnicaAreaWeatherForecastView,

                                    HourlyForecastViewset, 
                                    DailyForecastViewset, 
                                    OctaveOfDayViewset
                                    )


router = routers.DefaultRouter()
router.register('hourlyforecast', HourlyForecastViewset)
router.register('dailyforecast', DailyForecastViewset)
router.register('octaveofday', OctaveOfDayViewset)

urlpatterns = [
    path('', IndexView.as_view(template_name="index1.html"), name='index'),
    path('day-detail/', DetailDayView.as_view(template_name="day-detail.html"), name='detail-day'),
    path('Banikov/', BanikovOctaveOfDayView.as_view(), name='Baníkov'),
    path('viewset/', include(router.urls)),
    path('viewset/hourlyforecast/<int:pk>/', include(router.urls)),
    path('zakopane/', ZakopaneAreaWeatherForecastView.as_view(), name='Zakopane'),
    path('dolina_chocholowska/', DolinaChocholowskaAreaWeatherForecastView.as_view(), name='Dolina Chochołowska'),
    path('dolina_koscieliska/', DolinaKoscieliskaAreaWeatherForecastView.as_view(), name='Dolina Kościeliska'),
    path('dolina_pieciu_stawow/', DolinaPieciuStawowAreaWeatherForecastView.as_view(), name='Dolina Pięciu Stawów Polskich'),
    path('kasprowy_wierch/', KasprowyWierchAreaWeatherForecastView.as_view(), name='Kasprowy Wierch'),
    path('morskie_oko/', MorskieOkoAreaWeatherForecastView.as_view(), name='Morskie Oko'),
    path('lomnica/', LomnicaAreaWeatherForecastView.as_view(), name='Łomnica'),
]