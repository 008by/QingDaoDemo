from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import  ActionChains
from selenium.webdriver.common.by import By
driver = webdriver.Firefox()
# driver.maximize_window()

driver.get("https://www.baidu.com/")
driver.find_element(By.ID,"kw").send_keys("taobao")
driver.find_element(By.ID,"su").click()



setting=driver.find_element_by_link_text("设置")
ActionChains(driver).move_to_element(setting).perform()


