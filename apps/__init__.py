from flask import Flask
from werkzeug.utils import import_string

from apps.spatial import spatial_bp


def create_app():
    app = Flask(__name__)
    # app.config.from_object(object_name)
    app.config.from_pyfile('custom_config.py')
    blueprints = ['apps.spatial:spatial_bp']
    for bp_name in blueprints:
        bp = import_string(bp_name)
        app.register_blueprint(bp)

    return app






