from flask import Flask, render_template, request
from flask import Response, make_response

app = Flask(__name__)

# query parameter
@app.route('/area')
def area():
  # pi값이 주어지지 않으면 3.14를 주어라
  pi = request.args.get('pi', '3.14')
  radius = request.args['radius']
  s = float(pi) * float(radius) * float(radius)
  return 'pi={}, radius={}, area={}'.format(pi, radius, s)



@app.route('/login', methods=['GET', 'POST'])
def login():
  if request.method == 'GET':
    return render_template('03.login.html')
  else:
    # do the login process
    # uid = request.args.get('uid', '123')
    uid = request.form['uid']
    pwd = request.form['pwd']
    return 'uid={}, pwd={}'.format(uid, pwd)



@app.route('/response')
def response_fn():
  custom_res = Response('Custom Response', 200, {'test':'ttt'})
  return make_response(custom_res)



if __name__ == '__main__':
  app.run(debug=True)
