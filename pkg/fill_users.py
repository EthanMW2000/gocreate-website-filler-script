from selenium.webdriver.common.by import By

def fill_users(file, browser):
  searchbar = browser.find_element(By.CSS_SELECTOR, 'search')
  