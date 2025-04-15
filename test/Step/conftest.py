import pytest
from selenium import webdriver
import from_root
from jproperties import Properties


# @pytest.fixture()
# def browser():
#     driver = webdriver.Chrome()
#     driver.maximize_window()
#     driver.get("https://www.hirist.tech/")
#     yield driver  # Return the driver for use in tests
#     driver.quit()

@pytest.fixture()
def file_path():
    files = from_root('test', 'Config', 'config.properties')
    print("\n\nConfig File Path:", files)
    return files


@pytest.fixture()
def browser(read_properties):
    url = read_properties.data
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(url)
    yield driver
    driver.quit()


@pytest.fixture()
def read_properties(file_path):
    configs = Properties()
    with open(file_path, 'rb') as config_file:
        configs.load(config_file)
        return configs
