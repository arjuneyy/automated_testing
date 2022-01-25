from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.webdriver import WebDriver


class BaseHelper:
    __TIMEOUT = 10

    def __init__(self, driver: WebDriver) -> None:
        super().__init__()
        self._driver_wait = WebDriverWait(driver, BaseHelper.__TIMEOUT)
        self._driver = driver

    @property
    def driver(self) -> WebDriver:
        return self._driver

    def open(self, url: str) -> None:
        self._driver.get(url)

    def maximize(self) -> None:
        self._driver.maximize_window()

    def close(self) -> None:
        self._driver.quit()

    # Helper functions that are used to identify the web locators in Selenium Python tutorial
    def find_by_xpath(self, xpath):
        return self._driver_wait.until(EC.visibility_of_element_located((By.XPATH, xpath)))

    def find_by_name(self, name):
        return self._driver_wait.until(EC.visibility_of_element_located((By.NAME, name)))

    def find_by_id(self, id):
        return self._driver_wait.until(EC.visibility_of_element_located((By.ID, id)))

    def find_by_tag_name(self, tag_name: str):
        return self._driver_wait.until(EC.visibility_of_element_located((By.TAG_NAME, tag_name)))
