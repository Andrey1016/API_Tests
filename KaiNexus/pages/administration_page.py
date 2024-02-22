from pages.base_page import BasePage
from selenium.webdriver.common.by import By


user_titles_click = (By.XPATH, "(//a[contains(@class, 'x-tree-node-text') and text()='Titles'])[1]")
user_positions_click = (By.XPATH, "//a[contains(@class, 'x-tree-node-text') and text()='Positions']")
user_empStatus_click = (By.XPATH, "//a[contains(@class, 'x-tree-node-text') and text()='Employment Status']")
user_certifications_click = (By.XPATH, "//a[contains(@class, 'x-tree-node-text') and text()='Certifications']")
org_level_types = (By.XPATH, "//a[contains(@class, 'x-tree-node-text') and text()='Level Types']")


class AdministrationPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    @property
    def user_titles_click(self):
        return self.find(user_titles_click).click

    @property
    def user_positions_click(self):
        return self.find(user_positions_click).click

    @property
    def user_empStatus_click(self):
        return self.find(user_empStatus_click).click

    @property
    def user_certifications_click(self):
        return self.find(user_certifications_click).click

    @property
    def org_level_types(self):
        return self.find(org_level_types).click
