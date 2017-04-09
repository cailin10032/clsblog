# coding=utf-8

import uuid
from flask_httpauth import HTTPBasicAuth
from flask import g
from models import AnonymousUser, User
import functools

auth = HTTPBasicAuth()

@auth.verify_password
def virify_password(email_or_token, password):
    if not email_or_token:
        g.current_user = AnonymousUser()
        return True
    if not password:
        g.current_user = User.verify_auth_token(email_or_token)
        g.user_token = True
        return g.current_user is not None
    user = User.query.filter_by(email=email_or_token).first()
    if not user:
        return False
    g.current_user = user
    g.use_token = False
    return user.verify_password(password)
