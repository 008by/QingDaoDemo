from selenium import webdriver
from time import sleep,ctime
from selenium.webdriver.common.action_chains import  ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import  WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
import  logging

# logging.basicConfilogging.DEBUG)g(level=
driver = webdriver.Firefox()
driver.get("http://localhost:8032/test/checkboxdemo.html")
# driver.find_element_by_id("31").click()
select=Select(driver.find_element_by_name("fruit"))
# select.select_by_index(2) 索引值从0开始计数
select.select_by_value()
select.select_by_visible_text()
# element = driver.find_element_by_tag_name("video")
# element =driver.find_element_by_id("preview-player_html5_api")
# url=driver.execute_script("return arguments[0].currentSrc;", element)
# print(url)
#
# driver.get_screenshot_as_file("d:\\demo\\aaaa18.png")
# driver.close()
# driver.quit()
# driver.execute_script("arguments[0].play()",element)


# driver.execute_script("window.scrollTo(100,300)")
# sleep(3)
# driver.get("http://localhost:8032/test/06Alert.html")
# driver.find_element_by_id("btn3").click()
# a=driver.switch_to.alert
# sleep(2)
# print(a.text)
# a.accept()
# a.dismiss()
# a.send_keys("hello")


# driver.get("http://localhost:8032/mymovie/")
# # print(driver.get_cookies())
# driver.add_cookie({'name':'username','value':'lhz'})
# for cookie in driver.get_cookies():
#     print("%s -> %s" %(cookie['name'],cookie['value']))
# search_windows = driver.current_window_handle
# driver.find_element_by_link_text("新闻").click()
# all_handles = driver.window_handles
# for handle in all_handles:
#     if handle==search_windows:
#         driver.switch_to.window(handle)
#         print(driver.title)


# driver.get("http://localhost:8032/test/frame.html")
# driver.switch_to.frame("leftframe")

# xf =driver.find_element_by_xpath("//*[@src='left.html']")
# driver.switch_to.frame(xf)
# driver.find_element_by_id("uname").send_keys("hello")
# driver.switch_to.default_content()
# print(driver.title)
# fruit = driver.find_elements_by_tag_name("input")
# for i in fruit:
#     if i.get_attribute('type') == 'checkbox':
#         i.click()
#         sleep(1)

# fruit = driver.find_elements_by_xpath("//input[@type='checkbox']")
# for i in fruit:
#     i.click()
#     sleep(1)
# print(fruit)
# driver.find_elements_by_xpath("//input[@type='checkbox']").pop().click()
# element =WebDriverWait(driver,5,0.5).until(EC.presence_of_element_located(By.NAME,"username"))
# driver.find_element(By.NAME,"username").send_keys("admin")
# text = driver.find_element(By.NAME,"username").text
# size =driver.find_element(By.NAME,"username").size
# attribute = driver.find_element(By.NAME,"username").get_attribute("class")
# display =  driver.find_element(By.NAME,"username").is_displayed()
# print(text)
# print(size)
# print(attribute)
# print(display)
# driver.find_element_by_name("password").send_keys("admin")
# driver.find_element_by_name("password").submit()

# driver.find_element_by_name("password").send_keys(Keys.TAB)

#driver.find_element_by_xpath("//input[@type='submit']").click()
