from pages.base_page import BasePage
from selenium.webdriver.common.by import By

name = (By.XPATH, "//input[@name='name']")
save = (By.XPATH, '//span[text()="Save"]')
create_empStatus = (By.XPATH, "//span[text()='AutoTest Certifications Folder']")


class CreateUserCertificationsFolder(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def name(self):
        self.find(name).send_keys('AutoTest Certifications Folder')

    @property
    def save(self):
        return self.find(save).click
