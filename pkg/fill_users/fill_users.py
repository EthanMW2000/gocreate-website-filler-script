from pandas import DataFrame
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from tkinter.messagebox import Message
from set_dob import set_dob
from set_contact import set_contact
from set_emergency_contact import set_emergency_contact
from set_payments import set_payments


def fill_users(file: DataFrame, browser: Chrome):
  user_not_found = []
  file.reset_index()
  
  searchbar = browser.find_element(By.CSS_SELECTOR, 'search')
  
  for row in file.iterrows():
    searchbar.send_keys(row[1]['Email'][:])
    firstName = row[1]['Full Name'][:].split(' ')[0]
    
    try:
      user = browser.find_element(By.XAPTH, f"//[@text()='{firstName}']")
    except:
      user_not_found.append(row[1]['Email'][:])
      continue
    else:
      user.click()
      fill_info(row, browser)

    searchbar.clear()
    
def fill_info(row: tuple, browser: Chrome):
  set_dob(row, browser)
  browser.find_element(By.XPATH,
    "//input[@type='checkbox' and @data-flag='membership_agreement']"
    ).click()
  set_contact(row, browser)
  set_emergency_contact(row, browser)
  set_payments(row, browser)
  
  