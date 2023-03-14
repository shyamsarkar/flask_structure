from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models import Post

post_bp = Blueprint('post', __name__, url_prefix='/api/posts')


@post_bp.route('/', methods=['POST'])
@jwt_required
def create_post():
    data = request.json
    author_id = get_jwt_identity()
    post = Post(title=data['title'], body=data['body'], author_id=author_id)
    post.save()
    return jsonify(post.to_dict()), 201


@post_bp.route('/', methods=['GET'])
def list_posts():
    posts = Post.query.all()
    return jsonify([post.to_dict() for post in posts]), 200


@post_bp.route('/<int:id>', methods=['GET'])
def get_post(id):
    post = Post.query.get(id)
    if not post:
        return jsonify({'message': 'Post not found'}), 404
    return jsonify(post.to_dict()), 200


@post_bp.route('/<int:id>', methods=['PUT'])
@jwt_required
def update_post(id):
    data = request.json
    post = Post.query.get(id)
    if not post:
        return jsonify({'message': 'Post not found'}), 404
    if post.author_id != get_jwt_identity():
        return jsonify({'message': 'Unauthorized'}), 401
    post.title = data.get('title', post.title)
    post.body = data.get('body', post.body)
    post.save()
    return jsonify(post.to_dict()), 200


@post_bp.route('/<int:id>', methods=['DELETE'])
@jwt_required
def delete_post(id):
    post = Post.query.get(id)
    if not post:
        return jsonify({'message': 'Post not found'}), 404
    if post.author_id != get_jwt_identity():
        return jsonify({'message': 'Unauthorized'}), 401
    post.delete()
    return jsonify({'message': 'Post deleted'}), 200
