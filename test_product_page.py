from pages.product_page import BasketPage
from time import sleep


def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = BasketPage(browser, link)
    page.open()
    page.add_name_price_message()
    sleep(5)
