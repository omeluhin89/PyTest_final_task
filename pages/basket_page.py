from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_empty_basket(self):
        assert self.is_disappeared(*BasketPageLocators.PRODUCT_CARD), "Basket is not empty"

    def should_be_message(self):
        assert "Your basket is empty." in self.browser.find_element(*BasketPageLocators.BASKET_EMPTY_MESSAGE).text,\
            "Message text is wrong"
