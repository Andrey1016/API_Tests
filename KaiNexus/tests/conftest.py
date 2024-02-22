from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest


@pytest.fixture
def browser(request):
    chrome_browser = webdriver.Chrome()
    chrome_browser.implicitly_wait(10)
    chrome_browser.maximize_window()
    return chrome_browser
    # request.cls.driver = browser
    # yield
    chrome_browser.close()

@pytest.fixture
def browser_quit():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()
