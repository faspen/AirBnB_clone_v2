#!/usr/bin/python3
""" Start flask"""


from flask import Flask


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello():
    """ Say hello """
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    """ Say hbnb """
    return 'HBNB'


@app.route('/c/<text>')
def c_is_fun(text):
    """ C is fun """
    return 'C {}'.format(text.replace('_', ' '))


@app.route('/python/')
@app.route('/python/<text>')
def python_is_cool(text='is cool'):
    """ Display python followed by text """
    return 'Python {}'.format(text.replace('_', ' '))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
