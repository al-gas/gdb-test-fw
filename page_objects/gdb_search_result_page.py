from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from lib.const import BASE_URL


class ResultsPage:
    """"""

    # We assume that this is a robotically produced ideal web page with IDs that make sense
    SHIP_NAME_FIELD = (By.ID, 'ship_name_field')
    SHIP_CLASS_FIELD = (By.ID, 'ship_class_field')
    SHIP_STATUS_FIELD = (By.ID, 'ship_status_field')
    QTY_TURBO_LASER_FIELD = (By.ID, 'qty_turbo_laser_field')
    QTY_ION_CANNON_FIELD = (By.ID, 'qty_ion_cannon_field')
    QTY_TRACTOR_BEAMS_FIELD = (By.ID, 'div.qty_tractor_beams_field')

    def __init__(self, browser):
        self.browser = browser
        self.url = BASE_URL + '/search'

    def load(self):
        self.browser.get(self.url)

    def search_by_name(self, search_input):
        ship_name_field = self.browser.find_element(*self.SHIP_NAME_FIELD)
        ship_name_field.text = search_input
        response = ship_name_field.send_keys(Keys.RETURN)
        return response

    def search_by_class(self, search_input):
        ship_class_field = self.browser.find_element(*self.SHIP_CLASS_FIELD)
        ship_class_field.text = search_input
        response = ship_class_field.send_keys(Keys.RETURN)
        return response

    def search_by_status(self, search_input):
        ship_status_field = self.browser.find_element(*self.SHIP_STATUS_FIELD)
        ship_status_field.text = search_input
        response = ship_status_field.send_keys(Keys.RETURN)
        return response
