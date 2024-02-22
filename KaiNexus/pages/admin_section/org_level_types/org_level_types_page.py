from selenium.webdriver.common import actions

from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

add_click = (By.XPATH, "//span[text()='Add'][1]")
create_levelType = (By.XPATH, "//span[text()='Create Level Type']")
click_delete = (By.XPATH, "(//div[contains(text(), 'AutoTest Level Type')]/following::div//a[@data-qtip='Delete'])[1]")
level_type_name = (By.XPATH, "//div[text()='AutoTest Level Type']")


# //span[contains(text(), 'test')]/following::a[@data-qtip='Delete']
# //tbody[descendant::span[text()='test'] and descendant::a[@data-qtip='Delete']]
# //div[contains(text(), 'AutoTest Level Type')]/following::div//a[@data-qtip='Delete']
class OrgLevelTypes(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    @property
    def add_click(self):
        return self.find(add_click).click

    @property
    def create_levelType(self):
        return self.find(create_levelType).click

    # @property
    # def create_EmpStatus(self):
    #     return self.find(create_EmpStatus).click

    @property
    def level_type_name(self):
        return self.find(level_type_name).click

    @property
    def delete_title(self):
        return self.find(click_delete).click

    def assert_level_type_name(self):
        title = self.find(level_type_name)
        assert title.is_displayed(), "AutoTest Level Type"
        expected_text = "AutoTest Level Type"
        assert title.text == expected_text, f"Expected: {expected_text}, Actual: {title.text}"

    # def assert_empStatus(self):
    #     title = self.find(empStatus_name)
    #     assert title.is_displayed(), "Test EmpStatus"
    #     expected_text = "TestEmp Status"
    #     assert title.text == expected_text, f"Expected: {expected_text}, Actual: {title.text}"

    def hover_over_click_delete(self):
        element = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located(click_delete))
        if element.is_displayed():
            element.click()
        else:
            print("Element is not displayed.")
