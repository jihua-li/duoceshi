import requests

url = 'http://0.0.0.0:5000/account/dcs'
# url = 'http://0.0.0.0:5000/account/?user=dcs'
res = requests.get(url)
print(res.text)