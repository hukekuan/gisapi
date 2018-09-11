from flask import Blueprint
from flask_restful import Api

spatial_bp = Blueprint('spatial', __name__, url_prefix='/spatial')
spatial = Api(spatial_bp)

from . import view