from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time, random

path = '/Users/lijihua/Desktop/lijihua/duoceshi/software/chromedriver 3'
browser = webdriver.Chrome(executable_path=path)

browser.get('https://www.baidu.com')
#定位搜索框
inp = browser.find_element(By.CSS_SELECTOR, '#kw')
#输入搜索内容
inp.send_keys('吃货')
#清空输入框内容
inp.clear()
#重新输入搜索内容
inp.send_keys('吃货')
#回车键
inp.send_keys(Keys.ENTER)

#设置隐形等待时间
wait = WebDriverWait(browser, 5)
#检查到指定元素存在时结束等待
wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'h3.t')))

#获取搜索结果
# lists = browser.find_elements(By.CSS_SELECTOR, 'div[id=content_left] div h3.t a')
# lists = browser.find_elements(By.CSS_SELECTOR, 'h3[class=t]>a')
# lists = browser.find_elements(By.CSS_SELECTOR, 'h3.t a')
lists = browser.find_elements_by_css_selector("h3.t>a")
# print(res)
for r in lists:
    print(r)

#设置隐形等待时间
# wait = WebDriverWait(browser, 5)

# time.sleep(5)

random_index = random.randint(0, 9)
print(random_index)
lists[random_index].click()




time.sleep(6)
browser.quit()