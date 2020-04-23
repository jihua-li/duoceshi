#访问需要登录的地址：http://192.168.0.150:5001/login
#登录需要传csrf_token
import requests
import re

s= requests.session()

url = 'http://192.168.0.150:5001/login'
data = {
    "username": "lijihua",
    "password": "lijihua198915",
}

# get请求login 获取csrf_token
r = s.get(url)
print(r)
# 获取csrf_token
csrf_token = re.findall(r'csrf_token.*?value="(.*?)">-', r.text)
data["csrf_token"] = csrf_token

#第一次登录session自带cookie
rsu = s.post(url, data= data)
print(rsu.history)
#访问登录后才能访问的页面，session自带cookie
url2 = 'http://192.168.0.150:5001/user/lijihua'

res = s.get(url2)
# print(res.status_code)
# print(res.text, type(res.text))
print(res.history)
assert "资料编辑" in res.text, "进入用户页面接口请求失败"


#<<<<<<<<======>>>>>>>>>>

import requests, time, re

url = 'http://127.0.0.1:5001/login'

data = {
    "username": "dcs",
    "password": "123",
}
# get请求login页获取csrf_token
r = requests.get(url)
# 获取csrf_token
csrf_token = re.findall(r'csrf_token.*?value="(.*?)">-', r.text)
print(data)
data["csrf_token"] = csrf_token
print(data)
# # 登录
r2 = requests.post(url, data=data, cookies=r.cookies)
# # 获取重定向的cookie
print(r2.history)
cks = r2.history[0].cookies

# # 访问登录后才能访问的页面
url2 = 'http://127.0.0.1:5001/user/dcs'
r3 = requests.get(url2, cookies=cks)
# 直接使用r2的cookies无法登录，因为r2是被重定向后的结果
# r3 = requests.get(url2, cookies=r2.cookies)
print(r3.status_code)
# print(r3.text)

assert '资料编辑' in r3.text, "访问失败"