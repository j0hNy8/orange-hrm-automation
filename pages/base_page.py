from selenium.common.exceptions import ElementClickInterceptedException
from utils.waits import wait_visible, wait_clickable


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def open_url(self, url):
        """Opens the specified URL in the browser."""
        self.driver.get(url)

    def click(self, locator):
        """Clicks on an element specified by the locator."""
        """Tries standard click. If blocked (e.g. by header), forces JS click."""
        element = wait_clickable(self.driver, locator)

        try:
            # Try the "Human" click first
            # This is better because it verifies the button is actually accessible.
            element.click()

        except ElementClickInterceptedException:
            # If the click is blocked (e.g. by a sticky header), use JS to force the click.
            print(
                f"Warning: Click intercepted for {locator}. Using JS Click fallback.")
            self.driver.execute_script(
                "arguments[0].click();", element)

    def type_text(self, locator, text):
        """Types text into an input field specified by the locator."""
        element = wait_visible(self.driver, locator)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        """Gets the text of an element specified by the locator."""
        return wait_visible(self.driver, locator).text

    def find(self, locator, timeout=None):
        """Finds an element using the provided locator."""
        if timeout is None:
            return wait_visible(self.driver, locator)
        else:
            return wait_visible(self.driver, locator, timeout)
