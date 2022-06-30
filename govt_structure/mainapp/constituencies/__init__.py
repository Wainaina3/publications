from flask import Blueprint

#create a Constituencies module blueprint
constituencies_bp = Blueprint('constituencies',__name__)

#import Constituencies module routes
from mainapp.constituencies import route