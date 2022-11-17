import datetime

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By


def set_payments(row: tuple, browser: Chrome):
  browser.find_element(By.XPATH, "//a[@aria-controls='payments']").click()
  browser.find_element(By.XPATH, "//button[@data-target='#new_subscription_modal']").click()
  
  currentdate = datetime.datetime.now()
  startdate = browser.find_element(By.NAME, 'start')
  startdate.send_keys(currentdate.strftime("%m/%d/%Y"))
  
  enddate_input = generate_enddate(currentdate)
  enddate = browser.find_element(By.NAME, 'end')
  enddate.send_keys(enddate_input)
  
  return

def generate_enddate(currentdate: datetime.datetime) -> str:
  if (currentdate.month <= 5):
    enddate = datetime.datetime(currentdate.year, 5, 31)
  elif (currentdate.month == 12):
    enddate = datetime.datetime(currentdate.year + 1, 5, 31)
  else:
    enddate = datetime.datetime(currentdate.year, 12, 31) 
  
  return enddate.strftime("%m/%d/%Y")