#-*- coding:utf-8 -*-
#!/usr/bin/env python
from flask import Blueprint
from flask_restful import Api

main_bp = Blueprint('main', __name__)
api = Api(main_bp)

from . import view