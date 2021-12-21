from pages.main_page import MainPage
import time


def test_guest_can_go_to_login_page(browser):
    """Открытие окна регистрации"""
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    time.sleep(3)


def test_guest_should_see_login_link(browser):
    """Проверка наличия элемента"""
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()
