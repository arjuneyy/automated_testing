import sure
from behave import given, then
from features.steps import constants as const
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


@given(u'add new user with access level "{access_level:d}" if not existing')
def step_impl(context, access_level: int):
    accounts = context.account_util.filter_by_(
        account_username=context.username,
        account_access_level=access_level)
    if not accounts:
        context.account_util.create_account(context.username,
                                            context.password,
                                            access_level)

    accounts = context.account_util.filter_by_(
        account_username=context.username,
        account_access_level=access_level)

    accounts.shouldnt.be.empty


@then(u'delete newly added user with username "{username}" and access level "{access_level:d}"')
def step_impl(context, username: str, access_level: int):
    accounts = context.account_util.filter_by_(
        account_username=username,
        account_access_level=access_level)

    accounts.shouldnt.be.empty
    context.account_util.delete(accounts[0])

# Scenario: User with either of the specified access level should have no modules in his/her dashboard


@then(u'should have "{mod_cnt:d}" number of modules displayed in sidebar')
def step_impl(context, mod_cnt: int):
    sidebar = context.helper.find_by_id(const.SIDEBAR_GROUP_ID)
    children = sidebar.find_elements(By.TAG_NAME, 'button')

    len(children).should.be.equal(mod_cnt)


# Scenario: Account type for user with access level 2 should have 'Monitoring' title in sidebar
@then(u'account type should be displayed as "{account_type}" in sidebar title')
def step_impl(context, account_type: str):
    context.helper.find_by_xpath(const.LBL_ACCOUNT_TYPE_XPATH).text\
        .should.be.equal(account_type)


# Scenario: Account type for user with access level 2 should have access to specific modules
@then(u'get displayed modules displayed in sidebar')
def step_impl(context):
    parent_elem = context.helper.find_by_id(const.SIDEBAR_GROUP_ID)
    context.modules = [elem.text for elem in
                       parent_elem.find_elements(By.TAG_NAME, 'button')]


@then(u'"{module}" module should be displayed')
def step_impl(context, module: str):
    context.modules.should.contain(module)
