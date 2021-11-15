from .db import db

class Product(db.Model):
    HEADERS = ['id', 'name', 'image', 'price']
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    image = db.Column(db.Text, nullable=False)
    price = db.Column(db.Numeric, nullable=False)

    def __repr__(self):
        return '<Produto %r>' % self.name

class Item(db.Model):
    HEADERS = ['id', 'name', 'available_qty']
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    available_qty = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return '<Item %r>' % self.name

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False, unique=True)
    password = db.Column(db.String(80), nullable=False)

class Cart(db.Model):
    HEADERS = ['id', 'name', 'image', 'price']
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.String(80), nullable=False)
    creation_time = db.Column(db.Text, nullable=False)
    status = db.Column(db.Numeric, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'),
        nullable=False)
    # category = db.relationship('User',
    #     backref=db.backref('posts', lazy=True))

    def __repr__(self):
        return '<Pedidos %r>' % self.name