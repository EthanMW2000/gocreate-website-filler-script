from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

def set_comment(row: tuple, browser: Chrome):
  browser.find_element(By.XPATH, "//a[@href='#comments']").click()
  browser.find_element(By.XPATH, "//a[@data-target='#new_report_user']").click()
  textinput = browser.find_element(By.NAME, 'report_user')
  
  textinput.sendkeys(row[1]['WSU or WSU Tech Id'][:])
  
  browser.find_element(By.XPATH,
    "(//button[@type='submit' and contains(., 'Save Changes')])[2]"
  ).click()
  
  return