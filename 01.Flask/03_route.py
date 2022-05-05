from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
  return 'Hello Flask!!!'

# string type parameter
@app.route('/user/<uid>')
def string_fn(uid):
  return uid

# int type parameter
@app.route('/int/<int:number>')
def int_fn(number):
  return str(number * 100)

# float type parameter
@app.route('/float/<float:number>')
def float_fn(number):
  return str(number * 10)



@app.route('/path/<path:path>')
def path_fn(path):
  return '{}'.format(path)



@app.route('/login', methods=['GET', 'POST'])
def login():
  if request.method == 'GET':
    return render_template('03.login.html')
  else:
    # do the login process
    return render_template('02.welcome.html')

if __name__ == '__main__':
  app.run(debug=True)
