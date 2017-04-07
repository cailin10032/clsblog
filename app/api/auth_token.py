from base import BaseResource, register
from flask import request
from ..models import User


@register.register_resource()
class AuthTokenResource(BaseResource):
    def get(self):
        email = request.args.get('email')
        psw = request.args.get('psw')
        user = User.verify_login(email, psw)
        if user is not None:
            token = user.generate_auth_token()
            return self.response(data=token)
        return self.response(status=False)


@register.register_resource()
class TestResource(BaseResource):
    def get(self):
        return self.response(data='hello, world')
