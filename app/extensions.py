from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy.ext.hybrid import hybrid_property
from datetime import datetime
import uuid
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_babel import Babel
from flask.cli import AppGroup
from faker import Faker

# from flask_mail import Mail
# from celery import Celery
# from flask_jwt_extended import JWTManager

db = SQLAlchemy()
migrate = Migrate()
admin = Admin(name='Buyee', template_mode='bootstrap4')
babel = Babel()
custom_cli = AppGroup('custom')
fake = Faker()
# mail = Mail()
# celery = Celery(__name__)
# jwt = JWTManager()


# Optional: You can also define a custom error handler for JWT errors
# @jwt.expired_token_loader
# def expired_token_callback(expired_token):
#     token_type = expired_token['type']
#     return jsonify({
#         'status': 401,
#         'sub_status': 42,
#         'message': 'The {} token has expired'.format(token_type)
#     }), 401



class BaseModel(db.Model):
    __abstract__ = True
    id = db.Column(db.String(40), primary_key=True, default=str(uuid.uuid4()))  # maximum uuid = 36
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    deleted = db.Column(db.Boolean, default=False)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def discard(self):
        self.deleted = True
        db.session.add(self)
        db.session.commit()

    def distroy(self):
        db.session.delete(self)
        db.session.commit()

    def undiscard(self):
        self.deleted = False
        db.session.add(self)
        db.session.commit()
    
    @hybrid_property
    def is_not_deleted(self):
        return self.deleted == False


class views(ModelView):

    def is_accessible(self):
        return True

    def inaccessible_callback(self, name, **kwargs):
        # redirect to login page if user doesn't have access
        return "Unauthorized Token" #redirect(url_for('login', next=request.url))