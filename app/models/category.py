from app.extensions import BaseModel, db, views, admin


class Category(BaseModel):
    __tablename__ = 'categories'
    category_name = db.Column(db.String(255), nullable=False)
    products = db.relationship('Product', backref='category', lazy=True)



admin.add_view(views(Category, db.session))
