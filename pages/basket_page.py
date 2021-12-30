from pages.base_page import BasePage
from pages.locators import BasketPageLocators


class BasketPage(BasePage):
    def should_not_be_view_basket(self):
        """Проверка отсутствия элемента о пустой корзине"""
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), "Корзина не пуста"

    def should_be_message_basket(self):
        """Проверка сообщения о пустой корзине"""
        message = self.browser.find_element(*BasketPageLocators.BASKET_IS_EMPTY_MESSAGE).text
        assert 'Your basket is empty' in message, "Сообщение не соответствует пустой корзине"
