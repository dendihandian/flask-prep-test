from config.app import APP_DEBUG, APP_SECRET_KEY
from flask import Flask

from blueprints.products import products

app = Flask(__name__)
app.config['SECRET_KEY'] = APP_SECRET_KEY

@app.route('/')
def hello():
    return 'Hello World!'

app.register_blueprint(products)

if __name__ == '__main__':
    app.run(debug=APP_DEBUG)
