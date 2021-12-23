from pages.login_page import BasePage
from pages.locators import BasketPageLocators
import time


class BasketPage(BasePage):
    def add_name_price_message(self):
        self.go_to_add_basket()
        self.price_prod_must_be_equal_price_basket()
        self.message_add_result_basket()

    def go_to_add_basket(self):
        """Нажатие на кнопку "Добавить в корзину"""
        add_basket = self.browser.find_element(*BasketPageLocators.ADD_TO_BASKET)
        add_basket.click()
        self.solve_quiz_and_get_code()

    def price_prod_must_be_equal_price_basket(self):
        """Проверка цены продукта и цены в корзине"""
        time.sleep(3)
        price = self.browser.find_element(*BasketPageLocators.PRICE_PRODUCT).text
        price_basket = self.browser.find_element(*BasketPageLocators.PRICE_PRODUCT_BASKET).text
        assert price == price_basket, \
            "Цена в корзине не соответсвует цене товара"

    def message_add_result_basket(self):
        """Проверка сообщения что данный товар добален"""
        name = self.browser.find_element(*BasketPageLocators.NAME_PRODUCT).text
        message = "has been added to your basket."
        message_basket = self.browser.find_element(*BasketPageLocators.MESSAGES_PRODUCT_BASKET).text
        assert f"{name} {message}" == f"{message_basket}", \
            "Сообщение об успешном добавлении не появилось"
