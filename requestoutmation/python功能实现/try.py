import requests, logging, re
logging.basicConfig(level=logging.INFO, format='%(asctime)16s - %(levelname)8s - %(message)s')


def get_weather(city):
    res = requests.get('http://wthrcdn.etouch.cn/weather_mini?city={}'.format(city))
    # logging.info('调用天气预报返回结果：{}'.format(res.json()))
    data = res.json()['data']['forecast'][0]
    fengli = re.search('.*?CDATA.*?<(.*?)]]>', data['fengli']).group(1)
    return "{}: {} , {}, {}, {} {}".format(city, data['high'], data['low'], data['type'], data['fengxiang'], fengli)

# cities = ['北京', '上海', '广州', '深圳', '九江', '长沙', '新化']
# for c in cities:
#     print(get_weather(c))

a = ['s']
print(len(a))
# b = "['abcdef', 'xy']"
b = "('abcdef', 'xy')"
c = list(b)
d = ''.join(c)
print(c)
print([b])
print(d, type(d))