from flask import Flask, render_template, request
from flask import Response, make_response

import os
import glob

app = Flask(__name__)

# query parameter
@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
  dt = {'key1':'value1', 'key2':'value2'}
  return render_template('06.hello.html', name=name, dt=dt)


if __name__ == '__main__':
  app.run(debug=True)
