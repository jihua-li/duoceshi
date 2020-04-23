from flask import Flask

app = Flask(__name__)
app.debug = True

# @app.route('/hello/<name>/<int:age>/')
# def say_hello(name, age):
#     return 'hello {}, you age is {}'.format(name, age)

@app.route('/hello/<name>/<float:height>/')
def say_hello(name, height):
    return 'hello {}, you age is {}'.format(name, height)


if __name__ =='__main__':
    app.run(host='0.0.0.0', port=5001)