from pytest_bdd import scenarios, then, when, parsers
# from test.Page.login_page import LoginPage
from test.Page.common_steps_pages import CommonStepsPage
from test.Step.conftest import read_properties

scenarios('../Feature/login.feature')


@when('User visits the test environment')
def visit_url(browser):
    CommonStepsPage.env_url(browser)


@when('User clicks on the sign-in url')
def signin_link(browser):
    CommonStepsPage.click_login_link(browser)


@when('User clicks on the sign-in link')
def login_option(browser):
    CommonStepsPage.click_login_option(browser)


@then(parsers.parse('User enters "{phrase}" email'))
def enter_email(browser, phrase, read_properties):
    username = read_properties[phrase]
    CommonStepsPage.enter_email(browser, username)


@then(parsers.parse('User enters "{phrase}" password'))
def enter_password(browser, phrase, read_properties):
    password = read_properties[phrase]
    CommonStepsPage.enter_password(browser, password)


@then('User clicks on the sign-in button')
def signin_btn(browser):
    CommonStepsPage.click_signin_btn(browser)


@then('User asserts user profile')
def assert_user_profile(browser):
    CommonStepsPage.assert_user_profile(browser)

