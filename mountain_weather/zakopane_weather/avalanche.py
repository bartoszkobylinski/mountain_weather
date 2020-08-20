"""
file where is class responsible for geting information about current avalanche
status in Tatara Mountains
"""

import logging
from selenium.common.exceptions import NoSuchElementException
from zakopane_weather.scraper import Scraper


logging.basicConfig(filename='avalanche.log', level=logging.INFO)


class AvalancheWarningScraper(Scraper):
    """
    A class to represent Scraper for Avalanche Warning in
    Tatras Mountain
    """

    def __init__(self, url):
        super().__init__()
        self.url = url

    def navigate_and_extract_avalanche_data(self):
        """
        Navigate and extract data about avalanche status
        """
        self.browser.get(self.url)
        avalanche_status = {}
        try:
            avalanche_level = self.browser.find_element_by_xpath(
                '//*[@id="law-master"]/div[1]/div[1]/span/span')
            avalanche_status['avalanche_level'] = avalanche_level.text
            avalanche_warning_published = self.browser.find_element_by_class_name(
                'law-mst-iat')
            avalanche_status['avalanche_warning_published'] = avalanche_warning_published.text
            avalanche_warning_valid_until = self.browser.find_element_by_class_name('law-mst-exp')
            avalanche_status['avalanche_warning_valid_until'] = avalanche_warning_valid_until.text
            avalanche_description = self.browser.find_element_by_class_name("law-mst-dsc")
            avalanche_status['avalanche_description'] = avalanche_description.text.replace('\n', ' ')
        except NoSuchElementException as error:
            logging.info(f"""During scraping a website: {self.url} error has
            occured {error}""")
        return avalanche_status

    def __str__(self):
        return f"that is my {self.url}"


def get_avalanche_status():
    """
    function returns current avalanche status in Tatra Mountains
    """
    avalanche = AvalancheWarningScraper("http://lawiny.topr.pl/")
    avalanche_status = avalanche.navigate_and_extract_avalanche_data()
    return avalanche_status
