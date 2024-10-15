# app/routes.py
from flask import Blueprint

# Define a Blueprint for the main routes
main_bp = Blueprint('main', __name__)

# Root route
@main_bp.route('/')
def root_route():
    return "This is the root Route!"

# Secondary route
@main_bp.route('/secondary')
def secondary_route():
    return "This is the secondary Route!"
