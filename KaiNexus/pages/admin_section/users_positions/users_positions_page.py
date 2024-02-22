from pages.base_page import BasePage
from selenium.webdriver.common.by import By

add_click = (By.XPATH, "//span[text()='Add'][1]")
create_folder = (By.XPATH, "//span[text()='Create Folder']")
create_title = (By.XPATH, "//span[text()='Create Position']")
click_delete = (By.XPATH, "(//a[@data-qtip='Delete'])[1]")
title_name = (By.XPATH, "//span[text()='Test Position']")
folder_name = (By.XPATH, "(//span[text()='AutoTest Position Folder'])[1]")


class UsersPositions(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    @property
    def add_click(self):
        return self.find(add_click).click

    @property
    def create_folder(self):
        return self.find(create_folder).click

    @property
    def create_title(self):
        return self.find(create_title).click

    @property
    def title_name(self):
        return self.find(title_name).click

    @property
    def delete_position(self):
        return self.find(click_delete).click

    def assert_position_folder(self):
        title = self.find(folder_name)
        assert title.is_displayed(), "AutoTest Position Folder"
        expected_text = "AutoTest Position Folder"
        assert title.text == expected_text, f"Expected: {expected_text}, Actual: {title.text}"

    def assert_position(self):
        title = self.find(title_name)
        assert title.is_displayed(), "Test Position"
        expected_text = "Test Position"
        assert title.text == expected_text, f"Expected: {expected_text}, Actual: {title.text}"
