from pages.product_page import BasketPage
import pytest
from time import sleep


def test_guest_can_add_product_to_basket(browser):
    """Добаление продукта с выводом Alert"""
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = BasketPage(browser, link)
    page.open()
    page.add_name_price_message()
    # sleep(10)


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
    # sleep(10)


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    """Добавляет товар и проверяет что сообщение об успешном добавлении не появится"""
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
    page = BasketPage(browser, link)
    page.open()
    page.go_to_add_basket()
    page.should_not_be_message_is_not()


def test_guest_cant_see_success_message(browser):
    """проверяет что сообщение об успешном добавлении не появится"""
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
    page = BasketPage(browser, link)
    page.open()
    page.should_not_be_message_is_not()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    """Добавляет товар и проверяет что сообщение об успешном добавлении исчезнет за заданное время"""
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
    page = BasketPage(browser, link)
    page.open()
    page.go_to_add_basket()
    page.should_not_be_message_is_disappeared()


def test_guest_should_see_login_link_on_product_page(browser):
    """Проверка есть ли элемент 'Войти или зарегистрироваться'"""
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = BasketPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser):
    """Проверка есть ли элемент 'Войти или зарегистрироваться' и войти"""
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = BasketPage(browser, link)
    page.open()
    page.should_be_login_link()
    page.go_to_login_page()
