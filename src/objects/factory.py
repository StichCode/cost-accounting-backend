from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from config.config import CONFIG

db = SQLAlchemy()
migrate = Migrate()


def create_app():
    app = Flask(__name__)
    app.config.from_object(CONFIG)
    db.init_app(app)
    migrate.init_app(app, db)

    from src.api import bp as api_bp
    app.register_blueprint(api_bp)
    return app


from models import models
