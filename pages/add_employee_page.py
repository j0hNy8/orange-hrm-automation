from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage


class AddEmployeePage(BasePage):

    ADD_BUTTON = (By.XPATH, "//button[normalize-space()='Add']")

    INPUT_FIRST_NAME = (By.NAME, "firstName")
    INPUT_LAST_NAME = (By.NAME, "lastName")

    SAVE_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")

    SUCCESS_MESSAGE = (
        By.XPATH, "//div[contains(@class, 'oxd-toast-content') and contains(., 'Success')]")

    EMPLOYEE_ID = (
        By.XPATH, "//label[text()='Employee Id']/parent::div/parent::div//input")

    def click_add_employee(self):
        self.click(self.ADD_BUTTON)

    def add_employee(self, first_name, last_name, employee_id):
        self.type_text(self.INPUT_FIRST_NAME, first_name)
        self.type_text(self.INPUT_LAST_NAME, last_name)

        id_element = self.find(self.EMPLOYEE_ID)
        id_element.click()

        current_value = id_element.get_attribute("value")

        for _ in range(len(current_value)+1):
            id_element.send_keys(Keys.BACKSPACE)

        id_element.send_keys(employee_id)

    def click_save(self):
        self.click(self.SAVE_BUTTON)

    def is_add_successful(self):
        try:
            return self.find(self.SUCCESS_MESSAGE).is_displayed()
        except:
            return False
