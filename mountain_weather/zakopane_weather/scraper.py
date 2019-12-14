from selenium import webdriver
import time


class MountainWeatherScraper:


    def __init__(self):

        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--window-size=1420,1080')
        #chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')

        self.url = "https://www.mountain-forecast.com/peaks/Banikov/forecasts/2178"
        self.browser = webdriver.Chrome(executable_path='/home/bart/PythonProjects/mountain/chromedriver',options = chrome_options)


    def get_data(self):
        #self.browser.fullscreen_window()
        self.browser.get(self.url)
        time.sleep(5)
        buttons = self.browser.find_elements_by_class_name('forecast__table-days-toggle')
        for button in buttons:
            button.click()
        element = self.browser.find_element_by_tag_name('thead')
        days = element.find_elements_by_class_name('forecast__table-days-name')
        for day in days:
            print(day.text)
        
        times = element.find_elements_by_class_name('forecast__table-time-item')
        for hours in times:
            print(hours.text)
        print('eouoeu')

        

a = MountainWeatherScraper()
a.get_data()