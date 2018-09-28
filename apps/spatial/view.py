#-*- coding:utf-8 -*-
#!/usr/bin/env python
from flask_restful import Resource, reqparse, abort
from apps.spatial import spatial
from apps.util import make_result


@spatial.resource('/index', endpoint='index')
class Index(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('user_name', type=str, required=True, help='error name', location='args')
        args = parser.parse_args()
        user_name = args['user_name']

        return make_result(data={'name':user_name})

# 设置端点
# @spatial.resource('/endpoint')
# class TestWorld(Resource):
#     def get(self):
#         return redirect(url_for('spatial.index', user_name='cde'))


