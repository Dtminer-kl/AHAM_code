from flask import Flask
from flask_sqlalchemy import SQLAlchemy

## initialize flask app and sqlalchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///funds.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    with app.app_context():
        from . import routes, models, errors
        db.create_all()

    return app
