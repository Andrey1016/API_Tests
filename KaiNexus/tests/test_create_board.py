import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as es


from pages import boards_page
from pages.login_page import LoginPage
from pages.boards_page import BasePage


@pytest.mark.usefixtures("browser")
def test_login(browser):
    login_page = LoginPage(browser)
    login_page.open()
    login_page.username()
    login_page.password()
    login_page.sign_in()
    boards_page.headers_boards_click()
