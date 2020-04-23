from flask import Flask

app = Flask(__name__)

@app.route('/')
def say_hello():
    a = 12345678
    return 'hello tester' + str(a)


if __name__ =='__main__':
    app.run(host='0.0.0.0', port=5001)