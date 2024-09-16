from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .config import Config

# Initialise l'extension SQLAlchemy
db = SQLAlchemy()

# Fonction pour créer l'application Flask
def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialise les extensions
    db.init_app(app)
    Migrate(app, db)

    # Enregistre les routes
    from .routes import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
