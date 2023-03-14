from app.extensions import BaseModel, db, views, admin
# from sqlalchemy import text

class Post(BaseModel):
    __tablename__ = 'posts'
    title = db.Column(db.String(255), nullable=False)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.String(100), db.ForeignKey('users.id'), nullable=False)
    users = db.relationship('User', backref=db.backref('post', lazy=True))

    def __repr__(self):
        return f"Post('{self.title}', '{self.created_at}')"

    # @hybrid_property
    # def price(self):
    #     return self.price_cents / 100

    # @price.setter
    # def price(self, value):
    #     self.price_cents = int(value * 100)

    # @price.expression
    # def price(cls):
    #     return cls.price_cents / 100

    # @hybrid_property
    # def discounted_price(self):
    #     return self.price - (self.price * self.discount)

    # @discounted_price.expression
    # def discounted_price(cls):
    #     return cls.price - (cls.price * cls.discount)

    # @hybrid_method
    # def price_is_greater_than(self, amount):
    #     return self.price > amount

    # @price_is_greater_than.expression
    # def price_is_greater_than(cls, amount):
    #     return cls.price > amount





"""
# create an instance of your model
product = Product(name='Product1')

# set the values of the properties
product.cost_price = 10
product.sell_price = 20

# get the value of the `price` property
price = product.price

# set the value of the `price` property
product.price = 15
"""




admin.add_view(views(Post, db.session))
