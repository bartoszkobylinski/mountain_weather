from django.urls import path, include
from rest_framework import routers

from zakopane_weather.views import (IndexView,
                                    ZakopaneAreaWeatherForecastView,
                                    DolinaChocholowskaAreaWeatherForecastView,
                                    DolinaKoscieliskaAreaWeatherForecastView,
                                    DolinaPieciuStawowAreaWeatherForecastView,
                                    KasprowyWierchAreaWeatherForecastView,
                                    MorskieOkoAreaWeatherForecastView,
                                    LomnicaAreaWeatherForecastView,
                                    BanikovForecastView,
                                    BaranecForecastView,
                                    GerlachForecastView,
                                    GiewontForecastView,
                                    GubalowkaForecastView,
                                    KasprowyWierchForecastView,
                                    KrivanForecastView,
                                    KoscielecForecastView,
                                    MieguszowieckiForecastView,
                                    MnichForecastView,
                                    OstryForecastView,
                                    RysyForecastView,
                                    SlavkovskyForecastView,
                                    SwinicaForecastView,
                                    VolovecForecastView,
                                    VychodnaForecastView,
                                    WoloszynForecastView,
                                    HourlyForecastViewset, 
                                    DailyForecastViewset,
                                    CurrentDayView,
                                    DziekiView,
                                    MapView
                                    )


router = routers.DefaultRouter()
router.register('hourlyforecast', HourlyForecastViewset)
router.register('dailyforecast', DailyForecastViewset)
#router.register('octaveofday', OctaveOfDayViewset)

urlpatterns = [
    path('', IndexView.as_view(template_name="index1.html"), name='index'),
    path('day-detail/', CurrentDayView.as_view(), name='detail-day'),
    path('zakopane/', ZakopaneAreaWeatherForecastView.as_view(), name='Zakopane'),
    path('dolina_chocholowska/', DolinaChocholowskaAreaWeatherForecastView.as_view(), name='Dolina Chocholowska'),
    path('dolina_koscieliska/', DolinaKoscieliskaAreaWeatherForecastView.as_view(), name='Dolina Koscieliska'),
    path('dolina_pieciu_stawow/', DolinaPieciuStawowAreaWeatherForecastView.as_view(), name='Dolina Pieciu Stawow Polskich'),
    path('kasprowy_wierch/', KasprowyWierchAreaWeatherForecastView.as_view(), name='Kasprowy Wierch'),
    path('morskie_oko/', MorskieOkoAreaWeatherForecastView.as_view(), name='Morskie Oko'),
    path('lomnica/', LomnicaAreaWeatherForecastView.as_view(), name='Lomnica'),
    path('banikov/', BanikovForecastView.as_view(), name='Banikov'),
    path('baranec/', BaranecForecastView.as_view(), name='Baranec'),
    path('gerlach/', GerlachForecastView.as_view(), name='Gerlach'),
    path('giewont/', GiewontForecastView.as_view(), name='Giewont'),
    path('gubalowka/', GubalowkaForecastView.as_view(), name='Gubalowka'),
    path('szczyt_kasprowy_wierch/', KasprowyWierchForecastView.as_view(), name='Kasprowy'),
    path('koscielec/', KoscielecForecastView.as_view(), name='Koscielec'),
    path('krivan/', KrivanForecastView.as_view(), name='Krivan'),
    path('mieguszowiecki/', MieguszowieckiForecastView.as_view(), name='Mieguszowiecki'),
    path('mnich/', MnichForecastView.as_view(), name='Mnich'),
    path('ostry/', OstryForecastView.as_view(), name='Ostry'),
    path('rysy/', RysyForecastView.as_view(), name='Rysy'),
    path('slavkovsky/', SlavkovskyForecastView.as_view(), name='Slavkovsky'),
    path('swinica/', SwinicaForecastView.as_view(), name='Swinica'),
    path('volovec/', VolovecForecastView.as_view(), name='Volovec'),
    path('vychodna/', VychodnaForecastView.as_view(), name='Vychodna'),
    path('woloszyn/', WoloszynForecastView.as_view(), name='Woloszyn'),  
    path('map/', MapView.as_view(), name='map'),
    path('dzieki/', DziekiView.as_view(), name='dzieki'),
    path('viewset/', include(router.urls)),
    path('viewset/hourlyforecast/<int:pk>/', include(router.urls)),
    
]

'''
  
'''
