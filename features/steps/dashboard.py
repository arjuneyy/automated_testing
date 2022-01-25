import sure
from behave import given, then
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


# Background: Website url
@given(u'access website')
def step_impl(context):
    context.helper.open(context.url)


# Scenario: User with either of the specified access level should have no modules in his/her dashboard
@then(u'should have "{mod_cnt:d}" number of modules displayed in sidebar with id "{elem_id}"')
def step_impl(context, mod_cnt: int, elem_id: str):
    parent_elem = context.helper.find_by_id(elem_id)
    children = parent_elem.find_elements(By.TAG_NAME, 'button')

    len(children).should.be.equal(mod_cnt)

@then(u'element with id "{elem_id}" should not be visible')
def step_impl(context, elem_id: str):
    context.helper.driver.find_element.when.called_with(By.ID, elem_id)\
        .should.have.raised(NoSuchElementException)


# Scenario: Account type for user with access level 2 should have 'Monitoring' title in sidebar
@then(u'account type should be "{account_type}" in element with id "{xpath}"')
def step_impl(context, account_type: str, xpath: str):
    context.helper.find_by_xpath(xpath).text.should.be.equal(account_type)


# Scenario: Account type for user with access level 2 should have access to specific modules
@then(u'get displayed modules displayed in element with id "{parent_id}"')
def step_impl(context, parent_id: str):
    parent_elem = context.helper.find_by_id(parent_id)
    context.modules = [elem.text for elem in
                       parent_elem.find_elements(By.TAG_NAME, 'button')]

@then(u'"{module}" module should be displayed')
def step_impl(context, module: str):
    context.modules.should.contain(module)
