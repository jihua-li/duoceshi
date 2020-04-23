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