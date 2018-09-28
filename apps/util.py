#-*- coding:utf-8 -*-
#!/usr/bin/env python
from flask import jsonify
from flask_restful import abort


class Code:
    SUCCESS = 1200
    NO_PARAM = 1300
    # https://segmentfault.com/a/1190000012281928
    msg = {
        SUCCESS:'success',
        NO_PARAM:'no param'
    }

errors = {
    'UserAlreadyExistsError': {
        'message': "A user with that username already exists.",
        'status': 409,
    },
    'ResourceDoesNotExist': {
        'message': "A resource with that ID no longer exists.",
        'status': 404,
        'extra': "Any extra information you want.",
    },
}

def make_result(data = None, code = Code.SUCCESS):
    return jsonify({'code': code, 'data': data, 'msg': Code.msg[code]})




