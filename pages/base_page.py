from selenium.common.exceptions import NoSuchElementException, \
    NoAlertPresentException, TimeoutException
from .locators import BasePageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
import time


class BasePage(BasePageLocators):
    def __init__(self, browser, url, timeout=3):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        """Открытие браузера"""
        self.browser.get(self.url)

    def is_element_present(self, how, what, timeout=10):
        """Проверяет, что элемент есть на странице"""
        try:
            WebDriverWait(self.browser, timeout).until(
                EC.visibility_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True

    def is_not_element_present(self, how, what, timeout=4):
        """Ожидает что элемент не появится на странице"""
        try:
            WebDriverWait(self.browser, timeout).until(
                EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False

    def is_disappeared(self, how, what, timeout=4):
        """Ожидает, что элемент исчезнет за заданное время"""
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException). \
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True

    def should_be_authorized_user(self):
        """Проверка, что пользователь залогинен"""
        assert self.is_element_present(*BasePageLocators.USER_ICON), "User icon is not presented," \
                                                                     " probably unauthorised user"

    def solve_quiz_and_get_code(self):
        """Вносит данные примера в алерт и проверяет что появился новый алерт"""
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            time.sleep(1)
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def go_to_login_page(self):
        """Нажатие на кнопку 'Войти или зарегистрироваться'"""
        login_link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        login_link.click()

    def should_be_login_link(self):
        """Проверка наличия кнопки 'Войти или зарегистрироваться'"""
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link не существует"

    def go_to_view_basket(self):
        """Переход в корзину"""
        view_basket = self.browser.find_element(*BasePageLocators.VIEW_BASKET)
        view_basket.click()
