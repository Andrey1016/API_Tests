from pages.base_page import BasePage
from selenium.webdriver.common.by import By

name = (By.XPATH, "//input[@name='name']")
save = (By.XPATH, '//span[text()="Save"]')
create_title = (By.XPATH, "//span[text()='Create Title']")


class CreateUserTitle(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def name(self):
        self.find(name).send_keys('Test Title')

    @property
    def save(self):
        return self.find(save).click
