#!/usr/bin/python3

"""Init file that modularize flask server using blueprints"""
from flask import Blueprint

app_views = Blueprint("app_views", __name__, url_prefix="/views")
from views.orders import *
from views.authentication import *
from views.users import *
