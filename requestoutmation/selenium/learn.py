from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
path = '/Users/lijihua/Desktop/lijihua/duoceshi/software/chromedriver 3'
browser = webdriver.Chrome(executable_path=path)

# browser = webdriver.Chrome()
# res = browser.get('http://www.baidu.com')
# print(res)



browser.get('https://www.jd.com/')
#1. 通过id查找京东input
# res1 = browser.find_element_by_id('key')
# res1.send_keys('飞行器')
# res1.send_keys(Keys.ENTER)
# print(res1)
#3. 通过链接查找京东“秒杀” 
wait = WebDriverWait(browser, 5)
wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'elevator_lk_txt')))
res3 = browser.find_element_by_link_text('京东秒杀')
print(res3)

# 2. 通过name查找淘宝input 
# browser.get('https://www.tmall.com/')
# res2 = browser.find_element_by_id('mq')
# res2.send_keys('飞行器')
# res2.send_keys(Keys.ENTER)







#4. 通过classname 查找京东左边栏 5. 通过css选择器，查找指定的：话费/机票 完成扣1

time.sleep(2)
browser.close()