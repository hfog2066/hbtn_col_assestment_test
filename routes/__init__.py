from flask import Blueprint
routes = Blueprint('routes', __name__)

from .index import *
from .users import *
from .orders import *
from .home import *
