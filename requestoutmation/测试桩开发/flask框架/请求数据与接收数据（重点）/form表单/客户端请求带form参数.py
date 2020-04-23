import requests
from requests_toolbelt import MultipartEncoder

url = 'http://localhost:5000/test/?a=1'


# 1. 直接传字典，data=data，flask识别 到客户端发的data数据，会将其识别为form参数
# data = {"name": "黎记华"}
# res = requests.post(url, data=data)
# print(res.json())


#2. 通过multipart/form-data(一般是用来提交文件)，构造一个MultipartEncoder来提交表单
data = MultipartEncoder(
    fields={
        "field0": "value0",
        "field1": "value1"
    }
)
res = requests.post(url, data=data, headers={'Content_Type': data.content_type})
print(res.json())