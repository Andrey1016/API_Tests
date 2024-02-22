from pages.base_page import BasePage
from selenium.webdriver.common.by import By

add_click = (By.XPATH, "//span[text()='Add'][1]")
create_folder = (By.XPATH, "//span[text()='Create Folder']")
create_EmpStatus = (By.XPATH, "//span[text()='Create Employment Status']")
click_delete = (By.XPATH, "(//a[@data-qtip='Delete'])[1]")
empStatus_name = (By.XPATH, "//span[text()='Test Emp Status']")
empStatus_folder_name = (By.XPATH, "(//span[text()='AutoTest empStatus Folder'])[1]")


class UsersEmpStatus(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    @property
    def add_click(self):
        return self.find(add_click).click

    @property
    def create_folder(self):
        return self.find(create_folder).click

    @property
    def create_EmpStatus(self):
        return self.find(create_EmpStatus).click

    @property
    def empStatus_name(self):
        return self.find(empStatus_name).click

    @property
    def delete_title(self):
        return self.find(click_delete).click

    def assert_empStatus_folder(self):
        title = self.find(empStatus_folder_name)
        assert title.is_displayed(), "AutoTest empStatus Folder"
        expected_text = "AutoTest empStatus Folder"
        assert title.text == expected_text, f"Expected: {expected_text}, Actual: {title.text}"

    def assert_empStatus(self):
        title = self.find(empStatus_name)
        assert title.is_displayed(), "Test EmpStatus"
        expected_text = "TestEmp Status"
        assert title.text == expected_text, f"Expected: {expected_text}, Actual: {title.text}"
