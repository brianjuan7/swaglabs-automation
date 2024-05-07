import pytest

from data.Application import Title, Messages
from data.Product import Product
from utilities import Logger


@pytest.mark.usefixtures("initialize_with_login")
class TestCart:

    def test_successful_add_single_item_to_cart(self, pages):
        # Select an item from the test data
        product = Product()
        name = product.get_random_item()["label"]
        price = product.get_random_item()["price"]

        # Add the item in the cart
        pages["products_page"].get_add_to_cart_button(name).click()
        pages["products_page"].get_cart_link().click()

        # Verify if the cart page was loaded successfully
        assert Title.CART in pages["cart_page"].get_cart_page_title().text, Messages.cart_title_not_displayed

        # Verify if the item's label and price in the cart are correct
        for cart_item in pages["cart_page"].get_cart_labels_and_prices():
            if cart_item["label"] == name:
                actual_label = cart_item["label"]
                actual_price = cart_item["price"]
                assert name == actual_label, actual_label + Messages.product_name_incorrect + name
                assert price == actual_price, str(actual_price) + Messages.price_incorrect + str(price)
                return

        # If the script reaches this, it means that the item was not in the cart
        message = name + Messages.item_not_in_cart
        Logger.get_logger().error(message)
        raise SystemExit(message)

    def test_successful_add_multiple_items_to_cart(self, pages):
        # Add all test items in the cart
        items = Product.items
        for item in items:
            pages["products_page"].get_add_to_cart_button(item["label"]).click()
        pages["products_page"].get_cart_link().click()

        # Verify if the cart page was loaded successfully
        assert Title.CART in pages["cart_page"].get_cart_page_title().text, Messages.cart_title_not_displayed

        # Verify if all the items' labels and prices in the cart are correct
        for item in items:
            found = False
            name = item["label"]
            price = item["price"]
            for cart_item in pages["cart_page"].get_cart_labels_and_prices():
                if cart_item["label"] == name:
                    found = True
                    actual_label = cart_item["label"]
                    actual_price = cart_item["price"]
                    assert name == actual_label, actual_label + Messages.product_name_incorrect + name
                    assert price == actual_price, str(actual_price) + Messages.price_incorrect + str(price)
                    break
            if not found:
                # If the script reaches this, it means that the item was not in the cart
                message = name + Messages.item_not_in_cart
                Logger.get_logger().error(message)
                raise SystemExit(message)

    def test_successful_remove_an_item_in_cart(self, pages):
        # Select an item from the test data
        product = Product()
        name = product.get_random_item()["label"]

        # Add the item in the cart
        pages["products_page"].get_add_to_cart_button(name).click()
        pages["products_page"].get_cart_link().click()

        # Verify if the cart page was loaded successfully
        assert Title.CART in pages["cart_page"].get_cart_page_title().text, Messages.cart_title_not_displayed

        # Remove the item from the cart
        pages["cart_page"].get_remove_item_button(name).click()

        # Verify that the cart is empty after removing the item
        assert len(pages["cart_page"].get_cart_labels_and_prices()) == 0, name + Messages.item_not_removed_in_cart

    def test_successful_remove_all_items_in_cart(self, pages):
        # Add all test items in the cart
        items = Product.items
        for item in items:
            pages["products_page"].get_add_to_cart_button(item["label"]).click()
        pages["products_page"].get_cart_link().click()

        # Verify if the cart page was loaded successfully
        assert Title.CART in pages["cart_page"].get_cart_page_title().text, Messages.cart_title_not_displayed

        # Remove all items from the cart
        for item in items:
            pages["cart_page"].get_remove_item_button(item["label"]).click()

        # Verify that the cart is empty after removing all items
        assert len(pages["cart_page"].get_cart_labels_and_prices()) == 0, Messages.cart_not_empty
