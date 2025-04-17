from datetime import datetime, time

from test.Locator.common_steps_locators import CommonStepsLocators
from test.Utilities.BrowserUtilities import BrowserUtility


class CommonStepsPage:

    def login_with_user_creds(browser, user1, read_properties):
        user = read_properties[user1]
        password = read_properties['pwd']
        CommonStepsPage.enter_email(browser, user)
        CommonStepsPage.enter_password(browser, password)
        CommonStepsPage.click_signin_btn(browser)

    def click_login_option(browser):
        element = CommonStepsLocators.login_option
        BrowserUtility.click(browser, element)

    def click_login_link(browser):
        element = CommonStepsLocators.login_link
        BrowserUtility.click(browser, element)

    def enter_email(browser, text):
        username = CommonStepsLocators.email_id
        BrowserUtility.enter_text(browser, username, text)

    def enter_password(browser, text):
        password = CommonStepsLocators.password
        BrowserUtility.enter_text(browser, password, text)

    def click_signin_btn(browser):
        element = CommonStepsLocators.signin_btn
        BrowserUtility.click(browser, element)
        time.sleep(2)
