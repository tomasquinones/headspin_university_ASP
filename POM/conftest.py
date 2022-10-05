import pytest
from appium import webdriver
from os import path

CUR_DIR = path.dirname(path.abspath(__file__))
APP = path.join(CUR_DIR, "..", "mobile", "TheApp.app.zip")
APPIUM = "http://localhost:4723"


@pytest.fixture  # turns a function into a fixture
def driver():
    CAPS = {
        "platformName": "iOS",
        "platformVersion": "16.0",
        "deviceName": "iPhone 14",
        "automationName": "xcuitest",
        "app": APP,
    }

    driver = webdriver.Remote(command_executor=APPIUM, desired_capabilities=CAPS)

    yield driver  # returns driver, runs code, then returns to this function
    driver.quit()
