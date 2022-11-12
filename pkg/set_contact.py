from state_dictionary import state
from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome
from selenium.webdriver.support.ui import Select

def set_contact(row: tuple, browser: Chrome):
  browser.find_element(By.XPATH(
    "//a[@data-target='#edit_personal_contact']"
    )).click()
  
  address = browser.find_element(By.NAME, 'address')
  user_address = row.loc['Street Address']
  address.send_keys(user_address)
  
  city = browser.find_element(By.NAME, 'city')
  user_city = row.loc['City']
  city.send_keys(user_city)
  
  state = Select(browser.find_element(By.NAME, 'state'))
  user_state = row.loc['State']
  if not user_state.length > 2:
    user_state = state['user_state']
  state.select_by_value(user_state)
  
  zipcode = browser.find_element(By.NAME, 'zip')
  user_zipcode = row.loc['Zip Code']
  if '.' in user_zipcode:
    user_zipcode = user_zipcode.split('.')[0]
  zipcode.send_keys(user_zipcode)
  
  phone = browser.find_element(By.NAME, 'phone1')
  user_phone = row.loc['Phone Number']
  if '-' in user_phone:
    user_phone = user_phone.replace('-', '')
  phone.send_keys(user_phone)
  
  browser.find_element(By.XPATH(
    "(//button[@type='submit' and contains(., 'Save Changes')])[2]"
  )).click()