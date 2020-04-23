from flask import Flask

"""
两种方式：
1、使用装饰器 @app.route()
2、使用app.add_url_rule()
"""


app = Flask(__name__)
app.debug = True

# @app.route('/hello/<name>/')
# def say_hello(name):
#     return 'hello tester {}'.format(name)
#
#
# if __name__ =='__main__':
#     app.run(host='0.0.0.0', port=5001)


def say_hello():
    a = 123456789
    return 'hello tester' + str(a)
app.add_url_rule('/', 'hello', say_hello)

if __name__ =='__main__':
    app.run()