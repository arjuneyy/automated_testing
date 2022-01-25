from selenium import webdriver
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.utils import ChromeType
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from features.steps.utils import BaseHelper


def get_browser(browser) -> BaseHelper:
    if browser == "chrome":
        options = Options()
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--no-sandbox')
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')

        driver = ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()
        service = Service(driver)

        browser = webdriver.Chrome(service=service, options=options)
        return BaseHelper(browser)
