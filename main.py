from config.app import APP_DEBUG, APP_SECRET_KEY
from flask import Flask

from blueprints.products_blueprint import products_blueprint

app = Flask(__name__)
app.config['SECRET_KEY'] = APP_SECRET_KEY

@app.route('/')
def hello():
    return 'Hello World!'

app.register_blueprint(products_blueprint)

if __name__ == '__main__':
    app.run(debug=APP_DEBUG)
