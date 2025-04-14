import pytest
from selenium import webdriver

@pytest.fixture()
def browser():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.hirist.tech/")
    yield driver  # Return the driver for use in tests
    driver.quit()
