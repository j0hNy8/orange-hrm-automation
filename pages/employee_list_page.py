from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import time


class EmployeeListPage(BasePage):

    LINK_EMPLOYEE_LIST = (By.LINK_TEXT, "Employee List")

    INPUT_EMPLOYEE_NAME = (
        By.XPATH, "//label[text()='Employee Name']/../following-sibling::div//input")

    SEARCH_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")

    TABLE_ROW_NAME = "//div[contains(text(), '{}')]"

    def click_employee_list_tab(self):
        self.click(self.LINK_EMPLOYEE_LIST)

    def search_employee(self, full_name):
        self.type_text(self.INPUT_EMPLOYEE_NAME, full_name)
        time.sleep(0.5)  # Wait for suggestions to load
        self.click(self.SEARCH_BUTTON)

    def is_employee_in_table(self, first_name, last_name):
        xpath_query = (
            f"//div[contains(@class, 'oxd-table-card')]"
            f"[.//div[contains(text(), '{first_name}')]]"
            f"[.//div[contains(text(), '{last_name}')]]"
        )

        try:
            self.find((By.XPATH, xpath_query))
            return True
        except:
            return False
