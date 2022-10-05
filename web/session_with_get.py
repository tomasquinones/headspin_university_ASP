from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()  # instance of the Firefox driver

try:
    driver.get("http://the-internet.herokuapp.com")

    # driver.find_element(strategy, selector)

finally:
    driver.quit()
