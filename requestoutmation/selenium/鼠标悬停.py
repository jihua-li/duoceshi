from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
import time, random

path = '/Users/lijihua/Desktop/lijihua/duoceshi/software/chromedriver 3'
browser = webdriver.Chrome(executable_path=path)
browser.get('https://www.baidu.com')

mouse = browser.find_element(By.LINK_TEXT, '设置')
ActionChains(browser).move_to_element(mouse).perform()

browser.find_element(By.LINK_TEXT, '高级搜索').click()

time.sleep(3)
browser.close()