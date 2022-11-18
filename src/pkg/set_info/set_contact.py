from pkg.set_info.state_dictionary import states_dict
from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome
from selenium.webdriver.support.ui import Select
import time

def set_contact(row: tuple, browser: Chrome):
  browser.find_element(By.XPATH,
    "//a[@data-target='#edit_personal_contact']"
    ).click()
  time.sleep(1)
  
  address = browser.find_element(By.NAME, 'address')
  address.clear()
  user_address = row[1]['Street Address'][:]
  address.send_keys(user_address)
  
  city = browser.find_element(By.NAME, 'city')
  city.clear()
  user_city = row[1]['City'][:]
  city.send_keys(user_city)
  
  state = Select(browser.find_element(By.NAME, 'state'))
  user_state = row[1]['State'][:]
  if not len(user_state) > 2:
    user_state = states_dict[user_state]
  state.select_by_value(user_state)
  
  zipcode = browser.find_element(By.NAME, 'zip')
  zipcode.clear()
  user_zipcode = row[1]['Zip Code'][:]
  if '.' in user_zipcode:
    user_zipcode = user_zipcode.split('.')[0]
  zipcode.send_keys(user_zipcode)
  
  phone = browser.find_element(By.NAME, 'phone1')
  phone.clear()
  user_phone = row[1]['Phone Number'][:]
  if '-' in user_phone:
    user_phone = user_phone.replace('-', '')
  if ('(' in user_phone) or (')' in user_phone):
    user_phone = user_phone.replace('(', '')
    user_phone = user_phone.replace(')', '')
  if '.' in user_phone:
    user_phone = user_phone.split('.')[0]
  phone.send_keys(user_phone)
  
  browser.find_element(By.XPATH,
    "(//button[@type='submit' and contains(., 'Save Changes')])[2]"
  ).click()
  
  return