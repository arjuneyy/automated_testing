import os
import time
from configparser import ConfigParser
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from features.steps.utils.helper_web import get_browser
from features.steps.utils import UserAccountUtil
from behave.model import Scenario
from behave.runner import Context


def before_all(context: Context) -> None:
    config = ConfigParser()
    my_file = (os.path.join(os.getcwd(), 'setup.cfg'))
    config.read(my_file)

    # Reading the browser type from the configuration file for Selenium Python Tutorial
    helper_func = get_browser(config.get('Environment', 'Browser'))
    context.helper = helper_func
    context.driver = helper_func.driver

    # Setup account util
    context.account_util = UserAccountUtil()


def after_all(context: Context) -> None:
    # Delete all users created when testing
    context.account_util.delete_test_users()
    context.helper.close()


def before_scenario(context: Context, scenario: Scenario) -> None:
    if 'skip' in scenario.effective_tags:
        scenario.skip('Marked with @skip tag in feature file')

    if 'logout' in scenario.effective_tags:
        try:
            btn_logout = context.helper.driver\
                .find_element(By.ID, 'btn-logout')
            btn_logout.click()
            time.sleep(1)
        except NoSuchElementException:
            pass


def after_scenario(context: Context, scenario: Scenario) -> None:
    if 'logout' in scenario.effective_tags:
        try:
            btn_logout = context.helper.driver\
                .find_element(By.ID, 'btn-logout')
            btn_logout.click()
            time.sleep(1)
        except NoSuchElementException:
            pass
