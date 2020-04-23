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

#鼠标悬停
mouse = browser.find_element(By.LINK_TEXT, '设置')
ActionChains(browser).move_to_element(mouse).perform()

#点击选择框中的高级搜索
browser.find_element(By.LINK_TEXT, '搜索设置').click()


time.sleep(3)
s = browser.find_element(By.ID, 'nr')
Select(s).select_by_visible_text('每页显示50条')

browser.find_element(By.CSS_SELECTOR, 'div#gxszButton a.prefpanelgo').click()

time.sleep(5)
browser.quit()


