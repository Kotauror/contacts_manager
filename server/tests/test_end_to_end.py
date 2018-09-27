from flask import request
import pytest
import time
from selenium import webdriver
from settings import db
import unittest

class TestEndToEnd(unittest.TestCase):

    def setup_test(self):
        db.session.commit()
        db.drop_all()
        db.create_all()

    def get_driver(self):
        driver = webdriver.Chrome("/usr/local/bin/chromedriver")
        driver.set_page_load_timeout(10)
        driver.get("http://127.0.0.1:5000")
        return driver

    def test_add_contact_to_contacts(self):
        self.setup_test()
        driver = self.get_driver()
        driver.find_element_by_class_name("input-name").send_keys("Justyna")
        driver.find_element_by_class_name("input-Phone").send_keys("TestPhone")
        driver.find_element_by_class_name("btn-add").click()
        time.sleep(1)

        assert ("Justyna" in driver.page_source)

    def test_delete_contact(self):
        self.setup_test()
        driver = self.get_driver()
        driver.find_element_by_class_name("input-name").send_keys("kocia")
        driver.find_element_by_class_name("input-Phone").send_keys("000")
        driver.find_element_by_class_name("btn-add").click()
        time.sleep(1)
        driver.find_element_by_id("delete_button").click()
        time.sleep(1)

        assert not ("kocia" in driver.page_source)

    def test_edit_contact(self):
        self.setup_test()
        driver = self.get_driver()
        driver.find_element_by_class_name("input-name").send_keys("Another fake")
        driver.find_element_by_class_name("input-Phone").send_keys("222")
        driver.find_element_by_class_name("btn-add").click()
        time.sleep(1)
        driver.find_element_by_id("edit_button").click()
        driver.find_element_by_id("nameInput").send_keys("Edited fake contact")
        driver.find_element_by_id("telephoneInput").send_keys("444")
        driver.find_element_by_id("save_button").click()
        time.sleep(1)
        
        assert not ("Another fake contact" in driver.page_source)
        assert ("Another fakeEdited fake contact" in driver.page_source)
