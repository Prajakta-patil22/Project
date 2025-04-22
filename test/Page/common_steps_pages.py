import time

from test.Locator.common_steps_locators import CommonStepsLocators
from test.Utilities.BrowserUtilities import BrowserUtility


class CommonStepsPage:

    def env_url(browser):
        time.sleep(1)  # Ideally, use WebDriverWait

    # def login_with_user_creds(browser, user1, read_properties):
    #     user = read_properties[user1]
    #     password = read_properties['pwd']
    #     CommonStepsPage.enter_email(browser, user)
    #     CommonStepsPage.enter_password(browser, password)
    #     CommonStepsPage.click_signin_btn(browser)

    def click_login_option(browser):
        element = CommonStepsLocators.login_option
        BrowserUtility.click(browser, element)

    def click_login_link(browser):
        element = CommonStepsLocators.login_link
        BrowserUtility.click(browser, element)
        time.sleep(1)

    def enter_email(browser, phrase):
        username = CommonStepsLocators.email_id
        BrowserUtility.enter_text(browser, username, phrase)

    def enter_password(browser, phrase):
        password = CommonStepsLocators.password
        BrowserUtility.enter_text(browser, password, phrase)

    def click_signin_btn(browser):
        element = CommonStepsLocators.signin_btn
        BrowserUtility.click(browser, element)
        time.sleep(3)

    def assert_user_profile(browser):
        user_profile = CommonStepsLocators.user_profile
        BrowserUtility.assert_element_displayed(browser, user_profile)