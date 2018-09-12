#-*- coding:utf-8 -*-
#!/usr/bin/env python

from flask_restful import Resource

from apps.main import api


@api.resource(*['/', '/test'])
class APIWorld(Resource):
    def get(self):
        return {'hello': 'world'}