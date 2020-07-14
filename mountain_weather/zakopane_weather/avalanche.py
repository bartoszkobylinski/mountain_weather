from zakopane_weather.scraper import Scraper
from selenium.common.exceptions import NoSuchElementException

import logging

logging.basicConfig(filename='avalanche.log', level=logging.INFO)


class AvalancheWarningScraper(Scraper):

    def __init__(self,url):
        super().__init__()
        print('oeueue')
        self.url = url
    
    def _navigate_and_extract_avalanche_data(self):
        self.browser.get(self.url)
        avalanche_status = {}
        try:
            avalanche_level = self.browser.find_element_by_xpath('//*[@id="law-master"]/div[1]/div[1]/span/span')
            avalanche_status['avalanche_level'] = avalanche_level.text
            avalanche_warning_published = self.browser.find_element_by_class_name('law-mst-iat')
            avalanche_status['avalanche_warning_published'] = avalanche_warning_published.text
            avalanche_warning_valid_until = self.browser.find_element_by_class_name('law-mst-exp')
            avalanche_status['avalanche_warning_valid_until'] = avalanche_warning_valid_until.text
            avalanche_description = self.browser.find_element_by_class_name("law-mst-dsc")
            avalanche_status['avalanche_description'] = avalanche_description.text.replace('\n', ' ')
        except NoSuchElementException as error:
            logging.info(f"During scraping a website: {self.url} error has occured {error}")
        
        return avalanche_status


    def __str__(self):
        return f"that is my {self.url}"
    
def get_avalanche_status():
    print("11111111111")
    avalanche = AvalancheWarningScraper("http://lawiny.topr.pl/")
    print("aft")
    avalanche_status = avalanche._navigate_and_extract_avalanche_data()
    return avalanche_status
