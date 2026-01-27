from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

DEFAULT_TIMEOUT = 10


def wait_visible(driver, locator, timeout=DEFAULT_TIMEOUT):
    """Wait until the element located by 'locator' is visible on the page."""
    try:
        return WebDriverWait(driver, timeout).until(EC.visibility_of_element_located(locator))
    except TimeoutException as exc:
        raise TimeoutException(
            f"Element with locator {locator} not visible after {timeout} seconds") from exc


def wait_clickable(driver, locator, timeout=DEFAULT_TIMEOUT):
    """Wait until the element located by 'locator' is clickable."""
    try:
        return WebDriverWait(driver, timeout).until(EC.element_to_be_clickable(locator))
    except TimeoutException as exc:
        raise TimeoutException(
            f"Element with locator {locator} not clickable after {timeout} seconds") from exc
