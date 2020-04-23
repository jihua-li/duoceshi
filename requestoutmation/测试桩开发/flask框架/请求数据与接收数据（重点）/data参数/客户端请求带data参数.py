import requests

url = 'http://localhost:5000/test/?a=1'

#post请求也可以带args
# 1. 直接传字符 ，data=data，服务端会识别成为 data 参数，内容解析为字符串
# # data = 'hello'
# # 直接发"你好"会报错，必须进行编码
# data = 'hello你好'.encode('utf-8')
# res = requests.post(url, data=data)
# print(res.text)

# 2. 直接传字典，data=data，flask识别 到客户端发的data数据，会将其识别为form参数
# data = {"name": "黎记华"}
# res = requests.post(url, data=data)
# print(res.json())

# 3. 通过json关键字传参数，服务端会识别到data参数，但是是json ，同时json内容识别正常
data = {"name": "carl黎记华"}
res = requests.post(url, json=data)
print(res.json())

