import sure
import time
import os
from dotenv import load_dotenv
from behave import given, when, then


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


@given(u'username input field id "{id}"')
def step_impl(context, id: str):
    context.txt_username = context.helper.find_by_id(id)


@given(u'password input field id "{id}"')
def step_impl(context, id: str):
    context.txt_password = context.helper.find_by_id(id)


@given(u'login button xpath "{x_path}"')
def step_impl(context, x_path: str):
    context.btn_login = context.helper.find_by_xpath(x_path)
    context.btn_login_xpath = x_path


@given(u'input user credentials')
def step_impl(context):
    context.txt_username.clear()
    context.txt_password.clear()
    context.txt_username.send_keys(context.username)
    context.txt_password.send_keys(context.password)


@when(u'login button is clicked')
def step_impl(context):
    context.btn_login.click()
    time.sleep(1)
    context.console_log = [error.get('message')
                           for error in context.helper.driver
                           .get_log('browser')]


@then(u'console log should not be empty')
def step_impl(context):
    context.console_log.shouldnt.be.empty


@then(u'"{error_msg}" should be thrown in console log')
def step_impl(context, error_msg: str):
    any(msg for msg in context.console_log if error_msg in msg)\
        .should.be.ok


# Scenario: Successful login for users with correct credentials
@then(u'element with id "{elem_id}" should be visible')
def step_impl(context, elem_id: str):
    context.helper.find_by_id(elem_id).is_displayed().should.be.ok
