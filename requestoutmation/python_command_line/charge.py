#coding=utf-8
import requests, sys, getopt, json

user, sum = None, 0
keys, values = getopt.getopt(sys.argv[1:], '-u:-c:', ['user=', 'sum='])
for key, value in keys:
    if key in ('-u', '--user'):
        user = value
    if key in ('-c', '--sum'):
        sum = value
if not user:
    print('用户账号为空')
    sys.exit(1)
if not sum:
    sum = 1000

# print(user,charge)

url = 'http://192.168.0.125:5001/v2/charge'
data = {
    "user": user,
    "charge": sum
        }

res = requests.post(url, json=data, auth=('root', '123'))
print(res.status_code, res.text)