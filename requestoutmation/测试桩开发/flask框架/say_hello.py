from flask import Flask

#得到一个WSGI应用程序
app = Flask(__name__)

@app.route('/')
def say_hello():
    return "hello tester lijihua"


if __name__ =='__main__':
    app.run()