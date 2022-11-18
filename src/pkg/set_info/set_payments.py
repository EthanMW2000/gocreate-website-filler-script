import datetime
import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


def set_payments(browser: Chrome):
  browser.find_element(By.XPATH, "//a[@aria-controls='payments']").click()
  browser.find_element(By.XPATH, "//button[@data-target='#new_subscription_modal']").click()
  time.sleep(1)
  
  currentdate = datetime.datetime.now()
  startdate = browser.find_element(By.NAME, 'start')
  startdate.send_keys(currentdate.strftime("%m/%d/%Y"))
  
  enddate_input = generate_enddate(currentdate)
  enddate = browser.find_element(By.NAME, 'end')
  enddate.send_keys(enddate_input)
  
  paid_installments = browser.find_element(By.NAME, 'paid_installments')
  paid_installments.send_keys('1')
  total_installments = browser.find_element(By.NAME, 'total_installments')
  total_installments.send_keys('1')
  
  payment_mode = Select(browser.find_element(By.NAME, 'payment_mode'))
  payment_mode.select_by_visible_text('WSU Comp/Prize')
  
  amount = browser.find_element(By.NAME, 'amount')
  amount.send_keys('0')
  total = browser.find_element(By.NAME, 'amount')
  total.send_keys('0')
  
  auxiliary = browser.find_element(By.NAME, 'auxiliary')
  auxiliary.send_keys(f'WSU Student Free Membership {currentdate.strftime("%m/%d/%Y")} - Admin Script')
  
  browser.find_element(By.XPATH,
    "(//button[@type='submit' and contains(., 'Save changes')])[4]"
  ).click()
  
  return

def generate_enddate(currentdate: datetime.datetime) -> str:
  if (currentdate.month <= 5):
    enddate = datetime.datetime(currentdate.year, 5, 31)
  elif (currentdate.month == 12):
    enddate = datetime.datetime(currentdate.year + 1, 5, 31)
  else:
    enddate = datetime.datetime(currentdate.year, 12, 31) 
  
  return enddate.strftime("%m/%d/%Y")