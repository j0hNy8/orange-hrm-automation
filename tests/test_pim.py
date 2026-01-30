import random
from config.config import Config
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.add_employee_page import AddEmployeePage
from pages.employee_list_page import EmployeeListPage
from pages.personal_details_page import PersonalDetailsPage


def test_add_new_employee(driver):

    first_name = f"TestUser_{random.randint(1000, 9999)}"
    last_name = "Automated"
    employee_id = str(random.randint(50000, 99999))

    login_page = LoginPage(driver)
    login_page.load()
    login_page.login(Config.USERNAME, Config.PASSWORD)

    assert login_page.is_dashboard_displayed(
    ) == True, "Dashboard not displayed after login"

    dashboard_page = DashboardPage(driver)
    dashboard_page.navigate_to_pim()

    pim_add = AddEmployeePage(driver)
    pim_add.click_add_employee()
    pim_add.add_employee(first_name, last_name, employee_id)
    pim_add.click_save()

    assert pim_add.is_add_successful(
    ) == True, "Success message not displayed after adding employee"

    pim_list = EmployeeListPage(driver)
    pim_list.click_employee_list_tab()

    pim_list.search_employee(employee_id)

    pim_list.wait_for_search_complete()

    is_found = pim_list.is_employee_listed(employee_id)
    assert is_found == True, f"Employee {employee_id} not found in employee list"

    pim_list.click_edit_icon(employee_id)

    details_page = PersonalDetailsPage(driver)
    assert details_page.is_personal_details_displayed(
    ) == True, "Personal Details page not displayed after clicking edit icon"

    # print(
    #     f"Employee {employee_id} successfully added and verified in employee list.")

    # print(f"Deleting employee id: {employee_id}")

    # pim_list.click_delete_icon(employee_id)

    # pim_list.confirm_delete()

    # is_deleted = pim_list.is_delete_successful()
    # assert is_deleted == True, f"Employee {employee_id} was not deleted successfully"

    # print(f"Employee {employee_id} successfully deleted.")
