from flask import request, jsonify
from flask_jwt_extended import create_access_token, create_refresh_token, jwt_required, get_jwt_identity

from app.api.auth import api_auth_bp
from app.services.auth_service import AuthService


@api_auth_bp.post("/login")
def login():
    data = request.get_json()
    user = AuthService.authenticate(data.get("email"), data.get("password"))
    if not user:
        return jsonify({"error": "Invalid credentials"}), 401

    return jsonify(
        access_token=create_access_token(identity=str(user.id)),
        refresh_token=create_refresh_token(identity=str(user.id)),
    ), 200


@api_auth_bp.post("/register")
def register():
    data = request.get_json()
    user = AuthService.register(
        email=data.get("email"),
        password=data.get("password"),
        first_name=data.get("first_name"),
        last_name=data.get("last_name"),
    )
    if not user:
        return jsonify({"error": "Email already registered"}), 409

    return jsonify({"message": "Registration successful"}), 201


@api_auth_bp.post("/refresh")
@jwt_required(refresh=True)
def refresh():
    identity = get_jwt_identity()
    return jsonify(access_token=create_access_token(identity=identity)), 200