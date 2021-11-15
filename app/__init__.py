from flask import Flask
# from flask_appconfig import AppConfig
from flask_bootstrap import Bootstrap
from .frontend import frontend
from .api import api
from .nav import nav
from .db import db, init
from .models import Product, Item
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
init(app)

csrf = CSRFProtect(app)
csrf.init_app(app)

app.config.update(
    TESTING=True,
    SECRET_KEY='192b9bdd22ab9ed4d12e236c78afcb9a393ec15f71bbf5dc987d54727823bcbf'
)

# AppConfig(app)
Bootstrap(app)
app.register_blueprint(frontend)
app.register_blueprint(api)
# app.config['BOOTSTRAP_SERVE_LOCAL'] = True
nav.init_app(app)

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

# from .router import routes
