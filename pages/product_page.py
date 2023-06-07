from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def collection(self):
        self.go_to_product_page()
        self.solve_quiz_and_get_code()
        # self.should_be_url()
        self.msg_cost_of_the_basket()
        self.msg_product_added()

    def go_to_product_page(self):
        add_to_basket = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        add_to_basket.click()

    def should_be_url(self):
        assert self.availability_in_link("?promo=newYear"), \
            "Подстроки '?promo=newYear' нет в текущем url браузера"

    def msg_cost_of_the_basket(self):
        assert self.comparison(self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE),
                               self.browser.find_element(*ProductPageLocators.ALERT_PRODUCT_PRICE)),\
            "Цена в корзине отличается от цены товара"

    def msg_product_added(self):
        assert self.comparison(self.browser.find_element(*ProductPageLocators.PRODUCT_NAME),
                               self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE)), \
            "Название товара добавленного в корзину отличается от выбранного товара"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Сообщение об успешном завершении отображается, но не должно быть"

    def should_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Сообщение об исчезновения элемента, но не должно быть"
