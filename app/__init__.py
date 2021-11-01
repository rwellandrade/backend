from flask import Flask
# from flask_appconfig import AppConfig
from flask_bootstrap import Bootstrap
from .frontend import frontend
from .api import api
from .nav import nav
from .db import init

app = Flask(__name__)
db.init(app)

# AppConfig(app)
Bootstrap(app)
app.register_blueprint(frontend)
app.register_blueprint(api)
# app.config['BOOTSTRAP_SERVE_LOCAL'] = True
nav.init_app(app)


# from .router import routes
