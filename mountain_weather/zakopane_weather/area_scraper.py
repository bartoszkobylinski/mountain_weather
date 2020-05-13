from zakopane_weather.scraper import Scraper


class AreaScraper(Scraper):

    def __init__(self, url):
        super().__init__()
        self.url = url

    def get_areas_weather_forecasts(self):
        self.browser.get(self.url)
        area_weather_tables = self.browser.find_elements_by_class_name('meteotable')
        areas_weather_forecasts = []
        for table in area_weather_tables:
            meteostation = table.find_element_by_class_name('meteostation')
            meteoday = table.find_elements_by_class_name('meteocell')
            for day in meteoday:
                current_weather_forecast = {}
                date = day.find_element_by_tag_name('h3')
                temp_min = day.find_element_by_class_name('min')
                temp_max = day.find_element_by_class_name('max')
                pressure = day.find_element_by_class_name('size')
                rain = day.find_element_by_class_name('precipitation')
                current_weather_forecast.update(
                    name=meteostation.text,
                    date=date.text,
                    temp_min=temp_min.text[:-2],
                    temp_max=temp_max.text[:-2],
                    pressure=pressure.text[:-3],
                    rain=rain.text[7:-6]
                )
                areas_weather_forecasts.append(current_weather_forecast)
                
        
        return areas_weather_forecasts

    

def get_tatras_areas_weather_forecast():
    scraper = AreaScraper('https://tpn.pl/zwiedzaj/pogoda')
    areas_weather_forecasts = scraper.get_areas_weather_forecasts()
    return areas_weather_forecasts
