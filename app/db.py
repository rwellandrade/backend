from flask_sqlalchemy import SQLAlchemy

DB_NAME = 'popas.db'
SCHEMA = 'db_schema.sql'

db = SQLAlchemy()

def init(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/' + DB_NAME
    db.init_app(app)
