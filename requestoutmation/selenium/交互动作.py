from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
import time, random

path = '/Users/lijihua/Desktop/lijihua/duoceshi/software/chromedriver 3'
browser = webdriver.Chrome(executable_path=path)

url = 'http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'

browser.get(url)

# 切换到frame，可以了解成一个标签
# 需要切换到该frame下，id=iframeResult，面试会问
browser.switch_to.frame('iframeResult')
# 定位被拖拽的目标
dragg = browser.find_element(By.CSS_SELECTOR, '#draggable')
# 定位目标（拖拽到的位置）
dropp = browser.find_element(By.CSS_SELECTOR, '#droppable')

# 申请动作链对象
actions = ActionChains(browser)

# 定义执行的动作
actions.drag_and_drop(dragg, dropp)

#执行动作
actions.perform()

time.sleep(2)
browser.quit()
