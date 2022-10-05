from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Firefox()  # instance of the Firefox driver

try:
    wait = WebDriverWait(driver, 10)
    driver.get("https://the-internet.herokuapp.com")

    # driver.find_element(strategy, selector)
    driver.find_element(By.LINK_TEXT, "Form Authentication")
    wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Form Authentication")))
    print(driver.current_url)
    wait.until(EC.url_to_be("https://the-internet.herokuapp.com/"))


finally:
    driver.quit()
