from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

path = '/Users/lijihua/Desktop/lijihua/duoceshi/software/chromedriver 3'
browser = webdriver.Chrome(executable_path=path)

browser.get('https://www.jd.com/')
# 1. 使用id，*代表所有标签
# inp = browser.find_element(By.XPATH, "//*[@id='key']")

# 2. 使用class
# inp = browser.find_element(By.XPATH, "//*[@class='text']")

# 4. 还可以使用其他属性
# inp = browser.find_element(By.XPATH, "//*[@aria-label='搜索']")
# inp = browser.find_element(By.XPATH, "//*[@type='text']")

# 1. 层级关系定位:如果某个标签的属性不明显，我们可以通过它的父节点开始找
inp = browser.find_element(By.XPATH, "//div[@id='header']/input")

# inp.send_keys('飞行器')
print(inp)


time.sleep(3)
browser.close()