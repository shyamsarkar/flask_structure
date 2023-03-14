from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models import User

user_bp = Blueprint('user', __name__, url_prefix='/api/users')


@user_bp.route('/', methods=['POST'])
# @jwt_required
def create_user():
    data = request.json
    # if not data.get('email'):
    #     return jsonify({'message': 'Email is required'}), 400
    user = User(email=data.get('email'), password=data.get('password'))
    # if data.get('role'):
    #     role = Role.query.filter_by(name=data['role']).first()
    #     if role:
    #         user.roles.append(role)
    # user.save()
    return jsonify(user.to_dict()), 201


# @user_bp.route('/', methods=['GET'])
# @jwt_required
# def list_users():
#     users = User.query.all()
#     return jsonify([user.to_dict() for user in users]), 200


# @user_bp.route('/<int:id>', methods=['GET'])
# @jwt_required
# def get_user(id):
#     user = User.query.get(id)
#     if not user:
#         return jsonify({'message': 'User not found'}), 404
#     if user.id != get_jwt_identity() and 'admin' not in [role.name for role in user.roles]:
#         return jsonify({'message': 'Unauthorized'}), 401
#     return jsonify(user.to_dict()), 200


# @user_bp.route('/<int:id>', methods=['PUT'])
# @jwt_required
# def update_user(id):
#     data = request.json
