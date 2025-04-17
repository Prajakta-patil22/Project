from pytest_bdd import scenarios, then, when, parsers
from test.Page.login_page import LoginPage
from test.Page.common_steps_pages import CommonStepsPage

scenarios('../Feature/login.feature')


@when('User visits the test environment')
def visit_url(browser):
    LoginPage.env_url(browser)


@when('User clicks on the sign-in url')
def signin_link(browser):
    CommonStepsPage.click_login_link(browser)


@when('User clicks on the sign-in link')
def login_option(browser):
    CommonStepsPage.click_login_option(browser)


@then(parsers.parse('User enters "{email}" email'))
def enter_email(browser, email):
    CommonStepsPage.enter_email(browser, email)


@then('User enters "{password}" password')
def enter_password(browser, password):
    CommonStepsPage.enter_password(browser, password)


@then('User clicks on the sign-in button')
def signin_btn(browser):
    CommonStepsPage.click_signin_btn(browser)
