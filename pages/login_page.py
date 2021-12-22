from pages.base_page import BasePage
from pages.locators import LoginPageLocators


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
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM),\
            "Формы login не существует"

    def should_be_register_form(self):
        """Проверка, что есть форма регистрации на странице"""
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM),\
            "Формы register не существует"
