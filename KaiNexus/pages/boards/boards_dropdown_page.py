from pages.base_page import BasePage
from selenium.webdriver.common.by import By

create_board_btn = (By.XPATH, "//span[contains(@class,'x-btn-inner')and text()='Create Board']")
manege_boards_btn = (By.XPATH, "//span[contains(@class,'x-btn-inner')and text()='Manage Boards']")
board_autotest = (By.XPATH, "//span[contains(@class,'x-menu-item-text')and text()='Board Auto Test']")


class BoardsDropdown(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def create_board_btn(self):
        self.find(create_board_btn).click()

    def manege_boards_btn(self):
        self.find(manege_boards_btn).click()

    def find_board(self):
        self.find(board_autotest).click()
