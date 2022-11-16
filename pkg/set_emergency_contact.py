from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

def set_emergency_contact(row: tuple, browser: Chrome):
  if row[1][
    'Emergency Contact 1 - Full Name':
    'Emergency Contact 2 - Full Name'
    ][:].isnull().any():
    return
  
  browser.find_element(By.XPATH,
    "//a[@data-target='#edit_emergency_1']"
    ).click()
  
  name = browser.find_element(By.NAME, 'emergency_name_1')
  contact_name = row[1]['Emergency Contact 1 - Full Name'][:]
  name.send_keys(contact_name)
  
  relation = Select(browser.find_element(By.NAME, 'emergency_relation_1'))
  contact_relation = row[1]['Emergency Contact 1 - Relationship'][:]
  relation.select_by_visible_text(contact_relation)
  
  address = browser.find_element(By.NAME, 'emergency_address_1')
  contact_address = row[1]['Emergency Contact 1 - Street Address\n'][:]
  address.send_keys(contact_address)
  
  city = browser.find_element(By.NAME, 'emergency_city_1')
  contact_city = row[1]['Emergency Contact 1 - City'][:]
  city.send_keys(contact_city)
  
  state = Select(browser.find_element(By.NAME, 'emergency_state_1'))
  contact_state = row[1]['Emergency Contact 1 - State'][:]
  state.select_by_value(contact_state)
  
  zipcode = browser.find_element(By.NAME, 'emergency_zip_1')
  contact_zip = row[1]['Emergency Contact 1 - Zip Code'][:]
  zipcode.send_keys(contact_zip)
  
  phone = browser.find_element(By.NAME, 'emergency_phone1_1')
  contact_phone = row[1]['Emergency Contact 1 - Phone Number'][:]
  phone.send_keys(contact_phone)
  
  browser.find_element(By.XPATH,
    "(//button[@type='submit' and contains(., 'Save Changes')])[3]"
  ).click()
  