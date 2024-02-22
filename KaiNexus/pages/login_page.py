from pages.base_page import BasePage
from selenium.webdriver.common.by import By

username = (By.ID, 'username')
password = (By.ID, 'password')
sign_in = (By.ID, 'signInBtn')
need_help = (By.XPATH, '//a[@class="need-help"]')
page_text = (By.XPATH, '//span[text()="First time signing in?"]')
wrong_credentials = (By.XPATH, '//span[text()= Invalid username or password.]')
headers_admin_click = (By.XPATH, "//span[contains(@class,'x-btn-inner')and text()='Admin']")


class LoginPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def open(self):
        self.browser.get('https://test2.kainexus.com')

    def username(self):
        self.find(username).send_keys('Showroom')

    def username_wrong(self):
        self.find(username).send_keys('ShowroomXXX')

    def password(self):
        self.find(password).send_keys('knxdemo123')

    def password_wrong(self):
        self.find(password).send_keys('knxdemo123XXX')

    @property
    def sign_in(self):
        return self.find(sign_in).click

    @property
    def need_help(self):
        return self.find(need_help).click

    # ------------------full login method--------------------------
    def login(self):
        self.browser.get('https://test2.kainexus.com')
        self.find(username).send_keys('Showroom')
        self.find(password).send_keys('knxdemo123')
        self.find(sign_in).click()

    # --------------------full login and click Admin----------------------

    def login_to_admin(self):
        self.browser.get('https://test2.kainexus.com')
        self.find(username).send_keys('Showroom')
        self.find(password).send_keys('knxdemo123')
        self.find(sign_in).click()
        self.find(headers_admin_click).click()

