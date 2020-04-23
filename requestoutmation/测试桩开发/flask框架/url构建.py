from flask import Flask, redirect, url_for
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)16s - %(levelname)8s - %(message)s')


"""实际使用中，跳转url时不会会直接使用url地址，而是使用url_for方法找到对应的url。url_for接收一个函
数名称(字符串)，通过这个函数名称，找到与之绑定的url，发起请求"""


app = Flask(__name__)
app.debug = True

@app.route('/admin/')
def hello_admin():
    return 'hello admin'


@app.route('/guest/<guest>/')
def hello_guest(guest):
    return 'hello {}'.format(guest)


@app.route('/user/<name>/')
def hello_user(name):
    logging.info('[name is {}]'.format(name))
    #根据url参数控制逻辑分支
    if name == 'admin':
        # return redirect("http://0.0.0.0:5001/admin")
        #获取并返回hello_admin函数绑定的URL
        return redirect(url_for('hello_admin'))
    else:
        # return redirect("http://0.0.0.0:5001/guest")
        # 获取并返回hello_guest函数绑定的URL
        return redirect(url_for('hello_guest', guest=name))


if __name__ =='__main__':
    app.run(host='0.0.0.0', port=5001)

