from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

browser = webdriver.Chrome( chrome_options=chrome_options)

browser.get("https://techstepacademy.com/training-ground")


input2_locator = "input[id='ipt2']"
button4_locator = "//button[@id='b4']"

 # Assign Elements
input1_elem = browser.find_element('css selector', input2_locator)

butn4_elem = browser.find_element(By.XPATH, button4_locator)

# Manipulate Elements
input1_elem.send_keys("Test Text")
butn4_elem.click()
