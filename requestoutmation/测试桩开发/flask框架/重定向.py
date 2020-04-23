from flask import Flask, redirect, url_for
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)16s - %(levelname)8s - %(message)s')

app = Flask(__name__)
app.debug = True

@app.route('/admin/')
def hello_admin():
    return 'hello admin'


@app.route('/guest/')
def hello_guest():
    return 'hello guest'


@app.route('/user/<name>')
def hello_user(name):
    logging.info('[name is {}]'.format(name))
    #根据url参数控制逻辑分支
    if name == 'admin':
        return redirect("http://0.0.0.0:5001/admin")
    elif name == 'guest':
        return redirect("http://0.0.0.0:5001/guest")
    else:
        return redirect("https://www.baidu.com/")

if __name__ =='__main__':
    app.run(host='0.0.0.0', port=5001)

