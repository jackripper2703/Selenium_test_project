from .base_page import BasePage
from .locators import LoginPageLocators
import time


class LoginPage(BasePage):
    email = str(time.time()) + "@fakemail.org"

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert self.availability_in_link("login"), "Подстроки 'login' нет в текущем url браузера"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Форма логина отсутствует"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Форма регистрации отсутствует"

    def register_new_user(self):
        password = 'ReGiStErPaSsWoRd'
        email = str(time.time()) + "@fakemail.org"
        self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL).send_keys(email)
        self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD1).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD2).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTER).click()

