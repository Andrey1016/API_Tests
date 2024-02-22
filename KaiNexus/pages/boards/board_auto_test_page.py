import time

import pytest
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import logging

from pages.base_page import BasePage
from selenium.webdriver.common.by import By

action_dropdown = (By.XPATH, "//span[contains(@class,'x-btn-inner')and text()='Actions']")
delete_board = (By.XPATH, "//div[contains(@class,'x-menu')]//parent::span[text()='Delete Board']")

create_board_btn = (By.XPATH, "//span[contains(@class,'x-btn-inner')and text()='Create Board']")
manage_boards_btn = (By.XPATH, "//span[contains(@class,'x-btn-inner')and text()='Manage Boards']")
board_autotest = (By.XPATH, "//span[contains(@class,'x-menu-item-text')and text()='Board Auto Test']")

checkbox_delete = (By.XPATH, "//label[@data-ref='boxLabelEl' and contains(text(), 'I understand')]")
delete_btn = (By.XPATH, "//span[@data-ref='btnInnerEl' and contains(text(), 'Delete')]")

headers_boards_click = (By.XPATH, "//span[contains(@class,'x-btn-inner')and text()='Boards']")


# delete_board = (By.XPATH, "//span[contains(@class,'x-btn-inner')and text()='Delete Board']")


class BoardAutoTest(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def action_dropdown(self):
        self.find(action_dropdown).click()

    # ------------------------delete Board Loop-----------------------------------------------
    def search_and_delete_board(self):
        while True:
            try:
                self.find(headers_boards_click).click()
                self.find(board_autotest).click()

            except NoSuchElementException:
                break

            self.find(action_dropdown).click()
            self.find(delete_board).click()
            self.find(checkbox_delete).click()
            self.find(delete_btn).click()
            time.sleep(1)


