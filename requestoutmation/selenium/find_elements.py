from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

path = '/Users/lijihua/Desktop/lijihua/duoceshi/software/chromedriver 3'
browser = webdriver.Chrome(executable_path=path)

# browser.get('https://www.taobao.com/')
# goods = browser.find_elements(By.CSS_SELECTOR, '.goods-inner .list a')
# print(goods)
# for g in goods:
#     print(g.text)

#https://www.jd.com/
browser.get('https://www.jd.com/')
# lis = browser.find_elements(By.CSS_SELECTOR, '.J_cate ul li')
# lis = browser.find_elements(By.CSS_SELECTOR, 'div[class=fs_col1] ul li')
lis = browser.find_elements(By.CSS_SELECTOR, 'div[class="grid_c1 fs_inner"] ul li')


print(lis)

for l in lis:
    print(l.text)

time.sleep(3)
browser.close()