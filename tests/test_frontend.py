import pytest
import unittest
from selenium import webdriver
from flask import request

class TestFrontEnd(unittest.TestCase):

    def test_web_app_fires_up(self):
        driver = webdriver.Chrome("/usr/local/bin/chromedriver")
        driver.set_page_load_timeout(10)
        driver.get("http://127.0.0.1:5000/")

        try:
            driver.find_element_by_id("single_contact")
        except:
            self.fail("The website is not running")

    def test_web_app_running(self):
        driver = webdriver.Chrome("/usr/local/bin/chromedriver")
        driver.set_page_load_timeout(10)
        driver.get("http://127.0.0.1:5000/")

        try:
            driver.find_element_by_id("single_contact")
        except:
            self.fail("There are no contacts on the website")

    def test_add_contact_to_contacts(self):
        driver = webdriver.Chrome("/usr/local/bin/chromedriver")
        driver.set_page_load_timeout(10)
        driver.get("http://127.0.0.1:5000/")
        driver.find_element_by_id("form-name").send_keys("Kota")
        driver.find_element_by_id("form-telephone").send_keys("123")
        driver.find_element_by_id("submit").click()

        try:
            driver.getPageSource().contains("Kota")
        except:
            self.fail("This contact is not visible on the website")
