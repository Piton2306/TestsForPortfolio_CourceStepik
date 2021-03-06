from pages.login_page import BasePage
from pages.locators import ProductPageLocators


class ProductPage(BasePage):
    def add_name_price_message(self):
        self.go_to_add_basket()
        self.price_prod_must_be_equal_price_basket()
        self.name_prod_must_be_equal_name_basket()

    def go_to_add_basket(self):
        """Нажатие на кнопку "Добавить в корзину"""
        add_basket = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        add_basket.click()
        self.solve_quiz_and_get_code()

    def price_prod_must_be_equal_price_basket(self):
        """Проверка цены продукта и цены в корзине"""
        self.is_element_present(*ProductPageLocators.PRICE_PRODUCT_BASKET)
        price = self.browser.find_element(*ProductPageLocators.PRICE_PRODUCT).text
        price_basket = self.browser.find_element(*ProductPageLocators.PRICE_PRODUCT_BASKET).text
        assert price == price_basket, \
            "Цена в корзине не соответствует цене товара"

    def name_prod_must_be_equal_name_basket(self):
        """Проверка имени товара после добавления в корзину"""
        self.is_element_present(*ProductPageLocators.NAME_PRODUCT_BASKET)
        name = self.browser.find_element(*ProductPageLocators.NAME_PRODUCT).text
        name_basket = self.browser.find_element(*ProductPageLocators.NAME_PRODUCT_BASKET).text
        assert name == name_basket, \
            "Название товара несоответствует названию в корзине"

    def should_not_be_message_is_not(self):
        """Проверяет что сообщения об успешном добавлении не появится"""
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_not_be_message_is_disappeared(self):
        """Проверяет что сообщения об успешном добавлении не исчезнет"""
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"
