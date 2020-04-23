import requests, re, logging, json
from collections import Iterable, Iterator
from flask import Flask, request

logging.basicConfig(level=logging.INFO, format='%(asctime)16s - %(levelname)8s - %(message)s')



"""获取指定城市天气情况"""


# def get_weather(city):
#     res = requests.get('http://wthrcdn.etouch.cn/weather_mini?city={}'.format(city))
#     # logging.info('调用天气预报返回结果：{}'.format(res.json()))
#     data = res.json()['data']['forecast'][0]
#     fengli = re.search('.*?CDATA.*?<(.*?)]]>', data['fengli']).group(1)
#     # 获取纯粹的风力值
#     fengli = re.search('.*?CDATA.*?<(.*?)]]>', data['fengli']).group(1)
#     weathers = {}
#     weathers[city] = data['high'], data['low'], data['type'], data['fengxiang'], fengli
#     # return "{}: {} , {}, {}, {} {}".format(city, data['high'], data['low'], data['type'], data['fengxiang'], fengli)
#     return weathers
#
# # cities = ['北京', '上海', '广州', '深圳', '九江', '长沙', '新化']
# cities = ["新化"]
# for c in cities:
#     print(get_weather(c))



app = Flask(__name__)
app.debug = True

class WeatherIterator(Iterator):
    """实现一个迭代对象，next方法每次返回一个城市天气情况"""
    def __init__(self, cities):
        self.cities = cities
        self.index = 0

    def get_weather(self, city):
        logging.info('city: {}'.format(city))
        res = requests.get('http://wthrcdn.etouch.cn/weather_mini?city={}'.format(city))
        logging.info('调用天气预报返回结果：{}'.format(res.json()))
        data = res.json()['data']['forecast'][0]
        #获取纯粹的风力值
        fengli = re.search('.*?CDATA.*?<(.*?)]]>', data['fengli']).group(1)
        weathers = {}
        weathers[city] = data['low'], data['high'], data['type'], data['fengxiang'], fengli
        # return "{}: {} , {}, {}, {} {}".format(city, data['high'], data['low'], data['type'], data['fengxiang'],
        #                                        fengli)
        return weathers

    def __next__(self):
        if self.index == len(self.cities):
            raise StopIteration
        city = self.cities[self.index]
        self.index += 1
        return self.get_weather(city)

# @app.route('/weather/<cities>/')
class WeatherIterable(Iterable):
    """实现一个可迭代对象，__iter__方法返回一个迭代器对象"""
    def __init__(self, cities):
        self.cities = cities

    def __iter__(self):
        logging.info('cities: {}, type: {}'.format(self.cities, type(self.cities)))
        return WeatherIterator(self.cities)


@app.route('/weather/', methods=['POST', 'GET'])
def weather():
    if request.json:
        req_data = request.json
        logging.info('请求json数据: {}'.format(req_data))
        cities = req_data.get('cities')

    elif request.form:
        req_data = request.form
        logging.info('请求form数据: {}'.format(req_data))
        cs = [req_data['cities']]
        cities = []
        for c in cs:
            if c == 'shenzhen' or c == '深圳':
                cities.append('深圳')


    elif request.args:
        req_data = request.args
        cities = [req_data.get('cities')]
        logging.info('请求args数据: {}'.format(req_data))

    else:
        req_data = request.data.decode()
        logging.info('请求data数据: {}'.format(req_data))
        cities = [req_data]



    # req_data = request.json
    # logging.info('请求json数据: {}'.format(req_data))
    # cities = req_data.get('cities')

    logging.info('reqest data: {} , type: {}'.format(req_data, type(req_data)))
    logging.info('cities: {}'.format(cities))
    weathers = WeatherIterable(cities)
    ws = {}
    wl = []
    for w in weathers:
        wl.append(w)
        print(w)
    ws['weathers'] = wl
    # return req_data, 200
    return ws, 200




if __name__ =='__main__':
    app.run(host="192.168.0.103", port=8915)
    # app.run(host="0.0.0.0", port=5001)
#     # cities = ['北京', '上海', '广州', '深圳', '九江', '长沙', '新化']
#     # weathers1 = WeatherIterator(cities) #通过__next__方法实现可迭代
#     # print(weathers1)
#     # for w1 in weathers1:
#     #     print(w1)
#     # print("*" * 30)
#     # weathers2 = WeatherIterable(cities)
#     # print(weathers2)
#     # for w2 in weathers1:
#     #     print(w2)
#     # print(weather(cities))
