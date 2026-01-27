import pytest
from pages.login_page import LoginPage
from config.config import Config


def test_valid_login(driver):

    login_page = LoginPage(driver)
    login_page.load()
    login_page.login(Config.USERNAME, Config.PASSWORD)

    assert login_page.is_dashboard_displayed(
    ) == True, "Dashboard not displayed after login"
