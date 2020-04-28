"""
参考地址：
https://www.jianshu.com/p/0e7fc1b6b5cc
"""

"""
一、简介
介绍
urllib是python自带的一个包，里面有很多处理url的模块。
 主要模块：
     urllib.request: 请求模块
     urllib.error: 异常处理模块
     urllib.parse: url解析模块
官方文档
  https://docs.python.org/3/library/urllib.html
Python2和Python3
 Python2: urllib, urllib2
 Python3: urllib
Python 3.x中把urllib库和urilib2库合并成了urllib库。
"""

# 二、主要的模块
# urllib.request模块
# 先来一个简单的例子
# 获取并打印百度的页面 GET请求
import urllib.request

response = urllib.request.urlopen('http://www.baidu.com')
print(response.read().decode('utf-8'))
# urllib.request模块

# urllib.requeset.urlopen(url,data,timeout):
#   - 只传入url是get请求, 传入url和data是post请求
#   - tiomeout：超时时间
#   - 返回值: response对象

# response对象:
#   - read(): 获取字节类型的响应内容
#   - geturl(): 获取请求的那个url
#   - getheaders(): 获得响应头信息
#   - getcode(): 获取状态码
#   - readline(): 读取一行
#   - readlines(): 返回一个列表，列表中是每一行内容

# urllib.request.urlretrieve(url, path): 读取url内容，直接保存到本地
#   - 可以根据url获取图片
#   - 根据url下载视频
#   - 根据url下载网页
#   - 从Python2模块urllib（而不是urllib2）移植，在将来的某个时候可能会被弃用
# response实例
# 获取百度首页
# 查看对象中的一些属性
import urllib.request

url = 'http://www.baidu.com'
res_obj = urllib.request.urlopen(url)
print(res_obj.read())  # 可以获取二进制数据print(res_obj.readline())  # 按行读取print(res_obj.readlines())  # 获取多行 装入列表
print(res_obj.getcode())  # 服务器响应的状态码
print(res_obj.geturl())  # 响应的来源
print(res_obj.getheaders())  # 获取响应头

# urllib.request.urlretrieve实例
# urlretrieve 根据地址获取资源
import urllib.request

# 获取图片
img_url = 'https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1540200586434&di=751ff5eb97f7388184dac2447ddeb170&imgtype=0&src=http%3A%2F%2Fimgsrc.baidu.com%2Fimgad%2Fpic%2Fitem%2Ffc1f4134970a304e4aeda8dcdbc8a786c8175ccc.jpg'
# 传入 url路径 和 本地的路径（将来获取数据后保存到哪里）
urllib.request.urlretrieve(img_url,'./pengyou.jpg')

# 文本
text_url = 'http://www.baidu.com'
urllib.request.urlretrieve(text_url,'baidu.html')

# 视频
video_url = 'http://mvvideo11.meitudata.com/5bcc4b72dc93c4767.mp4?k=366fd214b835823cf8c2def8c6357e1c&t=5bd167d0'
urllib.request.urlretrieve(video_url,'xiaojiejie.mp4')

# urllib.parse模块
# quote() 编码
# 按照RFC规定 URL中不能出现 空格 中文,只允许一部分 ASCII字符（数字字母和部分符号），其他的字符（如汉字）是不符合 URL 标准的。所以，URL中使用其它字符就需要先进行编码。
# unquote() 解码
# 其功能和quote相反, 对编码的内容进行解码。
# urlencode()
# 对字典进行编码，把key-value这样的键值对转换成我们想要的格式，返回的是a=1&b=2这样的字符串
# quote和unquote实例
import urllib.parse

# https://baike.baidu.com/item/%E5%B0%8F%E5%A5%B6%E7%8B%97/3266312?fr=aladdin
# url编码
# RFC规定 url中不能出现 空格 中文

# http://image.baidu.com/search/index?tn=baiduimage&ps=1&ct=201326592&lm=-1&cl=2&nc=1&ie=utf-8&word=%E7%8B%97

# 对url中的中文进行编码
# quote把中文转成url编码
code = urllib.parse.quote('小奶狗')
print(code)

# 对url编码的内容 进行 解码
word = urllib.parse.unquote('%E5%B0%8F%E5%A5%B6%E7%8B%97')
print(word)

# urlencode实例
import urllib.parse

url = 'http://image.baidu.com/search/index?'
# http://image.baidu.com/search/index?tn=baiduimage&word=%E5%A5%B3%E6%9C%8B%E5%8F%8B

wd = '男朋友'
data = {
    'tn': 'baiduimage',
    'word': wd
}

# urlencode传入请求的数据对象 返回url编码后的字符串
query_string = urllib.parse.urlencode(data)
# print(query_string)
print(url + query_string)

# 三、请求头配置
# 配置请求头
# 谷歌浏览器
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
}
# 一般具有反爬虫的网站都会对请求头进行检查， 如果不携带请求头
# 服务器就会返回一个4xx的客户端相关的错误（甚至有的网站开发人员检查到爬虫后故意抛出5xx的服务器错误）。

# 携带请求头
import urllib.request

url = 'http://www.baidu.com/'

# 把爬虫伪装成 pc端的浏览器
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
}

# 创建请求对象
# 使用Request 传入 目标地址 请求参数 还有就是 字典形式的headers信息
request_obj = urllib.request.Request(url, headers=headers)

# urlopen的参数可以是简单的字符串 也可以是一个request请求对象
# 如果传入的是request请求对象则可以进行更高级的设置（比如设置headers）
response_obj = urllib.request.urlopen(request_obj)
print(response_obj.read())

# POST请求
# ajax的post请求

import urllib.request
import urllib.parse

# 要请求的接口（手机端百度翻译的api接口，PC端的有验证 ）
url = 'https://fanyi.baidu.com/sug'

"""
PC端百度翻译api接口需要的参数，sign是一个动态生成的值。每一次需要翻译的时候sign的值都会不一样
data = {
    'from': 'en',
    'to': 'zh',
    'query': 'wolf',
    'transtype': 'realtime',
    'simple_means_flag': '3',
    'sign': '275695.55262',
    'token': '67e2544c4cead16b8f4a9ac1c88e99d9',
}
"""
form_data = {
    'kw': '你好'
}
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
}

# 如果没有请求头 headers 会被反爬
# 注意 传入的表单数据 需要是二进制数据， 所以我们需要对它进行编码
form_data_str = urllib.parse.urlencode(form_data)
# print(form_data_str)
# 把字符串变成二进制
bytes_data = form_data_str.encode()
# print(bytes_data)

request_obj = urllib.request.Request(url, data=bytes_data, headers=headers)
response_obj = urllib.request.urlopen(request_obj)
# 二进制变字符串 decode 解码
# 要把Unicode符号 中的中文显示出来 需要使用 unicode_escape进行解码
print(response_obj.read().decode('unicode_escape'))

# 四、URLError和HTTPError
# Python中写爬虫程序时，可以使用urllib.error来接收urllib.request产生的异常。urllib.error有两个方法，URLError和HTTPError。

# URLError是OSError的一个子类，HTTPError是URLError的一个子类，服务器上HTTP的响应会返回一个状态码，根据这个HTTP状态码，我们可以知道我们的访问是否成功。

# URLError
from urllib import request
from urllib import error


#一个不存在的连接
url = "https://www.baidu.com/"
req = request.Request(url)
try:
    response = request.urlopen(req)
    html = response.read().decode('utf-8')
    print(html)
except error.URLError as e:
    print(e.reason)

# HTTPError
from urllib import request
from urllib import error

#一个不存在的连接
url = "https://www.baidu123321.com"
req = request.Request(url)
try:
    responese = request.urlopen(req)
except error.HTTPError as e:
    print(e.code)

# 一起使用
from urllib import request
from urllib import error

url = "https://www.baidu123321.com"
req = request.Request(url)
try:
    response = request.urlopen(req)
    print("It's OK!")               # 正常
except error.HTTPError as error:    # HTTP错误
    print('HTTPError')
    print('ErrorCode: %s' % error.code)
except error.URLError as error:     # URL错误
    print(error.reason)

# 输入正确url时，以www.baidu.com为例
#  It's OK!

# 输入一个不存在的域名时  URL错误
#  [Errno 11001] getaddrinfo failed

# 输入一个正常的域名，但是不存在的资源时  HTTP错误
# HTTPError
# ErrorCode: 404
# 用HTTPError和URLError一起捕获异常，那么需要将HTTPError放在URLError的前面，因为HTTPError是URLError的一个子类。如果URLError放在前面，出现HTTP异常会先响应URLError，这样HTTPError就捕获不到错误信息了。
