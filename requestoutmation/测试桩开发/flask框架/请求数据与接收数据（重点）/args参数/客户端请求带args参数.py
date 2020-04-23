from flask import Flask, redirect, url_for, request
import logging, requests

logging.basicConfig(level=logging.INFO, format='%(asctime)16s - %(levelname)8s - %(message)s')


#get请求只有args
# url = 'http://localhost:5000/test/?name=hello'
# res = requests.get(url)
# print(res.text)

#post请求带args参数
# url = 'http://localhost:5000/test/?name=hello'
# res = requests.post(url)
# print(res.text)

#使用params带args参数
url = 'http://localhost:5000/test/'
params = {"name": "lijihua"}
res = requests.get(url, params=params)
print(res.text, res.status_code)