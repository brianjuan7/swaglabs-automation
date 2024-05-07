import pytest

from data.Application import Title, Messages, Sort
from data.Product import Product
from utilities import Logger, Formatter


@pytest.mark.usefixtures("initialize_with_login")
class TestProduct:

    def test_successful_detailed_product_viewing(self, pages):
        # Select an item from the test data
        product = Product()
        name = product.get_random_item()["label"]
        description = product.get_random_item()["description"]
        price = product.get_random_item()["price"]
        pages["products_page"].get_a_product_label(name).click()

        # Verify if the detailed product page was loaded successfully
        assert Title.BACK_TO_PRODUCT in pages["products_page"].get_back_to_products_button().text, (
            Messages.detailed_title_not_displayed)

        # Verify that the product details are correct
        actual_name = pages["products_page"].get_detailed_product_name().text
        actual_description = pages["products_page"].get_detailed_product_description().text
        actual_price = Formatter.remove_currency(pages["products_page"].get_detailed_product_price().text)
        assert actual_name == name, actual_name + Messages.product_name_incorrect + name
        assert actual_description == description, actual_description + Messages.description_incorrect + description
        assert actual_price == price, str(actual_price) + Messages.price_incorrect + str(price)

    def test_successful_product_sort_by_name_asc(self, pages):
        # Select the product sorting mode
        pages["products_page"].get_sort_dropdown().click()
        pages["products_page"].select_sort(Sort.NAME_ASCENDING).click()

        # Verify if the products were sorted based on the selected mode
        expected_products_list = pages["products_page"].get_product_labels()
        expected_products_list.sort()
        actual_products_list = pages["products_page"].get_product_labels()
        assert actual_products_list == expected_products_list, Messages.product_sort_incorrect
        Logger.get_logger().info(Messages.product_successfully_sorted + Sort.NAME_ASCENDING)

    def test_successful_product_sort_by_name_desc(self, pages):
        # Select the product sorting mode
        pages["products_page"].get_sort_dropdown().click()
        pages["products_page"].select_sort(Sort.NAME_DESCENDING).click()

        # Verify if the products were sorted based on the selected mode
        expected_products_list = pages["products_page"].get_product_labels()
        expected_products_list.sort(reverse=True)
        actual_products_list = pages["products_page"].get_product_labels()
        assert actual_products_list == expected_products_list, Messages.product_sort_incorrect
        Logger.get_logger().info(Messages.product_successfully_sorted + Sort.NAME_DESCENDING)

    def test_successful_product_sort_by_price_asc(self, pages):
        # Select the product sorting mode
        pages["products_page"].get_sort_dropdown().click()
        pages["products_page"].select_sort(Sort.PRICE_ASCENDING).click()

        # Verify if the products were sorted based on the selected mode
        expected_products_list = pages["products_page"].get_product_prices()
        expected_products_list.sort()
        actual_products_list = pages["products_page"].get_product_prices()
        assert actual_products_list == expected_products_list, Messages.product_sort_incorrect
        Logger.get_logger().info(Messages.product_successfully_sorted + Sort.PRICE_ASCENDING)

    def test_successful_product_sort_by_price_desc(self, pages):
        # Select the product sorting mode
        pages["products_page"].get_sort_dropdown().click()
        pages["products_page"].select_sort(Sort.PRICE_DESCENDING).click()

        # Verify if the products were sorted based on the selected mode
        expected_products_list = pages["products_page"].get_product_prices()
        expected_products_list.sort(reverse=True)
        actual_products_list = pages["products_page"].get_product_prices()
        assert actual_products_list == expected_products_list, Messages.product_sort_incorrect
        Logger.get_logger().info(Messages.product_successfully_sorted + Sort.PRICE_DESCENDING)
