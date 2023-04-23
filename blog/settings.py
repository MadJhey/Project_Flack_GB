import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
SECRET_KEY = os.environ.get("SECRET_KEY")
DATABASE_PASSWORD = os.environ.get("DATABASE_PASSWORD")
FLASK_DEBUG = True
SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
SQLALCHEMY_TRACK_MODIFICATIONS = False
WTF_CSRF_ENABLED = True
FLASK_ADMIN_SWATCH = 'cerulean'

OPENAPI_URL_PREFIX = '/api/swagger'
OPENAPI_VERSION = '3.0.0'
OPENAPI_SWAGGER_UI_PATH = '/'
OPENAPI_SWAGGER_UI_VERSION = '3.51.1'  # see version on https://cdnjs.com/libraries/swagger-ui
