import os
from configparser import ConfigParser
from features.steps.utils.helper_web import get_browser


def before_all(context) -> None:
    config = ConfigParser()
    my_file = (os.path.join(os.getcwd(), 'setup.cfg'))
    config.read(my_file)

    # Reading the browser type from the configuration file for Selenium Python Tutorial
    helper_func = get_browser(config.get('Environment', 'Browser'))
    context.helper = helper_func
    context.driver = helper_func.driver


def after_all(context) -> None:
    context.helper.close()
