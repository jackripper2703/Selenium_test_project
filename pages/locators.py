from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "[id='login_link']")


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
