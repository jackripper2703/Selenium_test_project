import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default="en",
                     help="Choose language: '--language=en' or '--language=ru'")
    parser.addoption('--browser', action='store', default="Chrome",
                     help="Choose browser: chrome or firefox")


@pytest.fixture()
def browser(request):
    user_language = request.config.getoption("language")
    browser = request.config.getoption("browser")
    if browser == "Chrome":
        options = webdriver.ChromeOptions()
        # options.add_argument("--headless")
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option('useAutomationExtension', False)
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        browser = webdriver.Chrome(options=options)
    elif browser == "Firefox":
        fp = webdriver.FirefoxOptions()
        fp.set_preference("intl.accept_languages", user_language)
        browser = webdriver.Firefox(options=fp)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    browser.quit()
