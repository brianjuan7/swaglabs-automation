from utilities.Locators import LoginPageLocators
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.locator = LoginPageLocators

    def get_username_input(self):
        return self.driver.find_element(*self.locator.username_input)

    def get_password_input(self):
        return self.driver.find_element(*self.locator.password_input)

    def get_submit_button(self):
        return self.driver.find_element(*self.locator.login_button)

    def get_error_message(self):
        return WebDriverWait(self.driver, 3).until(ec.visibility_of_element_located(self.locator.error_message))
