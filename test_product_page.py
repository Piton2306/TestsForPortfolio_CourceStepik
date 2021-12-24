from pages.product_page import BasketPage
from time import sleep
import pytest


def test_guest_can_add_product_to_basket(browser):
    """Добаление продукта с выводом Alert"""
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = BasketPage(browser, link)
    page.open()
    page.add_name_price_message()
    sleep(5)


@pytest.mark.parametrize('link', [
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
    pytest.param(
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
        marks=pytest.mark.xfail),  # ожидаем падение теста
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9",
])
def test_guest_can_add_product_to_basket_new_product(browser, link):
    """Добаления товара на разных страницах проврка цены, имени в корзине и сообщение об успешном довавлении"""
    page = BasketPage(browser, link)
    page.open()
    page.add_name_price_message()
