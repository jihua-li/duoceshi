from flask import Flask, redirect, url_for, request
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)16s - %(levelname)8s - %(message)s')


app = Flask(__name__)
app.debug = True


@app.route('/test/', methods=['POST', 'GET'])
def get_args():
    logging.info('[请求方式]：{}'.format(request.method))
    logging.info('[请求args]：{}'.format(request.args))
    logging.info('[尝试获取args中name参数值]：{}'.format(request.args.get('name')))
    #必须return, 不然会报错
    return request.args, 200


if __name__ =='__main__':
    app.run()