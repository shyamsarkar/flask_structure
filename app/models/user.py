from app.extensions import BaseModel, db, views, admin
from .roles_users import roles_users


class User(BaseModel):
    __tablename__ = 'users'
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    active = db.Column(db.Boolean, default=False)
    last_login_at = db.Column(db.DateTime)
    current_login_at = db.Column(db.DateTime)
    last_login_ip = db.Column(db.String(50))
    current_login_ip = db.Column(db.String(50))
    login_count = db.Column(db.Integer)
    roles = db.relationship('Role', secondary=roles_users, backref=db.backref('user', lazy='dynamic'))
    # posts = db.relationship('Post', backref='user', lazy=True)
    # documents = db.relationship('Document', backref='user', lazy=True)

    def __repr__(self):
        return f"User('{self.email}')"

    def to_dictionary(self):
        return {"email":self.email, "password":self.password}

admin.add_view(views(User, db.session))
