from flask.ext import restful
from flask import Blueprint
from flask import make_response
import functools
from flask import jsonify
from . import api
import json

class ApiManager(object):
    def __init__(self, api_blueprint):
        self.api = restful.Api(api_blueprint)

    def register_resource(self, path=None):
        def decorator(cls):
            self.api.add_resource(cls, path or cls.name())
            return cls
        return decorator

    def register_output(self, *args, **kwargs):
        def decorator(fn):
            self.api.representation(*args, **kwargs)(fn)
            return fn
        return decorator

register = ApiManager(api)

@register.register_output('application/json')
def output_json(data, code=200, headers=None):
    resp = make_response(json.dumps(data), code)
    resp.headers.extend(headers or {})
    return resp


class BaseResource(restful.Resource):
    @classmethod
    def name(cls):
        return cls.__name__.lower()[:-8]

    @classmethod
    def response(cls, data={}, status=True):
        ret_data = {'status': status}
        if status:
            ret_data.update({
                'data': data,
                'code': '200'
            })

        else:
            ret_data.update({
                'code': '401'
            })

        return jsonify(ret_data)
