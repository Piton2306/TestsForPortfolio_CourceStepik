from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class MainPage(BasePage):
    def go_to_login_page(self):
        """Нажатие на кнопку "Войти или зарегистрироваться"""
        login_link = self.browser.find_element(By.CSS_SELECTOR, "#login_link")
        login_link.click()

    def should_be_login_link(self):
        """Проверка кнопки "Войти или зарегистрироваться"""
        self.browser.find_element(By.CSS_SELECTOR, "#login_link_invalid")
