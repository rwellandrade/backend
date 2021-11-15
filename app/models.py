from .db import db
from decimal import Decimal as D
import sqlalchemy.types as types
from sqlalchemy import Table, Column, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.associationproxy import association_proxy

Base = declarative_base()

class SqliteNumeric(types.TypeDecorator):
    impl = types.String

    def load_dialect_impl(self, dialect):
        return dialect.type_descriptor(types.VARCHAR(100))

    def process_bind_param(self, value, dialect):
        return str(value)

    def process_result_value(self, value, dialect):
        return D(value)


product_items = db.Table('product_item',
    db.Column('product_id', db.Integer, db.ForeignKey('product.id'), primary_key=True),
    db.Column('item_id', db.Integer, db.ForeignKey('item.id'), primary_key=True),
    db.Column('quantity', db.Integer, primary_key=True)
)




class Item(db.Model):
    HEADERS = ['id', 'name', 'available_qty']
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    available_qty = db.Column(db.Integer, nullable=False)
    # products = db.relationship(
    #     "Product",
    #     secondary=product_item_association_table, backref=db.backref('items'))

    def __repr__(self):
        return '<Item %r>' % self.name


class Product(db.Model):
    HEADERS = ['id', 'name', 'image', 'price']
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    image = db.Column(db.Text, nullable=False)
    price = db.Column(SqliteNumeric(12, 2), nullable=False)
    items = db.relationship(
        "Item", secondary=product_items, lazy='subquery', backref=db.backref('products', lazy=True))

    its = association_proxy('items', 'product_item', creator=lambda it: Item(product_id=it.product_id, quantity=it.quantity, item_id=it.item_id))

    def __repr__(self):
        return '<Produto %r>' % self.name

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False, unique=True)
    password = db.Column(db.String(80), nullable=False)


class Cart(db.Model):
    HEADERS = ['id', 'name', 'image', 'price']
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.String(80), nullable=False)
    creation_time = db.Column(db.Text, nullable=False)
    status = db.Column(SqliteNumeric(12, 2), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'),
                        nullable=False)
    # category = db.relationship('User',
    #     backref=db.backref('posts', lazy=True))

    def __repr__(self):
        return '<Pedidos %r>' % self.name
