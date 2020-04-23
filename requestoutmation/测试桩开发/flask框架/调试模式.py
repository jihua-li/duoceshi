from flask import Flask
"""
两种方式：
# 1. 通过属性变量设置 app.debug = True app.run()
# 2. 通过参数设置 app.run(debug = True)
"""


#方法一
# app = Flask(__name__)
# app.debug = True
#
# @app.route('/')
# def say_hello():
#     a = 123456789
#     return 'hello tester' + str(a)
#
#
# if __name__ =='__main__':
#     app.run(host='0.0.0.0', port=5001)


#方法二
app = Flask(__name__)

@app.route('/')
def say_hello():
    a = 123456789
    return 'hello tester' + str(a)


if __name__ =='__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)