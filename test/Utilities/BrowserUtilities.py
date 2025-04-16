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

    def enter_text(driver, element, text):
        field = driver.find_element(*element)
        field.clear()
        field.send_keys(text)

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
