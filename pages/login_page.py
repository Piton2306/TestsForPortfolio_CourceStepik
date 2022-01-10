from pages.base_page import BasePage
from pages.locators import LoginPageLocators
import time


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        """Проверка на корректный url адрес"""
        assert self.browser.current_url == "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/", \
            "Ссылка не соответсвует ссылке форм регистрации"

    def should_be_login_form(self):
        """Проверка, что есть форма логина"""
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), \
            "Формы login не существует"

    def should_be_register_form(self):
        """Проверка, что есть форма регистрации на странице"""
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), \
            "Формы register не существует"

    def register_new_user(self, email='', password=''):
        email = str(time.time()) + "@fakemail.org"
        password = "dfsdfdfssdf"
        input_email = self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL).send_keys(email)
        input_password1 = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD).send_keys(password)
        input_password2 = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD_CONFIRM).send_keys(password)
        button_click = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON).click()
