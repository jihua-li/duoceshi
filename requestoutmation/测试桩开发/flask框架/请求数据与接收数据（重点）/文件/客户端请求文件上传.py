import requests
from requests_toolbelt import MultipartEncoder

url = 'http://localhost:5000/test/?a=1'


## 参数说明:
# ('name', (None, 'dcs')) 1. files字段名 2. 文件名 3. 文件内容
# 1. 如果文件名为None，文件内容是 个字符 ，则requests会将其视为 form内容发送
#  2. 如果文件名称为None，且文件内容为一个文件对象，则requests将其视为files 发送
files = {
    ('name', (None, 'testfile')),
    ('file_field_name', ('file', open('file', 'r'))) # "r"  式 与 "rb" 式都可
}

res = requests.post(url, files=files)
print(res.text)



#2. 使用requests_toolbelt库，同时提交form和files
# data = MultipartEncoder(
#     fields={
#         'field0': 'hello lijihua',
#         'field1': 'hello carl',
#         'file_field_name': ('file', open('file', 'rb')) #  件内容，只可rb 式打开
#     }
# )
# res = requests.post(url, data=data, headers={'Content_Type': data.content_type})
# print(res.text)