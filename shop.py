import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from login_registration import email, password, home_url#, 
from login_registration import login_shop
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)

login_shop (email, password, home_url)

driver.quit()