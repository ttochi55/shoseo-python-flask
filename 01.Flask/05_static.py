from flask import Flask, render_template, request
from flask import Response, make_response

import os
import glob

app = Flask(__name__)

# query parameter
@app.route('/')
def index():
  img_file = os.path.join(app.root_path, 'static/img/cat.jpeg')
  mtime = int(os.stat(img_file).st_mtime)
  return render_template('05.index.html', mtime=mtime)


if __name__ == '__main__':
  app.run(debug=True)
