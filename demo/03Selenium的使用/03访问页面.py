from selenium import webdriver
from selenium.webdriver.common.by import By

# 浏览器chrome browser对象初始化
browser = webdriver.Chrome()
# 访问头条首页
browser.get('https://www.toutiao.com')
# 打印网页源代码
print("browser.page_source = ", browser.page_source)

lis = browser.find_elements(By.CSS_SELECTOR, '.service-bd li')
# 关闭浏览器chrome browser对象
browser.close()
