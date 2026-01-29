from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class EmployeeListPage(BasePage):

    LINK_EMPLOYEE_LIST = (By.LINK_TEXT, "Employee List")

    INPUT_EMPLOYEE_ID = (
        By.XPATH, "//label[text()='Employee Id']/../following-sibling::div//input")

    SEARCH_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")

    CONFIRM_DELETE_BUTTON = (By.XPATH, "//button[contains(., 'Yes, Delete')]")

    SUCCESS_MESSAGE = (
        By.XPATH, "//div[contains(@class, 'oxd-toast-content') and contains(., 'Success')]")

    def click_employee_list_tab(self):
        self.click(self.LINK_EMPLOYEE_LIST)

    def search_employee(self, employee_id):
        self.type_text(self.INPUT_EMPLOYEE_ID, employee_id)
        self.click(self.SEARCH_BUTTON)

    def wait_for_search_complete(self):
        locator = (By.XPATH, "//span[normalize-space()='(1) Record Found']")
        try:
            self.find(locator)
            return True
        except:
            return False

    def is_employee_listed(self, employee_id):
        locator = (
            By.XPATH, f"//div[@role='row']//div[contains(text(), '{employee_id}')]")
        try:
            self.find(locator)
            return True
        except:
            return False

    def is_delete_successful(self):
        try:
            return self.find(self.SUCCESS_MESSAGE).is_displayed()
        except:
            return False

    def click_delete_icon(self, employee_id):
        delete_btn_xpath = (f"//div[contains(text(), '{employee_id}')]"
                            f"/ancestor::div[@role='row']"
                            f"//button[i[contains(@class, 'bi-trash')]]")
        self.click((By.XPATH, delete_btn_xpath))

    def confirm_delete(self):
        self.click(self.CONFIRM_DELETE_BUTTON)
