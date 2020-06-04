from selenium import webdriver
from page_objects.gdb_search_result_page import ResultsPage


"""
Tests:
 1. Verify Ship Name field
 2. Verify Class field
 3. Verify Status field
 4. Verify Armament fields
    4.1 Qty Turbo Laser
    4.2 Qty Ion Cannons
    4.3 Qty Tractor Beams
"""


class TestFilterFields:
    browser = webdriver.Chrome()
    res_page = ResultsPage(browser=browser)
    res_page.load()

    def ship_name_field_test(self):
        pass

    def class_field_test(self):
        pass

    def status_field_test(self):
        pass

