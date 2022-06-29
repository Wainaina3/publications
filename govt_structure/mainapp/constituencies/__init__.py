from flask import Blueprint

#create a morning module blueprint
morning_bp = Blueprint('morning',__name__)

#import morning module routes
from mainapp.morning import routes