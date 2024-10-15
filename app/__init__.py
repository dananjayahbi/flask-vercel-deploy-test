# app/__init__.py
from flask import Flask

# Initialize the Flask application
def create_app():
    app = Flask(__name__)

    # Import routes from routes.py
    from .routes import main_bp
    app.register_blueprint(main_bp)  # Register the blueprint

    return app
