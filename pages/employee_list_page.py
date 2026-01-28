from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class EmployeeListPage(BasePage):

    LINK_EMPLOYEE_LIST = (By.LINK_TEXT, "Employee List")

    INPUT_EMPLOYEE_NAME = (
        By.XPATH, "//label[text()='Employee Name']/../following-sibling::div//input")

    SEARCH_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")

    TABLE_ROW_NAME = "//div[contains(text(), '{}')]"

    def click_employee_list_tab(self):
        self.click(self.LINK_EMPLOYEE_LIST)

    def search_employee(self, employee_name):
        self.type_text(self.INPUT_EMPLOYEE_NAME, employee_name)
        # time.sleep(1)
        self.click(self.SEARCH_BUTTON)

    def is_employee_in_table(self, full_name):
        dynamic_xpath = (By.XPATH, self.TABLE_ROW_NAME.format(full_name))

        try:
            self.find(dynamic_xpath)
            return True
        except:
            return False
