'''第七周课后作业：
1. 写一个正则表达式，匹配出：http://www.captaintests.club/user/{你的用户名}/sign下的所有表格内容，包括：创建时间/签名id/签名内容/审核状态
2. 将这个上述的正则表达式和session登录结合，封装成一个方法。功能：接收参数：查找类型/用户名/密码，
返回一个列表。def(reg_type, user=xxx, passwd=xxx)  return list。注意：查找类型指定本次匹配的是签名web还是模版web内容
3. 把之前写的一些用例，包括：签名正常/异常；模版正常/异常；迁移到unittest框架中，注意合理处理前置和后置
4. 迁移完成后，试着使用run_all_cases_01.py批量执行一下'''

from tsms.tsms_base import Tsmstest
import requests, re

ts = Tsmstest()
s = requests.session()
# http://www.captaintests.club/user/lijihua/sign
#登录页面地址
url = 'http://www.captaintests.club/login'
data1 = {
    "username": "carl",
    "password": "lijihua198915",
}
#进入登录页面
r = s.get(url)
# print(res.text,type(res)
#从登录页面的html中获取csrf_token，正则提取
csrf_token = re.findall(r'<input.*?id="csrf_token".*?value="(.*?)">-',r.text)
# print(csrf_token)
#将提取到的csrf_token添加到登录数据data1中
data1['csrf_token']= csrf_token[0]
# print(data1)
#登录
res1 = s.post(url, data1)
# print(res.history)
# print(res.status_code, res.cookies)
# print(res.text,type(res))
assert '登录' in res1.text, "登录接口请求失败"

#访问登录后才能访问的页面
url1= 'http://www.captaintests.club/user/carl/sign'
res2 = s.get(url1)
# print(res2.text)

#获取页面表格中 创建时间/签名id/签名内容/审核状态
# result = re.findall('<tr>.*?<p>(.*?)</p>.*?<p>(.*?)</p>.*?<p>(.*?)</p>.*?<p>(.*?)</p>.*?</tr>', res2.text, re.S)
# print(len(result))
# for r in result:
#     print(r[0],r[1],r[2],r[3])


# url = 'http://www.captaintests.club/login'

#方法一，将login单独封装成一个接口
# def log_in(url, user= 'carl', passwd= 'lijihua198915'):
#     '''登录接口封装'''
#     s = requests.session()
#     # 登录页面地址
#     data1 = {
#         "username": user,
#         "password": passwd,
#     }
#     # 进入登录页面
#     r = s.get(url)
#     # 从登录页面的html中获取csrf_token，正则提取
#     csrf_token = re.findall(r'<input.*?id="csrf_token".*?value="(.*?)">-', r.text)
#     # 将提取到的csrf_token添加到登录数据data1中
#     data1['csrf_token'] = csrf_token[0]
#     # 登录
#     s.post(url, data1)
#     return s
#
# def get_page_content(req_type, url):
#     '''获取签名/模版页面表格中的内容'''
#     login_url = 'http://www.captaintests.club/login'
#     s= log_in(login_url)
#     if req_type == 'sign':
#         res = s.get(url)
#     else:
#         res = s.get(url)
#     # 正则提取页面表格中的内容
#     result = re.findall('<tr>.*?<p>(.*?)</p>.*?<p>(.*?)</p>.*?<p>(.*?)</p>.*?<p>(.*?)</p>', res.text, re.S)
#     return result

#
# def get_page_content(req_type, url, user = 'carl', passwd = 'lijihua198915'):
#     '''获取签名/模版页面表格中的内容'''
#     s =requests.session()
#     # 登录页面地址
#     login_url = 'http://www.captaintests.club/login'
#     data1 = {
#         "username": user,
#         "password": passwd,
#     }
#     # 进入登录页面
#     r = s.get(login_url)
#     # 从登录页面的html中获取csrf_token，正则提取
#     csrf_token = re.findall(r'<input.*?id="csrf_token".*?value="(.*?)">-', r.text)
#     # 将提取到的csrf_token添加到登录数据data1中
#     data1['csrf_token'] = csrf_token[0]
#     # 登录
#     res1 = s.post(login_url, data1)
#     if req_type == 'sign':
#         res = s.get(url)
#     else:
#         res = s.get(url)
#
#     # 正则提取页面表格中的内容
#     result = re.findall('<tr>.*?<p>(.*?)</p>.*?<p>(.*?)</p>.*?<p>(.*?)</p>.*?<p>(.*?)</p>', res.text, re.S)
#     return result

# sign_url = 'http://www.captaintests.club/user/carl/sign'
# temp_url = 'http://www.captaintests.club/user/carl/sign/113'
# gpc = get_page_content('sign', sign_url)
# # gpc = get_page_content('temp', temp_url)
# print(gpc)


'''第八周课后作业：
1. tsms_web模块中，还有剩余一个匹配模版表格的方法没有编写，把这个方法补充一下，自己调试通过才行哦
2. 大家把上节课的数据驱动的作业继续完成一下，保证数据驱动的执行结果都是通过的
3. 复习一下装饰器的原理和写法，下节课讲错误重试机制会用到
4. 上周的课程主要是学习参数化与封装的思路和数据驱动，这两块的内容偏理解性多一点，要想真正的用好，还需要大量的实战演练，希望大家每天抽出一点时间学习和巩固'''

#循环
i = 20
# for x in range(i):
#     print('hello')
#     i -=1

while i >0:
    print('hello')
    i -=1

'''第九周课后作业：
1. 掌握错误重试机制，带参数的装饰器最好能自己写出来
2. 熟悉业务逻辑流程，理解同步和异步调用
3. 预习基本的sql，下节课会开始讲python数据库操作模块
4. 预习一下redis，重点看看有哪些命令字，哪些数据类型
注意：特别是不熟悉的同学，就更要提前看预习一下了，不然学起来会有点吃力的哈
5. 大家有条件的话，可以选择在自己电脑上安装一个虚拟机：推荐ubuntu16.04，后续的实操会用的比较频繁'''

'''第十周课后作业：
1. 掌握records库的用法，一定要熟悉，很重要，大家可以用生产的数据库练习，特别对数据库操作不多的同学，可以多练练，注意使用自己的表
2. 改造用例，创建/审核 模版，断言需要的 真实结果，从db去拿(之前是从前端拿的)
3. 预习db操作后面的内容，包括：数据的更新，数据的删除'''