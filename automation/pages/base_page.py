from appium.webdriver import Remote
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    def __init__(self, driver: Remote) -> None:
        self.driver = driver

    def _wait(self, timeout: int = 15) -> WebDriverWait:
        return WebDriverWait(self.driver, timeout)
