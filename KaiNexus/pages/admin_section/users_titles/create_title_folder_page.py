from pages.base_page import BasePage
from selenium.webdriver.common.by import By
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as es
from pages.login_page import LoginPage

name = (By.XPATH, "//input[@name='name']")
save = (By.XPATH, '//span[text()="Save"]')
create_title = (By.XPATH, "//span[text()='Create Title']")


class CreateUserTitleFolder(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def name(self):
        self.find(name).send_keys('AutoTest Title Folder')

    @property
    def save(self):
        return self.find(save).click



