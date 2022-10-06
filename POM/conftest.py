import pytest
from appium import webdriver
from os import path
from views.home_view import HomeView

CUR_DIR = path.dirname(path.abspath(__file__))
IOS_APP = path.join(CUR_DIR, "..", "mobile", "TheApp.app.zip")
ANDROID_APP = path.join(CUR_DIR, "..", "mobile", "TheApp.apk")

APPIUM = "http://localhost:4723"


@pytest.fixture
def driver():
    """Defines and instanciates the webdriver."""

    IPHONE_CAPS = {
        "platformName": "iOS",
        "platformVersion": "16.0",
        "deviceName": "iPhone 14",
        "automationName": "xcuitest",
        "app": IOS_APP,
    }

    """     
    ANDROID_CAPS = {
        "platformName": "Android",
        "platformVersion": "13.0",
        "deviceName": "Pixel 4a",
        "automationName": "UiAutomator2",
        "app": ANDROID_APP,
    } """

    driver = webdriver.Remote(
        command_executor=APPIUM, desired_capabilities=IPHONE_CAPS
    )  # ANDROID_CAPS or IPHONE_CAPS

    yield driver  # returns driver, runs code, then returns to this function
    driver.quit()


@pytest.fixture
def home(driver):
    return HomeView(driver)
