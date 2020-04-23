from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select
import time, random

path = '/Users/lijihua/Desktop/lijihua/duoceshi/software/chromedriver 3'

#打开浏览器
browser = webdriver.Chrome(executable_path=path)

#访问tsms登录页面
browser.get('http://www.captaintests.club')

#输入账号
input_user = browser.find_element(By.CSS_SELECTOR, '#inputUsername')
input_user.send_keys("carl")

#输入密码
input_passwd = browser.find_element(By.CSS_SELECTOR, '#password')
input_passwd.send_keys('lijihua198915')

#点击登录按钮
botton = browser.find_element(By.CSS_SELECTOR, '.btn.btn-lg.btn-primary.btn-block')
botton.click()

#获取登录后的cookies
cookie = browser.get_cookies()
print('get_cookies is: {}'.format(cookie))

time.sleep(3)
#请求登录后的页面
browser.get('http://www.captaintests.club/user/carl')

time.sleep(3)
#关闭浏览器
browser.quit()