#-*- coding:utf-8 -*-
#!/usr/bin/env python
import flask_restful
from flask import Flask, abort
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import import_string

from apps.util import make_result, Code
from config import config


db = SQLAlchemy()

def custom_abord(http_status_code, *args, **kwargs):
    # if http_status_code == 404:
    #     abort(make_result(code = Code.NO_PARAM))
    # return abort(http_status_code)
    return abort(make_result(code = Code.NO_PARAM))

def create_app():
    app = Flask(__name__)
    # app.config.from_object(object_name)
    app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
    app.config.from_object(config['development'])
    app.config.from_pyfile('custom_config.py')

    flask_restful.abort = custom_abord

    db.init_app(app)
    blueprints = ['apps.main:main_bp', 'apps.spatial:spatial_bp']
    for bp_name in blueprints:
        bp = import_string(bp_name)
        app.register_blueprint(bp)


    return app






