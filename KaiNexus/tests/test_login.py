import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as es
from pages.login_page import LoginPage


@pytest.mark.usefixtures("browser")
def test_login(browser):
    login_page = LoginPage(browser)
    login_page.open()
    login_page.username()
    login_page.password()
    login_page.sign_in()
    expected_url = 'https://test2.kainexus.com/#b'
    WebDriverWait(browser, 5).until(es.url_to_be(expected_url))


def test_login_wrong_username(browser):
    login_page = LoginPage(browser)
    login_page.open()
    login_page.username_wrong()
    login_page.password()
    login_page.sign_in()
    assert 'Invalid username or password.' == browser.find_element(By.XPATH,
                                                                   "//span[text()='Invalid username or password.']").text


def test_login_wrong_password(browser):
    login_page = LoginPage(browser)
    login_page.open()
    login_page.username()
    login_page.password_wrong()
    login_page.sign_in()
    assert 'Invalid username or password.' == browser.find_element(By.XPATH,
                                                                   "//span[text()='Invalid username or password.']").text


def test_need_help(browser):
    login_page = LoginPage(browser)
    login_page.open()
    login_page.need_help()





