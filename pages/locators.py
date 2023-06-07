from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "[id='login_link']")
    BASKET_TRANSFER = (By.CSS_SELECTOR, ".icon-signin")


class BasePageLocators:
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
    LOGIN_LINK = (By.CSS_SELECTOR, "[id='login_link']")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "[id='login_link']")


class LoginPageLocators:

    LOGIN_FORM = (By.CSS_SELECTOR, '[id="login_form"]')
    REGISTER_FORM = (By.CSS_SELECTOR, '[id="register_form"]')

    LOGIN_EMAIL = (By.CSS_SELECTOR, "[id='id_login-username']")
    REGISTER_EMAIL = (By.CSS_SELECTOR, "[id='id_registration-email']")

    LOGIN_PASSWORD = (By.CSS_SELECTOR, "[id='id_login-password']")
    REGISTER_PASSWORD1 = (By.CSS_SELECTOR, "[id='id_registration-password1']")
    REGISTER_PASSWORD2 = (By.CSS_SELECTOR, "[id='id_registration-password2']")

    LOGIN = (By.CSS_SELECTOR, "[value='Log In']")
    REGISTER = (By.CSS_SELECTOR, "[value='Register']")


class ProductPageLocators:

    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main h1+p")

    ADD_TO_BASKET = (By.CSS_SELECTOR, "button[type='submit'].btn-add-to-basket")

    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages .alert:nth-last-child(3) strong")
    ALERT_PRODUCT_PRICE = (By.CSS_SELECTOR, "#messages .alert:nth-last-child(1) strong")


class BasketPageLocators:
    BASKET_CLEAN = (By.CSS_SELECTOR, "#content_inner p")
    PRODUCT_IN_BASKET = (By.CSS_SELECTOR, ".basket-items")
