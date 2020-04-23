# from flask import Flask, render_template
import flask
app = flask.Flask(__name__)
app.debug = True

@app.route('/user/<name>/')
def index(name):
    return flask.render_template('hello.html', user_name=name)

if __name__ =='__main__':
    app.run(host='0.0.0.0', port=5000)