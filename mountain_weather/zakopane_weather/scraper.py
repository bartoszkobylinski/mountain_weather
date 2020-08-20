"""
Module to scrape weatherforecast for peaks
"""

from urllib.parse import urljoin
from datetime import datetime, timedelta
import logging
import os
import time

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from unidecode import unidecode
from zakopane_weather.location import peaks

logging.basicConfig(filename="scraper.log", level=logging.WARNING)


def get_url(peaks):
    """
    function generates absolute url for specific paeaks
    """
    base_url = "https://www.mountain-forecast.com/peaks/"
    for key, val in peaks.items():
        url1 = f"{key}/forecasts/{val}"
        url2 = base_url
        absolute_url = urljoin(url2, url1)
        yield absolute_url


class Scraper:
    path = os.environ.get("PATH_SCRAPER")

    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--window-size=1420,1080')
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        self.browser = webdriver.Chrome(
            executable_path=self.path, options=chrome_options)


class MountainWeatherScraper(Scraper):

    dict_octave_of_day = {
        '1AM': '01::00',
        '2AM': '02::00',
        '4AM': '04::00',
        '5AM': '05::00',
        '7AM': '07::00',
        '8AM': '08::00',
        '10AM': '10::00',
        '11AM': '11::00',
        '1PM': '13::00',
        '2PM': '14::00',
        '4PM': '16::00',
        '5PM': '17::00',
        '7PM': '19::00',
        '8PM': '20::00',
        '10PM': '22::00',
        '11PM': '23::00',
        }

    def __init__(self, url):
        super().__init__()
        self.url = url

    def _navigate_to_data_table(self):
        self.browser.get(self.url)
        time.sleep(5)
        mountain_name = self.browser.title
        logging.info(
            f"Scraper navigate to data table on the website: {mountain_name}")

        try:
            cookie_button = self.browser.find_element_by_xpath(
                '/html/body/div[1]/div/div/div[2]/div[1]/button'
                )
            if cookie_button:
                try:
                    cookie_button.click()
                    logging.info("i have clicked cookie button")
                except NoSuchElementException:
                    logging.warning(
                        """No Such Element Excertion has occured:
                        cookie button has not been found""")
        except Exception as error:
            logging.warning(f"""
            Other exception than NoSuchElementException has occured
            with error: {error}""")
        buttons = self.browser.find_elements_by_class_name(
            'forecast__table-days-toggle')
        try:
            for index in range(len(buttons)):
                java_script = f"""document.getElementsByClassName
                ('forecast__table-days-toggle')[{index}].click();"""
                self.browser.execute_script(java_script)
                logging.info("java_script has been executed")
        except Exception as error:
            logging.warning(f"""Error while java script has been
            executed has occured: {error}""")
        logging.info(f"""Script has found: {len(buttons)}
            buttons and all are pushed""")
        
    def _get_number_of_columns(self):
        self._navigate_to_data_table()
        table_days = self.browser.find_elements_by_class_name(
            "forecast__table-days")
        number_of_columns = []
        for tr in table_days:
            tags = tr.find_elements_by_tag_name("td")
            for tagname in tags:
                number_of_columns.append(int(tagname.get_attribute("colspan")))
        logging.info(f"""Scraper has found table with {str(number_of_columns)}
            numbers of columns""")
        return number_of_columns
        
    def make_correction_in_octave(self, octave):
        """
        Methods fixes format of octave of day which after scraping
        is looking like this 10\u2009PM and \u2009 has to be deleted
        """
        octave = [char for char in octave]
        octave.remove('\u2009')
        octave = "".join(octave)
        return octave

    def convert_timeinfo_to_requested_type(
            self, date, octaveofday, dict_octave_of_day):
        try:
            if octaveofday is not None:
                octaveofday = dict_octave_of_day.get(octaveofday, '')
                time_to_convert = datetime.strptime(
                        octaveofday, '%H::%M').time()
                converted_datetime = datetime.combine(date, time_to_convert)
                return converted_datetime
            else:
                return "None"
        except AttributeError as error:
            print(f"That is error: {error} and date is{date} and octaveofday {octaveofday}")
       
    def scrap_data_weather_for_octave_of_a_day(self):
        """
        methods returns a dictionary with peak name and elevation,
        date, windspeed, short summany, rain, snow, temperature and
        chill temperature
        """   
        try:     
            number_of_columns = self._get_number_of_columns()
            beggining = 1
            end = number_of_columns[0]
        except IndexError as error:
            logging.warning(
                f"An error occured while script gets number of columns {error}")
        data_weather = []
        current_date = datetime.today()
        delta = timedelta(days=1)
        name_of_peak = self.browser.title
        name_of_peak = name_of_peak.split(' ')
        elevation = name_of_peak[-1]
        elevation = int(elevation[1:-2])
        name_of_peak = unidecode(name_of_peak[0])
        for i in range(len(number_of_columns)):
            x = range(beggining, end + 1)
            date = current_date
            for y in x:
                try:
                    octave_element = self.browser.find_element_by_xpath(
                        f'//*[@id="forecast-cont"]/table/thead/tr[3]/td[{y}]/span'
                    )
                except Exception as error:
                    logging.warning(f"Error while getting octave_element: {error}")
                octave_of_a_day = octave_element.text
                octave_of_a_day = self.make_correction_in_octave(octave_of_a_day)
                if octave_of_a_day is not None:
                    date_after_scraping = self.convert_timeinfo_to_requested_type(
                        date, octave_of_a_day, self.dict_octave_of_day
                        )
                    date_after_scraping = date_after_scraping.strftime('%Y-%m-%d %H:%M')
                else:
                    date_after_scraping = "None"
                windspeed_element = self.browser.find_element_by_xpath(
                    f'//*[@id="forecast-cont"]/table/tbody/tr[2]/td[{y}]/div/div/span'
                )
                windspeed_element = windspeed_element.text
                if windspeed_element == '' or windspeed_element == "-":
                    windspeed_element = 0

                summary_element = self.browser.find_element_by_xpath(
                    f'//*[@id="forecast-cont"]/table/tbody/tr[3]/td[{y}]'
                )
                summary_element = summary_element.text

                rain_element = self.browser.find_element_by_xpath(
                    f'//*[@id="forecast-cont"]/table/tbody/tr[5]/td[{y}]/span/span'
                )
                rain_element = rain_element.text
                if rain_element == '' or rain_element == "-":
                    rain_element = 0

                snow_element = self.browser.find_element_by_xpath(
                    f'//*[@id="forecast-cont"]/table/tbody/tr[6]/td[{y}]/span/span'
                )
                snow_element = snow_element.text
                if snow_element == '' or snow_element == "-":
                    snow_element = 0

                temperature_element = self.browser.find_element_by_xpath(
                    f'//*[@id="forecast-cont"]/table/tbody/tr[7]/td[{y}]/span/span'
                )
                temperature_element = temperature_element.text
                if temperature_element == '' or temperature_element == "-":
                    temperature_element = 0
                chill_temp_element = self.browser.find_element_by_xpath(
                    f'//*[@id="forecast-cont"]/table/tbody/tr[9]/td[{y}]/span/span'
                )
                chill_temp_element = chill_temp_element.text
                if chill_temp_element == '' or chill_temp_element == '-':
                    chill_temp_element = 0

                data_weather.append({
                    "name_of_peak": name_of_peak,
                    "elevation": elevation,
                    "date": date_after_scraping,
                    "windspeed": windspeed_element,
                    "summary": summary_element,
                    "rain": rain_element,
                    "snow": snow_element,
                    "temperature": temperature_element,
                    "chill_temperature": chill_temp_element
                })
                date = current_date
            current_date = current_date + delta

            beggining = end + 1
            try:
                end = beggining + int(number_of_columns[i + 1]) - 1
            except IndexError:
                break
        self.browser.close()
        return data_weather


def get_pekas_detailed_weather():
    """
    generator yield a dictionary with a mountain scraped weather forecast
    """
    for url in get_url(peaks):
        mountain = MountainWeatherScraper(url)
        mountain_weather = mountain.scrap_data_weather_for_octave_of_a_day()
        yield mountain_weather
