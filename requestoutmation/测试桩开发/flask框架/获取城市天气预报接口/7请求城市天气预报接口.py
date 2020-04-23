import requests
from requests_toolbelt import MultipartEncoder

#192.168.0.103:8915, 0.0.0.0:5001
#args -- 传多个值时有问题
# url = "http://0.0.0.0:5001/weather/?cities=深圳"
# url = "http://192.168.0.103:8915/weather/?cities=深圳"
# res = requests.get(url)
# print(res.json())

#data
# url = "http://0.0.0.0:5001/weather/"
# data = ['深圳', '新化'] #传list不行
# data = '深圳'.encode('utf-8')
# res = requests.get(url, data=data)
# print(res)

#from
# url = "http://0.0.0.0:5001/weather/"
url = "http://192.168.0.103:8915/weather/"
data = {
    # 'cities': ['深圳', '新化'] #传列表不行，接口中只能取到第一个值
    'cities': '深圳'
}
res = requests.post(url, data=data)
print(res.json())
print(res.text)

#json
# url = 'http://b301226m73.wicp.vip/weather/'
# # url = "http://0.0.0.0:5001/weather/"
#
# data = {
#     'cities': ['深圳', '九江', '长沙', '新化']
# }
# res = requests.post(url, json=data)
# # print(res.status_code, res.json(), type(res.json()))
# print(res.json())