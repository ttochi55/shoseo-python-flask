from flask import Flask
from routers.pages import router

app = Flask(__name__)
app.register_blueprint(router, url_prefix='/pages')

@app.route('/')
def index():
    return 'Index Page'

if __name__ == '__main__':
    app.run(debug=True)