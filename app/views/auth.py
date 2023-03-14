from flask import jsonify, request
from flask_jwt_extended import create_access_token, create_refresh_token
from app.extensions import jwt
from app.models.user import User
from app.views import auth_bp

@jwt.user_loader_callback_loader
def user_loader_callback(identity):
   
