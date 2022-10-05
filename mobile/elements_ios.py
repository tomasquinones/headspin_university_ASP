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
    wait = WebDriverWait(driver, 10)
    wait.until(
        EC.presence_of_element_located((MobileBy.ACCESSIBILITY_ID, "Echo Box"))
    ).click()

    wait.until(
        EC.presence_of_element_located((MobileBy.ACCESSIBILITY_ID, "messageInput"))
    ).send_keys("Hello Frank")

    driver.find_element(MobileBy.ACCESSIBILITY_ID, "messageSaveBtn").click()
    saved_text = driver.find_element(MobileBy.ACCESSIBILITY_ID, "savedMessage").text
    assert saved_text == "Hello Frank"
    driver.back()
    wait.until(
        EC.presence_of_element_located((MobileBy.ACCESSIBILITY_ID, "Echo Box"))
    ).click()
    saved_text = wait.until(
        EC.presence_of_element_located((MobileBy.ACCESSIBILITY_ID, "savedMessage"))
    ).text
    assert saved_text == "Hello Frank"

    """
    go back to the echobox view
    assert that the 'Hello Frank' text is still displayed
    
    
    """

finally:
    driver.quit()
