import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_admin import Admin
import time
from flask_wtf.csrf import CSRFProtect



basedir = os.path.abspath(os.path.dirname(__file__)) #__file__ is the name of this file // default variable

app = Flask(__name__, static_folder = 'static',static_url_path='/static', template_folder = 'templates')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = '12345'
app.config['ADMIN_CREDENTIALS'] = ('admin', '12345')

csrf = CSRFProtect(app)
db = SQLAlchemy(app)

Migrate(app, db, render_as_batch=True)
admin = Admin(app)
db.create_all()

