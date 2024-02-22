from pages.base_page import BasePage
from selenium.webdriver.common.by import By

checkbox_delete = (By.XPATH, "//label[@data-ref='boxLabelEl' and contains(text(), 'I understand')]")
delete_btn = (By.XPATH, "//span[@data-ref='btnInnerEl' and contains(text(), 'Delete')]")
delete_board = (By.XPATH, "//span[contains(@class,'x-btn-inner')and text()='Delete Board']")

class DeleteModul(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    @property
    def checkbox_delete(self):
        return self.find(checkbox_delete).click

    @property
    def delete_btn(self):
        return self.find(delete_btn).click

    @property
    def delete_board(self):
        return self.find(delete_board).click
