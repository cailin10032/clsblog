from flask.ext import restful
from flask import Blueprint
import functools
from flask import jsonify


api_blueprint = Blueprint('api', __name__)
api = restful.Api(api_blueprint)

class ResourceRegister(object):
    def __init__(self, api):
        self.api = api

    def register_resource(self, path=None):
        def decorator(cls):
            self.api.add_resource(cls, path or cls.name())
            return cls
        return decorator

register = ResourceRegister(api)


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
