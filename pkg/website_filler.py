from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

def fill_website(file):
  try:
    browser = open_browser()
  except:
    print('Error: Could not open browser')
    return
  
  login(browser)
  browser.get('https://gocreate.com/admin/users')
  print('Success: got to users')
  
    

def set_browser():
  opts = Options()
  opts.add_argument('--headless')
  service = ChromeService(ChromeDriverManager().install())
  browser = Chrome(options=opts, service=service)
  return browser

def open_browser():
  browser = set_browser()
  browser.get('https://gocreate.com/login')
  return browser

def login(browser):
  username = browser.find_element(By.ID, 'username')
  if not username:
    return
  password = browser.find_element(By.ID, 'password')
  username.send_keys('ethanmw2000@gmail.com')
  password.send_keys('Viper135')
  button = browser.find_element(By.XPATH, "//button[@type= 'submit']")
  button.click()
  return
