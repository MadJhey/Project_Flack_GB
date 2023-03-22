from datetime import time

import werkzeug
from flask import Flask
from flask import Request

# __name__ имя файла
app = Flask(__name__)


@app.route('/<int:num>')
def index(num: int):
    return f'Hello {num}'


@app.before_request
def before_request():
    pass


@app.errorhandler(404)
def error_404(error):
    return f'error 404'
