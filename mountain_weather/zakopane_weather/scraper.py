from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementNotInteractableException, ElementNotSelectableException, ElementNotVisibleException, ElementClickInterceptedException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.alert import Alert
import time


class MountainWeatherScraper:


    def __init__(self):

        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--window-size=1420,1080')
        #chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')

        self.url = "https://www.mountain-forecast.com/peaks/Banikov/forecasts/2178"
        self.browser = webdriver.Chrome(executable_path="/home/bart/PythonProjects/mountain_weather/mountain_weather/zakopane_weather/chromedriver", options = chrome_options)


    def _navigate_to_data_table(self):
        self.browser.get(self.url)
        time.sleep(5)
        cookie_agree = self.browser.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div[1]/button')
        cookie_agree.click()
        buttons = self.browser.find_elements_by_class_name('forecast__table-days-toggle')
        for button in buttons:
            button.click()

    def _get_number_of_columns(self):
        self._navigate_to_data_table()
        table_days = self.browser.find_elements_by_class_name('forecast__table-days')
        number_of_columns = []
        for tr in table_days:
            tags = tr.find_elements_by_tag_name('td')
            for tagname in tags:
                number_of_columns.append(int(tagname.get_attribute('colspan')))
        return number_of_columns      
        
    def make_correction_in_octave(self,octave):
        # Methods to fix format of octave of day which after scraping is like this 10\u2009PM and \u2009 has to be deleted
        octave = [char for char in octave]
        if octave[1] == '0':
            del(octave[2])
        else:
            del(octave[1])
        octave = ''.join(octave)
        return octave
    def scrap_data_weather_for_octave_of_a_day(self):        
        number_of_columns = self._get_number_of_columns()
        beggining = 1
        end = number_of_columns[0]
        headers = ['octave_of_a_day','windspeed','summary','rain','snow','temperature','chill_temperature']
        data_weather = []
        for i in range(len(number_of_columns)):
            x = range(beggining, end+1)
            for y in x:
                data = []
                octave_element = self.browser.find_element_by_xpath(f'//*[@id="forecast-cont"]/table/thead/tr[3]/td[{y}]/span')
                octave_of_a_day = octave_element.text
                octave_of_a_day = self.make_correction_in_octave(octave_of_a_day)
                data.append(octave_of_a_day)
                windspeed_element = self.browser.find_element_by_xpath(f'//*[@id="forecast-cont"]/table/tbody/tr[2]/td[{y}]/div/div/span')
                windspeed_of_octave = windspeed_element.text
                data.append(windspeed_of_octave)
                summary_element = self.browser.find_element_by_xpath(f'//*[@id="forecast-cont"]/table/tbody/tr[3]/td[{y}]')
                summary_of_octave = summary_element.text
                data.append(summary_of_octave)
                rain_element = self.browser.find_element_by_xpath(f'//*[@id="forecast-cont"]/table/tbody/tr[5]/td[{y}]/span/span')
                rain_of_octave = rain_element.text
                data.append(rain_of_octave)
                snow_element = self.browser.find_element_by_xpath(f'//*[@id="forecast-cont"]/table/tbody/tr[6]/td[{y}]/span/span')
                snow_of_octave = snow_element.text
                data.append(snow_of_octave)
                temperature_element = self.browser.find_element_by_xpath(f'//*[@id="forecast-cont"]/table/tbody/tr[7]/td[{y}]/span/span')
                temperature_of_octave = temperature_element.text
                data.append(temperature_of_octave)
                chill_temp_element = self.browser.find_element_by_xpath(f'//*[@id="forecast-cont"]/table/tbody/tr[9]/td[{y}]/span/span')
                chill_temp_of_octave = chill_temp_element.text
                data.append(chill_temp_of_octave)
                one_octave_data = dict(zip(headers,data))
                data_weather.append(one_octave_data)

            beggining = end+1
            try:
                end = beggining + int(number_of_columns[i+1])-1
            except IndexError:
                break
        return data_weather


        


 
a = MountainWeatherScraper()
a = a.scrap_data_weather_for_octave_of_a_day()
for i in a:
    print(i)