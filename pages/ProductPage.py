from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from utilities import Logger, Formatter
from utilities.Locators import ProductsPageLocators


class ProductsPage:

    def __init__(self, driver):
        self.driver = driver
        self.locator = ProductsPageLocators

    def get_page_title(self):
        return WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located(self.locator.products_page_title))

    def get_back_to_products_button(self):
        return WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located(self.locator.back_to_products_button))

    def get_cart_link(self):
        return self.driver.find_element(*self.locator.cart_link)

    def get_sort_dropdown(self):
        return self.driver.find_element(*self.locator.sort_dropdown)

    def get_product_items(self):
        return self.driver.find_elements(*self.locator.product_item)

    def select_sort(self, sort_type):
        options = self.driver.find_element(*self.locator.sort_dropdown).find_elements(*self.locator.sort_options)

        for option in options:
            if option.text == sort_type:
                return option

        message = f"Product Sort: {sort_type} not found."
        Logger.get_logger().error(message)
        raise SystemExit(message)

    def get_a_product_label(self, label):
        for item in self.get_product_items():
            item_element = item.find_element(*self.locator.product_label)
            if item_element.text == label:
                return WebDriverWait(self.driver, 5).until(ec.element_to_be_clickable(
                    item.find_element(*self.locator.product_label)))

        message = f"Unable to find item: {label}."
        Logger.get_logger().error(message)
        raise SystemExit(message)

    def get_product_labels(self):
        labels = []

        for item in self.get_product_items():
            labels.append(item.find_element(*self.locator.product_label).text)
        return labels

    def get_product_prices(self):
        prices = []

        for item in self.get_product_items():
            prices.append(Formatter.remove_currency(item.find_element(*self.locator.product_price).text))
        return prices

    def get_add_to_cart_button(self, product_name):
        for item in self.get_product_items():
            label = item.find_element(*self.locator.product_label).text
            if label == product_name:
                Logger.get_logger().info(f"{product_name} added to cart.")
                return item.find_element(*self.locator.add_to_cart_button)

        message = f"Unable to find item: {product_name}."
        Logger.get_logger().error(message)
        raise SystemExit(message)

    def get_detailed_product_name(self):
        return self.driver.find_element(*self.locator.detailed_product_name)

    def get_detailed_product_description(self):
        return self.driver.find_element(*self.locator.detailed_product_description)

    def get_detailed_product_price(self):
        return self.driver.find_element(*self.locator.detailed_product_price)
