
class Login():
    # 登录
    def user_login(driver,username,password):
        driver.find_element_by_name("username").send_keys(username)
        driver.find_element_by_name("password").send_keys(password)
        driver.find_element_by_class_name('sub').click()
        driver.switch_to.default_content()

    # 退出
    def user_logout( driver):
        driver.find_element_by_link_text("退出").click()
        driver.quit()