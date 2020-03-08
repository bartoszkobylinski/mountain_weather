from urllib.parse import urljoin


from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


import logging
import time

# logger settings
logging.basicConfig(filename="scraper.log", level=logging.INFO)

class Scraper:
     path = "/home/bart/PythonProjects/mountain/chromedriver"
     
     def __init__(self):
        # chrome_options.add_argument('--headless') Add that after testing!!!!
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--window-size=1420,1080')
        #chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        self.browser = webdriver.Chrome(executable_path=self.path, options = chrome_options)

# move it to another file after tests
peaks = {
        'Banikov':'2178',
        'Baranec':'2184',
        'Gerlach':'2655',
        'Giewont':'1909',
        'Gubalowka':'1126',
        'Kasprowy-Wierch':'1987',
        'Koscielec':'2155',
        'Krivan':'2494',
        'Mieguszowiecki-Szczyt-Wielki':'2438',
        'Mnich-mountain':'2068',
        'Ostry-Rohac':'2087',
        'Rysy':'2499',
        'Slavkovsky-Stit':'2452',
        'Swinica':'2301',
        'Volovec-Tatra':'2063',
        'Vychodna-Vysoka':'2574',
        'Woloszyn':'2155'
    }

base_url="https://www.mountain-forecast.com/peaks/"

def get_url(peaks, base_url):
    for key, val in peaks.items():
        url1 = f"{key}/forecasts/{val}" 
        url2 = base_url
        absolute_url = urljoin(url2,url1)
        yield absolute_url

class MountainWeatherScraper(Scraper):

    def __init__(self,url):
        super().__init__()
        self.url = url


    def _navigate_to_data_table(self):
        self.browser.get(self.url)
        time.sleep(5)
        mountain_name = self.browser.title
        logging.info("Scraper navigate to data table on the website: " + mountain_name)

        try:
            cookie_button = self.browser.find_element_by_xpath(
                '/html/body/div[1]/div/div/div[2]/div[1]/button'
                )
            if cookie_button:
                try: 
                    cookie_button.click()
                    logging.info("i have clicked cookie button")
                except NoSuchElementException:
                    logging.info("No Such Element Excertion has occured: cookie button has not been found")
        except Exception as error:
            logging.info("Other exception than NoSuchElementException has occured with error:" + error)
        buttons = self.browser.find_elements_by_class_name('forecast__table-days-toggle')
        try:
            for index in range(len(buttons)):
                java_script = f"document.getElementsByClassName('forecast__table-days-toggle')[{index}].click();"
                self.browser.execute_script(java_script) 
                logging.info("java_script has been executed")
        except Exception as error:
            logging.info("Error while java script has been executed has occured: " + error)
        logging.info("Script has found: " + str(len(buttons)) + " buttons and all are pushed")
        
    def _get_number_of_columns(self):
        self._navigate_to_data_table()
        table_days = self.browser.find_elements_by_class_name("forecast__table-days")
        number_of_columns = []
        for tr in table_days:
            tags = tr.find_elements_by_tag_name("td")
            for tagname in tags:
                number_of_columns.append(int(tagname.get_attribute("colspan")))
        logging.info("Scraper has found table with " + str(number_of_columns) + " numbers of columns")
        return number_of_columns
        

    def make_correction_in_octave(self, octave):
        """
        Methods to fix format of octave of day which after scraping
        is like this 10\u2009PM and \u2009 has to be deleted
        """
        octave = [char for char in octave]
        logging.info("octave is: " + str(octave))
        try:
            if octave[1] == "0":
                del octave[2]
            else:
                del octave[1]
            octave = "".join(octave)
            return octave
        except Exception as error:
            logging.warning(f"""
            Error in make_correction_in_octave has occured. Octave variable is: + {octave} 
            and error is: + {error}. 
            """)
        
    def scrap_data_weather_for_octave_of_a_day(self):        
        number_of_columns = self._get_number_of_columns()
        beggining = 1
        end = number_of_columns[0]
        headers = [
            "octave_of_a_day",
            "windspeed",
            "summary",
            "rain",
            "snow",
            "temperature",
            "chill_temperature",
        ]
        data_weather = []
        for i in range(len(number_of_columns)):
            x = range(beggining, end + 1)
            for y in x:
                data = []
                octave_element = self.browser.find_element_by_xpath(
                    f'//*[@id="forecast-cont"]/table/thead/tr[3]/td[{y}]/span'
                )
                octave_of_a_day = octave_element.text
                octave_of_a_day = self.make_correction_in_octave(octave_of_a_day)

                data.append(octave_of_a_day)
                windspeed_element = self.browser.find_element_by_xpath(
                    f'//*[@id="forecast-cont"]/table/tbody/tr[2]/td[{y}]/div/div/span'
                )
                windspeed_of_octave = windspeed_element.text
                data.append(windspeed_of_octave)
                summary_element = self.browser.find_element_by_xpath(
                    f'//*[@id="forecast-cont"]/table/tbody/tr[3]/td[{y}]'
                )
                summary_of_octave = summary_element.text
                data.append(summary_of_octave)
                rain_element = self.browser.find_element_by_xpath(
                    f'//*[@id="forecast-cont"]/table/tbody/tr[5]/td[{y}]/span/span'
                )
                rain_of_octave = rain_element.text
                data.append(rain_of_octave)
                snow_element = self.browser.find_element_by_xpath(
                    f'//*[@id="forecast-cont"]/table/tbody/tr[6]/td[{y}]/span/span'
                )
                snow_of_octave = snow_element.text
                data.append(snow_of_octave)
                temperature_element = self.browser.find_element_by_xpath(
                    f'//*[@id="forecast-cont"]/table/tbody/tr[7]/td[{y}]/span/span'
                )
                temperature_of_octave = temperature_element.text
                data.append(temperature_of_octave)
                chill_temp_element = self.browser.find_element_by_xpath(
                    f'//*[@id="forecast-cont"]/table/tbody/tr[9]/td[{y}]/span/span'
                )
                chill_temp_of_octave = chill_temp_element.text
                data.append(chill_temp_of_octave)
                one_octave_data = dict(zip(headers, data))
                data_weather.append(one_octave_data)

            beggining = end + 1
            try:
                end = beggining + int(number_of_columns[i + 1]) - 1
            except IndexError :
                break
        logging.info("I have gathered data from: " + self.browser.title)
        return data_weather


def get_pekas_detailed_weather(peaks, base_url):

    for url in get_url(peaks,base_url):
        mountain = MountainWeatherScraper(url)
        mountain_weather = mountain.scrap_data_weather_for_octave_of_a_day()
        yield mountain_weather



if __name__ == "__main__":

    for mountian_weather in get_pekas_detailed_weather(peaks,base_url):
        print(mountian_weather)
'''    
    for url in get_url(peaks,base_url):

        a = MountainWeatherScraper(url)    
        a = a.scrap_data_weather_for_octave_of_a_day()
        print(a)
'''