from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class MainPage(BasePage):
    def go_to_login_page(self):
        """Нажатие на кнопку "Войти или зарегистрироваться"""
        login_link = self.browser.find_element(By.CSS_SELECTOR, "#login_link")
        login_link.click()

    def should_be_login_link(self):
        """Поиск наличи кнопки "Войти или зарегистрироваться"""
        assert self.is_element_present(By.CSS_SELECTOR, "#login_link"), "Login link is not presented"
