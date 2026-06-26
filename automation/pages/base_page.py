from appium.webdriver import Remote
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    def __init__(self, driver: Remote) -> None:  # pragma: no cover
        self.driver = driver

    def _wait(self, timeout: int = 15) -> WebDriverWait:  # pragma: no cover
        return WebDriverWait(self.driver, timeout)
