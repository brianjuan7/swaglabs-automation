import pytest

from data import User
from data.Application import Title, Messages
from data.Product import Product
from utilities import Logger, Formatter


def add_single_item_to_cart(pages):
    # Select an item from the test data
    product = Product()
    name = product.get_random_item()["label"]

    # Add the item in the cart then verify if the cart page was displayed
    pages["products_page"].get_add_to_cart_button(name).click()
    pages["products_page"].get_cart_link().click()
    assert Title.CART in pages["cart_page"].get_cart_page_title().text, Messages.cart_title_not_displayed

    # Go to checkout page then verify if the checkout page was displayed
    pages["cart_page"].get_checkout_button().click()
    assert Title.CHECKOUT_YOUR_INFORMATION in pages["checkout_page"].get_checkout_page_title().text, (
        Messages.checkout_information_title_not_displayed)

    return product


def input_checkout_information(pages, first_name, last_name, postal):
    pages["checkout_page"].get_first_name_input().send_keys(first_name)
    pages["checkout_page"].get_last_name_input().send_keys(last_name)
    pages["checkout_page"].get_postal_input().send_keys(postal)
    pages["checkout_page"].get_continue_button().click()


def verify_information_and_prices(pages, all_prices):
    # Assign all the expected values and get the actual values
    total_price_without_tax = sum(all_prices)
    tax = Formatter.get_two_decimals_float(total_price_without_tax * Product.TAX)
    total_price_with_tax = Formatter.get_two_decimals_float(total_price_without_tax + tax)
    actual_payment_information = pages["checkout_page"].get_payment_information().text
    actual_shipping_information = pages["checkout_page"].get_shipping_information().text
    actual_total_price_without_tax = Formatter.remove_currency(pages["checkout_page"].get_total_without_tax().text)
    actual_tax = Formatter.remove_currency(pages["checkout_page"].get_tax().text)
    actual_total_price_with_tax = Formatter.remove_currency(pages["checkout_page"].get_total_with_tax().text)

    # Verify if the actual values are the same with the expected
    assert actual_payment_information == User.PAYMENT_INFORMATION, (
            actual_payment_information + Messages.payment_information_incorrect + User.PAYMENT_INFORMATION)
    assert actual_shipping_information == User.SHIPPING_INFORMATION, (
            actual_shipping_information + Messages.payment_information_incorrect + User.SHIPPING_INFORMATION)
    assert actual_total_price_without_tax == total_price_without_tax, str(
        actual_total_price_without_tax) + Messages.total_price_incorrect + str(total_price_without_tax)
    assert actual_tax == tax, str(actual_tax) + Messages.tax_incorrect + str(tax)
    assert actual_total_price_with_tax == total_price_with_tax, str(
        actual_total_price_with_tax) + Messages.total_price_incorrect + str(total_price_with_tax)


@pytest.mark.usefixtures("initialize_with_login")
class TestCheckout:

    def test_successful_checkout_single_item(self, pages):
        # Add an item to the cart
        product = add_single_item_to_cart(pages)
        name = product.get_random_item()["label"]
        price = product.get_random_item()["price"]
        description = product.get_random_item()["description"]

        # Input checkout information then proceed
        input_checkout_information(pages, User.FIRST_NAME, User.LAST_NAME, User.POSTAL_CODE)

        # Verify if the checkout overview page was displayed
        assert Title.CHECKOUT_OVERVIEW in pages["checkout_page"].get_checkout_page_title().text, (
            Messages.checkout_overview_title_not_displayed)

        # Verify if the item's label and price in the cart are correct
        found = False
        all_prices = []
        for cart_item in pages["checkout_page"].get_checkout_items_information():
            if cart_item["label"] == name:
                found = True
                actual_label = cart_item["label"]
                actual_price = cart_item["price"]
                actual_description = cart_item["description"]
                all_prices.append(actual_price)
                assert name == actual_label, actual_label + Messages.product_name_incorrect + name
                assert price == actual_price, str(actual_price) + Messages.price_incorrect + str(price)
                assert description == actual_description, actual_description + Messages.description_incorrect + description

        if found and len(all_prices) > 0:
            # Verify if the general information and total price are correct
            verify_information_and_prices(pages, all_prices)

        else:
            # If the script reaches this, it means that the item was not in the cart
            message = name + Messages.item_not_in_cart
            Logger.get_logger().error(message)
            raise SystemExit(message)

    def test_successful_checkout_multiple_items(self, pages):
        # Add all test items in the cart then verify if the cart page was loaded successfully
        items = Product.items
        for item in items:
            pages["products_page"].get_add_to_cart_button(item["label"]).click()
        pages["products_page"].get_cart_link().click()
        assert Title.CART in pages["cart_page"].get_cart_page_title().text, Messages.cart_title_not_displayed

        # Go to checkout page then verify if the checkout page was displayed
        pages["cart_page"].get_checkout_button().click()
        assert Title.CHECKOUT_YOUR_INFORMATION in pages["checkout_page"].get_checkout_page_title().text, (
            Messages.checkout_information_title_not_displayed)

        # Input checkout information then proceed
        input_checkout_information(pages, User.FIRST_NAME, User.LAST_NAME, User.POSTAL_CODE)

        # Verify if the checkout overview page was displayed
        assert Title.CHECKOUT_OVERVIEW in pages["checkout_page"].get_checkout_page_title().text, (
            Messages.checkout_overview_title_not_displayed)

        # Verify if all the items' labels and prices in the cart are correct
        all_prices = []
        for item in items:
            found = False
            name = item["label"]
            price = item["price"]
            description = item["description"]
            for cart_item in pages["checkout_page"].get_checkout_items_information():
                if cart_item["label"] == name:
                    found = True
                    actual_label = cart_item["label"]
                    actual_price = cart_item["price"]
                    actual_description = cart_item["description"]
                    all_prices.append(actual_price)
                    assert name == actual_label, actual_label + Messages.product_name_incorrect + name
                    assert price == actual_price, str(actual_price) + Messages.price_incorrect + str(price)
                    assert description == actual_description, actual_description + Messages.description_incorrect + description
                    break
            if not found:
                # If the script reaches this, it means that the item was not in the cart
                message = name + Messages.item_not_in_cart
                Logger.get_logger().error(message)
                raise SystemExit(message)

        if len(all_prices) > 0:
            # Verify if the general information and total price are correct
            verify_information_and_prices(pages, all_prices)

    def test_failed_checkout_no_firstname(self, pages):
        # Add an item to the cart
        add_single_item_to_cart(pages)

        # Input checkout information then proceed
        input_checkout_information(pages, "", User.LAST_NAME, User.POSTAL_CODE)

        # Verify if the error message was displayed
        error = pages["checkout_page"].get_error_message().text
        assert Messages.firstname_required in error, Messages.firstname_required_not_displayed
        Logger.get_logger().info(Messages.error_is_displayed + error)

    def test_failed_checkout_no_lastname(self, pages):
        # Add an item to the cart
        add_single_item_to_cart(pages)

        # Input checkout information then proceed
        input_checkout_information(pages, User.FIRST_NAME, "", User.POSTAL_CODE)

        # Verify if the error message was displayed
        error = pages["checkout_page"].get_error_message().text
        assert Messages.lastname_required in error, Messages.lastname_required_not_displayed
        Logger.get_logger().info(Messages.error_is_displayed + error)

    def test_failed_checkout_no_zip_code(self, pages):
        # Add an item to the cart
        add_single_item_to_cart(pages)

        # Input checkout information then proceed
        input_checkout_information(pages, User.FIRST_NAME, User.LAST_NAME, "")

        # Verify if the error message was displayed
        error = pages["checkout_page"].get_error_message().text
        assert Messages.postalcode_required in error, Messages.postal_required_not_displayed
        Logger.get_logger().info(Messages.error_is_displayed + error)
