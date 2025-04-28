from datetime import time

# @pytest.fixture()
# def browser():
#     driver = webdriver.Chrome()
#     driver.maximize_window()
#     driver.get("https://www.hirist.tech/")
#     yield driver  # Return the driver for use in tests
#     driver.quit()


import pytest
from selenium import webdriver
import configparser
import os


@pytest.fixture()
def read_properties():
    config = configparser.ConfigParser()
    base_dir = os.path.dirname(os.path.abspath(__file__))
    config_path = os.path.join(base_dir, '..', 'Config', 'config.properties')
    config.read(config_path)

    # Get the URL from the config file
    try:
        user1 = config['default']['user1']
        pwd = config['default']['pwd']
    except KeyError as e:
        raise KeyError(f"Missing required section or key in config file: {e}")

    return {
        "user1": user1,
        "pwd": pwd
    }


@pytest.fixture()
def browser():
    # Set up the browser
    config = configparser.ConfigParser()
    base_dir = os.path.dirname(os.path.abspath(__file__))
    config_path = os.path.join(base_dir, '..', 'Config', 'config.properties')
    config.read(config_path)

    url = config['default']['url']
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(url)  # Use the URL from the config file
    yield driver  # Return the driver for use in tests
    driver.quit()
