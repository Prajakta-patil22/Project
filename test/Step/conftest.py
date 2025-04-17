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
def browser():
    config = configparser.ConfigParser()
    # config_path = r'C:\Users\shruti.umbarkar\MYProjects\Project\test\Config\config.properties'
    # Construct the relative path to the config.properties file
    base_dir = os.path.dirname(os.path.abspath(__file__))  # Directory containing conftest.py
    config_path = os.path.join(base_dir, '..', 'Config', 'config.properties')  # Adjust as per your project structure

    # Check if the config file exists
    if not os.path.exists(config_path):
        raise FileNotFoundError(f"Configuration file not found at: {config_path}")

    # Read the configuration file
    config.read(config_path)

    # Get the URL from the config file
    try:
        url = config['default']['url']
        user1 = config['default']['user1']
        pwd = config['default']['pwd']
    except KeyError as e:
        raise KeyError(f"Missing required section or key in config file: {e}")

    # Set up the browser
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(url) # Use the URL from the config file
    yield driver  # Return the driver for use in tests
    driver.quit()




