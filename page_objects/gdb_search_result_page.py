from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from lib.const import BASE_URL


class ResultsPage:
    """"""

    # We assume that this is a robotically produced ideal web page with IDs that make sense
    LANGUAGE_OPTIONS_BUTTON = (By.ID, 'language_options_button')
    EXECUTE_SEARCH_BUTTON = (By.ID, 'execute_search_button')
    CLEAR_ALL_DATA_BUTTON = (By.ID, 'clear_all_data_button')
    RETURN_TO_MAIN_DB_SCREEN_BUTTON = (By.ID, 'return_to_main_db_screen_button')

    SHIP_NAME_FIELD = (By.ID, 'ship_name_field')
    SHIP_CLASS_FIELD = (By.ID, 'ship_class_field')
    SHIP_STATUS_FIELD = (By.ID, 'ship_status_field')
    QTY_TURBO_LASER_FIELD = (By.ID, 'qty_turbo_laser_field')
    QTY_ION_CANNON_FIELD = (By.ID, 'qty_ion_cannon_field')
    QTY_TRACTOR_BEAMS_FIELD = (By.ID, 'qty_tractor_beams_field')

    def __init__(self, browser):
        self.browser = browser
        self.url = BASE_URL + '/search'

    def load(self):
        self.browser.get(self.url)

    def search_by_name(self, search_input):
        ship_name_field = self.browser.find_element(*self.SHIP_NAME_FIELD)
        execute_search_button = self.browser.find_element(*self.EXECUTE_SEARCH_BUTTON)

        ship_name_field.text = search_input
        execute_search_button.click()

    def get_name_value(self):
        ship_name_field = self.browser.find_element(*self.SHIP_NAME_FIELD)
        return ship_name_field.text

    def search_by_class(self, search_input):
        ship_class_field = self.browser.find_element(*self.SHIP_CLASS_FIELD)
        execute_search_button = self.browser.find_element(*self.EXECUTE_SEARCH_BUTTON)

        ship_class_field.text = search_input
        execute_search_button.click()

    def get_class_value(self):
        ship_class_field = self.browser.find_element(*self.SHIP_CLASS_FIELD)
        return ship_class_field.text

    def search_by_status(self, search_input):
        ship_status_field = self.browser.find_element(*self.SHIP_STATUS_FIELD)
        execute_search_button = self.browser.find_element(*self.EXECUTE_SEARCH_BUTTON)

        ship_status_field.text = search_input
        execute_search_button.click()

    def get_status_value(self):
        ship_status_field = self.browser.find_element(*self.SHIP_STATUS_FIELD)
        return ship_status_field.text

    def clear_all_data(self):
        clear_all_data_button = self.browser.find_element(*self.CLEAR_ALL_DATA_BUTTON)
        clear_all_data_button.click()

    def return_to_main_db_screen(self):
        return_to_main_db_screen_button = self.browser.find_element(*self.RETURN_TO_MAIN_DB_SCREEN_BUTTON)
        return_to_main_db_screen_button.click()

    def set_language_option(self, language):
        language_options_button = self.browser.find_element(*self.LANGUAGE_OPTIONS_BUTTON)
        language_options_button.click()

        # Do logic to set the language in accordance to the parameter passed into the method
        pass


