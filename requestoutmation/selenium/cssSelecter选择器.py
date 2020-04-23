from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

path = '/Users/lijihua/Desktop/lijihua/duoceshi/software/chromedriver 3'
browser = webdriver.Chrome(executable_path=path)

"""cssSelector常用定位方法"""
browser.get('https://www.jd.com/')
#1、通过标签
# input1 = browser.find_element(By.CSS_SELECTOR, "input")

#2、通过id
# input1 = browser.find_element(By.CSS_SELECTOR, '#key')

#3、通过class
# input1 = browser.find_element(By.CSS_SELECTOR, '.text')

#4、通过标签+classname组合，或者标签+id组合
# input1 =browser.find_element(By.CSS_SELECTOR, "input.text")
# input1 = browser.find_element(By.CSS_SELECTOR, "input#key")

#5、多个classname组合
# input1 = browser.fin_element(By.CSS_SELECTOR, ".XXX.XXX")

"""精准匹配"""
#6、精准匹配，标签下，属性名=属性值
# input1 = browser.find_element(By.CSS_SELECTOR, "input[id=key]")
# input1 = browser.find_element(By.CSS_SELECTOR, "input[class=text]")

#标签下，包含某个属性
input1 = browser.find_element(By.CSS_SELECTOR, "input[id]")

input1.send_keys('飞行器')
print(input1)


"""模糊匹配"""


time.sleep(3)
browser.close()