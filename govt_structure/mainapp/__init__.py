from flask import Flask

from mainapp.database.db import DB
#function to initiate the application
def create_app():
    app = Flask(__name__)

    #initiate DB connection
    DB.init()
    #call the below method to register modules
    register_modules(app)

    return app

#import and register modules as blueprints here. 
#you can register as many modules you have
def register_modules(app):
    from mainapp.counties import counties_bp

    app.register_blueprint(counties_bp)

