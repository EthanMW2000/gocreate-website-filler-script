from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
import time


def set_dob(row: tuple, browser: Chrome):
  browser.find_element(By.XPATH, "//a[@data-original-title='Edit']").click()
  time.sleep(1)
  
  dob = browser.find_element(By.XPATH, "//input[@name='dob']")
  dob.clear()
  
  user_dob = row[1]['Birthdate'][:]
  if not '/' in user_dob:
    if '-' in user_dob:
      user_dob = user_dob.replace('-', '/')
    else:
      user_dob = user_dob[:2] + '/' + user_dob[2:4] + '/' + user_dob[4:]
      
  dob.send_keys(user_dob)
  browser.find_element(By.XPATH,
    "(//button[@type='submit' and contains(., 'Save Changes')])[1]"
    ).click()
  
  return