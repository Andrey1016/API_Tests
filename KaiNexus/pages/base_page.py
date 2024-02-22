from lib2to3.pgen2 import driver
import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains

from tests.conftest import browser


class BasePage:
    def __init__(self, browser):
        self.driver = driver
        self.browser = browser

    def find(self, args):
        return self.browser.find_element(*args)

    # def hover_over_title_name(self):
    #     title_name_selector = "your_css_selector_here"  # Replace with the actual CSS selector
    #     return self.hover_over_title_name(title_name_selector)


    # @pytest.fixture
    # def browser():
    #     driver = webdriver.Chrome()
    #     yield driver
    #     driver.quit()


@pytest.fixture
def api_credentials():
    return {'username': 'api', 'password': 'MjczLTVhYjZiYTFmLTYyNmItNDQxMS1iNjExLTYwY2M2Mzk4ZTc5Ng=='}
