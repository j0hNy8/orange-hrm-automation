from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class PersonalDetailsPage(BasePage):

    HEADER_PERSONAL_DETAILS = (By.XPATH, "//h6[text()='Personal Details']")

    def is_personal_details_displayed(self):
        try:
            return self.find(self.HEADER_PERSONAL_DETAILS).is_displayed()
        except:
            return False
