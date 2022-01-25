from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.utils import ChromeType
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from features.steps.utils import BaseHelper


def get_browser(browser: str) -> BaseHelper:
    if browser == "chrome":
        options = Options()
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--no-sandbox')
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')

        desired_cap = DesiredCapabilities.CHROME
        desired_cap['goog:loggingPrefs'] = {'browser': 'ALL'}

        driver = ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()
        service = Service(driver)

        browser = webdriver.Chrome(service=service,
                                   options=options,
                                   desired_capabilities=desired_cap)
        return BaseHelper(browser)
