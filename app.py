import flask
from flask import Flask,render_template



#API  - Application programming interface 


#creat an flask app instance 

app = Flask(__name__)

@app.route('/')
def index():
    return flask.render_template('index.html')


@app.route('/test')
def test():
    return flask.render_template('test.html')

