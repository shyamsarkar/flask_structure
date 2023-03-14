from app.extensions import BaseModel, db, views, admin
# from .roles_users import roles_users


class Role(BaseModel):
    __tablename__ = 'roles'
    name = db.Column(db.String(100), unique=True, nullable=False)
    # users = db.relationship('User', secondary='roles_users', backref=db.backref('role', lazy='dynamic'))
    
    def to_dictionary(self):
        # return {"name":self.name}
        print(self)
        return "role dictionary"
    
admin.add_view(views(Role, db.session))