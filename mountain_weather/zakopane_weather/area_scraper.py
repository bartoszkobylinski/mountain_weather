from unidecode import unidecode
from zakopane_weather.scraper import Scraper


class AreaScraper(Scraper):
    """
     Class for scraper gathering weather forecast for specific area in
     Tatras Mountain
    """

    def __init__(self, url):
        super().__init__()
        self.url = url

    def get_areas_weather_forecasts(self):
        """
        Creating dictionary with particular paramethers of weather forecast
        for specific area
        """
        self.browser.get(self.url)
        area_weather_tables = self.browser.find_elements_by_class_name(
            'meteotable')
        areas_weather_forecasts = []
        for table in area_weather_tables:
            meteostation = table.find_element_by_class_name('meteostation')
            meteostation = unidecode(meteostation.text)
            meteoday = table.find_elements_by_class_name('meteocell')
            for day in meteoday:
                current_weather_forecast = {}
                date = day.find_element_by_tag_name('h3')
                temp_min = day.find_element_by_class_name('min')
                temp_max = day.find_element_by_class_name('max')
                pressure = day.find_element_by_class_name('size')
                summary = day.find_element_by_class_name('desc')
                icon_number = self.set_icon_number(summary.text)
                rain = day.find_element_by_class_name('precipitation')
                current_weather_forecast.update(
                    name=meteostation,
                    date=date.text,
                    temp_min=temp_min.text[:-2],
                    temp_max=temp_max.text[:-2],
                    pressure=pressure.text[:-3],
                    summary=summary.text,
                    icon_number=icon_number,
                    rain=rain.text[7:-6]
                )
                areas_weather_forecasts.append(current_weather_forecast)

        return areas_weather_forecasts

    def set_icon_number(self, summary):
        '''
        Depends on what weatherforecast is in summary field icon number can
        describe: sunny, stormy, cloudy and so on
        '''
        if "burz" in summary:
            icon_number = 1
        elif "rozwój" or "rozpogodzenia" in summary:
            icon_number = 2
        elif "zachmurzenie" in summary:
            icon_number = 3
        else:
            icon_number = 4

        return icon_number


def get_tatras_areas_weather_forecast():
    """
    Function recives all areas weatherforecast
    """
    scraper = AreaScraper('https://tpn.pl/zwiedzaj/pogoda')
    areas_weather_forecasts = scraper.get_areas_weather_forecasts()
    return areas_weather_forecasts
