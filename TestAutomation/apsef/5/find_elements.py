from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
try:
    #Once browser is opened this command opens the link with get
    driver.get('https://the-internet.herokuapp.com')
    #Finds the element link with the specific text Form Authentication
    driver.find_element(By.LINK_TEXT, 'Form Authentication')

    #Finds all the link elements present in the page
    els = driver.find_elements(By.TAG_NAME, 'a')
    print(f'There were {len(els)} anchor elements')
    #Finds all the foo elements
    els = driver.find_elements(By.TAG_NAME, 'foo')
    print(f'There were {len(els)} foo elements')
finally:
    driver.quit()