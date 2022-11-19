import os
import time
from pandas import DataFrame
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from tkinter import messagebox
from src.pkg.set_info.set_dob import set_dob
from src.pkg.set_info.set_contact import set_contact
from src.pkg.set_info.set_emergency_contact import set_emergency_contact
from src.pkg.set_info.set_payments import set_payments
from src.pkg.set_info.set_comment import set_comment


def fill_users(file: DataFrame, browser: Chrome):
  user_not_found = []
  file.reset_index()
  
  for row in file.iterrows():
    email = row[1]['WSU or WSU Tech Email'][:]
    searchbar = browser.find_element(By.XPATH, "(//input[@type='search'])[1]")
    searchbar.clear()
    searchbar.send_keys(email)
    time.sleep(2)
    
    try:
      user = browser.find_element(
        By.XPATH, 
        "(//td[@class='sorting_1'])[1]"
        ).text
      user_link = browser.find_element(
        By.XPATH, 
        f"(//a[@href='/admin/users/{user}'])[1]"
      )
      
      if not user_link.text == row[1]['Full Name'][:].split(' ')[0]:
        raise Exception
    except:
      user_not_found.append(email)
      continue
    else:
      user_link.click()
      fill_info(row, browser)

    browser.get(os.getenv('USERS_URL'))
    
  if len(user_not_found) > 0:
    for user in user_not_found:
      messagebox.showinfo(
        'User Not Found', f'{user} was not found on the website.'
      )
  
  return

def fill_info(row: tuple, browser: Chrome):
  set_dob(row, browser)
  time.sleep(1)
  set_contact(row, browser)
  set_emergency_contact(row, browser)
  set_comment(row, browser)
  set_payments(browser)
  
  return
  
  