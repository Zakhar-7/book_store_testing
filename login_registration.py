import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
global driver

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(7)
my_password = 'Test_pass851'
my_email = "J_Smith@testmail.ru"
home_url = 'https://practice.automationtesting.in/'


def registration (email,password,url):
    #1
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
   

def login_shop (email,password,url):
    #1
    driver.get (url)
    #2
    my_acc_pg = driver.find_element("id", "menu-item-50")
    my_acc_pg.click()
    #3
    login_field = driver.find_element("id", "username")
    login_field.send_keys(email)
    #4
    pass_field = driver.find_element("id", "password")
    pass_field.send_keys(password)
    #5
    login_btn =driver.find_element("css selector", ".login .woocommerce-Button.button")
    login_btn.click()
    #6 Добавьте проверку, что на странице есть элемент "Logout"


if __name__ == "__main__":
    # ========================= ниже раскомментировать строку с нужной функцией
    #registration (email,password,home_url)
    #login_shop (my_email,my_password,home_url)
    driver.quit()