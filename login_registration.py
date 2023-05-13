import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
driver = webdriver.Chrome()
driver.maximize_window()
#1
password = 'Test_pass851'
email = "J_Smith@testmail.ru"
home_url = 'https://practice.automationtesting.in/'
driver.implicitly_wait(10)

def registration (email,password,url):
    driver.get (url)
    #2
    my_acc_pg = driver.find_element("id", "menu-item-50")
    my_acc_pg.click()
    #3
    reg_email_field = driver.find_element("id", "reg_email")
    reg_email_field.send_keys(email)
    #4
    reg_pass_field = driver.find_element("id", "reg_password")
    reg_pass_field.send_keys(password)
    #5
    register_btn =driver.find_element("css selector", ".register .woocommerce-Button.button")
    register_btn.click()
   

def login (email,password,url): 
    driver.get (url)
    #2
    my_acc_pg = driver.find_element("id", "menu-item-50")
    my_acc_pg.click()
    #3
    reg_email_field = driver.find_element("id", "reg_email")
    reg_email_field.send_keys("J_Smith@testmail.ru")
    #4
    reg_pass_field = driver.find_element("id", "reg_password")
    reg_pass_field.send_keys("Test_pass851")
    #5 .
    login_btn =driver.find_element("css selector", "login .woocommerce-Button.button")
    login_btn.click()



registration (email,password,home_url)   

login (email,password,home_url)
   
driver.quit()