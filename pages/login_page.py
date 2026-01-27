from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from config.config import Config


class LoginPage(BasePage):

    USERNAME_INPUT = (By.CSS_SELECTOR, "input[name='username']")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "input[name='password']")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")

    DASHBOARD_HEADER = (By.XPATH, "//h6[text()='Dashboard']")

    def load(self):
        self.driver.get(Config.BASE_URL)

    def login(self, username, password):
        self.type_text(self.USERNAME_INPUT, username)
        self.type_text(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)

    def is_dashboard_displayed(self):
        try:
            self.find(self.DASHBOARD_HEADER)
            return True
        except:
            return False
