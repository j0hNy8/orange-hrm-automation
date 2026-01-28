from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class AddEmployeePage(BasePage):

    ADD_BUTTON = (By.XPATH, "//button[normalize_space()='Add']")

    INPUT_FIRST_NAME = (By.NAME, "firstName")
    INPUT_LAST_NAME = (By.NAME, "lastName")

    SAVE_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")

    SUCCESS_MESSAGE = (
        By.XPATH, "//div[contains(@class, 'oxd-toast-content')]")

    def click_add_employee(self):
        self.click(self.ADD_BUTTON)

    def add_employee(self, first_name, last_name):
        self.type_text(self.INPUT_FIRST_NAME, first_name)
        self.type_text(self.INPUT_LAST_NAME, last_name)
        self.click(self.SAVE_BUTTON)

    def is_success_message_displayed(self):
        try:
            return self.find(self.SUCCESS_MESSAGE).is_displayed()
        except:
            return False
