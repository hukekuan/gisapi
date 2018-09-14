#-*- coding:utf-8 -*-
#!/usr/bin/env python
from flask import url_for, redirect, request
from flask_restful import Resource, reqparse
from apps.spatial import spatial


@spatial.resource('/index', endpoint='index')
class Index(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('user_name', type=int, help='名称')
        args = parser.parse_args()
        user_name = args['user_name']
        return {'hello': user_name}

# 设置端点
# @spatial.resource('/endpoint')
# class TestWorld(Resource):
#     def get(self):
#         return redirect(url_for('spatial.index', user_name='cde'))