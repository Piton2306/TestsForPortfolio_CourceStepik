import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import random


# pytest -v -s --browser_name=chrome test.py
# pytest -v -s --language=en test.py
def pytest_addoption(parser):
    """Добавляет параметр --browser_name для выбора браузера"""
    parser.addoption('--browser_name', action='store', default='chrome',
                     help="Choose browser:chrome or firefox")

    # Добавляет параметр --language для выбора языка
    parser.addoption('--language', action='store', default='en',
                     help="Choose language")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    user_language = request.config.getoption("language")

    if browser_name == "chrome":
        print("\nStart browser Chrome for test..")
        print(f"\nlanguage browser {user_language}")
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        print("\nStart browser Firefox for test..")
        print(f"\nlanguage browser {user_language}")
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", user_language)
        browser = webdriver.Firefox(firefox_profile=fp)
    else:
        raise pytest.UsageError("--browse_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()
