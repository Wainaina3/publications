from flask import Blueprint

#create a counties module blueprint
general_bp = Blueprint('general',__name__)

#import counties module routes
from mainapp.counties import routes