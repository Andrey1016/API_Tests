from pages.base_page import BasePage
from selenium.webdriver.common.by import By

headers_boards_click = (By.XPATH, "//span[contains(@class,'x-btn-inner')and text()='Boards']")
headers_admin_click = (By.XPATH, "//span[contains(@class,'x-btn-inner')and text()='Admin']")


class BoardsPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    @property
    def headers_boards_click(self):
        return self.find(headers_boards_click).click

    @property
    def headers_admin_click(self):
        return self.find(headers_admin_click).click
