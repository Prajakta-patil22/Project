from pytest_bdd import scenarios, then, when

from test.Page.login_page import LoginPage

scenarios('../Feature/login.feature')

@when('User visits the test environment')
def visit_url(browser):
    LoginPage.env_url(browser)

@when('User clicks on the sign-in url')
def signin_link(browser):
    LoginPage.click_login_link(browser)

@when('User clicks on the sign-in link')
def login_option(browser):
    LoginPage.click_login_option(browser)

@then('User enters email ID')
def enter_email(browser):
    LoginPage.enter_email(browser)

@then('User enters password')
def enter_password(browser):
    LoginPage.enter_password(browser)

@when('User clicks on the sign-in button')
def signin_btn(browser):
    LoginPage.click_signin_btn(browser)
