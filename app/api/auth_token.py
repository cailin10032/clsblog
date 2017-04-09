from base import BaseResource, register
from flask import request
from ..models import User


@register.register_resource()
class AuthTokenResource(BaseResource):

    def post(self):
        data = request.data
        email = data.get('email')
        psw = data.get('password')
        user = User.verify_login(email, psw)
        if user is not None:
            token = user.generate_auth_token()
            return {'token': token}
        return {}, 401
