#! /usr/bin/python
# coding=utf-8

from time import sleep
from selenium import webdriver

driver = webdriver.Chrome()  # 初始化一个谷歌浏览器实例：driver
driver.maximize_window()  # 最大化浏览器
driver.get("http://www.126.com")
sleep(2)

driver.find_element_by_id("switchAccountLogin").click()

login_frame = driver.find_element_by_css_selector('iframe[id^="x-URS-iframe"]')  # 切换到 iframe（多表单切换法）
# login_frame = driver.find_element_by_id("x-URS-iframe")  # # 切换到 iframe（多表单切换法2）
# 切换
driver.switch_to.frame(login_frame)
driver.find_element_by_name("email").send_keys("username")
driver.find_element_by_name("password").send_keys("password")
driver.find_element_by_id("dologin").click()

# driver.switch_to.default_content()
# driver.quit()

# driver.find_element_by_id("lbNormal").click()  # 登录页面，点击切换到帐号密码登录方式
# result = driver.find_element_by_id("lbApp").is_displayed()   # 通过ID，检查某元素是否可见
# print(result)


