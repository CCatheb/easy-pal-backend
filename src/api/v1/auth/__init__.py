from flask import Blueprint

user_bp = Blueprint('auth', __name__, url_prefix='/api/v1')

from . import routes