from flask import jsonify, request, url_for
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.extensions import db
from app.models.post import Post
from app.models.user import User
from app.views import api_bp

@api_bp.route('/posts', methods=['GET'])
def get_posts():
    posts = Post.query.filter_by(is_deleted=False).all()
    return jsonify([post.to_dict() for post in posts])

@api_bp.route('/posts/<int:id>', methods=['GET'])
def get_post(id):
    post = Post.query.get_or_404(id)
    if post.is_deleted:
        return jsonify({'error': 'Post not found'}), 404
    return jsonify(post.to_dict())

@api_bp.route('/posts', methods=['POST'])
@jwt_required
def create_post():
    data = request.get_json()
    current_user = get_jwt_identity()
    user = User.query.get(current_user['id'])
    post = Post(title=data['title'], content=data['content'], user=user)
    db.session.add(post)
    db.session.commit()
    response = jsonify(post.to_dict())
    response.status_code = 201
    response.headers['Location'] = url_for('api.get_post', id=post.id)
    return response

@api_bp.route('/posts/<int:id>', methods=['PUT'])
@jwt_required
def update_post(id):
    data = request.get_json()
    post = Post.query.get_or_404(id)
    if post.is_deleted:
        return jsonify({'error': 'Post not found'}), 404
    post.title = data['title']
    post.content = data['content']
    db.session.commit()
    return jsonify(post.to_dict())

@api_bp.route('/posts/<int:id>', methods=['DELETE'])
@jwt_required
def delete_post(id):
    post = Post.query.get_or_404(id)
    if post.is_deleted:
        return jsonify({'error': 'Post not found'}), 404
    post.is_deleted = True
    db.session.commit()
    return '', 204

@api_bp.route('/users/<int:id>/posts', methods=['GET'])
def get_user_posts(id):
    posts = Post.query.filter_by(user_id=id, is_deleted=False).all()
    return jsonify([post.to_dict() for post in posts])

@api_bp.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    user = User(email=data['email'], password=data['password'])
    db.session.add(user)
    db.session.commit()
    response = jsonify(user.to_dict())
    response.status_code = 201
    response.headers['Location'] = url_for('auth.login')
    return response
