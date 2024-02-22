from pages.base_page import BasePage
from selenium.webdriver.common.by import By

board_title = (By.XPATH, "//input[@placeholder='Required']")
board_create_btn = (By.XPATH, "//span[contains(@class,'x-btn-inner x-btn-inner-de')and text()='Create']")


class CreateBoard(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def board_title(self):
        self.find(board_title).send_keys("Board Auto Test")

    def board_title_click(self):
        self.find(board_title).click()

    def board_create_btn(self):
        self.find(board_create_btn).click()

