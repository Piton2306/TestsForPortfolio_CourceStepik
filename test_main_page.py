from pages.main_page import MainPage
from pages.login_page import LoginPage
import time


def test_guest_can_go_to_login_page(browser):
    """Открытие окна регистрации"""
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    time.sleep(2)


def test_guest_should_see_login_link(browser):
    """Проверка наличия элемента"""
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_form_login_register_url(browser):
    """Проверка форм регистрации и url"""
    link = "http://selenium1py.pythonanywhere.com/accounts/login/"
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_page()