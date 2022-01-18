from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_basket_form(self):
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        add_to_basket_button.click()

    def should_be_add_to_basket_message(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_MESSAGE), "Message is not presented"
        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME), "Product name is not presented"
        assert self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text in \
               self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_MESSAGE).text, "Product is wrong"

    def should_be_price_product_equals_price_basket(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_PRICE), "Product price is not presented"
        assert self.is_element_present(*ProductPageLocators.BASKET_PRICE), "Basket price is not presented"
        assert self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text == \
               self.browser.find_element(*ProductPageLocators.BASKET_PRICE).text, "Basket price is wrong"
