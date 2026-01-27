import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from datetime import datetime


@pytest.fixture(scope="function")
def driver(request):

    ChromeOptions = Options()
    # ChromeOptions.add_argument("--headless")
    ChromeOptions.add_argument("--no-sandbox")
    ChromeOptions.add_argument("--disable-dev-shm-usage")
    ChromeOptions.add_argument("--window-size=1920,1080")

    driver = webdriver.Chrome(options=ChromeOptions)

    request.node.driver = driver

    yield driver

    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    pytest_html = item.config.pluginmanager.getplugin("html")
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, "extra", [])

    if report.when == "call" or report.when == "setup":
        xfail = hasattr(report, "wasxfail")
        if (report.skipped and xfail) or (report.failed and not xfail):
            driver = getattr(item, "driver", None)

            if driver:

                screenshot_dir = "screenshots"
                if not os.path.exists(screenshot_dir):
                    os.makedirs(screenshot_dir)

                timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
                file_name = f"{item.name}_{timestamp}.png"
                file_path = os.path.join(screenshot_dir, file_name)

                driver.save_screenshot(file_path)

                if pytest_html:
                    extra.append(
                        pytest_html.extras.image(file_path)
                    )
        report.extra = extra
