from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import  ActionChains
from selenium.webdriver.common.by import By
from modularization_model.Login import Login

driver = webdriver.Firefox()
driver.maximize_window()
driver.get("http://localhost:8032/mymovie/admin.php/")
Login.user_login(driver,"123","123")
sleep(3)
Login.user_logout(driver)
