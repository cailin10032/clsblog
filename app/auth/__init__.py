from flask import Blueprint

auth = Blueprint('auth', __name__)

#to load views.py (note: there is no other way to load it)
from . import views