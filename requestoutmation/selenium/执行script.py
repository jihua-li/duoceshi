from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
import time, random

path = '/Users/lijihua/Desktop/lijihua/duoceshi/software/chromedriver 3'
browser = webdriver.Chrome(executable_path=path)
browser.get('https://www.taobao.com/')

"""下拉进度条"""
# 通过js代码，来实现浏览器操作，下拉到最下
# browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
# browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
#
# # 弹出altert提示框
# browser.execute_script('alert("To Bottom)')


"""元素聚焦"""
target = browser.find_element(By.CSS_SELECTOR, 'li.mod.conve-item-6')
browser.execute_script('arguments[0].scrollIntoView()', target)

# time.sleep(3)
# browser.quit()