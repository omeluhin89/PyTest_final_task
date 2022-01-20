from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    LOGIN_REGISTER = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators():
    ADD_TO_BASKET = (By.CSS_SELECTOR, '#add_to_basket_form button')
    ADD_TO_BASKET_MESSAGE = (By.CSS_SELECTOR, '#messages .alert:nth-child(1) .alertinner strong')
    BASKET_PRICE = (By.CSS_SELECTOR, '#messages .alert:nth-child(3) .alertinner strong')
    PRODUCT_PRICE = (By.CSS_SELECTOR, '#content_inner .product_main .price_color')
    PRODUCT_NAME = (By.CSS_SELECTOR, '#content_inner h1')


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_BUTTON = (By.CSS_SELECTOR, ".basket-mini a.btn")


class BasketPageLocators():
    BASKET_EMPTY_MESSAGE = (By.CSS_SELECTOR, "#content_inner p")
    PRODUCT_CARD = (By.CSS_SELECTOR, ".basket-items")
