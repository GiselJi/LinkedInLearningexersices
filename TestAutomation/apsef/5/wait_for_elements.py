from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()
try:
    wait = WebDriverWait(driver, 10)
    #Once browser is opened this command opens the link with get
    driver.get('https://the-internet.herokuapp.com')
    wait.until(EC.presence_of_element_located(
        (By.LINK_TEXT, 'Form Authentication')
        ))
    wait.until(EC.url_to_be('https://the-internet.herokuapp.com/'))
finally:
    driver.quit()