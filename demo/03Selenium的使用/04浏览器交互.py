from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# 浏览器对象
browser = webdriver.Chrome()
# 访问头条主页
browser.get('https://www.toutiao.com/')
# 获取文本框
input = browser.find_element(By.CLASS_NAME, 'tt-input__inner')
# 输入关键词
input.send_keys('Python大星')
# 获取按钮节点
button = browser.find_element(By.CLASS_NAME, 'tt-button')
# 点击按钮
button.click()
# 暂停1s
time.sleep(1)
# 清除文本内容
input.clear()
# 输入关键词
input.send_keys('趣说爬虫')
# 获取按钮节点
button = browser.find_element(By.CLASS_NAME, 'tt-button')
# 点击按钮
button.click()
