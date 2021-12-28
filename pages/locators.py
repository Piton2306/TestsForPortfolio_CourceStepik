from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")  # На страницу регистрации
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators:
    ADD_TO_BASKET = (By.CSS_SELECTOR, "#add_to_basket_form")
    NAME_PRODUCT = (By.CSS_SELECTOR, ".product_main h1")
    PRICE_PRODUCT = (By.CSS_SELECTOR, ".product_main p.price_color")
    PRICE_PRODUCT_BASKET = (By.CSS_SELECTOR, ".alert-info .alertinner strong")
    NAME_PRODUCT_BASKET = (By.CSS_SELECTOR, "#messages .alertinner strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages .alertinner")
