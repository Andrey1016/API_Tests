from pages.base_page import BasePage
from selenium.webdriver.common.by import By

add_click = (By.XPATH, "//span[text()='Add'][1]")
create_folder = (By.XPATH, "//span[text()='Create Folder']")
create_certifications = (By.XPATH, "//span[text()='Create Certification']")
click_delete = (By.XPATH, "(//a[@data-qtip='Delete'])[1]")
certifications_name = (By.XPATH, "(//span[text()='Test Certification'])[1]")
certifications_folder_name = (By.XPATH, "(//span[text()='AutoTest Certifications Folder'])[1]")


class UsersCertifications(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    @property
    def add_click(self):
        return self.find(add_click).click

    @property
    def create_folder(self):
        return self.find(create_folder).click

    @property
    def create_certifications(self):
        return self.find(create_certifications).click

    @property
    def certifications_name(self):
        return self.find(certifications_name).click

    @property
    def delete_title(self):
        return self.find(click_delete).click

    def assert_certifications_folder(self):
        title = self.find(certifications_folder_name)
        assert title.is_displayed(), "AutoTest Certifications Folder"
        expected_text = "AutoTest Certifications Folder"
        assert title.text == expected_text, f"Expected: {expected_text}, Actual: {title.text}"

    def assert_certifications(self):
        title = self.find(certifications_name)
        assert title.is_displayed(), "Test Certification"
        expected_text = "Test Certification"
        assert title.text == expected_text, f"Expected: {expected_text}, Actual: {title.text}"
