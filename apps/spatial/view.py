from flask_restful import Resource
from apps.spatial import spatial


@spatial.resource('/')
class HelloWorld(Resource):
    def get(self):
        return {'hello': 'API'}