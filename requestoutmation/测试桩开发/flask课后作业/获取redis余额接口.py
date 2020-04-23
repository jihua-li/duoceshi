from flask import Flask, redirect, url_for, request
import logging, redis

logging.basicConfig(level=logging.INFO, format='%(asctime)16s - %(levelname)8s - %(message)s')

def get_redis_value(key):
    #连接redis
    pool = redis.ConnectionPool(host='148.70.194.135', port=6379, password='dcs123', db=0, decode_responses=True)
    re_db = redis.Redis(connection_pool=pool)
    res = re_db.get("tsms:{}:account".format(key))
    return res


app = Flask(__name__)
app.debug = True

#请求接口"http://0.0.0.0:5000/account/dcs"
@app.route('/account/<user>/', methods=['GET'])
def get_account(user):
    print('[传参user]：{}'.format(user))
    #获取redis中account值
    account = get_redis_value(user)
    return account

#请求接口"http://0.0.0.0:5000/account/?user=dcs"
# @app.route('/account/', methods=['GET'])
# def get_account():
#     user = request.args.get('user')
#     account = get_redis_value(user)
#     return account


if __name__ =='__main__':
    app.run(host="0.0.0.0", port=5000)
