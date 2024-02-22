from telnetlib import EC
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from pages.base_page import BasePage
from selenium.webdriver.common.by import By

add_click = (By.XPATH, "//span[text()='Add'][1]")
create_folder = (By.XPATH, "//span[text()='Create Folder']")
create_title = (By.XPATH, "//span[text()='Create Title']")
click_delete = (By.XPATH, "(//span[contains(text(), 'Auto')]/following::div//a[@data-qtip='Delete'])[1]")
title_name = (By.XPATH, "//span[text()='Test Title']")
folder_name = (By.XPATH, "(//span[text()='AutoTest Title Folder'])[1]")
search_title = (By.XPATH, "(//input[@placeholder='Search Titles...'])[1]")


class UsersTitles(BasePage):
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
    def click_delete(self):
        return self.find(click_delete).click

    @property
    def delete_title(self):
        return self.find(click_delete).click

    @property
    def folder_name(self):
        return self.find(folder_name).click

    @property
    def search_title_click(self):
        return self.find(search_title).click

    def search_title(self):
        self.find(search_title).send_keys('AutoTest Title Folder')

    def assert_title_folder(self):
        title = self.find(folder_name)
        assert title.is_displayed(), "AutoTest Title Folder"
        expected_text = "AutoTest Title Folder"
        assert title.text == expected_text, f"Expected: {expected_text}, Actual: {title.text}"

    def assert_title_(self):
        title = self.find(title_name)
        assert title.is_displayed(), "Test Title"
        expected_text = "Test Title"
        assert title.text == expected_text, f"Expected: {expected_text}, Actual: {title.text}"

    def hover_over_click_delete2(self):
        element = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located(click_delete))
        if element.is_displayed():
            element.click()
        else:
            print("Element is not displayed.")


