from .pages.product_page import ProductPage


def test_product_add_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket_form()
    page.solve_quiz_and_get_code()
    page.should_be_add_to_basket_message()
    page.should_be_price_product_equals_price_basket()
