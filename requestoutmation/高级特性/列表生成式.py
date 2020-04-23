import requests
import json
import random
import string
from 函数式编程.函数式编程 import use_logging

url = "https://tieba.baidu.com/hottopic/browse/topicList"
header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36"
}

def get_baibu_tianbao(url, header):
    respons = requests.get(url, headers = header)
    return respons

res = get_baibu_tianbao(url, header)
# print(type(res))
# print(res.status_code)
# print(res.text)
res_json = res.json()
# print(type(res_json))
# print(res_json)
# print(res_json.json.dumps(res, ensure_ascii=False, sort_keys= True, indent= 2))


'''递归函数，下载图图片，随机函数'''
@use_logging('info')
def get_exp(getkey, resdict):
    exp = []
    def get_imag(get_key, res_dict):
        if isinstance(res_dict, dict):
            for k, v in res_dict.items():
                if k == get_key:
                    #把数据增加到exp中
                    exp.append(v)
                get_imag(get_key,v)
        elif isinstance(res_dict, list):
            for ele in res_dict:
                get_imag(get_key, ele)

    get_imag(getkey, resdict)
    return exp

# exp =get_exp("topic_pic", res_json)
# print(exp)

def write_imag(exp):
    for i in exp:
        # file_name = "image/%s.jpg" % ''.join(random.sample(string.ascii_lowercase, 5))
        file_name = "image/baidu.jpg"
        with open(file_name, 'wb') as fp:
            res = requests.get(i, headers = header)
            fp.write(res.content)#图片要通过二进制写进文件
            fp.close()

# write_imag(exp)


#列出当前路径下文件列表
import os

file = [d for d in os.listdir(".")]
# print(file)

#字典生成列表
dict = {"name":"carl","age":18}
l = [k+str(v) for k,v in dict.items()]
print(l)

#字符串大小写切换
a = ['Hello','WORD','ibm','Apple']
#转换成小写
b = [i.lower() for i in a]
# print(b)
#转换成大写
c = [i.upper() for i in a]
# print(c)


#随机生成字符
import random,string
def create_str2(num_int=0, num_letters=0, num_zh=0, num_pun=0):
    a = [random.choice(string.digits) for i in range(int(num_int))]
    b = [random.choice(string.ascii_letters) for i in range(int(num_letters))]
    c = [chr(random.randint(0x4e00, 0x9fbf)) for i in range(int(num_zh))]
    d = [random.choice(string.punctuation) for i in range(int(num_pun))]
    # print(a)
    ran_list = a + b + c + d
    # print(ran_list)
    random.shuffle(ran_list) #代码运行看起来加不加没什么变化
    # print(ran_list)
    return ''.join(ran_list)

# print(create_str2(2,2))


#随机生成指定号段的手机号码
t= '130,131,132,145,146,155,156,166,167,170,170,170,170,171,175,176,185,186'
t_list = t.split(',')
# print(t_list)
# c = [random.choice(t_list) + ''.join(random.sample(string.digits*10,11-len(random.choice(t_list)))) for i in range(10)]
c = [random.choice(t_list) + ''.join(random.sample(string.digits*10, 11-len(random.choice(t_list))))]
# print(c)


# print(string.digits*10)
# print(string.digits)


#列表转成字符串最快的方式
l = ''.join(a)
print(l)