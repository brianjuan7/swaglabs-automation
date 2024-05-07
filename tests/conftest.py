import time
import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from data import User
from data.Application import URL
from pages.CartPage import CartPage
from pages.CheckoutPage import CheckoutPage
from pages.LoginPage import LoginPage
from pages.NavigationMenu import NavigationMenu
from pages.ProductPage import ProductsPage
from utilities import Logger


global_driver = None


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")


def initialize_driver(request):
    # Select the appropriate browser based on the command line input
    browser = request.config.getoption("browser")
    if browser == "chrome":
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        pass
    elif browser == "firefox":
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        pass
    elif browser == "edge":
        driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
        pass
    else:
        message = f"Test terminated. Invalid browser: {browser}"
        Logger.get_logger().error(message)
        raise SystemExit(message)

    # Initialize the driver
    driver.get(URL.MAIN)
    driver.maximize_window()
    return driver


@pytest.fixture(scope="function")
def initialize(request):
    # Initialize the driver without logging in
    global global_driver
    global_driver = initialize_driver(request)

    # Cleanup
    yield
    time.sleep(3)
    if global_driver is not None:
        global_driver.quit()


@pytest.fixture(scope="function")
def initialize_with_login(request):
    # Initialize the driver with logging in
    global global_driver
    global_driver = initialize_driver(request)
    login_page = LoginPage(global_driver)
    product_page = ProductsPage(global_driver)
    navigation_menu = NavigationMenu(global_driver)

    # Perform login
    login_page.get_username_input().send_keys(User.get_username())
    login_page.get_password_input().send_keys(User.get_password())
    login_page.get_submit_button().click()
    assert "Swag Labs" in navigation_menu.get_swag_labs_title().text, "Swag Labs title was not displayed"
    assert "Products" in product_page.get_page_title().text, "Products title was not displayed"
    Logger.get_logger().info("User successfully logged in.")

    # Cleanup
    yield
    time.sleep(3)
    if global_driver is not None:
        global_driver.quit()


@pytest.fixture
def pages():
    pages = {"navigation_menu": NavigationMenu(global_driver),
             "login_page": LoginPage(global_driver),
             "products_page": ProductsPage(global_driver),
             "cart_page": CartPage(global_driver),
             "checkout_page": CheckoutPage(global_driver)}
    return pages
