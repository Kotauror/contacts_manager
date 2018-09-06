import pytest
import unittest
from selenium import webdriver
from flask import request

class TestFrontEnd(unittest.TestCase):

    def test_web_app_running(self):
        driver = webdriver.Chrome("/usr/local/bin/chromedriver")
        driver.set_page_load_timeout(10)
        driver.get("http://127.0.0.1:5000/contacts")

        try:
            driver.find_element_by_id("welcome-message")
        except:
            self.fail("The website is not running")

    def test_add_contact_to_contacts(self):
        driver = webdriver.Chrome("/usr/local/bin/chromedriver")
        driver.set_page_load_timeout(10)
        driver.get("http://127.0.0.1:5000/contacts")
        driver.find_element_by_id("form-name").send_keys("Fake contact")
        driver.find_element_by_id("form-telephone").send_keys("111")
        driver.find_element_by_id("submit").click()

        assert ("Fake contact" in driver.page_source)
        assert ("Contact added successfully" in driver.page_source)

        driver.find_element_by_id("delete-Fake contact").click()

    def test_delete_contact(self):
        driver = webdriver.Chrome("/usr/local/bin/chromedriver")
        driver.set_page_load_timeout(10)
        driver.get("http://127.0.0.1:5000/contacts")
        driver.find_element_by_id("form-name").send_keys("Another fake contact")
        driver.find_element_by_id("form-telephone").send_keys("000")
        driver.find_element_by_id("submit").click()
        driver.find_element_by_id("delete-Another fake contact").click()

        assert not ("Another fake contact" in driver.page_source)
        assert ("Contact deleted successfully" in driver.page_source)

    def test_edit_contact(self):
        driver = webdriver.Chrome("/usr/local/bin/chromedriver")
        driver.set_page_load_timeout(10)
        driver.get("http://127.0.0.1:5000/contacts")
        driver.find_element_by_id("form-name").send_keys("Another fake")
        driver.find_element_by_id("form-telephone").send_keys("222")
        driver.find_element_by_id("submit").click()
        driver.find_element_by_id("edit").click()
        driver.find_element_by_id("form-name").send_keys("Edited fake contact")
        driver.find_element_by_id("form-telephone").send_keys("444")
        driver.find_element_by_id("submit").click()

        assert not ("Another fake contact" in driver.page_source)
        assert ("Edited fake contact" in driver.page_source)
        assert ("Contact edited successfully" in driver.page_source)

        driver.find_element_by_id("delete-Edited fake contact").click()
