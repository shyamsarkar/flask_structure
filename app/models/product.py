from app.extensions import BaseModel, db, views, admin

class Product(BaseModel):
    __tablename__ = 'products'
    product_name = db.Column(db.String(255), nullable=False)
    price = db.Column(db.Float, nullable=False)
    quantity = db.Column(db.Float, nullable=False)
    category_id = db.Column(db.String(100), db.ForeignKey('categories.id'), nullable=False)
    unit_id = db.Column(db.String(100), db.ForeignKey('units.id'), nullable=False)
    # categories = db.relationship('Category', backref=db.backref('product', lazy=True))
    # units = db.relationship('Unit', backref=db.backref('product', lazy=True))



admin.add_view(views(Product, db.session))
