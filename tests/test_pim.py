import random
from config.config import Config
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.add_employee_page import AddEmployeePage
from pages.employee_list_page import EmployeeListPage


def test_add_new_employee(driver):

    first_name = f"TestUser_{random.randint(1000, 9999)}"
    last_name = "Automated"
    full_name = f"{first_name} {last_name}"

    login_page = LoginPage(driver)
    login_page.load()
    login_page.login(Config.USERNAME, Config.PASSWORD)

    dashboard_page = DashboardPage(driver)
    dashboard_page.navigate_to_pim()

    pim_add = AddEmployeePage(driver)
    pim_add.click_add_employee()
    pim_add.add_employee(first_name, last_name)

    assert pim_add.is_success_message_displayed(
    ) == True, "Success message not displayed after adding employee"

    pim_list = EmployeeListPage(driver)
    pim_list.click_employee_list_tab()

    print(f"Searching for employee: {full_name}")
    pim_list.search_employee(full_name)

    is_found = pim_list.is_employee_in_table(first_name, last_name)
    assert is_found == True, f"Employee {full_name} not found in employee list"

    print(
        f"Employee {full_name} successfully added and verified in employee list.")
