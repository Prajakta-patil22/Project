from selenium.webdriver.common.by import By


class CommonStepsLocators:
    email_id = (By.ID, "login-email-input")
    password = (By.ID, "loginPassword")
    login_link = (By.ID, "user-login-button-id")
    signin_btn = (By.ID, "loginSubmit")
    login_option = (By.CSS_SELECTOR, " div.switch-container  span")

