from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from utilities import Formatter
from utilities.Locators import CheckoutPageLocators


class CheckoutPage:

    def __init__(self, driver):
        self.driver = driver
        self.locator = CheckoutPageLocators

    def get_checkout_page_title(self):
        return WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located(self.locator.checkout_page_title))

    def get_first_name_input(self):
        return self.driver.find_element(*self.locator.first_name_input)

    def get_last_name_input(self):
        return self.driver.find_element(*self.locator.last_name_input)

    def get_postal_input(self):
        return self.driver.find_element(*self.locator.postal_input)

    def get_continue_button(self):
        return self.driver.find_element(*self.locator.continue_button)

    def get_error_message(self):
        return WebDriverWait(self.driver, 3).until(ec.visibility_of_element_located(self.locator.error_message))

    def get_payment_information(self):
        return self.driver.find_element(*self.locator.payment_information)

    def get_shipping_information(self):
        return self.driver.find_element(*self.locator.shipping_information)

    def get_total_without_tax(self):
        return self.driver.find_element(*self.locator.total_without_tax_label)

    def get_tax(self):
        return self.driver.find_element(*self.locator.tax_label)

    def get_total_with_tax(self):
        return self.driver.find_element(*self.locator.total_with_tax_label)

    def get_checkout_cart_items(self):
        return self.driver.find_elements(*self.locator.checkout_cart_item)

    def get_checkout_items_information(self):
        checkout_cart = []

        for item in self.get_checkout_cart_items():
            label = item.find_element(*self.locator.checkout_cart_item_label).text
            price = Formatter.remove_currency(item.find_element(*self.locator.checkout_cart_item_price).text)
            description = item.find_element(*self.locator.checkout_cart_item_description).text
            checkout_cart.append({"label": label, "price": price, "description": description})
        return checkout_cart
