from app.extensions import db

roles_users = db.Table(
    'roles_users',
    db.Column('user_id', db.String(100), db.ForeignKey('users.id')),
    db.Column('role_id', db.String(100), db.ForeignKey('roles.id'))
)
