from flask import Blueprint

#create a counties module blueprint
counties_bp = Blueprint('counties',__name__)

#import counties module routes
from mainapp.counties import route