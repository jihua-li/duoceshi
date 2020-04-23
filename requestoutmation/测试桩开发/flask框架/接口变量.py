from flask import Flask



app = Flask(__name__)
app.debug = True

@app.route('/hello/<name>')
def say_hello(name):
    return 'hello tester {}'.format(name)


if __name__ =='__main__':
    app.run(host='0.0.0.0', port=5001)