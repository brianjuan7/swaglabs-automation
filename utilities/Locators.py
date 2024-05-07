from selenium.webdriver.common.by import By


class NavigationMenuLocators:
    swag_labs_title = (By.CLASS_NAME, "app_logo")


class LoginPageLocators:
    username_input = (By.ID, "user-name")
    password_input = (By.ID, "password")
    login_button = (By.ID, "login-button")
    error_message = (By.XPATH, "//div[@class='error-message-container error']/h3")


class ProductsPageLocators:
    products_page_title = (By.CLASS_NAME, "title")
    cart_link = (By.CLASS_NAME, "shopping_cart_link")
    back_to_products_button = (By.ID, "back-to-products")
    sort_dropdown = (By.CLASS_NAME, "product_sort_container")
    sort_options = (By.TAG_NAME, "option")
    products_list = (By.CLASS_NAME, "inventory_list")
    product_item = (By.XPATH, "//div[@class='inventory_item']")
    product_label = (By.XPATH, ".//div[@class='inventory_item_description']/div[@class='inventory_item_label']/a/div")
    product_price = (By.XPATH, ".//div[@class='inventory_item_description']/div[@class='pricebar']/"
                               "div[@class='inventory_item_price']")
    add_to_cart_button = (By.XPATH, ".//div[@class='inventory_item_description']/div[@class='pricebar']/button")
    detailed_product_name = (By.XPATH, "//div[contains(@class, 'inventory_details_name')]")
    detailed_product_description = (By.XPATH, "//div[@class='inventory_details_desc_container']/"
                                              "div[contains(@class, 'inventory_details_desc')]")
    detailed_product_price = (By.CLASS_NAME, "inventory_details_price")


class CartPageLocators:
    cart_page_title = (By.CLASS_NAME, "title")
    cart_item = (By.CLASS_NAME, "cart_item")
    cart_item_label = (By.XPATH, ".//div[@class='cart_item_label']/a/div[@class='inventory_item_name']")
    cart_item_price = (By.XPATH, ".//div[@class='cart_item_label']/div[@class='item_pricebar']/"
                                 "div[@class='inventory_item_price']")
    remove_item_button = (By.XPATH, ".//div[@class='cart_item_label']/div[@class='item_pricebar']/button")
    checkout_button = (By.ID, "checkout")


class CheckoutPageLocators:
    checkout_page_title = (By.CLASS_NAME, "title")
    first_name_input = (By.ID, "first-name")
    last_name_input = (By.ID, "last-name")
    postal_input = (By.ID, "postal-code")
    continue_button = (By.ID, "continue")
    error_message = (By.XPATH, "//div[contains(@class, 'error-message-container')]")
    checkout_cart_item = (By.CLASS_NAME, "cart_item")
    checkout_cart_item_label = (By.XPATH, ".//div[@class='cart_item_label']/a/div[@class='inventory_item_name']")
    checkout_cart_item_price = (By.XPATH, ".//div[@class='cart_item_label']/div[@class='item_pricebar']/"
                                          "div[@class='inventory_item_price']")
    checkout_cart_item_description = (By.XPATH, ".//div[@class='cart_item_label']/div[@class='inventory_item_desc']")
    payment_information = (By.XPATH, "//div[@data-test='payment-info-value']")
    shipping_information = (By.XPATH, "//div[@data-test='shipping-info-value']")
    total_without_tax_label = (By.CLASS_NAME, "summary_subtotal_label")
    total_with_tax_label = (By.CLASS_NAME, "summary_total_label")
    tax_label = (By.CLASS_NAME, "summary_tax_label")

