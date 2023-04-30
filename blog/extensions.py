from flask_admin import Admin
from flask_combo_jsonapi import Api
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect

login_manager = LoginManager()
db = SQLAlchemy()
migrate = Migrate()
csrf = CSRFProtect()
admin = Admin(name='Admin panel', template_mode='bootstrap4', )
api = Api()
