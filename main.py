from config.app import APP_DEBUG, APP_SECRET_KEY
from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = APP_SECRET_KEY

@app.route('/')
def hello():
    return 'Hello World!'

if __name__ == '__main__':
    app.run(debug=APP_DEBUG)