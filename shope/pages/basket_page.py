from .base_page import BasePage
from .locators import BasketPageLocators, MainPageLocators


class BasketPage(BasePage):
    def go_to_login_page(self):
        login_link = self.browser.find_element(*MainPageLocators.BASKET_TRANSFER)
        login_link.click()

    def should_be_basket_clear(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_CLEAN), \
            "Нет сообщения, что корзина пуста"

    def should_not_products(self):
        assert self.is_not_element_present(*BasketPageLocators.PRODUCT_IN_BASKET), \
            "Сообщение об успешном завершении отображается, но не должно быть"
