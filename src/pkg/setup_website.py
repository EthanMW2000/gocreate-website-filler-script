from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import os
from dotenv import load_dotenv

def setup() -> Chrome:
  load_dotenv()
  try:
    browser = open_browser()
  except:
    print('Error: Could not open browser')
    return
  
  login(browser)
  browser.get(os.getenv('USERS_URL'))
  return browser
    

def set_browser() -> Chrome:
  opts = Options()
  opts.add_argument('--headless')
  service = ChromeService(ChromeDriverManager().install())
  browser = Chrome(options=opts, service=service)
  return browser

def open_browser() -> Chrome:
  browser = set_browser()
  browser.get(os.getenv('LOGIN_URL'))
  return browser

def login(browser: Chrome):
  username = browser.find_element(By.ID, 'username')
  if not username:
    return
  password = browser.find_element(By.ID, 'password')
  username.send_keys(os.getenv('ADMIN_USERNAME'))
  password.send_keys(os.getenv('PASSWORD'))
  button = browser.find_element(By.XPATH, "//button[@type= 'submit']")
  button.click()
  return
