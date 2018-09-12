#-*- coding:utf-8 -*-
#!/usr/bin/env python

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import import_string
from config import config


db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    # app.config.from_object(object_name)
    app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
    app.config.from_object(config['development'])
    app.config.from_pyfile('custom_config.py')
    blueprints = ['apps.spatial:spatial_bp']

    db.init_app(app)
    for bp_name in blueprints:
        bp = import_string(bp_name)
        app.register_blueprint(bp)

    return app






