#-*- coding:utf-8 -*-
#!/usr/bin/env python
from flask import jsonify

from apps.code import Code


def make_result(data=None, code=Code.SUCCESS):
    return jsonify({'code':code, 'data':data, 'msg':Code.msg[code]})
