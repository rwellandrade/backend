from flask_sqlalchemy import SQLAlchemy

DB_NAME = 'popas.db'
SCHEMA = 'db_schema.sql'

db = SQLAlchemy()

def init(app):
    print("bati?")
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/' + DB_NAME
    db.init_app(app)
    with app.app_context():
        db.drop_all()
        db.create_all()
        db.session.add(Product(name='Hamburguer', image='', price=30.5),)
        db.session.add(Product(name='Porção de Batata', image='', price=15),)
        db.session.add(Product(name='Guaraná', image='', price=7),)
        db.session.add(Product(name='Heineken', image='', price=7),)
        db.session.add(Product(name='Coca-Cola', image='', price=5))
        db.session.add(Item(name='Tomate', available_qty=50))
        db.session.add(Item(name='Alface', available_qty=30))
        db.session.add(Item(name='Cebola', available_qty=5))
        db.session.add(Item(name='Alho', available_qty=5))
        db.session.add(Item(name='Carne', available_qty=15))
        db.session.add(Item(name='Frango', available_qty=15))
        db.session.add(Item(name='Batata', available_qty=20))
        db.session.add(Item(name='Coca-Cola', available_qty=10))
        db.session.add(Item(name='Heineken', available_qty=10))
        db.session.add(Item(name='Guaraná', available_qty=15))
        db.session.commit()



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