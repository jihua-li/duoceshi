from flask import Flask, request
import logging, json

logging.basicConfig(level=logging.INFO, format='%(asctime)16s - %(levelname)8s - %(message)s')


app = Flask(__name__)
app.debug = True

"""
{"code": -1, "msg": "authfail"}, 400 
{"code": 1, "msg": "lengthlimit"}, 403 
{"code": 1, "msg": "blackword"}, 403 
{"code": 0, "msg": "success"}"""

# a = '''{"name":"carl"}'''
# print(json.loads(a))

@app.route('/v1/3rd', methods=['POST'])
def receive_data():
    data= json.loads(request.data.decode())
    logging.info('[请求data]: {} {}'.format(data, type(data)))
    logging.info('content值为：{}'.format(data.get('content')))


    return {"code": 0, "msg": "success"}, 200

if __name__ =='__main__':
    app.run(host='192.168.0.103', port=8915)