from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.bcrypt import Bcrypt
from blinker import Namespace

db = SQLAlchemy()

flask_bcrypt = Bcrypt()

socializer_signals = Namespace()
user_followed = socializer_signals.signal('user-followed')

from signal_handlers import *

def create_app(config=None):
    app = Flask(__name__)

    if config is not None:
        app.config.from_object(config)

    db.init_app(app)
    flask_bcrypt.init_app(app)

    return app
