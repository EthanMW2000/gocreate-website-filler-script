import pandas as pd
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from tkinter.messagebox import Message


def fill_users(file: pd.DataFrame, browser: Chrome):
  user_not_found = []
  searchbar = browser.find_element(By.CSS_SELECTOR, 'search')
  file.reset_index()
  for index, row in file.iterrows():
    searchbar.send_keys(row.loc['Email'])
    firstName = row.loc['Full Name'].split(' ')[0]
    try:
      user = browser.find_element(By.XAPTH(f"//<>[text()='{firstName}']"))
    except:
      user_not_found.append(row.loc['Email'])
      continue
    else:
      user.click()
      fill_info(file, browser)
      
    searchbar.clear()
    
def fill_info(file: pd.DataFrame, browser: Chrome):
  print('') 