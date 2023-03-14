from flask import Blueprint, jsonify, request
# from flask_jwt_extended import jwt_required
# from flask_restful import Api, Resource

# from app import db, bcrypt
# from app.models import User

api_bp = Blueprint('views', __name__,url_prefix='/api')
# views_api = Api(api_bp)url_prefix


@api_bp.route('/')
def Index():
    # obj = User(email="Shyam", password="123")
    # obj.save()
    return "Inside API Home"

# class UserView(Resource):
#     @jwt_required
#     def get(self, user_id):
#         user = User.query.filter_by(id=user_id).first()
#         if user:
#             return jsonify({'id': user.id, 'username': user.username, 'email': user.email})
#         else:
#             return {'error': 'User not found'}, 404

#     def post(self):
#         data = request.get_json()
#         username = data['username']
#         email = data['email']
#         password = bcrypt.generate_password_hash(data['password']).decode('utf-8')

#         user = User(username=username, email=email, password=password)
#         db.session.add(user)
#         db.session.commit()

#         return jsonify({'id': user.id, 'username': user.username, 'email': user.email}), 201

# class PostView(Resource):
#     def get(self, post_id):
#         post = Post.query.filter_by(id=post_id).first()
#         if post:
#             return jsonify({'id': post.id, 'title': post.title, 'body': post.body})
#         else:
#             return {'error': 'Post not found'}, 404

#     def post(self):
#         data = request.get_json()
#         title = data['title']
#         body = data['body']

#         post = Post(title=title, body=body)
#         db.session.add(post)
#         db.session.commit()

#         return jsonify({'id': post.id, 'title': post.title, 'body': post.body}), 201

# views_api.add_resource(UserView, '/user', '/user/<int:user_id>')
# views_api.add_resource(PostView, '/post', '/post/<int:post_id>')







# from flask import Blueprint, jsonify, request
# from flask_jwt_extended import jwt_required, get_jwt_identity

# from app.models.post import Post
# from app.models.user import User

# api_bp = Blueprint("api", __name__)

# @api_bp.route("/posts", methods=["GET"])
# @jwt_required
# def get_posts():
#     """
#     Returns a list of all posts
#     """
#     posts = Post.query.filter_by(deleted=False).all()
#     return jsonify([post.to_dict() for post in posts])

# @api_bp.route("/posts", methods=["POST"])
# @jwt_required
# def create_post():
#     """
#     Creates a new post
#     """
#     user_id = get_jwt_identity()
#     user = User.query.get(user_id)

#     title = request.json.get("title")
#     content = request.json.get("content")

#     post = Post(title=title, content=content, user=user)
#     post.save()

#     return jsonify(post.to_dict())

# @api_bp.route("/posts/<int:post_id>", methods=["GET"])
# @jwt_required
# def get_post(post_id):
#     """
#     Returns a specific post
#     """
#     post = Post.query.filter_by(id=post_id, deleted=False).first()

#     if not post:
#         return jsonify({"message": "Post not found"}), 404

#     return jsonify(post.to_dict())

# @api_bp.route("/posts/<int:post_id>", methods=["PUT"])
# @jwt_required
# def update_post(post_id):
#     """
#     Updates a specific post
#     """
#     post = Post.query.filter_by(id=post_id, deleted=False).first()

#     if not post:
#         return jsonify({"message": "Post not found"}), 404

#     title = request.json.get("title", post.title)
#     content = request.json.get("content", post.content)

#     post.title = title
#     post.content = content
#     post.save()

#     return jsonify(post.to_dict())

# @api_bp.route("/posts/<int:post_id>", methods=["DELETE"])
# @jwt_required
# def delete_post(post_id):
#     """
#     Deletes a specific post
#     """
#     post = Post.query.filter_by(id=post_id, deleted=False).first()

#     if not post:
#         return jsonify({"message": "Post not found"}), 404

#     post.delete()

#     return jsonify({"message": "Post deleted"})
