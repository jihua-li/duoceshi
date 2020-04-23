h = '''{"name": "carl"}'''
print(h, type(h))

#json序列化
import json
# json.dumps()
#接受两个参数，1列表参数，2文件对象
# json.dump()

#转化成普通字符串
# repr()

#反序列化
#将json转换成字典
# json.loads()
# json.load()


#练习，使用python的json模块，将json串
'''{"name": "dcs", "location": []}''' #修改成为：
'''{"name": "dcs", "age": 15, "location": ["shenzhen", "guangzhou"]'''

a = '''{"name": "dcs", "location": []}'''

b = json.loads(a)
print(b)
# b['age'] = 15
# b['location'] = ["shenzhen","guangzhou"]
# print(b)
# c = json.dumps(b)
# print(c, type(c))

import requests
url = "http://192.168.0.154:5001/v1/signature"
data =  {
    "signature": "xiaoxiao",
    "source": "shenzhen",
    "pics": ["dd"]
    }
header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36",
    "Content-Type": "application/json"
}

# res = requests.post(url, json=data, auth = ("lijihua", "lijihua198915"), headers = header)
# print(res.text)
# r = json.loads(res.text)
# assert isinstance(r['sign_id'], int), "接口请求失败"

'''练习2，编写一个方法，满足功能:传一个json数据，指定添加1个或多个 key-value，
返回新的json格式数据。 如:add_field(json_data="{"score": 100}", 
name="dcs", age=15) ，返回json数 据:{"score": 100, "name": "dcs", "age": 15}'''

def add_field(json_data, **kwargs):
    pass


#删除json串,单层
def del_field(json_data, *args):
    try:
        dic_data = json.loads(json_data)
    except:
        print("json格式转换失败", json_data)
        raise

    for i in args:
        if i in dic_data.keys():
            del dic_data[i]
        else:
            continue
    return json.dumps(dic_data)

# a = '''{"name":"xiaoming","age":20,"score":100}'''
# b = del_field(a,"age","hh","score")
# print(b)


#删除json串,多层
def del_fields(json_data, *args):
    try:
        dic_data = json.loads(json_data)
    except:
        print("json格式转换失败")
        raise

a = '''{"student":[{"name":"xiaoming","score":100},{"name":"xiaowang":"score":99}]}'''
