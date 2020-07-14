from django.test import TestCase

# Create your tests here.
'''
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from urllib.parse import urljoin
 
import unittest
import time
 
class NewVisitorTest(StaticLiveServerTestCase):
 
    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(3)
 
    def tearDown(self):
        self.browser.quit()
   
    # Test przechodzi, wpisuję niepoprawne dane przy logowaniu i dostaję, to czego oczekuję "Invalid login"
    def test_user_cannot_sign_in_after_entering_invalid_data(self):
        url = urljoin(self.live_server_url, '/login/')
        self.browser.get(url)
 
        # User goes to login page and realizes that the login form is there
        expected_login_header = "Login to account"
        login_header_text = self.browser.find_element_by_tag_name('h3').text
        self.assertEqual(expected_login_header, login_header_text)
 
        # User enters invalid username and password and then receives info
        # about invalid login process
        input_login = self.browser.find_element_by_id('id_username')
        input_password = self.browser.find_element_by_id('id_password')
        button_login = self.browser.find_element_by_css_selector('.button_login')
 
        input_login.send_keys('username')
        input_password.send_keys('password')
        button_login.click()
 
        invalid_login_text = self.browser.find_element_by_tag_name('body').text
        self.assertEqual(invalid_login_text, 'Invalid login')
 
    # Test nie przechodzi - wpisuję poprawne dane i dostaję "Invalid login" zamiast "Authenticated successfully"
    def test_user_can_sign_in_after_entering_valid_data(self):
        url = urljoin(self.live_server_url, '/login/')
        self.browser.get(url)
 
        # User enters valid username and password and then receives info
        # about successful login process
        input_login = self.browser.find_element_by_id('id_username')
        input_password = self.browser.find_element_by_id('id_password')
        button_login = self.browser.find_element_by_css_selector('.button_login')
 
        input_login.send_keys('usernametest')
        input_password.send_keys('passwordtest')
        button_login.click()
 
        time.sleep(10)
        valid_login_text = self.browser.find_element_by_tag_name('body').text
        self.assertEqual(valid_login_text, 'Authenticated successfully')
'''





a=1
b=2
c=3
d=4
given_parabola = str(a) + "x^2 + " + str(b) + "x + " + (str(c)) + " = " + str(d)
print(given_parabola)
given_parabola = f"{a} x^2 {b} x {c} = {d}"
print(given_parabola)