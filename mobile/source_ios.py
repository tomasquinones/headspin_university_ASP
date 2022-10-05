import time
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from os import path

CUR_DIR = path.dirname(path.abspath(__file__))
APP = path.join(CUR_DIR, "TheApp.app.zip")
APPIUM = "http://localhost:4723"

CAPS = {
    "platformName": "iOS",
    "platformVersion": "16.0",
    "deviceName": "iPhone 14",
    "automationName": "xcuitest",
    "app": APP,
}

driver = webdriver.Remote(command_executor=APPIUM, desired_capabilities=CAPS)

try:
    time.sleep(10)

    print(driver.page_source)

finally:
    driver.quit()
