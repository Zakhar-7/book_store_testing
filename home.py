import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
driver = webdriver.Chrome()
driver.maximize_window()
#1
driver.get ('https://practice.automationtesting.in/')
driver.implicitly_wait(10)
#2 
driver.execute_script("window.scrollBy(0, 600);")
#3
Ruby_read_more_btn = driver.find_element("css selector", '.product_tag-ruby > a:nth-child(2)')
Ruby_read_more_btn.click()
#4
reviews_tab = driver.find_element("css selector", '.reviews_tab > a')
reviews_tab.click()
#5
five_star = driver.find_element("css selector", '.star-5')
five_star.click()
#6
comment = driver.find_element("id", 'comment')
comment.send_keys("Nice book!")
#7
name_field = driver.find_element("id","author" )
name_field.send_keys("John")
#8
email_field = driver.find_element("id", "email")
email_field.send_keys("J_Smith@testmail.ru")
#9
submit_btn = driver.find_element("id", "submit")
submit_btn.click()