import sure
import time
import os
from dotenv import load_dotenv
from behave import given, when, then
from features.steps import constants as const
from features.steps.utils import ElementUtil as ElemUtil
from features.steps.utils.element_util import ElementUtil


# Scenario: Title should be properly set
@given(u'website url from environment file')
def step_impl(context):
    load_dotenv()

    url = os.getenv('WEBSITE_URL')
    url.shouldnt.be.none
    context.url = str(url)


@given(u'access the website')
def step_impl(context):
    context.helper.open(context.url)


@then(u'title should be "{title}"')
def step_impl(context, title: str):
    context.helper.driver.title.should.be.equal(title)


# Scenario: Failed login for unregistered users
@given(u'user credentials username "{username}" and password "{password}"')
def step_impl(context, username: str, password: str):
    context.username = username if username != 'None' else ""
    context.password = password if password != 'None' else ""


@given(u'input user credentials')
def step_impl(context):
    txt_username = context.helper.find_by_id(const.TXT_USERNAME_ID)
    txt_password = context.helper.find_by_id(const.TXT_PASSWORD_ID)

    txt_username.clear()
    txt_password.clear()
    txt_username.send_keys(context.username)
    txt_password.send_keys(context.password)


@when(u'login button is clicked')
def step_impl(context):
    btn_login = context.helper.find_by_xpath(const.BTN_LOGIN_XPATH)
    btn_login.click()
    time.sleep(1)

    context.console_log = [error.get('message')
                           for error in context.helper.driver
                           .get_log('browser')]


@then(u'console log should not be empty')
def step_impl(context):
    context.console_log.shouldnt.be.empty


@then(u'"Empty fields!" should be thrown in console log')
def step_impl(context):
    ElementUtil.is_err_in_console_log(context, const.CONSOLE_LOG_EMPTY_FIELDS)\
        .should.be.ok


@then(u'"login error!" should be thrown in console log')
def step_impl(context):
    ElemUtil.is_err_in_console_log(context, const.CONSOLE_LOG_LOGIN_ERROR)\
        .should.be.ok


@then(u'logout button should be visible')
def step_impl(context):
    ElemUtil.element_visibility_by_id(context, const.BTN_LOGOUT_ID).should.be.ok


@then(u'sidebar should be visible')
def step_impl(context):
    ElemUtil.element_visibility_by_id(context, const.SIDEBAR_GROUP_ID)\
        .should.be.ok
