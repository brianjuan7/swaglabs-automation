from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from utilities import Locators


class NavigationMenu:

    def __init__(self, driver):
        self.driver = driver
        self.locator = Locators.NavigationMenuLocators

    def get_swag_labs_title(self):
        return WebDriverWait(self.driver, 5).until(ec.presence_of_element_located(self.locator.swag_labs_title))
