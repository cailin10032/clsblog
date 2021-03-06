from functools import wraps
from flask import abort, request
from flask.ext.login import current_user
from .models import Permission

def permission_required(permission):
    def decorator(f):
        @wraps(f)
        def decoratored_function(*args, **kwargs):
            if not current_user.can(permission):
                abort(403)
            return f(*args, **kwargs)
        return decoratored_function
    return decorator


def admin_required(f):
    return permission_required(Permission.ADMINISTER)(f)
