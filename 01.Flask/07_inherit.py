from flask import Flask, render_template, request
from flask import Response, make_response

import os
import glob

app = Flask(__name__)

# query parameter
@app.route('/child1/')
def child1():
  return render_template('07.child1.html')

@app.route('/child2/')
def child2():
  return render_template('07.child2.html')


if __name__ == '__main__':
  app.run(debug=True)
