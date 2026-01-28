from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class DashboardPage(BasePage):

    MENU_PIM = (By.XPATH, "//span[text()='PIM']")

    def navigate_to_pim(self):
        self.click(self.MENU_PIM)
