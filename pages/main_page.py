from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from pages.locators import MainPageLocators


class MainPage(BasePage):
    def go_to_login_page(self):
        """Нажатие на кнопку "Войти или зарегистрироваться"""
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()

    def should_be_login_link(self):
        """Проверка наличия кнопки "Войти или зарегистрироваться"""
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link не существует"
