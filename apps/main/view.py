#-*- coding:utf-8 -*-
#!/usr/bin/env python

from flask_restful import Resource


class APIWorld(Resource):
    def get(self):
        return {'hello': 'world'}