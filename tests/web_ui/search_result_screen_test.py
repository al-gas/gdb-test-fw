from selenium import webdriver
from page_objects.gdb_search_result_page import ResultsPage


"""
Tests:
 1. Verify Ship Name field
 2. Verify Class field
 3. Verify Status field
 4. Verify Language Options
 5. Verify all data is cleared
 6. Verify return to main DB screen
"""


class TestOptions:
    browser = webdriver.Chrome()
    res_page = ResultsPage(browser=browser)
    res_page.load()
    language = "Zurbagan"

    def test_clear_all_data(self):
        """
        Verify all data is cleared
        """
        self.res_page.clear_all_data()
        name_field_value = self.res_page.get_name_value()
        class_field_value = self.res_page.get_class_value()
        status_field_value = self.res_page.get_status_value()
        assert name_field_value == '', "Expected name empty field, got {}".format(name_field_value)
        assert class_field_value == '', "Expected class empty field, got {}".format(class_field_value)
        assert status_field_value == '', "Expected status empty field, got {}".format(status_field_value)

    def test_language_options(self):
        """
        Verify testing options
        """
        self.res_page.set_language_option(self.language)
        # Need to assert if all labels are displayed on Zurbagan language
        assert True

    def test_return_to_main_db_screen(self):
        """
        Verify returning to the main DB screen
        Will need another Page Object for the Main screen to test it
        """
        self.res_page.return_to_main_db_screen()
        # Need to assert that we returned to the main DB screen
        # Don't have specs to work on it
        assert True


class TestFilterFields:
    browser = webdriver.Chrome()
    res_page = ResultsPage(browser=browser)
    res_page.load()

    def test_ship_name_field_positive(self):
        name = 'Devastator'
        self.res_page.search_by_name(name)
        name_field_value = self.res_page.get_name_value()

        assert name_field_value == name, "Expected name: {}, got: {}".format(name, name_field_value)
        self._clear_data()

    def test_ship_name_field_empty_set(self):
        self.res_page.search_by_name('Some Not Existing Ship')
        name_field_value = self.res_page.get_name_value()
        class_field_value = self.res_page.get_class_value()
        status_field_value = self.res_page.get_status_value()
        assert name_field_value == '', "Expected name empty field, got {}".format(name_field_value)
        assert class_field_value == '', "Expected class empty field, got {}".format(class_field_value)
        assert status_field_value == '', "Expected status empty field, got {}".format(status_field_value)

    def class_field_test(self):
        pass

    def status_field_test(self):
        pass

    def _clear_data(self):
        self.res_page.clear_all_data()
        name_field_value = self.res_page.get_name_value()
        class_field_value = self.res_page.get_class_value()
        status_field_value = self.res_page.get_status_value()
        assert name_field_value == '', "Expected name empty field, got {}".format(name_field_value)
        assert class_field_value == '', "Expected class empty field, got {}".format(class_field_value)
        assert status_field_value == '', "Expected status empty field, got {}".format(status_field_value)
