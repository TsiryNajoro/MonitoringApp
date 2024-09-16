from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Initialize the database object
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    
    # Configure the application
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:jojo@localhost/audit_db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    # Initialize the database with the app
    db.init_app(app)
    
    # Import and register blueprints or routes here if needed
    with app.app_context():
        from app.models import AuditLog  # Ensure this import is correct
    
    return app

# Check if this script is being run directly and not imported as a module
if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
