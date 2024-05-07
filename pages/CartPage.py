from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from utilities import Logger, Formatter
from utilities.Locators import CartPageLocators


class CartPage:

    def __init__(self, driver):
        self.driver = driver
        self.locator = CartPageLocators

    def get_cart_page_title(self):
        return WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located(self.locator.cart_page_title))

    def get_cart_items(self):
        return self.driver.find_elements(*self.locator.cart_item)

    def get_checkout_button(self):
        return WebDriverWait(self.driver, 5).until(ec.element_to_be_clickable(self.locator.checkout_button))

    def get_cart_labels_and_prices(self):
        cart = []

        for item in self.get_cart_items():
            label = item.find_element(*self.locator.cart_item_label).text
            price = Formatter.remove_currency(item.find_element(*self.locator.cart_item_price).text)
            cart.append({"label": label, "price": price})
        return cart

    def get_remove_item_button(self, label):
        for item in self.get_cart_items():
            if item.find_element(*self.locator.cart_item_label).text == label:
                return item.find_element(*self.locator.remove_item_button)

        message = f"Unable to find item: {label} in the cart."
        Logger.get_logger().error(message)
        raise SystemExit(message)

