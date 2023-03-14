from app.extensions import BaseModel, db, views, admin


class Unit(BaseModel):
    __tablename__ = 'units'
    unit_name = db.Column(db.String(255), nullable=False)
    products = db.relationship('Product', backref='unit', lazy=True)



admin.add_view(views(Unit, db.session))
