from rest_framework import routers
from zakopane_weather import api_views as zakopane_views

router = routers.DefaultRouter()
router.register(r'hourlyforecast', zakopane_views.HourlyForecastViewset)
router.register(r'dailyforecast', zakopane_views.DailyForecastViewset)
router.register(r'mountain', zakopane_views.MountainViewset)
router.register(r'octaveofday', zakopane_views.OctaveOfDayViewset)