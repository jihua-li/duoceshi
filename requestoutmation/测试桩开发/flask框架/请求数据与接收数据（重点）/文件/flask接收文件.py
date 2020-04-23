from flask import Flask, redirect, url_for, request
import logging, os

logging.basicConfig(level=logging.INFO, format='%(asctime)16s - %(levelname)8s - %(message)s')

#获取当前文件所在的目录
basedir = os.path.abspath(os.path.dirname(__name__))
#当前目录下需要创建这个文件夹
path = basedir + '/upload/'


app = Flask(__name__)
app.debug = True

@app.route('/test/', methods=['POST', 'GET'])
def get_args():
    logging.info('[请求方式]：{}'.format(request.method))
    logging.info('[请求args]：{}'.format(request.args))
    #接收文件内容
    logging.info('[接收文件]：{}'.format(request.files))
    file_obj = request.files.get('file_field_name')
    logging.info('[尝试获取文件字段对应内容]：{}'.format(file_obj))
    logging.info('[尝试获取文件名称]: {}'.format(file_obj.filename))
    # 读取文件内容，如果需要重复读取，需要调整指针file_obj.seek(0, 0)
    logging.info('[第一次读取文件内容]：{}'.format(file_obj.read()))
    logging.info('[第二次读取文件内容，没有调整指针]：{}'.format(file_obj.read()))
    #调整指针都初始位置
    file_obj.seek(0, 0)
    logging.info('[第三次读取文件内容，调整指针位置到初始位置]：{}'.format(file_obj.read()))
    #保存到服务器，仍然需要调整位置
    file_obj.seek(0, 0)
    file_path = path + file_obj.filename
    logging.info('[开始保存文件]')
    file_obj.save(file_path)
    logging.info('[保存文件成功]')
    return 'OK'


if __name__ =='__main__':
    app.run()