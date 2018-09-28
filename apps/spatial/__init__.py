#-*- coding:utf-8 -*-
#!/usr/bin/env python
from flask import Blueprint
from flask_restful import Api, abort
from werkzeug.exceptions import HTTPException

from apps.util import errors, make_result, Code

spatial_bp = Blueprint('spatial', __name__, url_prefix='/spatial')
spatial = Api(spatial_bp, catch_all_404s=True)


from . import view