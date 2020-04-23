from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select
import time, random

path = '/Users/lijihua/Desktop/lijihua/duoceshi/software/chromedriver 3'
browser = webdriver.Chrome(executable_path=path)
browser.get('https://www.baidu.com/')

"""隐式等待"""
#第一个参数浏览器对象，第二个参数，等待市场（s），第三个参数多久查询一次（s）,默认0.5s一次
wait = WebDriverWait(browser, 10, poll_frequency=1)

input = wait.until(lambda x: x.find_element(By.CSS_SELECTOR, '#kw'))

input.send_keys('hello word')

time.sleep(3)
browser.quit()

"""显式等待"""