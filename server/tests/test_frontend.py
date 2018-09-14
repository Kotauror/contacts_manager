# import pytest
# import unittest
# from selenium import webdriver
# from flask import request
# from settings import db
#
# class TestFrontEnd(unittest.TestCase):
#
#     def setup_test(self):
#         db.session.commit()
#         db.drop_all()
#         db.create_all()
#
#     def get_driver(self):
#         driver = webdriver.Chrome("/usr/local/bin/chromedriver")
#         driver.set_page_load_timeout(10)
#         driver.get("http://127.0.0.1:5000/contacts")
#         return driver
#
#     def test_web_app_running(self):
#         self.setup_test()
#         driver = self.get_driver()
# 
#         try:
#             driver.find_element_by_id("welcome-message")
#         except:
#             self.fail("The website is not running")
#
#     def test_add_contact_to_contacts(self):
#         self.setup_test()
#         driver = self.get_driver()
#         driver.find_element_by_id("form-name").send_keys("Fake contact")
#         driver.find_element_by_id("form-telephone").send_keys("111")
#         driver.find_element_by_id("submit").click()
#
#         assert ("Fake contact" in driver.page_source)
#         assert ("Contact added successfully" in driver.page_source)
#
#     def test_delete_contact(self):
#         self.setup_test()
#         driver = self.get_driver()
#         driver.find_element_by_id("form-name").send_keys("Another fake contact")
#         driver.find_element_by_id("form-telephone").send_keys("000")
#         driver.find_element_by_id("submit").click()
#         driver.find_element_by_id("delete-Another fake contact").click()
#
#         assert not ("Another fake contact" in driver.page_source)
#         assert ("Contact deleted successfully" in driver.page_source)
#
#     def test_edit_contact(self):
#         self.setup_test()
#         driver = self.get_driver()
#         driver.find_element_by_id("form-name").send_keys("Another fake")
#         driver.find_element_by_id("form-telephone").send_keys("222")
#         driver.find_element_by_id("submit").click()
#         driver.find_element_by_id("edit-Another fake").click()
#         driver.find_element_by_id("form-name").send_keys("Edited fake contact")
#         driver.find_element_by_id("form-telephone").send_keys("444")
#         driver.find_element_by_id("submit").click()
#
#         assert not ("Another fake contact" in driver.page_source)
#         assert ("Edited fake contact" in driver.page_source)
#         assert ("Contact edited successfully" in driver.page_source)
