from flask import Flask, redirect, url_for, request
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)16s - %(levelname)8s - %(message)s')


app = Flask(__name__)
app.debug = True


@app.route('/success/<name>/')
def success(name):
    return 'welcome {}'.format(name)



@app.route('/login/', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        logging.info('[请求表单是]：{}'.format(request.form))
        #处理post请求
        user = request.form['name']
        logging.info('[从表单取出的name值为]：{}'.format(user))
        #重定向到successs()
        return redirect(url_for('success', name=user))
    else:
        #处理其他（如get）请求
        logging.info('[get请求参数为]：{}'.format(request.args))
        #处理其他（如get）请求
        user = request.args.get('name')
        return redirect(url_for('success', name=user))


if __name__ =='__main__':
    app.run()