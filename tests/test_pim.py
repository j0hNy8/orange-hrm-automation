import random
from config.config import Config
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.add_employee_page import AddEmployeePage


def test_add_new_employee(driver):

    first_name = f"TestUser_{random.randint(1000, 9999)}"
    last_name = "Automated"

    login_page = LoginPage(driver)
    login_page.load()
    login_page.login(Config.USERNAME, Config.PASSWORD)

    assert login_page.is_dashboard_displayed(
    ) == True, "Dashboard not displayed after login"

    dashboard_page = DashboardPage(driver)
    dashboard_page.navigate_to_pim()

    pim = AddEmployeePage(driver)
    pim.click_add_employee()
    pim.add_employee(first_name, last_name)

    assert pim.is_success_message_displayed(
    ) == True, "Success message not displayed after adding employee"

    print(f"Employee {first_name} {last_name} added successfully.")
