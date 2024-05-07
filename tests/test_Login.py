import pytest

from data import User
from data.Application import Messages, Title
from utilities import Logger


@pytest.mark.usefixtures("initialize")
class TestLogin:

    def test_successful_login(self, pages):
        # Input username and password
        pages["login_page"].get_username_input().send_keys(User.get_username())
        pages["login_page"].get_password_input().send_keys(User.get_password())
        pages["login_page"].get_submit_button().click()

        # Verify if login is successful
        assert Title.MAIN in pages["navigation_menu"].get_swag_labs_title().text, Messages.main_title_not_displayed
        assert Title.PRODUCTS in pages["products_page"].get_page_title().text, Messages.product_title_not_displayed
        Logger.get_logger().info(Messages.successfully_logged_in)

    def test_failed_login_invalid_credentials(self, pages):
        # Input username and password
        pages["login_page"].get_username_input().send_keys(User.INVALID_USERNAME)
        pages["login_page"].get_password_input().send_keys(User.INVALID_PASSWORD)
        pages["login_page"].get_submit_button().click()

        # Verify if the error message was displayed
        error = pages["login_page"].get_error_message().text
        assert Messages.credential_not_found in error, Messages.invalid_user_not_displayed
        Logger.get_logger().info(Messages.error_is_displayed + error)

    def test_failed_login_no_username(self, pages):
        # Input username and password
        pages["login_page"].get_username_input().send_keys("")
        pages["login_page"].get_password_input().send_keys(User.get_password())
        pages["login_page"].get_submit_button().click()

        # Verify if the error message was displayed
        error = pages["login_page"].get_error_message().text
        assert Messages.username_required in error, Messages.username_required_not_displayed
        Logger.get_logger().info(Messages.error_is_displayed + error)

    def test_failed_login_no_password(self, pages):
        # Input username and password
        pages["login_page"].get_username_input().send_keys(User.get_username())
        pages["login_page"].get_password_input().send_keys("")
        pages["login_page"].get_submit_button().click()

        # Verify if the error message was displayed
        error = pages["login_page"].get_error_message().text
        assert Messages.password_required in error, Messages.password_required_not_displayed
        Logger.get_logger().info(Messages.error_is_displayed + error)