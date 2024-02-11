
from flask import request
from pal_utils import logger_factory
from . import user_bp

logger = logger_factory.CustomLogger.get_logger("USER")

@user_bp.route("/login", methods=["POST"])
def login():

    data = request.get_json()

    logger.info("Login command received!")
    username = data["username"]
    password = data["password"]
    
    if username is None or password is None:
        logger.error("Username, email, or password is missing. Cannot proceed to login.")
        return "No user or password given.", 400
    
    if '@' in username:
        return f"<p>Connexion réussie avec l'email {username}!</p>"
    else:
        return f"<p>Connexion réussie pour l'utilisateur {username}!</p>"

@user_bp.route("/register")
def register():
    #TODO: implement register logic
    return "<p>Register page</p>"

@user_bp.route("/reset-password")
def reset_password():
    #TODO: implement reset password logic
    return "<p>Change password</p>"