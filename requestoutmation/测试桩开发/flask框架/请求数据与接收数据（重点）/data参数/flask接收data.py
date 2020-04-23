from flask import Flask, redirect, url_for, request
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)16s - %(levelname)8s - %(message)s')


app = Flask(__name__)
app.debug = True

@app.route('/test/', methods=['POST', 'GET'])
def get_args():
    logging.info('[请求方式]：{}'.format(request.method))
    logging.info('[请求args]：{}'.format(request.args))
    # 1. requests客户端直接提交的字符串数据，会识别成为bytes数据，如果需要字符 ，需要自行解码
    # 2. requests客户端直接提交的字典数据，request.data会识别为 b
    logging.info('[请求data]: {} {}'.format(request.data, type(request.data)))
    logging.info('[data数据解析后结果]: {}'.format(request.data.decode()))
    logging.info('[尝试获取data中name参数]：{}'.format(request.args.get('name')))
    #若没有取到则使用默认值word
    logging.info('[没有取到name参数值，默认为]：{}'.format(request.args.get('name'), 'word'))
    #获取form数据
    logging.info('[请求form数据]：{}'.format(request.form, type(request.form)))
    logging.info('[尝试获取form中name参数值]：{}'.format(request.form.get('name')))
    #获取json
    logging.info('[请求json数据]：{} {}'.format(request.json, type(request.json)))
    #必须reture，不然会报错
    if request.data:
        return request.data
    elif request.form:
        return request.form
    else:
        return request.json
if __name__ =='__main__':
    app.run()