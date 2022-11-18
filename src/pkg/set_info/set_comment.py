from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
import time

def set_comment(row: tuple, browser: Chrome):
  browser.find_element(By.XPATH, "//a[@href='#comments']").click()
  browser.find_element(By.XPATH, "//button[@data-target='#new_report_user']").click()
  time.sleep(1)
  textinput = browser.find_element(By.NAME, 'report_user')
  
  textinput.send_keys(row[1]['WSU or WSU Tech Id'][:])
  
  browser.find_element(By.XPATH,
    "(//button[@type='submit' and contains(., 'Save changes')])[2]"
  ).click()
  
  return