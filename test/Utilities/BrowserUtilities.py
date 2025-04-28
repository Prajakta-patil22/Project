from selenium.common import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BrowserUtility:

    def click(driver, element):
        wait = WebDriverWait(driver, 30)
        wait.until(EC.visibility_of_element_located(element))
        wait.until(EC.element_to_be_clickable(element))
        m = driver.find_element(*element)
        driver.execute_script("arguments[0].scrollIntoView();", m)
        driver.find_element(*element).click()

    # def enter_text(driver, element, text):
    #     field = driver.find_element(*element)
    #     field.clear()
    #     field.send_keys(text)

    def enter_text(browser, element, text):
        BrowserUtility.wait_for_element(browser, *element)
        browser.find_element(*element).clear()
        # print("Entering " + text + " text into " + str(element[1]) + " element")
        browser.find_element(*element).send_keys(text)

    def wait_for_element(driver, by, locator, timeout=10):
        return WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located((by, locator))
        )

    def refresh(driver):
        driver.refresh()
        print("refreshes the page")

    def back(driver):
        driver.back()

    def forward(driver):
        driver.forward()

    def get_title(driver):
        title = driver.get_title()
        print('Page title is: ' + title)

    def assert_element_displayed(browser, element):
        WebDriverWait(browser, 30).until(EC.visibility_of_element_located(element))
        assert browser.find_element(*element).is_displayed()
        print('The expected element ' + str(element[1]) + ' is displayed')
